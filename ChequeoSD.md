# Chequeo del Sistema docs-kb

**Fecha de actualizacion:** 2026-11-07

Pruebas para verificar el correcto funcionamiento del sistema docs-kb despues de cualquier modificacion, reinicio de servicios, o como healthcheck periodico. **Se ejecutan en el servidor** (`ssh server`). Desde el cliente, las 12 pruebas remotas se corren con `./chequeo_remoto.sh` (ver GuiaMCP.md).

Las pruebas que usan el proxy necesitan el token en la variable `DOCS_KB_TOKEN` (nunca escribirlo en este documento):

```bash
export DOCS_KB_TOKEN=$(grep -oP 'expected_key\s+"Bearer \K[0-9a-f]+' ~/server-stack/nginx/conf.d/mcp-docs-proxy.conf)
```

---

## Verificacion Rapida (1 bloque)

```bash
cd ~/server-stack/docs-kb && \
echo "=== 1. Docker services ===" && docker ps --filter name=mcp_docs_kb_http_core --filter name=nginx_firecrawl_proxy --filter name=firecrawl_core --filter name=firecrawl_playwright --format "{{.Names}}: {{.Status}}" && \
echo "=== 2. HTTP server (8765) ===" && \
  SESSION=$(curl -s -D - -X POST http://localhost:8765/mcp \
    -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
    -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":0}' \
    | grep -i "mcp-session-id" | awk '{print $2}' | tr -d '\r') && \
  curl -s -X POST http://localhost:8765/mcp \
    -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
    -H "mcp-session-id: $SESSION" \
    -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' \
    | grep "^data:" | python3 -c "import json,sys; d=json.loads(sys.stdin.read().replace('data: ','',1)); print(f'{len(d[\"result\"][\"tools\"])} tools')" && \
echo "=== 3. FAISS index ===" && ls index/embeddings.faiss && python3 -c "import json; m=json.load(open('index/embeddings-meta.json')); i=json.load(open('index/embeddings-info.json')); print(f'{len(m)} vectores, modelo {i[\"model\"]}')" && \
echo "=== 4. Section index ===" && python3 -c "import json; d=json.load(open('index/section-index.json')); print(f'{len(d)} archivos, {sum(len(v) for v in d.values())} secciones')" && \
echo "=== 5. Error hook ===" && echo '{"tool_result":{"stderr":"ModuleNotFoundError: No module named x"}}' | python3 error_hook.py && \
echo "=== 6. Cron ===" && crontab -l 2>/dev/null | grep -c docs-kb && echo "cron job(s)" && \
echo "=== CHEQUEO COMPLETO ==="
```

**Resultado esperado:**

- 4 containers Up (mcp_docs_kb_http_core, nginx_firecrawl_proxy, firecrawl_core, firecrawl_playwright)
- 8 tools
- embeddings.faiss existe, N vectores, modelo `paraphrase-multilingual-MiniLM-L12-v2`
- >500 archivos, >2000 secciones
- `NOTA: Error detectado en python...`
- 1 cron job

---

## Prerequisitos

- [ ] Docker services corriendo: `docker ps | grep -E "mcp_docs_kb|nginx_firecrawl"`
- [ ] HTTP server en localhost:8765 accesible
- [ ] FAISS index construido: `ls ~/server-stack/docs-kb/index/embeddings.faiss`
- [ ] Firecrawl (para docs_fetch_live y el collector): `curl -s http://localhost:3002/ | grep Firecrawl`
- [ ] Playwright de Firecrawl (paginas con JavaScript): `docker ps | grep firecrawl_playwright`
- [ ] Venv con fastembed: `.venv/bin/python3 -c "import faiss; import fastembed; print('OK')"`

---

## 1. Docker Services

### 1.1 Containers corriendo

```bash
docker ps --filter name=mcp_docs_kb_http_core --filter name=nginx_firecrawl_proxy \
  --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

**Esperado:** 4 containers Up. `mcp_docs_kb_http_core` con `127.0.0.1:8765->8765/tcp`.

### 1.2 Logs limpios del MCP server

```bash
docker logs mcp_docs_kb_http_core 2>&1 | tail -5
```

**Esperado:** `[docs-kb] FAISS loaded: N vectors, model sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` y `Uvicorn running on http://0.0.0.0:8765`. Sin errores de TypeError o ImportError. (El aviso de fastembed sobre *mean pooling* es normal: es el pooling correcto para este modelo.)

---

## 2. MCP Server HTTP

### 2.1 Responde en localhost:8765

```bash
SESSION=$(curl -s -D - -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":0}' \
  | grep -i "mcp-session-id" | awk '{print $2}' | tr -d '\r')
echo "Session ID: $SESSION"
```

**Esperado:** Session ID de 32 caracteres hexadecimales.

### 2.2 Verifica 8 tools registrados

```bash
curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' \
  | grep "^data:" | python3 -c "
import json,sys
d=json.loads(sys.stdin.read().replace('data: ','',1))
tools=[t['name'] for t in d['result']['tools']]
print(f'{len(tools)} tools: {tools}')
assert len(tools) == 8, f'Expected 8, got {len(tools)}'
print('OK')
"
```

**Esperado:** `8 tools: ['docs_search', 'docs_list_technologies', 'docs_get_section', 'docs_changelog', 'docs_fetch_live', 'docs_status', 'docs_version_history', 'docs_generate_context']`

### 2.3 docs_status (verifica FAISS, cache, tecnologias)

```bash
curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"docs_status","arguments":{}},"id":2}' \
  | grep "^data:" | python3 -c "
import json,sys
d=json.loads(sys.stdin.read().replace('data: ','',1))
print(d['result']['content'][0]['text'][:600])
"
```

**Esperado:** Muestra FAISS como `Active (N vectors indexed, paraphrase-multilingual-MiniLM-L12-v2)`, technologies configuradas, cache stats.

### 2.4 docs_search con busqueda semantica

```bash
# Primera busqueda (cache miss)
time curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"docs_search","arguments":{"query":"combinar tablas filas"}},"id":3}' \
  | grep "^data:" | python3 -c "
import json,sys
d=json.loads(sys.stdin.read().replace('data: ','',1))
text=d['result']['content'][0]['text']
print(text[:400])
assert 'Result' in text, 'No results'
print('OK: semantic search works')
"

# Segunda busqueda (debe ser mas rapida por cache)
time curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"docs_search","arguments":{"query":"combinar tablas filas"}},"id":4}' \
  | grep "^data:" > /dev/null && echo "Cache hit (segunda llamada mas rapida)"
```

**Esperado:** Primera busqueda < 5s. Segunda < 1s (cache).

### 2.5 docs_version_history

```bash
curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"docs_version_history","arguments":{"technology":"stringr"}},"id":5}' \
  | grep "^data:" | python3 -c "
import json,sys; d=json.loads(sys.stdin.read().replace('data: ','',1)); print(d['result']['content'][0]['text'][:300])
"
```

### 2.6 docs_generate_context

```bash
curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"docs_generate_context","arguments":{"technologies":"numpy","context_type":"summary"}},"id":6}' \
  | grep "^data:" | python3 -c "
import json,sys; d=json.loads(sys.stdin.read().replace('data: ','',1)); print(d['result']['content'][0]['text'][:400])
"
```

**Esperado:** Muestra el summary de numpy (paginas, version, fecha de actualizacion).

---

## 3. Nginx Proxy (Bearer Token Auth)

### 3.1 Sin token → 401

```bash
NGINX_IP=$(docker inspect nginx_firecrawl_proxy | python3 -c "
import json,sys; d=json.load(sys.stdin)[0]
print(d['NetworkSettings']['Networks']['server-stack_agentic_automation_net']['IPAddress'])")
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://$NGINX_IP:8766/mcp
```

**Esperado:** `HTTP 401`

### 3.2 Token incorrecto → 403

```bash
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://$NGINX_IP:8766/mcp \
  -H "Authorization: Bearer token-incorrecto"
```

**Esperado:** `HTTP 403`

### 3.3 Token correcto → 8 tools via proxy

```bash
SESS_PROXY=$(curl -s -D - -X POST http://$NGINX_IP:8766/mcp \
  -H "Host: mcp-documentacion.adolfo-s-rey-b.com" \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer $DOCS_KB_TOKEN" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":0}' \
  | grep -i "mcp-session-id" | awk '{print $2}' | tr -d '\r') && echo "Proxy session: $SESS_PROXY" && \
curl -s -X POST http://$NGINX_IP:8766/mcp \
  -H "Host: mcp-documentacion.adolfo-s-rey-b.com" \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer $DOCS_KB_TOKEN" \
  -H "mcp-session-id: $SESS_PROXY" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' \
  | grep "^data:" | python3 -c "
import json,sys; d=json.loads(sys.stdin.read().replace('data: ','',1)); print(f'PROXY OK: {len(d[\"result\"][\"tools\"])} tools')"
```

**Esperado:** `PROXY OK: 8 tools`

### 3.4 Subdominio publico (requiere cloudflare activo)

```bash
curl -s -o /dev/null -w "HTTP %{http_code}\n" \
  https://mcp-documentacion.adolfo-s-rey-b.com/mcp \
  -X POST -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer $DOCS_KB_TOKEN" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":0}'
```

**Esperado:** HTTP 200 (con session ID en headers de respuesta).

---

## 4. FAISS Index

### 4.1 Archivos existen

```bash
ls -lh ~/server-stack/docs-kb/index/embeddings.faiss ~/server-stack/docs-kb/index/embeddings-meta.json
cat ~/server-stack/docs-kb/index/embeddings-info.json
```

**Esperado:** Ambos archivos existen. `embeddings.faiss` > 1MB. `embeddings-info.json` indica `model`, `normalized: true` y el numero de vectores. El servidor recarga el indice solo cuando cambia (no hace falta reiniciar el container).

### 4.2 Vectores indexados

```bash
python3 -c "
import json
meta = json.load(open('$HOME/server-stack/docs-kb/index/embeddings-meta.json'))
print(f'{len(meta)} vectores')
techs = set(e['tech'] for e in meta)
print(f'{len(techs)} tecnologias: {sorted(techs)[:5]}...')
"
```

**Esperado:** >2000 vectores, >10 tecnologias.

### 4.3 Busqueda semantica funciona (sinonimos)

Desde Claude Code (servidor) o con `docs_search` desde el cliente:

```text
/docs-search combinar dataframes por columna comun
```

**Esperado:** Debe encontrar resultados de `merge` o `join` en pandas/dplyr aunque esas palabras no esten en la query (el modelo multilingue cruza espanol -> ingles).

---

## 5. Contenido indexado (solo documentacion tecnica)

### 5.1 Sin fuentes personales

```bash
cd ~/server-stack/docs-kb && python3 -c "
import json; c=json.load(open('config.json'))['technologies']
local=[k for k,v in c.items() if v.get('source_type')=='local']
print(len(c), 'tecnologias;', 'fuentes locales:', local or 'ninguna')"
ls sources | wc -l
```

**Esperado:** 25 tecnologias, `fuentes locales: ninguna`, 25 carpetas en `sources/`. Desde 2026-11-07 docs-kb solo indexa documentacion tecnica publica; las notas de Obsidian y el stack Docker se retiraron (todo lo personal queda fuera del repositorio publico y del MCP).

---

## 6. Collector

### 6.1 Index-only con FAISS

```bash
cd ~/server-stack/docs-kb && \
.venv/bin/python3 collector.py --index-only && grep -E "Section index|FAISS index|Tech map" logs/collector.log | tail -3
```

**Esperado:**

```text
Section index: N files indexed.
FAISS index: N vectors, 384d. Saved to .../embeddings.faiss
Tech map: N aliases mapped.
```

### 6.2 Recoleccion idempotente

```bash
.venv/bin/python3 collector.py --tech jupyterlab --no-index && grep "TOTAL" logs/collector.log | tail -1
```

**Esperado:** `new: 0, updated: 0, unchanged: N, failed: 0` en la segunda corrida (las paginas no cambiaron). Con `--max-age-days 7` las paginas recientes se cuentan en `skipped` sin descargarse.

> Desde 2026-11-07 el collector solo escribe a stdout cuando corre en una terminal; en cron todo va a `logs/collector.log` (antes cada linea quedaba duplicada).

### 6.3 Reporte de estado

```bash
.venv/bin/python3 collector.py --report 2>&1 | tail -3 && head -20 ~/server-stack/docs-kb/ESTADO.md
```

**Esperado:** `ESTADO.md` generado con tabla de tecnologias.

### 6.4 Verificacion de actualizaciones (check)

```bash
.venv/bin/python3 collector.py --check --tech stringr 2>&1 | tail -5
```

**Esperado:** "Up to date: stringr" o "UPDATE AVAILABLE".

---

## 7. Error Hook

### 7.1 Detectar error Python

```bash
echo '{"tool_result": {"stdout": "", "stderr": "Traceback (most recent call last):\n  File \"test.py\", line 1\nModuleNotFoundError: No module named x"}}' | python3 ~/server-stack/docs-kb/error_hook.py
```

**Esperado:** `NOTA: Error detectado en python. Busqueda rapida: /docs-search python ModuleNotFoundError | Analisis detallado: /docs-debug-agent`

### 7.2 Detectar error pandas

```bash
echo '{"tool_result": {"stderr": "KeyError: Column nonexistent not found in DataFrame"}}' | python3 ~/server-stack/docs-kb/error_hook.py
```

**Esperado:** Detecta `pandas`, no `python`.

### 7.3 Sin error (silencioso)

```bash
echo '{"tool_result": {"stdout": "Hello World", "stderr": ""}}' | python3 ~/server-stack/docs-kb/error_hook.py; echo "exit: $?"
```

**Esperado:** Sin output, exit 0.

### 7.4 JSON invalido (robusto)

```bash
echo 'not json' | python3 ~/server-stack/docs-kb/error_hook.py; echo "exit: $?"
```

**Esperado:** Sin output, exit 0.

---

## 8. Skills

Estas pruebas requieren sesion interactiva de Claude Code **en el servidor** (los skills viven en `~/server-stack/.claude/skills`). Desde el cliente, usar los tools `mcp__docs-kb__*` equivalentes.

### 8.1 /docs-search (busqueda basica)

```text
/docs-search stringr str_detect
```

**Esperado:** Resultados de documentacion de str_detect.

### 8.2 /docs-search (busqueda semantica)

```text
/docs-search combinar tablas filas columnas
```

**Esperado:** Resultados de merge/join en pandas o dplyr.

### 8.3 /docs-context (cheatsheet)

```text
/docs-context pandas cheatsheet
```

**Esperado:** Quick Reference con funciones clave de pandas.

### 8.4 /docs-context (summary)

```text
/docs-context numpy summary
```

**Esperado:** Lista de paginas indexadas de numpy.

### 8.5 /docs-load

```text
/docs-load
```

**Esperado:** Detecta tecnologias del proyecto, reporta documentacion disponible.

### 8.6 /docs-changelog

```text
/docs-changelog 30
```

**Esperado:** Cambios de los ultimos 30 dias (puede ser vacio si nada cambia).

---

## 9. Integracion

### 9.1 .mcp.json usa HTTP

```bash
python3 -c "
import json
d = json.load(open('$HOME/server-stack/.mcp.json'))
entry = d['mcpServers']['docs-kb']
print('type:', entry.get('type'))
print('url:', entry.get('url'))
assert entry.get('type') == 'http', 'Should be HTTP transport'
assert '8765' in entry.get('url',''), 'Should point to port 8765'
print('OK')
"
```

**Esperado:** `type: http`, `url: http://localhost:8765/mcp`

### 9.2 Cron usa venv Python

```bash
crontab -l | grep docs-kb
```

**Esperado:** Contiene `.venv/bin/python3` (no `python3` del sistema).

### 9.3 Error hook configurado

```bash
python3 -c "
import json
d = json.load(open('$HOME/server-stack/.claude/settings.local.json'))
bash_hooks = [h for h in d['hooks']['PostToolUse'] if h['matcher'] == 'Bash']
print(f'{len(bash_hooks)} Bash PostToolUse hooks')
has_error_hook = any('error_hook.py' in h['hooks'][0]['command'] for h in bash_hooks)
print(f'Error hook present: {has_error_hook}')
"
```

**Esperado:** `1 Bash PostToolUse hooks`, `Error hook present: True`

---

## 10. Rendimiento

### 10.1 Tiempo de busqueda (< 3s primera vez, < 0.5s cached)

```bash
SESSION=$(curl -s -D - -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":0}' \
  | grep -i "mcp-session-id" | awk '{print $2}' | tr -d '\r')
echo "--- Primera busqueda (FAISS + keyword) ---"
time curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"docs_search","arguments":{"query":"groupby aggregate","technology":"pandas"}},"id":1}' > /dev/null
echo "--- Segunda busqueda (cache) ---"
time curl -s -X POST http://localhost:8765/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"docs_search","arguments":{"query":"groupby aggregate","technology":"pandas"}},"id":2}' > /dev/null
```

**Esperado:** Primera < 5s, segunda < 1s.

### 10.2 Tamano en disco

```bash
du -sh ~/server-stack/docs-kb/sources/ --exclude='.venv' 2>/dev/null || du -sh ~/server-stack/docs-kb/sources/
du -sh ~/server-stack/docs-kb/index/
```

**Esperado:** sources/ proporcional a techs recolectadas. index/ < 20 MB (incluye FAISS).

---

## 11. Descubrimiento de paginas (collector)

Firecrawl self-hosted `/v1/map` solo conoce URLs de un sitemap; los sitios sin sitemap (pandas, numpy, python...) devolvian 0 URLs y nunca se recolectaban. `discover_pages()` prueba estrategias en orden y usa la primera que da URLs que pasan `map_filters`: `map` -> `inventory` (Sphinx `objects.inv`) -> `sitemap` (xml/indice/.gz) -> `crawl` (BFS sobre links de paginas renderizadas por Firecrawl + Playwright). Por tecnologia se puede fijar `discovery`, `inventory_url`, `sitemap_url`, `crawl_start`, `crawl_depth`, `crawl_max_fetch` en `config.json`.

### 11.1 Estrategia usada por tecnologia

```bash
grep -E "discovery '.*' ->" ~/server-stack/docs-kb/logs/collector.log | tail -30
```

**Esperado:** Una linea por tecnologia web con la estrategia que funciono y cuantas paginas se seleccionaron.

### 11.2 Playwright de Firecrawl (paginas con JavaScript)

```bash
curl -s -X POST localhost:3002/v1/scrape -H "Content-Type: application/json" \
  -d '{"url":"https://react.dev/learn","formats":["markdown","links"]}' \
  | python3 -c "import json,sys; d=json.load(sys.stdin)['data']; print(len(d['markdown']), 'chars,', len(d['links']), 'links')"
docker logs firecrawl_core 2>&1 | grep -c "Scrape via playwright deemed successful"
```

**Esperado:** >5000 chars y >10 links; contador de playwright > 0.

### 11.3 Re-descubrir una tecnologia

```bash
cd ~/server-stack/docs-kb && .venv/bin/python3 collector.py --tech pandas --discover
```

**Esperado:** En el log, `pandas: discovery 'inventory' -> N pages`. `--tech` acepta una lista separada por comas (`--tech pandas,numpy`) y reconstruye el indice una sola vez al final.

---

## 12. Publicacion en GitHub (fuente unica de verdad)

`~/server-stack/docs-kb` es un clon de [github.com/adolfo-s-rey-b/docs-kb](https://github.com/adolfo-s-rey-b/docs-kb). `actualizar.sh` (cron) corre el collector y luego `publicar.sh`, que hace `pull --rebase`, commit de `sources/` + `config.json` y push con la deploy key `~/.ssh/docs-kb-deploy` (alias SSH `github-docs-kb`, escritura solo en ese repo).

### 12.1 Deploy key y remoto

```bash
ssh -T github-docs-kb 2>&1 | head -1
cd ~/server-stack/docs-kb && git remote -v | head -1 && git status -sb | head -1
```

**Esperado:** `Hi adolfo-s-rey-b/docs-kb! You've successfully authenticated...`; remoto `git@github-docs-kb:adolfo-s-rey-b/docs-kb.git`; rama `main...origin/main` sin commits pendientes.

### 12.2 Ultima publicacion

```bash
tail -3 ~/server-stack/docs-kb/logs/publicar.log
git -C ~/server-stack/docs-kb log --oneline -3
```

**Esperado:** `publicado: N archivos` o `sin cambios que publicar` despues de cada corrida del cron.

### 12.3 Nada personal en el repo

```bash
cd ~/server-stack/docs-kb && git ls-files | grep -iE "obsidian|docker-stack|\.env$|settings.local" ; echo "coincidencias: $?"
git grep -nE "Bearer [0-9a-f]{20,}|192\.168\." ; echo "coincidencias: $?"
```

**Esperado:** ambos `coincidencias: 1` (grep no encontro nada).
