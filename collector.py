#!/usr/bin/env python3
"""
docs-kb collector: Fetches and maintains technical documentation via Firecrawl.
Supports web scraping, local markdown folders, FAISS embedding
indexing, version snapshots, LLM compression, and status reporting.

Usage:
    python3 collector.py --all                          # Update all technologies
    python3 collector.py --tech python                  # Update one technology
    python3 collector.py --tech python --discover       # Re-discover pages
    python3 collector.py --add numpy --map-url "https://numpy.org/doc/stable/" --filters "reference/,user/"
    python3 collector.py --index-only                   # Rebuild indices + FAISS
    python3 collector.py --compress                     # Compress large pages with Gemini Flash
    python3 collector.py --report                       # Generate ESTADO.md
    python3 collector.py --check                        # Check for version updates (lightweight)
"""

import argparse
import gzip
import hashlib
import json
import logging
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
import zlib
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(os.environ.get("DOCS_KB_PATH", Path(__file__).parent))
CONFIG_PATH = BASE_DIR / "config.json"
SOURCES_DIR = BASE_DIR / "sources"
CHANGELOG_DIR = BASE_DIR / "changelog"
INDEX_DIR = BASE_DIR / "index"
LOG_DIR = BASE_DIR / "logs"

# Embedding model shared with mcp_server.py (the model actually used is also
# recorded in index/embeddings-info.json so the server always matches the index).
EMBED_MODEL = os.environ.get(
    "DOCS_KB_EMBED_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
EMBED_SNIPPET_CHARS = 300  # body text appended to each heading before embedding

LOG_DIR.mkdir(parents=True, exist_ok=True)
# Log to file always; to stdout only when interactive (cron redirects stdout to
# the same log file, which used to duplicate every line).
_handlers = [logging.FileHandler(LOG_DIR / "collector.log", mode="a")]
if sys.stdout.isatty():
    _handlers.append(logging.StreamHandler(sys.stdout))
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=_handlers,
)
log = logging.getLogger("collector")
for _noisy in ("httpx", "httpcore", "huggingface_hub", "urllib3"):
    logging.getLogger(_noisy).setLevel(logging.WARNING)

HTTP_HEADERS = {"User-Agent": "docs-kb-collector/1.1 (self-hosted documentation index)"}

# Optional wall-clock deadline (epoch seconds) set by --time-budget-min: scraping
# stops cleanly and the manifest is saved, e.g. before a CI job time limit.
DEADLINE: float | None = None


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return json.load(f)


def save_config(config: dict):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    log.info("Config saved.")


# ---------------------------------------------------------------------------
# Firecrawl API helpers
# ---------------------------------------------------------------------------

def firecrawl_map(base_url: str, firecrawl_url: str) -> list:
    log.info(f"Mapping site: {base_url}")
    try:
        resp = requests.post(
            f"{firecrawl_url}/v1/map",
            json={"url": base_url, "limit": 100000},
            timeout=300,
        )
        resp.raise_for_status()
        data = resp.json()
        links = data.get("links", data.get("urls", []))
        if not links and "data" in data:
            links = data["data"]
        log.info(f"  Map returned {len(links)} URLs")
        return links if isinstance(links, list) else []
    except Exception as e:
        log.error(f"  Map failed for {base_url}: {e}")
        return []


def firecrawl_scrape(url: str, firecrawl_url: str, options: dict) -> dict | None:
    payload = {"url": url, **options}
    try:
        resp = requests.post(
            f"{firecrawl_url}/v1/scrape",
            json=payload,
            timeout=60,
        )
        resp.raise_for_status()
        result = resp.json()
        return result.get("data", result)
    except Exception as e:
        log.error(f"  Scrape failed for {url}: {e}")
        return None


# ---------------------------------------------------------------------------
# URL filtering
# ---------------------------------------------------------------------------

def filter_urls(
    urls: list,
    base_url: str,
    include_filters: list,
    exclude_patterns: list,
    max_pages: int,
) -> list:
    filtered = []
    for u in urls:
        if not u.startswith(("http://", "https://")):
            continue
        if urlparse(base_url).netloc not in u:
            continue
        if include_filters:
            if not any(f in u for f in include_filters):
                continue
        if any(p in u for p in exclude_patterns):
            continue
        if "#" in u:
            u = u.split("#")[0]
        if "?" in u:
            u = u.split("?")[0]
        if u not in filtered:
            filtered.append(u)
    return filtered[:max_pages]


def url_to_slug(url: str, base_url: str) -> str:
    path = urlparse(url).path
    base_path = urlparse(base_url).path
    relative = path.removeprefix(base_path).strip("/")
    if not relative:
        relative = "index"
    slug = re.sub(r"[/\\]+", "-", relative)
    slug = re.sub(r"[^a-zA-Z0-9_\-.]", "_", slug)
    slug = slug.rstrip("-_.")
    slug = re.sub(r"\.html?$", "", slug)
    return slug or "index"


# ---------------------------------------------------------------------------
# Version detection
# ---------------------------------------------------------------------------

def detect_version(metadata: dict, url: str, markdown: str) -> str | None:
    title = metadata.get("title", "") or ""
    m = re.search(r"(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)", title)
    if m:
        return m.group(1)
    m = re.search(r"/(\d+\.\d+(?:\.\d+)?)/", url)
    if m:
        return m.group(1)
    first_lines = "\n".join(markdown.split("\n")[:10])
    m = re.search(r"[Vv]ersion\s+(\d+\.\d+(?:\.\d+)?)", first_lines)
    if m:
        return m.group(1)
    return None


# ---------------------------------------------------------------------------
# Section index builder
# ---------------------------------------------------------------------------

_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def clean_heading(text: str) -> str:
    """Strip markdown link syntax / permalink anchors from a heading.

    "Types of join[](https://...#types-of-join)" -> "Types of join"
    "Merge[#](https://...)"                      -> "Merge"
    "[`str_detect()`](https://...)"              -> "`str_detect()`"
    """
    text = re.sub(r"\[\s*[#¶]?\s*\]\([^)]*\)", "", text)
    text = _MD_LINK_RE.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip().rstrip("#¶").strip()


def build_section_index_for_file(markdown_path: Path) -> list:
    sections = []
    try:
        lines = markdown_path.read_text(encoding="utf-8").split("\n")
    except Exception:
        return sections
    current_section = None
    in_code = False
    for i, line in enumerate(lines, start=1):
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        m = None if in_code else re.match(r"^(#{1,4})\s+(.+)", line)
        if m:
            heading = clean_heading(m.group(2))
            if not heading:
                continue
            if current_section:
                current_section["line_end"] = i - 1
                sections.append(current_section)
            current_section = {
                "heading": heading,
                "level": len(m.group(1)),
                "line_start": i,
                "line_end": len(lines),
            }
    if current_section:
        current_section["line_end"] = len(lines)
        sections.append(current_section)
    return sections


def rebuild_section_index(config: dict):
    """Rebuild global section index from all markdown files."""
    log.info("Rebuilding section index...")
    index = {}
    for tech_key in config["technologies"]:
        md_dir = SOURCES_DIR / tech_key / "markdown"
        if not md_dir.exists():
            continue
        for md_file in sorted(md_dir.glob("*.md")):
            key = f"{tech_key}/{md_file.stem}"
            sections = build_section_index_for_file(md_file)
            if sections:
                index[key] = sections
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    tmp = INDEX_DIR / "section-index.json.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False)  # compact: grows to tens of MB
    tmp.replace(INDEX_DIR / "section-index.json")
    log.info(f"  Section index: {len(index)} files indexed.")

    # Also rebuild FAISS embeddings
    build_embedding_index(index)


def rebuild_tech_map(config: dict):
    """Build tech-map.json mapping aliases to directory names."""
    tech_map = {}
    for tech_key, tech_conf in config["technologies"].items():
        display = tech_conf.get("display_name", tech_key)
        tech_map[tech_key] = tech_key
        tech_map[display.lower()] = tech_key
        aliases = {
            "scikit-learn": ["sklearn"],
            "javascript": ["js"],
            "typescript": ["ts"],
            "ggplot2": ["ggplot"],
            "jupyterlab": ["jupyter"],
        }
        for extra in aliases.get(tech_key, []):
            tech_map[extra] = tech_key
    with open(INDEX_DIR / "tech-map.json", "w") as f:
        json.dump(tech_map, f, indent=2, ensure_ascii=False)
    log.info(f"  Tech map: {len(tech_map)} aliases mapped.")


# ---------------------------------------------------------------------------
# FAISS embedding index
# ---------------------------------------------------------------------------

def _embed_with_cache(texts: list, np, faiss, TextEmbedding):
    """Embed texts, reusing vectors of unchanged texts from the previous build.

    Cache = index/embeddings-cache.npy (normalized float32 rows) +
    index/embeddings-cache-keys.json ({"model": ..., "keys": [sha1(text), ...]}).
    Only new/changed sections are encoded, so re-indexing tens of thousands of
    pages takes minutes instead of hours. The cache is rewritten with only the
    current keys (stale rows are dropped).
    """
    cache_vec = INDEX_DIR / "embeddings-cache.npy"
    cache_keys = INDEX_DIR / "embeddings-cache-keys.json"
    keys = [hashlib.sha1(t.encode("utf-8")).hexdigest() for t in texts]
    old = {}
    try:
        meta = json.loads(cache_keys.read_text(encoding="utf-8"))
        if meta.get("model") == EMBED_MODEL:
            vecs = np.load(cache_vec)
            if len(vecs) == len(meta["keys"]):
                old = {k: i for i, k in enumerate(meta["keys"])}
            else:
                vecs = None
        else:
            vecs = None
    except (OSError, ValueError, KeyError):
        vecs = None

    missing = [i for i, k in enumerate(keys) if k not in old]
    log.info(f"  Embeddings: {len(texts) - len(missing)} reused from cache, {len(missing)} to encode")
    dim = vecs.shape[1] if vecs is not None and len(vecs) else None
    new_vecs = None
    if missing:
        encoder = TextEmbedding(model_name=EMBED_MODEL)
        new_vecs = np.array(list(encoder.embed([texts[i] for i in missing], batch_size=64)),
                            dtype="float32")
        faiss.normalize_L2(new_vecs)  # unit vectors -> L2 distance in [0, 2]
        dim = new_vecs.shape[1]
    out = np.empty((len(texts), dim), dtype="float32")
    pos = {i: j for j, i in enumerate(missing)}
    for i, k in enumerate(keys):
        out[i] = new_vecs[pos[i]] if i in pos else vecs[old[k]]

    # Persist cache (unique keys only)
    uniq = {}
    for i, k in enumerate(keys):
        uniq.setdefault(k, i)
    idx = list(uniq.values())
    tmp_vec = cache_vec.with_name("embeddings-cache.tmp.npy")
    np.save(tmp_vec, out[idx])
    tmp_vec.replace(cache_vec)
    cache_keys.write_text(json.dumps({"model": EMBED_MODEL, "keys": list(uniq.keys())}),
                          encoding="utf-8")
    return out


def build_embedding_index(section_index: dict):
    """Build FAISS embedding index from the section index for semantic search."""
    try:
        import faiss
        import numpy as np
        from fastembed import TextEmbedding
    except ImportError:
        log.info("  fastembed/faiss not available — skipping embedding index.")
        return

    if not section_index:
        log.info("  Section index is empty — skipping embedding index.")
        return

    log.info(f"Building FAISS embedding index (model: {EMBED_MODEL})...")
    texts = []
    meta = []

    for file_key, sections in section_index.items():
        parts = file_key.split("/", 1)
        if len(parts) != 2:
            continue
        tech, slug = parts
        try:
            file_lines = (SOURCES_DIR / tech / "markdown" / f"{slug}.md").read_text(
                encoding="utf-8").split("\n")
        except Exception:
            file_lines = []
        for sec in sections:
            heading = sec.get("heading", "")
            if not heading:
                continue
            # Heading + the first chars of the section body: gives the model
            # real content to match against, not just a title.
            body = file_lines[sec.get("line_start", 1):sec.get("line_end", 1)]
            snippet = " ".join(l.strip() for l in body if l.strip() and not l.lstrip().startswith(("```", "|", "#")))
            snippet = _MD_LINK_RE.sub(r"\1", snippet)[:EMBED_SNIPPET_CHARS]
            title = re.sub(r"[-_]+", " ", slug)[:80]
            texts.append(f"{tech} {title}: {heading}. {snippet}".strip())
            meta.append({
                "tech": tech,
                "slug": slug,
                "section": heading,
                "line_start": sec.get("line_start", 1),
                "line_end": sec.get("line_end", 1),
            })

    if not texts:
        log.warning("  No texts to embed.")
        return

    log.info(f"  Encoding {len(texts)} sections with fastembed...")
    try:
        embeddings_array = _embed_with_cache(texts, np, faiss, TextEmbedding)

        # Build IndexFlatL2 (exact search, fast for <50k vectors)
        dimension = embeddings_array.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings_array)

        faiss_path = INDEX_DIR / "embeddings.faiss"
        meta_path = INDEX_DIR / "embeddings-meta.json"
        info_path = INDEX_DIR / "embeddings-info.json"
        # Write to temp files and rename, so the server never reads a half-written index
        tmp_faiss = faiss_path.with_suffix(".faiss.tmp")
        faiss.write_index(index, str(tmp_faiss))
        with open(meta_path.with_suffix(".json.tmp"), "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False)
        with open(info_path, "w", encoding="utf-8") as f:
            json.dump({
                "model": EMBED_MODEL,
                "dimension": int(dimension),
                "normalized": True,
                "vectors": int(index.ntotal),
                "built": datetime.now(timezone.utc).isoformat(),
            }, f, indent=2)
        meta_path.with_suffix(".json.tmp").replace(meta_path)
        tmp_faiss.replace(faiss_path)

        log.info(f"  FAISS index: {index.ntotal} vectors, {dimension}d. Saved to {faiss_path}")
    except Exception as e:
        log.error(f"  FAISS index build failed: {e}")


# ---------------------------------------------------------------------------
# Manifest management
# ---------------------------------------------------------------------------

def load_manifest(tech_key: str) -> dict:
    manifest_path = SOURCES_DIR / tech_key / "manifest.json"
    if manifest_path.exists():
        with open(manifest_path) as f:
            return json.load(f)
    return {"pages": {}, "detected_version": None, "last_updated": None, "version_history": []}


def save_manifest(tech_key: str, manifest: dict):
    manifest_path = SOURCES_DIR / tech_key / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Version snapshots
# ---------------------------------------------------------------------------

def update_detected_version(tech_key: str, manifest: dict, run_versions: dict):
    """Set the tech version to the one detected in most pages of this run.

    Versions are guessed per page (title/URL/first lines), so single pages such
    as "What's new in 2.0" yield noise; only the majority counts, and only with
    enough evidence. A change is recorded in manifest["version_history"]; the
    previous content stays in the git history of the repository (no copies).
    """
    if not run_versions:
        return
    version, count = max(run_versions.items(), key=lambda kv: kv[1])
    total = sum(run_versions.values())
    if count < 3 or count / total < 0.5:
        log.info(f"  {tech_key}: version not determined this run ({run_versions if len(run_versions) < 6 else total} detections)")
        return
    old = manifest.get("detected_version")
    if old == version:
        return
    manifest["detected_version"] = version
    if old:
        manifest.setdefault("version_history", []).append({
            "version": old,
            "replaced_by": version,
            "date": datetime.now(timezone.utc).isoformat(),
        })
        log.info(f"  {tech_key}: version {old} -> {version} (previous content in git history)")
        log_change(tech=tech_key, slug="*", old_hash=None, new_hash="version-change",
                   old_version=old, new_version=version, version_change=True)
    else:
        log.info(f"  {tech_key}: version {version}")


# ---------------------------------------------------------------------------
# Changelog
# ---------------------------------------------------------------------------

def log_change(tech: str, slug: str, old_hash: str, new_hash: str,
               old_version: str = None, new_version: str = None,
               version_change: bool = False):
    CHANGELOG_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "tech": tech,
        "slug": slug,
        "old_hash": old_hash[:12] if old_hash else None,
        "new_hash": new_hash[:12],
        "version_change": version_change,
    }
    if old_version:
        entry["old_version"] = old_version
    if new_version:
        entry["new_version"] = new_version
    with open(CHANGELOG_DIR / f"{today}.jsonl", "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# LLM Compression (Gemini Flash)
# ---------------------------------------------------------------------------

def compress_with_gemini(content: str, tech: str, slug: str) -> str | None:
    """Compress long documentation pages using Gemini Flash via gemini-cli."""
    word_count = len(content.split())
    if word_count < 2000:
        return None  # Only compress long pages

    prompt = (
        f"Eres un tecnico de documentacion. Resume este documento de {tech} en ~500 palabras. "
        f"Incluye: funcion principal, parametros clave con tipos, ejemplos minimos de uso, "
        f"errores comunes y como evitarlos. Formato: markdown conciso con headers y codigo.\n\n"
        f"---\n{content[:8000]}\n---\nResumen:"
    )

    try:
        result = subprocess.run(
            ["gemini", "-m", "gemini-2.0-flash", "-p", prompt],
            capture_output=True,
            text=True,
            timeout=90,
        )
        if result.returncode == 0 and result.stdout.strip():
            summary = result.stdout.strip()
            log.info(f"  Compressed {tech}/{slug}: {word_count}w → {len(summary.split())}w")
            return summary
    except FileNotFoundError:
        log.debug("  gemini-cli not found in PATH — skipping compression.")
    except subprocess.TimeoutExpired:
        log.warning(f"  Gemini timeout for {tech}/{slug}")
    except Exception as e:
        log.error(f"  Gemini compression failed for {tech}/{slug}: {e}")
    return None


def compress_technology(tech_key: str, force: bool = False):
    """Compress large markdown pages for a technology using Gemini Flash."""
    md_dir = SOURCES_DIR / tech_key / "markdown"
    summary_dir = SOURCES_DIR / tech_key / "summaries"
    if not md_dir.exists():
        log.warning(f"  No markdown for {tech_key}")
        return

    summary_dir.mkdir(parents=True, exist_ok=True)
    compressed, skipped, existing = 0, 0, 0

    for md_file in sorted(md_dir.glob("*.md")):
        slug = md_file.stem
        summary_file = summary_dir / f"{slug}.md"
        if summary_file.exists() and not force:
            existing += 1
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            skipped += 1
            continue

        summary = compress_with_gemini(content, tech_key, slug)
        if summary:
            summary_file.write_text(summary, encoding="utf-8")
            compressed += 1
        else:
            skipped += 1
        time.sleep(1.0)  # Rate limiting for Gemini API

    log.info(f"  {tech_key} compression: {compressed} compressed, {existing} existing, {skipped} skipped")


# ---------------------------------------------------------------------------
# Local source collection (any folder of markdown files)
# ---------------------------------------------------------------------------

def file_to_slug(filepath: Path, base_path: Path) -> str:
    """Convert a local file path to a docs-kb slug (max 120 chars)."""
    relative = filepath.relative_to(base_path)
    slug = str(relative).replace("/", "-").replace("\\", "-")
    slug = re.sub(r"\.md$", "", slug, flags=re.IGNORECASE)
    slug = re.sub(r"[^a-zA-Z0-9_\-.]", "_", slug)
    slug = slug.strip("-_.")
    if len(slug) > 120:
        # Truncate and append short hash for uniqueness
        short_hash = hashlib.sha256(slug.encode()).hexdigest()[:8]
        slug = slug[:110] + "_" + short_hash
    return slug or "index"


def collect_local_technology(tech_key: str, tech_conf: dict) -> dict:
    """Collect markdown files from a local directory (source_type: "local")."""
    local_path = Path(tech_conf["local_path"])
    if not local_path.exists():
        log.warning(f"  Local path not found: {local_path}")
        return {"new": 0, "updated": 0, "unchanged": 0, "failed": 0}

    file_pattern = tech_conf.get("file_pattern", "*.md")
    include_dirs = tech_conf.get("include_dirs", [])
    exclude_dirs = tech_conf.get("exclude_dirs", [".git/", ".trash/"])

    md_dir = SOURCES_DIR / tech_key / "markdown"
    md_dir.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(tech_key)
    stats = {"new": 0, "updated": 0, "unchanged": 0, "failed": 0, "removed": 0}

    # Discover files
    try:
        all_files = list(local_path.rglob(file_pattern))
    except Exception as e:
        log.error(f"  Failed to scan {local_path}: {e}")
        return stats

    current_slugs = set()
    for filepath in all_files:
        # Filter by include/exclude dirs
        rel_str = str(filepath.relative_to(local_path))
        if exclude_dirs and any(excl in rel_str for excl in exclude_dirs):
            continue
        if include_dirs and not any(incl in rel_str for incl in include_dirs):
            continue

        slug = file_to_slug(filepath, local_path)
        current_slugs.add(slug)

        try:
            content = filepath.read_text(encoding="utf-8")
        except Exception as e:
            log.warning(f"  Cannot read {filepath}: {e}")
            stats["failed"] += 1
            continue

        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        old_hash = manifest["pages"].get(slug, {}).get("last_hash")

        if old_hash == content_hash:
            stats["unchanged"] += 1
            continue

        # Write to markdown dir
        dest = md_dir / f"{slug}.md"
        dest.write_text(content, encoding="utf-8")

        now = datetime.now(timezone.utc).isoformat()
        manifest["pages"][slug] = {
            "url": str(filepath),
            "last_hash": content_hash,
            "last_fetched": now,
            "title": filepath.stem,
        }
        manifest["last_updated"] = now

        log_change(
            tech=tech_key,
            slug=slug,
            old_hash=old_hash,
            new_hash=content_hash,
        )

        if old_hash is None:
            stats["new"] += 1
            log.info(f"  New: {slug}")
        else:
            stats["updated"] += 1
            log.info(f"  Updated: {slug}")

    # Prune pages whose source file was deleted/renamed (only if the scan found
    # something, so an unmounted/empty source never wipes the index).
    if current_slugs:
        stale = [s for s in list(manifest["pages"]) if s not in current_slugs]
        stale += [p.stem for p in md_dir.glob("*.md")
                  if p.stem not in current_slugs and p.stem not in stale]
        for slug in stale:
            old_hash = manifest["pages"].pop(slug, {}).get("last_hash")
            (md_dir / f"{slug}.md").unlink(missing_ok=True)
            summary = SOURCES_DIR / tech_key / "summaries" / f"{slug}.md"
            summary.unlink(missing_ok=True)
            log_change(tech=tech_key, slug=slug, old_hash=old_hash, new_hash="removed")
            stats["removed"] += 1
        if stale:
            log.info(f"  Removed {len(stale)} stale pages no longer in {local_path}")
            manifest["last_updated"] = datetime.now(timezone.utc).isoformat()

    save_manifest(tech_key, manifest)
    return stats


# ---------------------------------------------------------------------------
# Core web collection logic
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# URL discovery strategies
#
# Self-hosted Firecrawl /v1/map only knows URLs listed in a sitemap, so sites
# without one (pandas, numpy, python, react...) returned 0 URLs and were never
# collected. discover_pages() now tries several strategies in order and keeps
# the first one that yields URLs matching the tech's map_filters:
#   map        -> Firecrawl /v1/map (sitemap-based)
#   inventory  -> Sphinx objects.inv (complete page list of Sphinx sites)
#   sitemap    -> sitemap.xml / sitemap index / .gz parsed directly
#   crawl      -> BFS over links returned by Firecrawl scrape (rendered with
#                 Playwright, so it works for JS-built sites too)
# Per tech, "discovery": [...] in config.json overrides the order, and
# "inventory_url" / "sitemap_url" / "crawl_start" override the default URLs.
# ---------------------------------------------------------------------------

DEFAULT_DISCOVERY = ["map", "inventory", "sitemap", "crawl"]
DEFAULT_CRAWL_DEPTH = 6
DEFAULT_CRAWL_MAX_FETCH = 3000


def _in_scope(url: str, base_url: str) -> bool:
    """URL lives under doc_base_url (scheme-insensitive, ignores 'www.')."""
    def key(u):
        p = urlparse(u)
        return p.netloc.lower().removeprefix("www."), p.path
    (n, path), (bn, bpath) = key(url), key(base_url)
    return n == bn and path.startswith(bpath.rstrip("/") or "/")
_SKIP_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf", ".zip", ".gz", ".tar",
             ".ipynb", ".py", ".txt", ".css", ".js", ".json", ".xml", ".ico", ".whl")


def _http_get(url: str, timeout: int = 30):
    try:
        resp = requests.get(url, headers=HTTP_HEADERS, timeout=timeout, allow_redirects=True)
        if resp.status_code == 200:
            return resp
        log.info(f"    GET {url} -> HTTP {resp.status_code}")
    except Exception as e:
        log.info(f"    GET {url} failed: {e}")
    return None


def _dir_url(url: str) -> str:
    """Directory part of a URL ('https://x/a/b.html' -> 'https://x/a/')."""
    return url if url.endswith("/") else url.rsplit("/", 1)[0] + "/"


def discover_from_inventory(tech_conf: dict) -> list:
    """Page URLs from a Sphinx objects.inv (narrative pages first, then API objects)."""
    map_url = tech_conf.get("map_url", tech_conf["doc_base_url"])
    inv_url = tech_conf.get("inventory_url") or urljoin(_dir_url(map_url), "objects.inv")
    resp = _http_get(inv_url)
    if not resp:
        return []
    parts = resp.content.split(b"\n", 4)
    if len(parts) < 5 or not parts[0].startswith(b"# Sphinx inventory version 2"):
        log.info(f"    {inv_url} is not a Sphinx v2 inventory")
        return []
    try:
        body = zlib.decompress(parts[4]).decode("utf-8", "replace")
    except zlib.error as e:
        log.info(f"    Cannot decompress {inv_url}: {e}")
        return []
    version = parts[2].decode("utf-8", "replace").removeprefix("# Version:").strip()
    base = _dir_url(resp.url)
    docs, objects = [], []
    line_re = re.compile(r"(.+?)\s+(\S+:\S+)\s+(-?\d+)\s+(\S+)\s+(.*)")
    for line in body.splitlines():
        m = line_re.match(line)
        if not m:
            continue
        name, role, _prio, uri, _disp = m.groups()
        if uri.endswith("$"):
            uri = uri[:-1] + name
        url = urljoin(base, uri.split("#")[0])
        (docs if role == "std:doc" else objects).append(url)
    urls = list(dict.fromkeys(docs + objects))
    # Narrative pages and top-level API first: "merging.html" (1 dot) <
    # "pandas.merge.html" (2) < "pandas.DataFrame.abs.html" (3). Stable sort.
    urls.sort(key=lambda u: u.rstrip("/").rsplit("/", 1)[-1].count("."))
    log.info(f"    objects.inv v{version}: {len(docs)} doc pages, {len(urls)} unique URLs")
    return urls


def discover_from_sitemap(tech_conf: dict, max_sitemaps: int = 60) -> list:
    """URLs from sitemap.xml (handles sitemap indexes and gzip)."""
    map_url = tech_conf.get("map_url", tech_conf["doc_base_url"])
    p = urlparse(map_url)
    candidates = [tech_conf["sitemap_url"]] if tech_conf.get("sitemap_url") else [
        urljoin(_dir_url(map_url), "sitemap.xml"),
        f"{p.scheme}://{p.netloc}/sitemap.xml",
    ]
    queue, seen, urls = list(dict.fromkeys(candidates)), set(), []
    while queue and len(seen) < max_sitemaps:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        resp = _http_get(sm, timeout=60)
        if not resp:
            continue
        content = resp.content
        if content[:2] == b"\x1f\x8b":
            try:
                content = gzip.decompress(content)
            except OSError:
                continue
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            continue
        locs = [el.text.strip() for el in root.iter() if el.tag.endswith("loc") and el.text]
        if root.tag.endswith("sitemapindex"):
            queue.extend(locs)
        else:
            urls.extend(locs)
    urls = list(dict.fromkeys(urls))
    log.info(f"    sitemap: {len(urls)} URLs from {len(seen)} sitemap file(s)")
    return urls


def discover_by_crawl(tech_conf: dict, config: dict) -> list:
    """BFS over links of rendered pages (Firecrawl + Playwright)."""
    firecrawl_url = config["firecrawl_url"]
    base_url = tech_conf["doc_base_url"]
    start = tech_conf.get("crawl_start", tech_conf.get("map_url", base_url))
    include = tech_conf.get("map_filters", [])
    exclude = tech_conf.get("exclude_patterns", [])
    max_depth = tech_conf.get("crawl_depth", DEFAULT_CRAWL_DEPTH)
    max_fetch = tech_conf.get("crawl_max_fetch", DEFAULT_CRAWL_MAX_FETCH)
    netloc = urlparse(base_url).netloc

    def norm(u: str) -> str:
        return u.split("#")[0].split("?")[0]

    seen, found, frontier, fetched = {norm(start)}, [norm(start)], [norm(start)], 0
    for _depth in range(max_depth):
        next_frontier = []
        # Expand pages matching the filters first: they lead to more doc pages
        frontier.sort(key=lambda u: 0 if any(f in u for f in include) else 1)
        for page in frontier:
            if fetched >= max_fetch:
                break
            data = firecrawl_scrape(page, firecrawl_url, {"formats": ["links"], "onlyMainContent": False})
            fetched += 1
            for link in (data or {}).get("links") or []:
                u = norm(link)
                if u in seen or urlparse(u).netloc != netloc or u.lower().endswith(_SKIP_EXT):
                    continue
                seen.add(u)
                if any(x in u for x in exclude):
                    continue
                found.append(u)
                next_frontier.append(u)
        frontier = next_frontier
        if not frontier or fetched >= max_fetch:
            break
    log.info(f"    crawl: {len(found)} URLs after fetching {fetched} page(s)")
    return found


def _balance_by_filter(urls: list, include_filters: list) -> list:
    """Round-robin across map_filters so one big section (e.g. API reference)
    does not take all max_pages slots."""
    if len(include_filters) < 2:
        return urls
    groups = {f: [] for f in include_filters}
    for u in urls:
        for f in include_filters:
            if f in u:
                groups[f].append(u)
                break
    out = []
    while any(groups.values()):
        for f in include_filters:
            if groups[f]:
                out.append(groups[f].pop(0))
    return out


def discover_pages(tech_key: str, tech_conf: dict, config: dict) -> list:
    firecrawl_url = config["firecrawl_url"]
    map_url = tech_conf.get("map_url", tech_conf["doc_base_url"])
    base_url = tech_conf["doc_base_url"]
    include_filters = tech_conf.get("map_filters", [])
    exclude_patterns = tech_conf.get("exclude_patterns", [])
    max_pages = tech_conf.get("max_pages", config["defaults"].get("max_pages", 30))

    strategies = {
        "map": lambda: firecrawl_map(map_url, firecrawl_url),
        "inventory": lambda: discover_from_inventory(tech_conf),
        "sitemap": lambda: discover_from_sitemap(tech_conf),
        "crawl": lambda: discover_by_crawl(tech_conf, config),
    }
    for name in tech_conf.get("discovery", DEFAULT_DISCOVERY):
        if name not in strategies:
            log.warning(f"  Unknown discovery strategy '{name}' for {tech_key}")
            continue
        raw_urls = [u for u in strategies[name]() if isinstance(u, str)]
        raw_urls = [u for u in raw_urls if not u.lower().endswith(_SKIP_EXT)]
        matched = filter_urls(raw_urls, base_url, include_filters, exclude_patterns, len(raw_urls))
        matched = [u for u in matched if _in_scope(u, base_url)]
        if matched:
            pages = _balance_by_filter(matched, include_filters)
            if max_pages and max_pages > 0:  # 0 / null = no limit
                pages = pages[:max_pages]
            log.info(f"  {tech_key}: discovery '{name}' -> {len(pages)} pages "
                     f"({len(matched)} matched filters, {len(raw_urls)} discovered)")
            return pages
        log.info(f"  {tech_key}: discovery '{name}' gave no usable URLs ({len(raw_urls)} discovered)")
    log.warning(f"  No URLs discovered for {tech_key}")
    return []


def collect_technology(tech_key: str, tech_conf: dict, config: dict,
                       discover: bool = False, compress: bool = False,
                       max_age_days: float | None = None, dry_run: bool = False) -> dict:
    """Collect/update documentation for a single web technology."""
    # Route to local collection if source_type is "local"
    if tech_conf.get("source_type") == "local":
        stats = collect_local_technology(tech_key, tech_conf)
        if compress:
            compress_technology(tech_key)
        return stats

    firecrawl_url = config["firecrawl_url"]
    scrape_options = config["defaults"]["scrape_options"].copy()
    base_url = tech_conf["doc_base_url"]

    md_dir = SOURCES_DIR / tech_key / "markdown"
    html_dir = SOURCES_DIR / tech_key / "html"
    md_dir.mkdir(parents=True, exist_ok=True)
    html_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(tech_key)
    stats = {"new": 0, "updated": 0, "unchanged": 0, "failed": 0, "skipped": 0}

    if discover or not manifest["pages"]:
        urls = discover_pages(tech_key, tech_conf, config)
        if dry_run:
            known = sum(1 for u in urls if url_to_slug(u, base_url) in manifest["pages"])
            log.info(f"  [dry-run] {tech_key}: {len(urls)} pages discovered, {known} already known, "
                     f"{len(urls) - known} new")
            stats["skipped"] = len(urls)
            return stats
        if not urls:
            return stats
        for url in urls:
            slug = url_to_slug(url, base_url)
            if slug not in manifest["pages"]:
                manifest["pages"][slug] = {
                    "url": url,
                    "last_hash": None,
                    "last_fetched": None,
                    "title": None,
                }
    else:
        urls = [p["url"] for p in manifest["pages"].values() if p.get("url")]

    run_versions: dict = {}  # version string -> pages where it was detected in this run
    for url in urls:
        slug = url_to_slug(url, base_url)
        page_info = manifest["pages"].get(slug, {
            "url": url, "last_hash": None, "last_fetched": None, "title": None
        })

        if max_age_days is not None and page_info.get("last_fetched") and page_info.get("last_hash"):
            try:
                age = (datetime.now(timezone.utc)
                       - datetime.fromisoformat(page_info["last_fetched"])).total_seconds() / 86400
            except ValueError:
                age = None
            if age is not None and age < max_age_days:
                stats["skipped"] += 1
                continue

        if DEADLINE is not None and time.time() > DEADLINE:
            log.warning(f"  Time budget exhausted: stopping {tech_key} early (progress saved; "
                        f"remaining pages are picked up on the next run)")
            break

        log.info(f"  Scraping: {slug} ({url})")
        data = firecrawl_scrape(url, firecrawl_url, scrape_options)
        if not data:
            stats["failed"] += 1
            continue

        markdown = data.get("markdown", "")
        html_content = data.get("html", "")
        metadata = data.get("metadata", {})

        if not markdown:
            log.warning(f"    No markdown content for {slug}")
            stats["failed"] += 1
            continue

        content_hash = hashlib.sha256(
            (html_content or markdown).encode("utf-8")
        ).hexdigest()

        new_version = detect_version(metadata, url, markdown)
        if new_version:
            run_versions[new_version] = run_versions.get(new_version, 0) + 1

        old_hash = page_info.get("last_hash")
        if old_hash == content_hash:
            log.info(f"    Unchanged: {slug}")
            stats["unchanged"] += 1
            # last_fetched = last time the page was checked; without this,
            # --max-age-days would re-download unchanged pages every run.
            page_info["last_fetched"] = datetime.now(timezone.utc).isoformat()
            manifest["pages"][slug] = page_info
            continue

        # Write files
        (md_dir / f"{slug}.md").write_text(markdown, encoding="utf-8")
        if html_content:
            (html_dir / f"{slug}.html").write_text(html_content, encoding="utf-8")

        now = datetime.now(timezone.utc).isoformat()
        manifest["pages"][slug] = {
            "url": url,
            "last_hash": content_hash,
            "last_fetched": now,
            "title": metadata.get("title", page_info.get("title")),
        }

        manifest["last_updated"] = now

        log_change(tech=tech_key, slug=slug, old_hash=old_hash, new_hash=content_hash)

        if old_hash is None:
            stats["new"] += 1
            log.info(f"    New: {slug}")
        else:
            stats["updated"] += 1
            log.info(f"    Updated: {slug}")

        if (stats["new"] + stats["updated"]) % 50 == 0:
            save_manifest(tech_key, manifest)  # checkpoint for long runs
        time.sleep(0.5)

    update_detected_version(tech_key, manifest, run_versions)
    save_manifest(tech_key, manifest)

    if compress:
        compress_technology(tech_key)

    return stats


# ---------------------------------------------------------------------------
# Add technology
# ---------------------------------------------------------------------------

def add_technology(config: dict, name: str, map_url: str, filters: str):
    tech_key = re.sub(r"[^a-z0-9\-]", "", name.lower().replace(" ", "-"))
    if tech_key in config["technologies"]:
        log.warning(f"Technology '{tech_key}' already exists. Use --discover to refresh.")
        return tech_key
    filter_list = [f.strip() for f in filters.split(",") if f.strip()] if filters else []
    config["technologies"][tech_key] = {
        "display_name": name,
        "doc_base_url": map_url,
        "map_url": map_url,
        "map_filters": filter_list,
        "exclude_patterns": [],
        "max_pages": config["defaults"].get("max_pages", 30),
    }
    save_config(config)
    log.info(f"Added technology: {tech_key}")
    return tech_key


# ---------------------------------------------------------------------------
# Status report
# ---------------------------------------------------------------------------

def generate_status_report(config: dict):
    """Generate ESTADO.md with full knowledge base status."""
    log.info("Generating status report...")
    techs = config.get("technologies", {})
    from datetime import timedelta
    cutoff_30d = datetime.now(timezone.utc) - timedelta(days=30)

    rows = []
    stale = []

    for key in sorted(techs.keys()):
        manifest_path = SOURCES_DIR / key / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path) as f:
                manifest = json.load(f)
            pages = len(manifest.get("pages", {}))
            version = manifest.get("detected_version", "-") or "-"
            last_up = manifest.get("last_updated", "")
            last_up_str = last_up[:10] if last_up else "never"
            # Disk size
            md_dir = SOURCES_DIR / key / "markdown"
            size_kb = sum(f.stat().st_size for f in md_dir.glob("*.md") if f.is_file()) // 1024 if md_dir.exists() else 0
            # Check stale
            is_stale = False
            if last_up:
                try:
                    dt = datetime.fromisoformat(last_up.replace("Z", "+00:00"))
                    if dt < cutoff_30d:
                        is_stale = True
                        stale.append(key)
                except ValueError:
                    pass
            else:
                stale.append(key)
                is_stale = True
            flag = " ⚠" if is_stale else ""
            rows.append(f"| {key:22s} | {pages:3d} | v{version[:10]:<10} | {last_up_str} | {size_kb:5d} KB |{flag}")
        else:
            rows.append(f"| {key:22s} |   0 | -             | not collected  |      0 KB | ⚠")
            stale.append(key)

    # Changelog last 30 days
    changelog_rows = []
    if CHANGELOG_DIR.exists():
        for log_file in sorted(CHANGELOG_DIR.glob("*.jsonl"), reverse=True)[:30]:
            with open(log_file) as f:
                for line in f:
                    try:
                        e = json.loads(line.strip())
                        vc = " [VERSION CHANGE]" if e.get("version_change") else ""
                        changelog_rows.append(
                            f"| {e['ts'][:10]} | {e['tech']:20s} | {e['slug'][:40]:40s} |{vc}"
                        )
                    except Exception:
                        pass

    report_lines = [
        "# Estado del Sistema docs-kb",
        f"\n**Generado:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"\n**Tecnologias:** {len(techs)} configuradas",
        "\n## Tecnologias\n",
        "| Tecnologia            | Pags | Version       | Actualizado   | Tamaño    |",
        "|----------------------|------|---------------|--------------|-----------|",
    ]
    report_lines.extend(rows)

    if stale:
        report_lines.append(f"\n## Alertas\n\n{len(stale)} tecnologías sin actualizar en >30 días:\n")
        report_lines.append(", ".join(stale))

    if changelog_rows:
        report_lines.append("\n## Cambios Recientes (últimos 30 días)\n")
        report_lines.append("| Fecha      | Tecnologia           | Slug                                     |")
        report_lines.append("|------------|---------------------|------------------------------------------|")
        report_lines.extend(changelog_rows[:50])

    report_path = BASE_DIR / "ESTADO.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    log.info(f"  Status report saved to {report_path}")


# ---------------------------------------------------------------------------
# Lightweight update check
# ---------------------------------------------------------------------------

def check_for_updates(config: dict):
    """Check if documentation versions have changed (lightweight, no full scrape)."""
    log.info("Checking for updates (lightweight mode)...")
    firecrawl_url = config["firecrawl_url"]
    scrape_options = {"formats": ["markdown"], "onlyMainContent": True}
    needs_update = []

    for tech_key, tech_conf in config["technologies"].items():
        if tech_conf.get("source_type") == "local":
            continue

        manifest = load_manifest(tech_key)
        current_version = manifest.get("detected_version")
        map_url = tech_conf.get("map_url", tech_conf.get("doc_base_url", ""))
        if not map_url:
            continue

        log.info(f"  Checking {tech_key} (current: v{current_version})...")
        data = firecrawl_scrape(map_url, firecrawl_url, scrape_options)
        if not data:
            continue

        markdown = data.get("markdown", "")
        metadata = data.get("metadata", {})
        detected = detect_version(metadata, map_url, markdown)

        if detected and current_version and detected != current_version:
            log.info(f"  UPDATE AVAILABLE: {tech_key} v{current_version} → v{detected}")
            needs_update.append((tech_key, current_version, detected))
        else:
            log.info(f"  Up to date: {tech_key}")

        time.sleep(0.5)

    if needs_update:
        log.info(f"\n=== {len(needs_update)} updates available ===")
        for tech, old_v, new_v in needs_update:
            log.info(f"  {tech}: v{old_v} → v{new_v}  (run: python3 collector.py --tech {tech})")
    else:
        log.info("All technologies appear up to date.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="docs-kb documentation collector")
    parser.add_argument("--all", action="store_true", help="Update all technologies")
    parser.add_argument("--tech", type=str, help="Update one technology or a comma-separated list")
    parser.add_argument("--discover", action="store_true", help="Re-discover pages (map/inventory/sitemap/crawl)")
    parser.add_argument("--max-age-days", type=float, default=None,
                        help="Only re-scrape pages fetched more than N days ago (new pages always)")
    parser.add_argument("--time-budget-min", type=float, default=None,
                        help="Stop scraping after N minutes (saves progress); for CI time limits")
    parser.add_argument("--no-index", action="store_true",
                        help="Skip rebuilding section index/FAISS at the end (for parallel runs; run --index-only after)")
    parser.add_argument("--dry-run", action="store_true",
                        help="With --discover: only report how many pages would be collected")
    parser.add_argument("--add", type=str, help="Add a new technology (name)")
    parser.add_argument("--map-url", type=str, help="Documentation URL for --add")
    parser.add_argument("--filters", type=str, default="", help="Comma-separated URL filters for --add")
    parser.add_argument("--index-only", action="store_true", help="Only rebuild indices (section index + FAISS)")
    parser.add_argument("--compress", action="store_true", help="Compress large pages with Gemini Flash")
    parser.add_argument("--report", action="store_true", help="Generate ESTADO.md status report")
    parser.add_argument("--check", action="store_true", help="Check for version updates (lightweight)")
    args = parser.parse_args()

    for d in [SOURCES_DIR, CHANGELOG_DIR, INDEX_DIR, LOG_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    config = load_config()

    if args.time_budget_min:
        global DEADLINE
        DEADLINE = time.time() + args.time_budget_min * 60

    # Stand-alone actions (no scraping)
    if args.index_only:
        rebuild_section_index(config)
        rebuild_tech_map(config)
        log.info("Index rebuild complete.")
        return

    if args.check:
        check_for_updates(config)
        return

    if args.report:
        generate_status_report(config)
        return

    if args.add:
        if not args.map_url:
            log.error("--map-url is required with --add")
            sys.exit(1)
        tech_key = add_technology(config, args.add, args.map_url, args.filters)
        config = load_config()
        stats = collect_technology(tech_key, config["technologies"][tech_key], config,
                                   discover=True, compress=args.compress)
        log.info(f"Collection complete for {tech_key}: {stats}")
        rebuild_section_index(config)
        rebuild_tech_map(config)
        return

    if args.compress and not args.all and not args.tech:
        # Compress-only mode
        for tech_key in config["technologies"]:
            log.info(f"=== Compressing: {tech_key} ===")
            compress_technology(tech_key)
        return

    # Determine which technologies to process
    if args.all:
        techs = list(config["technologies"].items())
    elif args.tech:
        # Accepts one tech or a comma-separated list (indices are rebuilt once)
        keys = [t.strip().lower() for t in args.tech.split(",") if t.strip()]
        missing = [k for k in keys if k not in config["technologies"]]
        if missing:
            log.error(f"Technology not found in config: {', '.join(missing)}")
            sys.exit(1)
        techs = [(k, config["technologies"][k]) for k in keys]
    else:
        parser.print_help()
        sys.exit(0)

    total_stats = {"new": 0, "updated": 0, "unchanged": 0, "failed": 0, "skipped": 0}
    for tech_key, tech_conf in techs:
        log.info(f"=== Processing: {tech_conf.get('display_name', tech_key)} ===")
        try:
            stats = collect_technology(tech_key, tech_conf, config,
                                       discover=args.discover, compress=args.compress,
                                       max_age_days=args.max_age_days, dry_run=args.dry_run)
        except Exception as e:  # one broken tech must not abort the whole run
            log.exception(f"  {tech_key} failed: {e}")
            continue
        for k in total_stats:
            total_stats[k] += stats.get(k, 0)
        log.info(f"  Stats: {stats}")

    if args.dry_run:
        log.info(f"\n=== DRY-RUN TOTAL: {total_stats['skipped']} pages ===")
        return
    if args.no_index:
        log.info(f"\n=== TOTAL (index not rebuilt, --no-index): {total_stats} ===")
        return

    rebuild_section_index(config)
    rebuild_tech_map(config)

    if args.report:
        generate_status_report(config)

    log.info(f"\n=== TOTAL: {total_stats} ===")


if __name__ == "__main__":
    main()
