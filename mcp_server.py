#!/usr/bin/env python3
"""
docs-kb MCP Server: Intelligent search over local technical documentation.

Protects the agent's context window by returning only relevant sections.
Supports stdio transport (local) and streamable-http (Docker / remote).

Run locally:  python3 mcp_server.py
Run HTTP:     python3 mcp_server.py --transport streamable-http --port 8765
"""

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import requests
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(os.environ.get("DOCS_KB_PATH", Path(__file__).parent))
SOURCES_DIR = BASE_DIR / "sources"
INDEX_DIR = BASE_DIR / "index"
CHANGELOG_DIR = BASE_DIR / "changelog"
CONFIG_PATH = BASE_DIR / "config.json"

FIRECRAWL_URL = os.environ.get("FIRECRAWL_URL", "http://localhost:3002")

MAX_EXCERPT_CHARS = 800
MAX_TOTAL_CHARS = 4000

_STOPWORDS = set("""
a al algo como con cual de del desde donde el en entre es esta este esto la las lo los mas
mi muy no o para pero por que se si sin sobre su sus un una uno unos y ya
an and are as at be by can do does for from how i in is it of on or the this to what
when where which why with you your
""".split())

# ---------------------------------------------------------------------------
# Cache state
# ---------------------------------------------------------------------------

_cache_state: dict = {
    "entries": {},   # key -> result string
    "mtime": 0.0,    # last observed mtime of section-index.json
    "hits": 0,
    "misses": 0,
}


def _invalidate_cache_if_stale() -> None:
    index_path = INDEX_DIR / "section-index.json"
    try:
        mtime = index_path.stat().st_mtime
        if mtime != _cache_state["mtime"]:
            _cache_state["entries"].clear()
            _cache_state["mtime"] = mtime
            _cache_state["hits"] = 0
            _cache_state["misses"] = 0
    except OSError:
        pass


def _cache_get(key: str) -> Optional[str]:
    result = _cache_state["entries"].get(key)
    if result is not None:
        _cache_state["hits"] += 1
    else:
        _cache_state["misses"] += 1
    return result


def _cache_set(key: str, value: str) -> None:
    if len(_cache_state["entries"]) >= 200:
        # Simple FIFO eviction
        first = next(iter(_cache_state["entries"]))
        del _cache_state["entries"][first]
    _cache_state["entries"][key] = value


# ---------------------------------------------------------------------------
# FAISS / semantic search state
# ---------------------------------------------------------------------------

# Must match the model used by collector.py to build the index. The collector
# records it in index/embeddings-info.json, which takes precedence.
DEFAULT_EMBED_MODEL = os.environ.get(
    "DOCS_KB_EMBED_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

_faiss_index = None
_faiss_meta: list = []
_faiss_encoder = None
_faiss_state: dict = {"mtime": 0.0, "model": None, "normalized": False}


def _load_faiss_index() -> None:
    global _faiss_index, _faiss_meta, _faiss_encoder
    faiss_path = INDEX_DIR / "embeddings.faiss"
    meta_path = INDEX_DIR / "embeddings-meta.json"
    info_path = INDEX_DIR / "embeddings-info.json"
    if not faiss_path.exists() or not meta_path.exists():
        return
    try:
        import faiss
        import numpy as np  # noqa: F401 — ensure numpy available
        from fastembed import TextEmbedding
        info = {}
        if info_path.exists():
            with open(info_path, encoding="utf-8") as f:
                info = json.load(f)
        # Index without info file = legacy index built with all-MiniLM-L6-v2
        model = info.get("model", "sentence-transformers/all-MiniLM-L6-v2" if not info_path.exists()
                         else DEFAULT_EMBED_MODEL)
        mtime = faiss_path.stat().st_mtime
        index = faiss.read_index(str(faiss_path))
        with open(meta_path, encoding="utf-8") as f:
            meta = json.load(f)
        if _faiss_encoder is None or _faiss_state["model"] != model:
            _faiss_encoder = TextEmbedding(model_name=model)
        _faiss_index, _faiss_meta = index, meta
        _faiss_state.update(mtime=mtime, model=model, normalized=bool(info.get("normalized")))
        print(f"[docs-kb] FAISS loaded: {index.ntotal} vectors, model {model}", flush=True)
    except Exception as exc:
        _faiss_index = None
        _faiss_meta = []
        _faiss_encoder = None
        print(f"[docs-kb] FAISS not loaded: {exc}", flush=True)


def _reload_faiss_if_changed() -> None:
    """Hot-reload the index after collector.py rebuilds it (no container restart)."""
    try:
        mtime = (INDEX_DIR / "embeddings.faiss").stat().st_mtime
    except OSError:
        return
    if mtime != _faiss_state["mtime"]:
        _load_faiss_index()


def _semantic_search(query: str, tech_filter: Optional[str], k: int = 10) -> list:
    _reload_faiss_if_changed()
    if _faiss_index is None or _faiss_encoder is None:
        return []
    try:
        import numpy as np
        embedding = list(_faiss_encoder.embed([query]))[0]
        query_array = np.array([embedding], dtype="float32")
        if _faiss_state["normalized"]:
            import faiss
            faiss.normalize_L2(query_array)
        # With a tech filter, search much deeper so the filtered tech still
        # gets k candidates even if other techs dominate the nearest neighbours.
        faiss_k = min(k * 40 if tech_filter else k, _faiss_index.ntotal)
        if faiss_k == 0:
            return []
        distances, indices = _faiss_index.search(query_array, faiss_k)
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < 0 or idx >= len(_faiss_meta):
                continue
            meta = _faiss_meta[idx]
            if tech_filter and meta.get("tech") != tech_filter:
                continue
            if _faiss_state["normalized"]:
                # Unit vectors: squared L2 = 2 - 2*cos  ->  cosine similarity
                similarity = max(0.0, 1.0 - float(dist) / 2.0)
            else:
                # Legacy index: convert L2 distance to similarity 0-1
                similarity = float(1.0 / (1.0 + dist))
            results.append({**meta, "sem_score": similarity})
            if len(results) >= k:
                break
        return results
    except Exception:
        return []


# ---------------------------------------------------------------------------
# FastMCP app
# ---------------------------------------------------------------------------

_TRANSPORT_SECURITY = TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=[
        "127.0.0.1:*",
        "localhost:*",
        "[::1]:*",
        "mcp_docs_kb_http_core",      # Docker container name without port (nginx proxy)
        "mcp_docs_kb_http_core:*",    # Docker container name with any port
        "mcp-documentacion.adolfo-s-rey-b.com",  # Public subdomain (via cloudflare)
    ],
    allowed_origins=[
        "http://127.0.0.1:*",
        "http://localhost:*",
        "http://[::1]:*",
        "https://mcp-documentacion.adolfo-s-rey-b.com",
    ],
)

mcp_app = FastMCP(
    "docs-kb",
    instructions=(
        "Servidor MCP para consultar documentacion tecnica local. "
        "Usa docs_search para buscar informacion, docs_get_section para obtener "
        "secciones especificas, y docs_list_technologies para ver tecnologias disponibles. "
        "Patron recomendado: primero docs_search o docs_get_section (sin section) para "
        "obtener el indice, luego docs_get_section con la seccion especifica. "
        "Usa docs_status para ver el estado del sistema."
    ),
    transport_security=_TRANSPORT_SECURITY,
)

# Load FAISS at startup (silent if not available)
_load_faiss_index()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_config() -> dict:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {"technologies": {}}


_section_index_cache: dict = {"mtime": None, "data": {}}


def load_section_index() -> dict:
    """Section index, parsed once and re-read only when the file changes
    (it grows to tens of MB with full documentation sets)."""
    path = INDEX_DIR / "section-index.json"
    try:
        mtime = path.stat().st_mtime
    except OSError:
        return {}
    if _section_index_cache["mtime"] != mtime:
        with open(path, encoding="utf-8") as f:
            _section_index_cache["data"] = json.load(f)
        _section_index_cache["mtime"] = mtime
    return _section_index_cache["data"]


def load_tech_map() -> dict:
    path = INDEX_DIR / "tech-map.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def resolve_tech(name: str) -> Optional[str]:
    tech_map = load_tech_map()
    key = name.lower().strip()
    if key in tech_map:
        return tech_map[key]
    for alias, tech_key in tech_map.items():
        if key in alias or alias in key:
            return tech_key
    return None


def _markdown_dir(tech_key: str, version: str = "") -> Path:
    """Return the markdown directory for a tech, optionally version-specific."""
    if version:
        return SOURCES_DIR / tech_key / "versions" / version
    return SOURCES_DIR / tech_key / "markdown"


def _summary_path(tech_key: str, slug: str) -> Optional[Path]:
    """Return summary file path if it exists."""
    p = SOURCES_DIR / tech_key / "summaries" / f"{slug}.md"
    return p if p.exists() else None


def read_lines(filepath: Path, start: int, end: int) -> str:
    try:
        lines = filepath.read_text(encoding="utf-8").split("\n")
        selected = lines[max(0, start - 1):end]
        return "\n".join(selected)
    except Exception:
        return ""


def search_in_file(filepath: Path, query_terms: list) -> list:
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return []
    lines = content.split("\n")
    matches = []
    query_lower = [t.lower() for t in query_terms]
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(term in line_lower for term in query_lower):
            start = max(0, i - 5)
            end = min(len(lines), i + 11)
            excerpt = "\n".join(lines[start:end])
            if len(excerpt) > MAX_EXCERPT_CHARS:
                excerpt = excerpt[:MAX_EXCERPT_CHARS] + "..."
            matches.append({"line": i + 1, "excerpt": excerpt})
    return matches


def _dir_size_mb(path: Path) -> float:
    total = 0
    try:
        for f in path.rglob("*"):
            if f.is_file():
                total += f.stat().st_size
    except Exception:
        pass
    return round(total / 1_048_576, 2)


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------

@mcp_app.tool()
def docs_search(
    query: str,
    technology: str = "",
    max_results: int = 5,
    version: str = "",
) -> str:
    """Search technical documentation in the local knowledge base.

    Returns relevant sections matching the query. Uses semantic (FAISS) search
    when available, combined with keyword matching for maximum relevance.

    Args:
        query: Search terms (e.g., "groupby aggregate", "str_detect regex")
        technology: Optional technology filter (e.g., "pandas", "dplyr")
        max_results: Maximum number of results (default 5)
        version: Optional version snapshot (e.g., "2.1.0"); searches current if empty
    """
    _invalidate_cache_if_stale()
    cache_key = f"search:{query}:{technology}:{max_results}:{version}"
    cached = _cache_get(cache_key)
    if cached is not None:
        return cached

    section_index = load_section_index()
    raw_terms = [t.strip() for t in query.lower().split() if t.strip()]
    if not raw_terms:
        return "Error: query is empty."
    # Keyword phases ignore stopwords / very short words: otherwise "por" or
    # "de" match thousands of Spanish headings and drown the semantic results.
    query_terms = [t for t in raw_terms if len(t) > 2 and t not in _STOPWORDS] or raw_terms

    tech_filter = None
    if technology:
        tech_filter = resolve_tech(technology)
        if not tech_filter:
            available = ", ".join(sorted(load_config().get("technologies", {}).keys()))
            return f"Technology '{technology}' not found. Available: {available}"

    results = []
    seen_keys: set = set()

    # Phase 0: Semantic search via FAISS
    if _faiss_index is not None and not version:
        # Request more candidates than needed to allow per-tech capping
        sem_hits = _semantic_search(query, tech_filter, k=max_results * 6)
        # When no tech filter: cap results per technology to avoid large corpora
        # (e.g. tensorflow with 4000+ pages) dominating over smaller ones.
        _sem_per_tech: dict = {}
        _sem_cap = 2 if not tech_filter else max_results
        for hit in sem_hits:
            tech_key = hit["tech"]
            if not tech_filter and _sem_per_tech.get(tech_key, 0) >= _sem_cap:
                continue
            slug = hit["slug"]
            md_path = _markdown_dir(tech_key) / f"{slug}.md"
            sp = _summary_path(tech_key, slug)
            if sp:
                excerpt = sp.read_text(encoding="utf-8")[:MAX_EXCERPT_CHARS]
            else:
                ls = hit.get("line_start", 1)
                le = hit.get("line_end", ls + 20)
                excerpt = read_lines(md_path, ls, le)
                if len(excerpt) > MAX_EXCERPT_CHARS:
                    excerpt = excerpt[:MAX_EXCERPT_CHARS] + "..."
            sem_score = hit["sem_score"] * 12  # normalize to 0-12
            result_key = (tech_key, slug, hit.get("section", ""))
            seen_keys.add(result_key)
            results.append({
                "tech": tech_key,
                "file": slug,
                "section": hit.get("section", "semantic match"),
                "score": sem_score,
                "excerpt": excerpt,
            })
            _sem_per_tech[tech_key] = _sem_per_tech.get(tech_key, 0) + 1

    # Phase 1: Section heading keyword search
    for file_key, sections in section_index.items():
        tech_key = file_key.split("/")[0]
        if tech_filter and tech_key != tech_filter:
            continue
        slug = file_key.split("/", 1)[1] if "/" in file_key else file_key
        md_path = _markdown_dir(tech_key, version) / f"{slug}.md"
        for section in sections:
            heading_lower = section["heading"].lower()
            score = sum(1 for t in query_terms if t in heading_lower)
            if score > 0:
                sp = _summary_path(tech_key, slug)
                if sp:
                    excerpt = sp.read_text(encoding="utf-8")[:MAX_EXCERPT_CHARS]
                else:
                    excerpt = read_lines(md_path, section["line_start"], section["line_end"])
                    if len(excerpt) > MAX_EXCERPT_CHARS:
                        excerpt = excerpt[:MAX_EXCERPT_CHARS] + "..."
                result_key = (tech_key, slug, section["heading"])
                # 0-12 scale like the semantic score: all terms in heading -> 12,
                # one of four terms -> 6. Boost if also found semantically.
                base_score = 4 + 8 * score / len(query_terms)
                if result_key in seen_keys:
                    base_score += 5  # semantic + keyword match
                seen_keys.add(result_key)
                results.append({
                    "tech": tech_key,
                    "file": slug,
                    "section": section["heading"],
                    "score": base_score,
                    "excerpt": excerpt,
                })

    # Phase 2: Full-text search (only if results still sparse)
    if len(results) < max_results:
        config = load_config()
        techs_to_search = [tech_filter] if tech_filter else list(config.get("technologies", {}).keys())
        for tech_key in techs_to_search:
            md_dir = _markdown_dir(tech_key, version)
            if not md_dir.exists():
                continue
            for md_file in sorted(md_dir.glob("*.md")):
                file_matches = search_in_file(md_file, query_terms)
                for m in file_matches[:2]:
                    result_key = (tech_key, md_file.stem, f"line {m['line']}")
                    if result_key not in seen_keys:
                        seen_keys.add(result_key)
                        results.append({
                            "tech": tech_key,
                            "file": md_file.stem,
                            "section": f"line {m['line']}",
                            "score": sum(1 for t in query_terms if t in m["excerpt"].lower()),
                            "excerpt": m["excerpt"],
                        })

    # Sort, deduplicate by (tech, file, section), limit
    results.sort(key=lambda x: x["score"], reverse=True)
    deduped = []
    dedup_seen: set = set()
    for r in results:
        k = (r["tech"], r["file"], r.get("section", ""))
        if k not in dedup_seen:
            dedup_seen.add(k)
            deduped.append(r)

    final = []
    total_chars = 0
    for r in deduped[:max_results]:
        if total_chars + len(r["excerpt"]) > MAX_TOTAL_CHARS:
            r["excerpt"] = r["excerpt"][:MAX_TOTAL_CHARS - total_chars] + "..."
        total_chars += len(r["excerpt"])
        final.append(r)
        if total_chars >= MAX_TOTAL_CHARS:
            break

    if not final:
        result = f"No results found for '{query}'" + (f" in {technology}" if technology else "") + "."
        _cache_set(cache_key, result)
        return result

    output_lines = [f"Found {len(final)} result(s) for '{query}':\n"]
    for i, r in enumerate(final, 1):
        version_tag = f" [v{version}]" if version else ""
        output_lines.append(f"--- Result {i}: [{r['tech']}{version_tag}] {r['file']} > {r['section']} ---")
        output_lines.append(r["excerpt"])
        output_lines.append("")

    result = "\n".join(output_lines)
    _cache_set(cache_key, result)
    return result


@mcp_app.tool()
def docs_list_technologies() -> str:
    """List all documented technologies in the knowledge base.

    Returns technology names, page counts, last update dates, and detected versions.
    """
    config = load_config()
    techs = config.get("technologies", {})
    rows = []
    for key, conf in sorted(techs.items()):
        manifest_path = SOURCES_DIR / key / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path) as f:
                manifest = json.load(f)
            page_count = len(manifest.get("pages", {}))
            version = manifest.get("detected_version") or "-"
            last_updated = manifest.get("last_updated") or "-"
            if last_updated != "-":
                last_updated = last_updated[:10]
        else:
            page_count = 0
            version = "-"
            last_updated = "not collected"
        source_type = conf.get("source_type", "web")
        type_tag = " [local]" if source_type == "local" else ""
        rows.append(
            f"  {conf.get('display_name', key):22s}{type_tag} | {page_count:4d} pages"
            f" | v{version:10s} | updated: {last_updated}"
        )
    header = f"Technologies in docs-kb ({len(techs)} configured):\n"
    return header + "\n".join(rows)


@mcp_app.tool()
def docs_get_section(
    technology: str,
    slug: str,
    section: str = "",
    version: str = "",
) -> str:
    """Get a specific section from a documentation page.

    Without 'section': returns the table of contents for the page.
    With 'section': returns the content of that specific section.

    Args:
        technology: Technology name (e.g., "pandas", "python", "dplyr")
        slug: Page slug (e.g., "reference-str_detect", "user-guide-indexing")
        section: Optional section heading to retrieve
        version: Optional version snapshot (e.g., "2.1.0")
    """
    _invalidate_cache_if_stale()
    cache_key = f"section:{technology}:{slug}:{section}:{version}"
    cached = _cache_get(cache_key)
    if cached is not None:
        return cached

    tech_key = resolve_tech(technology)
    if not tech_key:
        return f"Technology '{technology}' not found."

    md_path = _markdown_dir(tech_key, version) / f"{slug}.md"
    if not md_path.exists():
        md_dir = _markdown_dir(tech_key, version)
        if md_dir.exists():
            candidates = [f.stem for f in md_dir.glob("*.md") if slug.lower() in f.stem.lower()]
            if candidates:
                return f"Slug '{slug}' not found. Did you mean: {', '.join(candidates[:10])}"
            available = [f.stem for f in md_dir.glob("*.md")][:20]
            return f"Slug '{slug}' not found. Available: {', '.join(available)}"
        ver_note = f" (version {version})" if version else ""
        return f"No documentation collected for '{technology}'{ver_note}."

    section_index = load_section_index()
    file_key = f"{tech_key}/{slug}"
    sections = section_index.get(file_key, [])

    if not section:
        if not sections:
            content = md_path.read_text(encoding="utf-8")
            lines = content.split("\n")[:50]
            result = f"TOC not available for {slug}. First 50 lines:\n\n" + "\n".join(lines)
            _cache_set(cache_key, result)
            return result
        toc_lines = [f"Table of contents for [{tech_key}] {slug}:\n"]
        for s in sections:
            indent = "  " * (s["level"] - 1)
            toc_lines.append(f"{indent}{'#' * s['level']} {s['heading']} (lines {s['line_start']}-{s['line_end']})")
        result = "\n".join(toc_lines)
        _cache_set(cache_key, result)
        return result

    section_lower = section.lower()
    best_match = None
    for s in sections:
        if section_lower == s["heading"].lower():
            best_match = s
            break
        if section_lower in s["heading"].lower():
            best_match = s

    if not best_match:
        headings = [s["heading"] for s in sections]
        return f"Section '{section}' not found. Available:\n" + "\n".join(f"  - {h}" for h in headings)

    content = read_lines(md_path, best_match["line_start"], best_match["line_end"])
    if len(content) > MAX_TOTAL_CHARS:
        content = content[:MAX_TOTAL_CHARS] + f"\n\n... (truncated, {len(content)} total chars)"

    result = f"[{tech_key}] {slug} > {best_match['heading']}:\n\n{content}"
    _cache_set(cache_key, result)
    return result


@mcp_app.tool()
def docs_changelog(
    technology: str = "",
    days: int = 7,
) -> str:
    """Show recent documentation changes.

    Args:
        technology: Optional filter by technology name
        days: Number of days to look back (default 7)
    """
    tech_filter = None
    if technology:
        tech_filter = resolve_tech(technology)
    entries = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    if not CHANGELOG_DIR.exists():
        return "No changelog data available."
    for log_file in sorted(CHANGELOG_DIR.glob("*.jsonl"), reverse=True):
        try:
            file_date = datetime.strptime(log_file.stem, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if file_date < cutoff:
            break
        with open(log_file) as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                except json.JSONDecodeError:
                    continue
                if tech_filter and entry.get("tech") != tech_filter:
                    continue
                entries.append(entry)
    if not entries:
        period = f"last {days} days"
        tech_note = f" for {technology}" if technology else ""
        return f"No changes{tech_note} in the {period}."
    output = [f"Documentation changes ({len(entries)} entries, last {days} days):\n"]
    for e in entries[:30]:
        version_note = ""
        if e.get("version_change"):
            version_note = f" [VERSION CHANGE: {e.get('old_version', '?')} -> {e.get('new_version', '?')}]"
        output.append(f"  [{e['ts'][:10]}] {e['tech']}/{e['slug']}{version_note}")
    return "\n".join(output)


@mcp_app.tool()
def docs_fetch_live(
    url: str,
    query: str = "",
) -> str:
    """Fetch documentation from a URL in real-time via Firecrawl.

    Args:
        url: The documentation URL to fetch
        query: Optional search term to extract only the relevant section
    """
    try:
        resp = requests.post(
            f"{FIRECRAWL_URL}/v1/scrape",
            json={"url": url, "formats": ["markdown"], "onlyMainContent": True},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        markdown = data.get("data", {}).get("markdown", "")
        if not markdown:
            return f"No content extracted from {url}"
    except Exception as e:
        return f"Firecrawl fetch failed: {e}"

    if query:
        query_terms = query.lower().split()
        lines = markdown.split("\n")
        best_start = -1
        best_score = 0
        for i, line in enumerate(lines):
            score = sum(1 for t in query_terms if t in line.lower())
            if score > best_score:
                best_score = score
                best_start = i
        if best_start >= 0:
            start = max(0, best_start - 5)
            end = min(len(lines), best_start + 30)
            section = "\n".join(lines[start:end])
            if len(section) > MAX_TOTAL_CHARS:
                section = section[:MAX_TOTAL_CHARS] + "..."
            return f"Relevant section from {url}:\n\n{section}"

    if len(markdown) > MAX_TOTAL_CHARS:
        markdown = markdown[:MAX_TOTAL_CHARS] + f"\n\n... (truncated, {len(markdown)} total chars)"
    return f"Content from {url}:\n\n{markdown}"


@mcp_app.tool()
def docs_status() -> str:
    """Show the current status of the docs-kb knowledge base.

    Returns: configured technologies, collection stats, FAISS status,
    cache stats, storage sizes, and stale technology alerts.
    """
    config = load_config()
    techs = config.get("technologies", {})

    total_pages = 0
    collected_count = 0
    stale_techs = []
    cutoff_30d = datetime.now(timezone.utc) - timedelta(days=30)
    tech_rows = []

    for key in sorted(techs.keys()):
        manifest_path = SOURCES_DIR / key / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path) as f:
                manifest = json.load(f)
            pages = len(manifest.get("pages", {}))
            version = manifest.get("detected_version", "-") or "-"
            last_up = manifest.get("last_updated", "")
            total_pages += pages
            collected_count += 1
            if last_up:
                try:
                    last_dt = datetime.fromisoformat(last_up.replace("Z", "+00:00"))
                    if last_dt < cutoff_30d:
                        stale_techs.append(key)
                    last_up_str = last_up[:10]
                except ValueError:
                    last_up_str = last_up[:10]
            else:
                last_up_str = "never"
                stale_techs.append(key)
            tech_rows.append(f"  {key:22s} | {pages:3d}p | v{version[:8]:<8} | {last_up_str}")
        else:
            stale_techs.append(key)
            tech_rows.append(f"  {key:22s} | not collected")

    # Section index stats
    section_index = load_section_index()
    total_sections = sum(len(v) for v in section_index.values())

    # FAISS status
    faiss_path = INDEX_DIR / "embeddings.faiss"
    faiss_meta_path = INDEX_DIR / "embeddings-meta.json"
    _reload_faiss_if_changed()
    if _faiss_index is not None:
        model_short = (_faiss_state["model"] or "?").split("/")[-1]
        faiss_status = f"Active ({_faiss_index.ntotal} vectors indexed, {model_short})"
    elif faiss_path.exists():
        faiss_status = "Index file exists but not loaded (restart server)"
    else:
        faiss_status = "Not built (run: python3 collector.py --index-only)"

    # Cache stats
    cache_entries = len(_cache_state["entries"])
    cache_hits = _cache_state["hits"]
    cache_misses = _cache_state["misses"]
    cache_status = f"{cache_entries} entries | {cache_hits} hits / {cache_misses} misses"

    # Summaries count
    summary_count = sum(
        len(list((SOURCES_DIR / k / "summaries").glob("*.md")))
        for k in techs if (SOURCES_DIR / k / "summaries").exists()
    )

    # Storage
    sources_mb = _dir_size_mb(SOURCES_DIR)
    index_mb = _dir_size_mb(INDEX_DIR)

    lines = [
        "=== docs-kb Status ===",
        f"Technologies:  {len(techs)} configured | {collected_count} collected",
        f"Pages:         {total_pages} total",
        f"Sections:      {total_sections} indexed",
        f"Summaries:     {summary_count} compressed pages (LLM)",
        "",
        f"FAISS Search:  {faiss_status}",
        f"Cache:         {cache_status}",
        "",
        f"Storage:       sources/ {sources_mb} MB | index/ {index_mb} MB",
        "",
    ]

    if stale_techs:
        lines.append(f"Alerts: {len(stale_techs)} technologies need update: {', '.join(stale_techs[:10])}")
        lines.append("")

    lines.append("Technologies:")
    lines.extend(tech_rows)

    return "\n".join(lines)


@mcp_app.tool()
def docs_version_history(technology: str) -> str:
    """Show version history and available snapshots for a technology.

    Args:
        technology: Technology name (e.g., "pandas", "react")
    """
    tech_key = resolve_tech(technology)
    if not tech_key:
        return f"Technology '{technology}' not found."

    manifest_path = SOURCES_DIR / tech_key / "manifest.json"
    if not manifest_path.exists():
        return f"No documentation collected for '{tech_key}'."

    with open(manifest_path) as f:
        manifest = json.load(f)

    current_version = manifest.get("detected_version", "-") or "-"
    last_updated = (manifest.get("last_updated") or "")[:10] or "unknown"
    page_count = len(manifest.get("pages", {}))

    lines = [
        f"Version history for {tech_key}:",
        f"  Current: v{current_version} ({last_updated}, {page_count} pages)",
    ]

    version_history = manifest.get("version_history", [])
    versions_dir = SOURCES_DIR / tech_key / "versions"

    # Also check filesystem for snapshots not in manifest
    fs_versions = set()
    if versions_dir.exists():
        for d in versions_dir.iterdir():
            if d.is_dir():
                fs_versions.add(d.name)

    history_versions = {entry["version"] for entry in version_history}
    all_versions = history_versions | fs_versions

    if all_versions:
        lines.append("  Snapshots:")
        for entry in version_history:
            v = entry["version"]
            date = entry.get("date", "")[:10]
            snap_path = versions_dir / v
            page_c = len(list(snap_path.glob("*.md"))) if snap_path.exists() else "?"
            lines.append(f"    v{v} (saved {date}, {page_c} pages) — docs_search(version='{v}')")
        for v in sorted(fs_versions - history_versions):
            snap_path = versions_dir / v
            page_c = len(list(snap_path.glob("*.md"))) if snap_path.exists() else "?"
            lines.append(f"    v{v} ({page_c} pages) — docs_search(version='{v}')")
    else:
        lines.append("  No version snapshots available.")
        lines.append("  Snapshots are created automatically when a version change is detected during collection.")

    # Changelog version changes
    changelog_changes = []
    if CHANGELOG_DIR.exists():
        for log_file in sorted(CHANGELOG_DIR.glob("*.jsonl"), reverse=True)[:30]:
            with open(log_file) as f:
                for line in f:
                    try:
                        e = json.loads(line.strip())
                        if e.get("tech") == tech_key and e.get("version_change"):
                            changelog_changes.append(e)
                    except Exception:
                        pass
    if changelog_changes:
        lines.append("\n  Version changes logged:")
        for e in changelog_changes[:5]:
            lines.append(
                f"    [{e['ts'][:10]}] {e.get('old_version', '?')} → {e.get('new_version', '?')}"
            )

    return "\n".join(lines)


@mcp_app.tool()
def docs_generate_context(
    technologies: str,
    context_type: str = "cheatsheet",
) -> str:
    """Generate a contextual documentation summary for one or more technologies.

    Args:
        technologies: Comma-separated technology names (e.g., "pandas,numpy")
        context_type:
          - "cheatsheet": Key functions, methods, and usage patterns
          - "migration": Recent version changes and what changed
          - "summary": High-level overview with list of available pages
    """
    tech_names = [t.strip() for t in technologies.split(",") if t.strip()]
    if not tech_names:
        return "Error: specify at least one technology."

    section_index = load_section_index()
    output = []

    for i, name in enumerate(tech_names):
        tech_key = resolve_tech(name)
        if not tech_key:
            output.append(f"# {name}\nNot found in knowledge base.")
            continue

        md_dir = _markdown_dir(tech_key)
        manifest_path = SOURCES_DIR / tech_key / "manifest.json"
        manifest = {}
        if manifest_path.exists():
            with open(manifest_path) as f:
                manifest = json.load(f)

        version = manifest.get("detected_version", "-") or "-"

        if context_type == "cheatsheet":
            output.append(f"# {tech_key.title()} Quick Reference (v{version})\n")
            ref_keywords = ("function", "method", "reference", "example", "usage", "argument",
                            "parameter", "syntax", "api", "return")
            cheat_sections = []
            for file_key, sections in section_index.items():
                if not file_key.startswith(tech_key + "/"):
                    continue
                slug = file_key.split("/", 1)[1]
                for sec in sections:
                    if any(kw in sec["heading"].lower() for kw in ref_keywords):
                        cheat_sections.append((slug, sec))
                    if len(cheat_sections) >= 15:
                        break
                if len(cheat_sections) >= 15:
                    break

            chars_used = 0
            for slug, sec in cheat_sections[:5]:
                if chars_used >= MAX_TOTAL_CHARS - 200:
                    break
                md_path = md_dir / f"{slug}.md"
                sp = _summary_path(tech_key, slug)
                if sp:
                    excerpt = sp.read_text(encoding="utf-8")[:350]
                else:
                    excerpt = read_lines(md_path, sec["line_start"], min(sec["line_start"] + 20, sec["line_end"]))
                    if len(excerpt) > 350:
                        excerpt = excerpt[:350] + "..."
                output.append(f"## {sec['heading']}\n{excerpt}\n")
                chars_used += len(excerpt) + len(sec["heading"])

        elif context_type == "migration":
            output.append(f"# {tech_key.title()} Migration Notes\n")
            changes = []
            if CHANGELOG_DIR.exists():
                for log_file in sorted(CHANGELOG_DIR.glob("*.jsonl"), reverse=True)[:30]:
                    with open(log_file) as f:
                        for line in f:
                            try:
                                e = json.loads(line.strip())
                                if e.get("tech") == tech_key and e.get("version_change"):
                                    changes.append(e)
                            except Exception:
                                pass
            if changes:
                output.append(f"**{len(changes)} version change(s) detected:**\n")
                for e in changes[:5]:
                    output.append(
                        f"- `{e.get('old_version', '?')}` → `{e.get('new_version', '?')}` "
                        f"on {e['ts'][:10]} (page: {e.get('slug', '?')})"
                    )
                    slug = e.get("slug", "")
                    if slug:
                        md_path = md_dir / f"{slug}.md"
                        excerpt = read_lines(md_path, 1, 15)[:250]
                        if excerpt:
                            output.append(f"\n```\n{excerpt}\n```\n")
            else:
                output.append("No version changes recorded in changelog yet.")

        elif context_type == "summary":
            output.append(f"# {tech_key.title()} Documentation Summary\n")
            page_count = len(manifest.get("pages", {}))
            last_up = (manifest.get("last_updated") or "")[:10] or "unknown"
            output.append(f"**Version:** {version} | **Pages:** {page_count} | **Updated:** {last_up}\n")
            if md_dir.exists():
                slugs = sorted(f.stem for f in md_dir.glob("*.md"))
                output.append("**Available pages:**")
                output.append("\n".join(f"  - {s}" for s in slugs[:40]))
                if len(slugs) > 40:
                    output.append(f"  ... and {len(slugs) - 40} more")
            versions_dir = SOURCES_DIR / tech_key / "versions"
            if versions_dir.exists():
                snap_versions = [d.name for d in versions_dir.iterdir() if d.is_dir()]
                if snap_versions:
                    output.append(f"\n**Version snapshots:** {', '.join(sorted(snap_versions))}")
        else:
            output.append(f"Unknown context_type '{context_type}'. Use: cheatsheet, migration, summary.")

        if i < len(tech_names) - 1:
            output.append("\n---\n")

    result = "\n".join(output)
    if len(result) > MAX_TOTAL_CHARS:
        result = result[:MAX_TOTAL_CHARS] + "\n\n... (truncated)"
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="docs-kb MCP Server")
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio", "streamable-http"],
        help="Transport: 'stdio' (default, for Claude Code) or 'streamable-http' (Docker/remote)",
    )
    parser.add_argument("--port", type=int, default=8765, help="HTTP port (default 8765)")
    parser.add_argument("--host", default="0.0.0.0", help="HTTP host (default 0.0.0.0)")
    args = parser.parse_args()

    if args.transport == "streamable-http":
        mcp_app.settings.host = args.host
        mcp_app.settings.port = args.port
        mcp_app.run(transport="streamable-http")
    else:
        mcp_app.run()


if __name__ == "__main__":
    main()
