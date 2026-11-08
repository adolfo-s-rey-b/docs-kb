# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

`docs-kb`: a public knowledge base of technical documentation (25 technologies, Markdown in `sources/<tech>/markdown/`) plus the MCP server that indexes it (FAISS multilingual semantic search, 8 tools). **Everything depends only on GitHub**: GitHub Actions re-collects the docs weekly and commits them here, builds the semantic index and publishes the local-MCP package to the `datos` Release; users run the MCP locally through the Claude Code plugin in `plugin/` (this repo is also a plugin marketplace). There is no server. All documentation is in Spanish.

**Only public technical documentation belongs here.** Never add personal notes, server configs, tokens, internal IPs or anything private — everything under `sources/` (and the `datos` Release) is public.

## Layout

- `mcp_server.py` — MCP server (8 tools; stdio, or streamable-http bound to localhost). Logs must go to stderr (stdout is the MCP channel)
- `collector.py` — collects docs via Firecrawl (+ Playwright) or from a GitHub repo (`source_type: "github"`, used for React), discovery map → objects.inv → sitemap → crawl, builds `index/` (section index + FAISS; `DOCS_KB_FAISS_INDEX=sq8` for the 8-bit index)
- `config.json` — the 25 technologies (`max_pages: 0` = no limit; `"recolectar_en": "congelada"` = keep but don't collect)
- `.github/workflows/actualizar-docs.yml` — weekly collection (one job per tech, ephemeral Firecrawl + Playwright from `.github/firecrawl/docker-compose.yml`), then calls `datos.yml`
- `.github/workflows/datos.yml` + `.github/scripts/` — incremental index build, changelog from git, package `docs-kb-datos.tar.gz` + `version.json` + `embeddings-cache.npz` → Release `datos`
- `.claude-plugin/marketplace.json`, `plugin/` — the plugin: `docs_kb_local.py` (stdlib-only launcher: install/update/serve/ensure/status/check), SessionStart hook, `/docs-kb:actualizar`, `/docs-kb:estado`, skill
- `requirements-local.txt` — pinned deps of the local MCP (`fastembed==0.8.0` must match the index build; `mcp<2`)
- `sources/<tech>/markdown/*.md` + `manifest.json` — the collected documentation (generated; don't hand-edit)
- Not versioned: `.env`, `.venv/`, `index/`, `logs/`, `dist/`, `sources/*/html/`, `changelog/`

Architecture and maintenance: [SistemaDocumentación.md](SistemaDocumentación.md). User guide: [GuiaMCP.md](GuiaMCP.md). Latest results: [ConclusionesSD.md](ConclusionesSD.md). Licenses: [ATTRIBUTION.md](ATTRIBUTION.md).

## Local MCP (primary)

```bash
python3 plugin/docs_kb_local.py install   # or: /plugin install docs-kb --marketplace adolfo-s-rey-b/docs-kb
python3 plugin/docs_kb_local.py check     # 12 end-to-end tests over stdio; exit code 0 = all pass
claude plugin validate .                  # marketplace + plugin manifests
```

Data dir: `$DOCS_KB_HOME`, `${CLAUDE_PLUGIN_DATA}` (plugin) or `~/.local/share/docs-kb`. The plugin intentionally has no `version` (tracks commits). After changing `mcp_server.py`, `collector.py`, `config.json` or `requirements-local.txt`, a push triggers `datos.yml`, which republishes the package; clients pick it up within 12 h.

## Working notes

- `collector.py`, `datos.yml` and the local MCP must use the same embedding model and `fastembed` version (`requirements-local.txt`); the model is recorded in `index/embeddings-info.json`.
- Test the collector locally against a scratch dir: `DOCS_KB_PATH=/tmp/x python collector.py --tech conda --discover --dry-run`.
- Validate workflows locally before pushing (`python -c "import yaml; yaml.safe_load(open('.github/workflows/datos.yml'))"`); a push that touches `mcp_server.py`, `collector.py`, `config.json`, `requirements-local.txt` or `.github/scripts/` republishes the Release `datos`.
- There is no server anymore: the self-hosted docs-kb server was retired on 2026-11-08 (see SistemaDocumentación.md §10).
