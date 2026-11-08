# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

`docs-kb`: a public knowledge base of technical documentation (25 technologies, Markdown in `sources/<tech>/markdown/`) plus the MCP server that indexes it (FAISS multilingual semantic search, 8 tools). This repo is the single source of truth: GitHub Actions re-collects the docs weekly and commits them here; the MCP server is a clone that only pulls and re-indexes. All documentation is in Spanish.

**Only public technical documentation belongs here.** Never add personal notes, server configs, tokens, internal IPs or anything private — `publicar.sh` pushes everything under `sources/` to the public repo.

## Layout

- `mcp_server.py` — MCP server (8 tools, streamable-http on :8765 in Docker)
- `collector.py` — collects docs via Firecrawl (+ Playwright), discovery map → objects.inv → sitemap → crawl, builds `index/` (section index + FAISS)
- `config.json` — the 25 technologies (base URL, exclude patterns, discovery overrides; `max_pages: 0` = no limit)
- `.github/workflows/actualizar-docs.yml` — weekly collection on GitHub Actions (one job per tech, ephemeral Firecrawl + Playwright from `.github/firecrawl/docker-compose.yml`; manual: `gh workflow run actualizar-docs.yml -f tecnologias=a,b -f publicar=false`)
- `"recolectar_en": "servidor"` in `config.json` (react, anaconda): those sites block GitHub runner IPs, so the workflow skips them and the server collects them monthly (`actualizar.sh --tech react,anaconda`).
- `sincronizar.sh` — server cron (hourly): `git pull --ff-only` + resumable `--index-only` (tracks `index/indexed-commit`)
- `actualizar.sh` / `publicar.sh` / `recoleccion_completa.sh` — manual fallback: collect from the server and push with its deploy key (don't run while the workflow runs)
- `chequeo_remoto.sh` — the 12 remote tests against the MCP endpoint
- `sources/<tech>/markdown/*.md` + `manifest.json` — the collected documentation (generated; don't hand-edit)
- Not versioned: `.env`, `.venv/`, `index/`, `logs/`, `sources/*/html/`, `changelog/`

Architecture and maintenance: [SistemaDocumentación.md](SistemaDocumentación.md). Server test suite: [ChequeoSD.md](ChequeoSD.md). Client guide: [GuiaMCP.md](GuiaMCP.md). Latest results: [ConclusionesSD.md](ConclusionesSD.md). Licenses: [ATTRIBUTION.md](ATTRIBUTION.md).

## Connecting to the MCP Server

The endpoint requires a Bearer token, kept only in `.env` (`DOCS_KB_TOKEN`, chmod 600, git-ignored; template `.env.example`). Never write the token into files or commands — use `$DOCS_KB_TOKEN`.

```bash
set -a; . ./.env; set +a
claude mcp add --transport http --scope user docs-kb \
  https://mcp-documentacion.adolfo-s-rey-b.com/mcp \
  --header "Authorization: Bearer $DOCS_KB_TOKEN"
claude mcp get docs-kb    # Status: ✔ Connected
```

Claude Code does **not** read `~/.claude/mcp.json`. Restart Claude Code to get the `mcp__docs-kb__*` tools (`docs_search`, `docs_get_section`, `docs_list_technologies`, `docs_status`, `docs_changelog`, `docs_fetch_live`, `docs_version_history`, `docs_generate_context`).

## Health Checks

```bash
./chequeo_remoto.sh          # 12 remote tests (PASS/WARN/FAIL); exit code = #FAIL
./chequeo_remoto.sh --md     # also writes resultados/chequeo-YYYY-MM-DD.md (git-ignored)
```

Manual curl checks must send `Accept: application/json, text/event-stream` and call `initialize` first (otherwise 406/400). 401 = no token, 403 = wrong token, 000 = server/tunnel down.

## Working on the Server

- Reached as `ssh server` (local SSH alias). Code lives in `~/server-stack/docs-kb` (git clone of this repo; pushes with a repo-scoped deploy key via the `github-docs-kb` SSH alias).
- Pushed changes reach the server within the hour via `sincronizar.sh`, which restarts `mcp_docs_kb_http_core` if `mcp_server.py` changed (code is volume-mounted). The FAISS index and section index hot-reload; no restart needed after re-indexing.
- Embedding model must match between collector and server; it is recorded in `index/embeddings-info.json`.
- The server must not modify tracked files (it would break `git pull --ff-only` in `sincronizar.sh`). Cron and manual collection scripts share `flock /tmp/docs-kb-collector.lock`.
- The server has rebooted abruptly several times (power/hardware); everything server-side is designed to resume (hourly sync, checkpointed embedding cache).
- Never edit a shell script on the server while it is running (bash reads scripts incrementally).
