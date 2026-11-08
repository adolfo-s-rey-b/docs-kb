# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

`docs-kb`: a public knowledge base of technical documentation (25 technologies, Markdown in `sources/<tech>/markdown/`) plus the MCP server that indexes it (FAISS multilingual semantic search, 8 tools). **Everything depends only on GitHub**: GitHub Actions re-collects the docs weekly and commits them here, builds the semantic index and publishes the local-MCP package to the `datos` Release; users run the MCP locally through the Claude Code plugin in `plugin/` (this repo is also a plugin marketplace). The old self-hosted server is legacy. All documentation is in Spanish.

**Only public technical documentation belongs here.** Never add personal notes, server configs, tokens, internal IPs or anything private — everything under `sources/` (and the `datos` Release) is public.

## Layout

- `mcp_server.py` — MCP server (8 tools; stdio locally, streamable-http on the legacy server). Logs must go to stderr (stdout is the MCP channel)
- `collector.py` — collects docs via Firecrawl (+ Playwright) or from a GitHub repo (`source_type: "github"`, used for React), discovery map → objects.inv → sitemap → crawl, builds `index/` (section index + FAISS; `DOCS_KB_FAISS_INDEX=sq8` for the 8-bit index)
- `config.json` — the 25 technologies (`max_pages: 0` = no limit; `"recolectar_en": "congelada"` = not collected, anaconda)
- `.github/workflows/actualizar-docs.yml` — weekly collection (one job per tech, ephemeral Firecrawl + Playwright from `.github/firecrawl/docker-compose.yml`), then calls `datos.yml`
- `.github/workflows/datos.yml` + `.github/scripts/` — incremental index build, changelog from git, package `docs-kb-datos.tar.gz` + `version.json` + `embeddings-cache.npz` → Release `datos`
- `.claude-plugin/marketplace.json`, `plugin/` — the plugin: `docs_kb_local.py` (stdlib-only launcher: install/update/serve/ensure/status/check), SessionStart hook, `/docs-kb:actualizar`, `/docs-kb:estado`, skill
- `requirements-local.txt` — pinned deps of the local MCP (`fastembed==0.8.0` must match the index build; `mcp<2`)
- `sources/<tech>/markdown/*.md` + `manifest.json` — the collected documentation (generated; don't hand-edit)
- Legacy server only: `sincronizar.sh`, `actualizar.sh`, `publicar.sh`, `recoleccion_completa.sh`, `Dockerfile.http`, `requirements.txt`, `error_hook.py`, `chequeo_remoto.sh`
- Not versioned: `.env`, `.venv/`, `index/`, `logs/`, `dist/`, `sources/*/html/`, `changelog/`

Architecture and maintenance: [SistemaDocumentación.md](SistemaDocumentación.md). User guide: [GuiaMCP.md](GuiaMCP.md). Latest results: [ConclusionesSD.md](ConclusionesSD.md). Licenses: [ATTRIBUTION.md](ATTRIBUTION.md).

## Local MCP (primary)

```bash
python3 plugin/docs_kb_local.py install   # or: /plugin install docs-kb --marketplace adolfo-s-rey-b/docs-kb
python3 plugin/docs_kb_local.py check     # 12 end-to-end tests over stdio; exit code 0 = all pass
claude plugin validate .                  # marketplace + plugin manifests
```

Data dir: `$DOCS_KB_HOME`, `${CLAUDE_PLUGIN_DATA}` (plugin) or `~/.local/share/docs-kb`. The plugin intentionally has no `version` (tracks commits). After changing `mcp_server.py`, `collector.py`, `config.json` or `requirements-local.txt`, a push triggers `datos.yml`, which republishes the package; clients pick it up within 12 h.

## Legacy remote endpoint (self-hosted server, to be retired)

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
