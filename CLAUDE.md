# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

`docs-kb`: a public knowledge base of technical documentation (25 technologies, Markdown in `sources/<tech>/markdown/`) plus the MCP server that indexes it (FAISS multilingual semantic search, 8 tools). This repo is the single source of truth: the server is a clone that re-collects the docs weekly and pushes them back here. All documentation is in Spanish.

**Only public technical documentation belongs here.** Never add personal notes, server configs, tokens, internal IPs or anything private — `publicar.sh` pushes everything under `sources/` to the public repo.

## Layout

- `mcp_server.py` — MCP server (8 tools, streamable-http on :8765 in Docker)
- `collector.py` — collects docs via Firecrawl (+ Playwright), discovery map → objects.inv → sitemap → crawl, builds `index/` (section index + FAISS)
- `config.json` — the 25 technologies (base URL, exclude patterns, discovery overrides; `max_pages: 0` = no limit)
- `actualizar.sh` / `publicar.sh` / `recoleccion_completa.sh` — cron wrapper, git publish, full parallel collection
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
- After changing `mcp_server.py`: `git pull` there and `docker restart mcp_docs_kb_http_core` (code is volume-mounted). The FAISS index and section index hot-reload; no restart needed after re-indexing.
- Embedding model must match between collector and server; it is recorded in `index/embeddings-info.json`.
- Long runs: `setsid nohup ./recoleccion_completa.sh > logs/recoleccion-FECHA.out 2>&1 &`. Cron and collection scripts share `flock /tmp/docs-kb-collector.lock`.
- Never edit a shell script on the server while it is running (bash reads scripts incrementally).
