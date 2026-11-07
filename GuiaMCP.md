# Guía de Conexión — docs-kb MCP Server

**Última actualización:** 2026-11-07 · Cliente: Linux (Arch) · Servidor: Ubuntu (`ssh server`)

Este documento es autocontenido: explica cómo conectar Claude Code al servidor MCP de documentación técnica y cómo verificar que funciona.

---

## Qué es este servidor

**docs-kb** es un servidor MCP que expone documentación técnica pública indexada (25 tecnologías: Python, pandas, numpy, matplotlib, scikit-learn, PyTorch, TensorFlow, Keras, R/tidyverse, React, MDN CSS/HTML/JavaScript, n8n, etc.). Devuelve solo las secciones relevantes, sin traer documentos completos al contexto. Solo contiene documentación técnica: ningún contenido personal.

- **Fuente única de verdad:** el repositorio público [github.com/adolfo-s-rey-b/docs-kb](https://github.com/adolfo-s-rey-b/docs-kb). Toda la documentación está en `sources/<tecnología>/markdown/` y se puede leer directamente allí, sin usar el MCP.
- Corre en el servidor Ubuntu (`~/server-stack/docs-kb`, que es un clon del repo; container `mcp_docs_kb_http_core`). Cada semana el collector actualiza la documentación y la publica en el repo.
- Se expone a internet por Cloudflare Tunnel → nginx (Bearer token) → `:8765`.
- Búsqueda semántica FAISS **multilingüe** (`paraphrase-multilingual-MiniLM-L12-v2`): las consultas en español encuentran documentación en inglés.
- Arquitectura completa del servidor: [SistemaDocumentación.md](SistemaDocumentación.md).

---

## Configuración del cliente

### 1. Token

El token **no** se escribe en los documentos. Vive en `.env` (permisos `600`, excluido de git):

```bash
cp .env.example .env && chmod 600 .env   # y completar DOCS_KB_TOKEN
set -a; . ./.env; set +a                 # cargarlo en la shell actual
```

Si no lo tienes, está en el servidor (configuración de nginx):

```bash
ssh server "grep -oP 'expected_key\s+\"Bearer \K[0-9a-f]+' ~/server-stack/nginx/conf.d/mcp-docs-proxy.conf"
```

### 2. Registrar el servidor MCP en Claude Code

> ⚠️ Claude Code **no lee** `~/.claude/mcp.json` (era el error de las guías anteriores). Usa `claude mcp add`, que guarda la configuración en `~/.claude.json`.

```bash
claude mcp add --transport http --scope user docs-kb \
  https://mcp-documentacion.adolfo-s-rey-b.com/mcp \
  --header "Authorization: Bearer $DOCS_KB_TOKEN"
```

- `--scope user`: disponible en todos los proyectos.
- Verificar: `claude mcp get docs-kb` → `Status: ✔ Connected`.
- Quitar: `claude mcp remove docs-kb -s user`.

### 3. Reiniciar Claude Code

Cierra y abre Claude Code (o la extensión de VS Code). Deben aparecer 8 tools con prefijo `mcp__docs-kb__`:

| Tool | Uso |
| --- | --- |
| `docs_search` | Búsqueda semántica + keyword (`query`, `technology?`, `max_results?`, `version?`) |
| `docs_list_technologies` | Lista las tecnologías con páginas y fecha de actualización |
| `docs_get_section` | TOC de una página o una sección específica (`technology`, `slug`, `section?`) |
| `docs_changelog` | Cambios recientes (`technology?`, `days?`) |
| `docs_fetch_live` | Fetch en tiempo real de una URL vía Firecrawl (`url`, `query?`) |
| `docs_status` | Estado global: FAISS, modelo, caché, tecnologías, disco |
| `docs_version_history` | Snapshots de versiones de una tecnología |
| `docs_generate_context` | Cheatsheet, migration notes o summary (`technologies`, `context_type`) |

**Patrón recomendado:** `docs_search` → tomar `tech` y `slug` del resultado → `docs_get_section` sin `section` (TOC) → `docs_get_section` con la sección.

---

## Verificación

### Chequeo automático (recomendado)

```bash
./chequeo_remoto.sh              # 12 pruebas, tabla PASS/WARN/FAIL
./chequeo_remoto.sh --md         # además: resultados/chequeo-AAAA-MM-DD.md
```

Ejecuta las 12 pruebas de abajo vía JSON-RPC contra el endpoint público. Código de salida = número de FAIL. Resultados más recientes: [ConclusionesSD.md](ConclusionesSD.md).

### Conectividad manual

El transporte streamable-http exige el header `Accept` con **ambos** tipos y un `initialize` antes de cualquier otro método. Sin ellos el servidor responde **406** o **400**.

```bash
curl -s -D - -o /dev/null -X POST https://mcp-documentacion.adolfo-s-rey-b.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer $DOCS_KB_TOKEN" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":0}' \
  | grep -iE "^HTTP|mcp-session-id"
```

**Esperado:** `HTTP/2 200` y un `mcp-session-id`.

---

## Las 12 pruebas remotas

Se pueden ejecutar a mano llamando los tools desde Claude Code, o todas juntas con `./chequeo_remoto.sh`.

| # | Llamada | Indicador de éxito |
| --- | --- | --- |
| 1 | (lista de tools) | 8 tools `docs_*` |
| 2 | `docs_status()` | `FAISS Search: Active (N vectors indexed, paraphrase-multilingual-MiniLM-L12-v2)` |
| 3 | `docs_list_technologies()` | Sin error; 25 tecnologías, todas con páginas |
| 4 | `docs_search(query="str_detect", technology="stringr")` | 1–5 resultados `[stringr] … > str_detect()` |
| 5 | `docs_search(query="combinar tablas por columna comun")` | Top-3 con `pandas`/`dplyr`/`tidyr` (merge/join) aunque la query no diga "merge" ni "join" |
| 6 | `docs_get_section(technology="stringr", slug="articles-stringr")` | TOC con headings y rangos de líneas |
| 7 | `docs_get_section(technology="stringr", slug="articles-stringr", section="<una sección del TOC>")` | Markdown de esa sección (p. ej. `Tasks`) |
| 8 | `docs_generate_context(technologies="numpy", context_type="summary")` | N páginas de numpy y fecha de actualización reciente |
| 9 | `docs_generate_context(technologies="pandas", context_type="cheatsheet")` | Quick reference de pandas con contenido |
| 10 | `docs_version_history(technology="stringr")` | `Current: v… (fecha, N pages)` |
| 11 | `docs_changelog(days=30)` | Lista de cambios o `No changes in the last 30 days.` |
| 12 | `docs_fetch_live(url="https://stringr.tidyverse.org/reference/str_detect.html", query="pattern")` | Markdown de la página filtrado por "pattern" |

> Prueba 7: usa un heading que aparezca en el TOC de la prueba 6 (la sección "Basic usage" de versiones anteriores de esta guía no existe). El script lo hace automáticamente.

---

## Qué se prueba desde dónde

| Desde el cliente (este equipo) | Solo en el servidor (`ssh server`) |
| --- | --- |
| Las 12 pruebas de arriba (`./chequeo_remoto.sh`) | [ChequeoSD.md](ChequeoSD.md) Secciones 1–7, 9–12: Docker, `localhost:8765`, nginx, archivos FAISS, collector, error hook, cron, publicación en GitHub, rendimiento |
| | Sección 8 (skills `/docs-search`, `/docs-context`…): viven en `~/server-stack/.claude/skills` y solo existen en sesiones de Claude Code abiertas en el servidor |

---

## Troubleshooting

| Síntoma | Causa / solución |
| --- | --- |
| `406 Not Acceptable` | Falta `Accept: application/json, text/event-stream` |
| `400` / "Missing session ID" | No se hizo `initialize` o no se envía `mcp-session-id` |
| `401` | Falta el header `Authorization` |
| `403` | Token incorrecto (revisa `.env` y `claude mcp get docs-kb`) |
| `000` / timeout | Servidor apagado o túnel Cloudflare caído: `ssh server "docker ps \| grep -E 'cloudflared\|nginx_firecrawl\|mcp_docs'"` |
| Tools `mcp__docs-kb__*` no aparecen | Registrar con `claude mcp add` (no `~/.claude/mcp.json`) y reiniciar Claude Code |
| `FAISS Search: … not loaded` | En el servidor: `docker restart mcp_docs_kb_http_core` y revisar `docker logs mcp_docs_kb_http_core` |
| `docs_fetch_live` falla | Firecrawl caído: `ssh server "cd ~/server-stack && docker compose up -d firecrawl_api firecrawl_playwright"` |
| `docs_search` vacío | Confirmar la tecnología con `docs_list_technologies()`; probar sin filtro `technology` |

---

## Referencia rápida

```text
URL:            https://mcp-documentacion.adolfo-s-rey-b.com/mcp
Token:          $DOCS_KB_TOKEN (archivo .env, nunca en los documentos)
Transporte:     streamable-http (MCP 2024-11-05)
Tools:          8 (prefijo mcp__docs-kb__)
Tecnologías:    25 (solo documentación técnica pública)
Repositorio:    https://github.com/adolfo-s-rey-b/docs-kb
Embeddings:     paraphrase-multilingual-MiniLM-L12-v2 (384d, FAISS)
Chequeo:        ./chequeo_remoto.sh   ·   servidor: ChequeoSD.md
SSH servidor:   ssh server  (alias local, red interna)
```
