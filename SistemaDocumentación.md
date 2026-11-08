# Sistema de Documentacion docs-kb

**Ultima actualizacion:** 2026-11-08

> Repositorio publico y fuente unica de verdad: [github.com/adolfo-s-rey-b/docs-kb](https://github.com/adolfo-s-rey-b/docs-kb). El servidor (`~/server-stack/docs-kb/`) es un clon que publica cada actualizacion de la documentacion. docs-kb contiene **solo documentacion tecnica publica**: ningun contenido personal.

---

## 1. Proposito

Repositorio local de documentacion tecnica para Claude Code. Protege la ventana de contexto retornando solo secciones relevantes, en lugar de documentos completos. Incluye busqueda semantica multilingue via FAISS: una consulta en espanol encuentra documentacion en ingles aunque los terminos sean distintos.

**Acceso:**

- **Local (servidor Ubuntu):** `http://localhost:8765/mcp` (sin auth, dentro de la red)
- **Remoto (cliente Linux, Claude Code):** `https://mcp-documentacion.adolfo-s-rey-b.com/mcp` (Bearer token requerido; ver GuiaMCP.md)

---

## 2. Arquitectura

```text
[Documentacion tecnica publica de 25 tecnologias]
         |
         v Firecrawl + Playwright (efimeros, uno por job)
    +-----------------------------------------------------------------------------------+
    |  GitHub Actions: .github/workflows/actualizar-docs.yml (domingos; dia 1 + discover)|
    |  - 1 job por tecnologia: collector.py --tech T --max-age-days 28 --no-index       |
    |  - Descubre paginas: map -> objects.inv -> sitemap -> crawl BFS                   |
    |  - Job final: un commit "docs: actualizacion automatica" (docs-kb-bot) en main    |
    +-----------------------------------------------------------------------------------+
                 |
                 v github.com/adolfo-s-rey-b/docs-kb  (fuente unica de verdad: sources/)
                 |
                 v git pull cada hora (sincronizar.sh, cron del servidor)
    +-----------------------------------------------------------------------------------+
    |  Servidor (~/server-stack/docs-kb = clon del repo)                                |
    |  - collector.py --index-only: section-index.json + embeddings.faiss (multilingue, |
    |    cache incremental con checkpoints; reanudable tras un reinicio)                |
    +-----------------------------------------------------------------------------------+
                 |
                 v index/
    +-----------------------------------------------------------------------------------+
    |                 mcp_server.py (Docker container :8765)                            |
    |  Transporte: streamable-http                                                      |
    |  - 8 tools MCP                                                                    |
    |  - Cache LRU (invalidacion por mtime de section-index)                            |
    |  - FAISS con recarga en caliente (mtime de embeddings.faiss)                      |
    |  - Busqueda semantica (fase 0) + keyword (fase 1+2)                               |
    +-----------------------------------------------------------------------------------+
                 |                                    |
          :8765 (interno)                    localhost:8765
                 |                                    |
    +---------------------------+        +--------------------------+
    |  nginx_firecrawl_proxy    |        |  Claude Code (servidor)  |
    |  :8766 Bearer token auth  |        |  .mcp.json type: http    |
    +---------------------------+        +--------------------------+
                 |
                 v
    +---------------------------+
    |  Cloudflare Tunnel        |
    |  mcp-documentacion.       |
    |  adolfo-s-rey-b.com       |
    +---------------------------+
                 |
                 v
    Claude Code (cliente Linux) — claude mcp add --scope user + Bearer token
```

---

## 3. Estructura de Directorios

```text
docs-kb/
+-- mcp_server.py              # MCP server (8 tools, HTTP + stdio)
+-- collector.py               # Recolector (web, FAISS, compression)
+-- error_hook.py              # PostToolUse hook para errores
+-- config.json                # 25 tecnologias configuradas
+-- .github/workflows/actualizar-docs.yml  # Recoleccion semanal en GitHub Actions (mecanismo principal)
+-- .github/firecrawl/docker-compose.yml   # Firecrawl + Playwright efimeros para los jobs
+-- sincronizar.sh             # Servidor (cron cada hora): git pull + reindexado reanudable
+-- actualizar.sh              # Alternativa manual en el servidor: collector.py <args> + publicar.sh
+-- publicar.sh                # pull --rebase, commit de sources/ + config.json, push (deploy key)
+-- recoleccion_completa.sh    # Alternativa manual: recoleccion completa en el servidor, 3 grupos paralelos
+-- requirements.txt           # mcp, requests, fastembed, faiss-cpu, scikit-learn
+-- Dockerfile.http            # Imagen Docker para transporte HTTP (codigo montado por volumen)
+-- .venv/                     # Python 3.12 venv (FastMCP + FAISS + fastembed)
|
+-- sources/                   # Documentacion indexada
|   +-- {tech}/
|       +-- markdown/          # Archivos .md entregados por el MCP
|       +-- html/              # Cache HTML para deteccion de cambios
|       +-- summaries/         # Resumenes LLM (Gemini Flash) para paginas largas
|       +-- manifest.json      # Estado: paginas, version, version_history
|
+-- index/
|   +-- section-index.json     # {tech/slug} -> headings (limpios) + lineas
|   +-- tech-map.json          # Aliases: sklearn->scikit-learn, js->javascript...
|   +-- embeddings.faiss       # Indice FAISS (IndexFlatL2 sobre vectores normalizados)
|   +-- embeddings-meta.json   # Metadatos: tech, slug, section, line_start/end
|   +-- embeddings-info.json   # Modelo usado, dimension, normalized, vectores, fecha
|   +-- embeddings-cache.npy   # Cache de vectores por sha1(texto): solo se codifican secciones nuevas
|   +-- embeddings-cache-keys.json
|
+-- changelog/
|   +-- YYYY-MM-DD.jsonl       # Cambios append-only: hash, version_change, "removed"
|
+-- logs/
|   +-- collector.log          # Logs de recoleccion (sin lineas duplicadas)
|
+-- ESTADO.md                  # Dashboard generado por --report (opcional)
```

Backups: `~/backups/docs-kb-AAAA-MM-DD.tgz` (codigo, config, index, sources), `docker-compose-AAAA-MM-DD.yml`, `crontab-AAAA-MM-DD.txt`.

---

## 4. Tecnologias Configuradas (25)

**Web (via Firecrawl):**
python, pandas, numpy, matplotlib, seaborn, scikit-learn, keras, tensorflow, pytorch, r,
tidyverse, dplyr, tidyr, purrr, stringr, lubridate, ggplot2, rstudio, css, html,
javascript, react, n8n, anaconda, jupyterlab

Fuente y licencia de cada una: `ATTRIBUTION.md`.

**Sin fuentes personales.** Hasta 2026-11-07 docs-kb tambien indexaba notas de Obsidian, el stack Docker y skills de OpenClaw; se retiraron del config, de `sources/`, del indice y del changelog para que todo lo personal quede separado del repositorio publico. El collector aun soporta `source_type: "local"` (carpetas de markdown), pero no hay ninguna configurada.

---

## 5. MCP Server (mcp_server.py)

**Transporte:** streamable-http (Docker, puerto 8765) o stdio
**Inicio HTTP:** `python3 mcp_server.py --transport streamable-http --port 8765`
**Inicio stdio:** `python3 mcp_server.py` (legacy, sin Docker)

### 8 Tools

| Tool | Descripcion | Parametros clave |
| --- | --- | --- |
| `docs_search` | Busqueda semantica + keyword | `query`, `technology?`, `max_results?`, `version?` |
| `docs_list_technologies` | Lista todas las techs con stats | - |
| `docs_get_section` | TOC o seccion especifica | `technology`, `slug`, `section?`, `version?` |
| `docs_changelog` | Cambios recientes | `technology?`, `days?` |
| `docs_fetch_live` | Fetch real-time via Firecrawl | `url`, `query?` |
| `docs_status` | Estado global de la KB (incluye modelo de embeddings) | - |
| `docs_version_history` | Version actual, cambios registrados y enlace al historial de git | `technology` |
| `docs_generate_context` | Cheatsheet/migration/summary | `technologies`, `context_type?` |

### Busqueda en 3 Fases

1. **Fase 0 (semantica FAISS):** Embeddings `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (384d, 50+ idiomas). Cada vector codifica `"{tech} {pagina}: {heading}. {primeros 300 caracteres de la seccion}"`. Vectores normalizados -> similitud coseno, score 0-12. Con filtro `technology` busca 40x mas profundo antes de filtrar. Sin filtro, maximo 2 resultados por tecnologia.
2. **Fase 1 (headings):** Busca terminos en section-index.json, ignorando stopwords (es/en) y palabras de <= 2 letras. Score 4-12 proporcional a la fraccion de terminos encontrados; +5 si tambien coincidio en la fase 0.
3. **Fase 2 (full-text):** Grep en archivos markdown. Solo si fase 0+1 tienen pocos resultados.

Vectores cacheados por `sha1(texto)` en `index/embeddings-cache.npy`: al reindexar solo se codifican secciones nuevas o modificadas (con ~25.000 paginas, codificar todo tomaria horas). El texto incluye el titulo de la pagina (`{tech} {slug}: {heading}. {snippet}`) para que headings genericos como "Parameters" tengan contexto. El modelo se lee de `index/embeddings-info.json` (escrito por el collector), asi servidor e indice siempre coinciden. Si el archivo no existe se asume el indice legacy (`all-MiniLM-L6-v2`). Override: variable `DOCS_KB_EMBED_MODEL` (en ambos procesos).

**Recarga en caliente:** si cambia el mtime de `embeddings.faiss`, el servidor recarga el indice en la siguiente busqueda o `docs_status`. No hace falta reiniciar el container despues del cron.

**Uso de summaries:** Si existe `summaries/{slug}.md`, se usa como excerpt en lugar del markdown completo.

**version parameter:** `docs_search(query, version="2.1.0")` busca en `sources/{tech}/versions/2.1.0/` en lugar de `markdown/`.

### Cache LRU

- Hasta 200 entradas en memoria del proceso
- Invalidacion automatica cuando cambia mtime de `section-index.json`
- `section-index.json` se parsea una vez y se re-lee solo si cambia (el collector lo escribe de forma atomica)
- Aplica a `docs_search` y `docs_get_section`
- Stats disponibles via `docs_status`

### Limites de Contexto

- `MAX_EXCERPT_CHARS = 800` por resultado
- `MAX_TOTAL_CHARS = 4000` por llamada a search

---

## 6. Collector (collector.py)

**Donde corre:** la recoleccion semanal corre en GitHub Actions (seccion 10); en el servidor el collector solo reindexa (`--index-only`, via `sincronizar.sh`). Para FAISS usar `.venv/bin/python3`; en Actions basta `requests` (con `--no-index` no se cargan fastembed ni FAISS). `--time-budget-min N` detiene la descarga de forma ordenada antes del limite de 6 h de cada job.

### CLI completo

```bash
# Recoleccion web
.venv/bin/python3 collector.py --all
.venv/bin/python3 collector.py --tech pandas
.venv/bin/python3 collector.py --tech pandas,numpy,python      # lista: indice se reconstruye 1 vez
.venv/bin/python3 collector.py --tech pandas --discover        # re-descubrir paginas
.venv/bin/python3 collector.py --all --discover --dry-run       # solo contar paginas, sin scrapear
.venv/bin/python3 collector.py --all --max-age-days 28          # re-scrapear solo paginas con >28 dias
.venv/bin/python3 collector.py --tech a,b --no-index            # sin reconstruir indice (corridas paralelas)
.venv/bin/python3 collector.py --add "fastapi" --map-url "https://..." --filters "tutorial/,ref/"

# Indices y FAISS
.venv/bin/python3 collector.py --index-only

# Mantenimiento
.venv/bin/python3 collector.py --compress              # Gemini Flash compression
.venv/bin/python3 collector.py --report                # Genera ESTADO.md
.venv/bin/python3 collector.py --check                 # Verifica versiones (ligero)
```

Recolecciones largas desde el servidor (alternativa manual a GitHub Actions): `setsid nohup ./recoleccion_completa.sh > logs/recoleccion-FECHA.out 2>&1 &` (3 grupos de tecnologias en paralelo, sitios distintos por grupo, `--discover --max-age-days 7 --no-index`, y un solo `--index-only` al final; usa el lock `/tmp/docs-kb-collector.lock`). El manifest se guarda cada 50 paginas, asi que una corrida interrumpida retoma sin repetir trabajo si se usa `--max-age-days`.

### Descubrimiento de paginas

Firecrawl self-hosted `/v1/map` solo devuelve URLs de sitemaps, por eso pandas, numpy, python, react, etc. nunca se recolectaban (0 URLs). `discover_pages()` prueba estrategias en orden y usa la primera con URLs que pasen `map_filters`/`exclude_patterns`; ademas exige que cada URL este bajo `doc_base_url` (mismo dominio y prefijo de ruta).

**Cobertura completa (desde 2026-11-07):** `max_pages: 0` (sin limite) en todas las tecnologias web y sin `map_filters`, salvo `tensorflow` (su `doc_base_url` es la raiz de tensorflow.org: se limita a `api_docs/python/`, `guide/`, `tutorials/`) y `r` (lista de manuales). Los `exclude_patterns` (release notes, indices, comunidad) se mantienen. El descubrimiento del 2026-11-07 encontro ~22.900 paginas en 21 tecnologias (tensorflow 4474, pytorch 3490, numpy 2520, matplotlib 2031, pandas 1756, n8n 1390, javascript 1346, css 1288, scikit-learn 1061...) mas las de crawl. Si se vuelve a usar `max_pages > 0`, el cupo se reparte en round-robin entre los `map_filters`.

| Estrategia | Como funciona | Usada por |
| --- | --- | --- |
| `map` | Firecrawl `/v1/map` (`limit` 100000) | sitios pkgdown con sitemap (dplyr, tidyr, stringr...), n8n, tensorflow, pytorch, tidyverse |
| `inventory` | Sphinx `objects.inv` (zlib): todas las paginas; narrativas y API de primer nivel primero | pandas, numpy, python, matplotlib, seaborn, scikit-learn, jupyterlab, pytorch |
| `sitemap` | `sitemap.xml`, indices y `.gz` leidos directamente | MDN (css, html, javascript) |
| `crawl` | BFS sobre `links` de `firecrawl_scrape` (pagina renderizada con Playwright) | react, rstudio, r, anaconda, keras (su sitemap solo lista 59 URLs) |

Opciones por tecnologia en `config.json`: `discovery` (orden), `inventory_url`, `sitemap_url`, `crawl_start`, `crawl_depth` (6), `crawl_max_fetch` (3000).

### Playwright (Firecrawl)

`firecrawl_playwright` (`ghcr.io/firecrawl/playwright-service`) renderiza paginas con JavaScript; `firecrawl_api` lo usa via `PLAYWRIGHT_MICROSERVICE_URL=http://firecrawl_playwright:3000/scrape`. El container `playwright_mcp_daemon` es otra cosa (MCP interactivo de navegador) y no lo usa el collector.

### Fuentes locales (soportadas, ninguna configurada)

Cualquier fuente local que se agregue queda publicada en el repo publico: no usar para contenido personal.

```json
{
  "source_type": "local",
  "local_path": "/ruta/absoluta/",
  "include_dirs": ["guias/"],
  "exclude_dirs": [".git/", ".trash/"],
  "file_pattern": "*.md"
}
```

Change detection via SHA-256 del contenido (sin Firecrawl). Slugs truncados a 120 chars. Los archivos eliminados o renombrados en la fuente se podan del indice (solo si el escaneo encontro archivos, para no vaciar el indice si la ruta falla). Si `local_path` no existe, el log muestra `Local path not found` y no se toca nada.

### Versiones

La version de cada tecnologia es la mas frecuente entre las paginas descargadas en la corrida (titulo/URL de cada pagina, con umbral: al menos 3 paginas y mayoria). Un cambio se registra en `manifest.json["version_history"]` y el contenido anterior queda en el **historial de git** del repo (`docs_version_history` enlaza a `commits/main/sources/<tech>`). Ya no se hacen copias en `versions/`: la deteccion pagina por pagina generaba snapshots espurios (~3 GB, 105 en matplotlib, por paginas tipo "What's new in 0.40"). `docs_search(version=...)` solo funciona con snapshots locales antiguos, si existieran.

### Indice de secciones

Ademas de `# Titulo`, reconoce los formatos que produce Firecrawl: titulos con ancla permalink (`Titulo[#](url "Link to this heading")`, `Usage[](url#ref-usage)` de pkgdown), subrayados setext (`=====` / `-----`, aunque haya una linea en blanco en medio) y definiciones de API de Sphinx (`firma[#](url "Link to this definition")`). Ignora bloques de codigo. Con solo `# Titulo` quedaban sin secciones la mayoria de paginas de API (numpy: 63 de 2.520); con los tres formatos se indexan ~94 % de las paginas.

### Compresion LLM (Gemini Flash)

- Activa solo si `gemini` esta en PATH
- Paginas > 2000 palabras -> resumen ~500 palabras
- Guardado en `sources/{tech}/summaries/{slug}.md`
- El MCP server usa el resumen como excerpt si existe

### Logging

Siempre a `logs/collector.log`; a stdout solo si corre en una terminal (el cron redirige stdout al mismo archivo y antes duplicaba cada linea). httpx/huggingface en nivel WARNING.

---

## 7. Error Hook (error_hook.py)

**Tipo:** PostToolUse hook, matcher: Bash
**Interprete:** System Python (sin venv)

Output al detectar error:

```text
NOTA: Error detectado en {tech}.
Busqueda rapida: /docs-search {tech} {keyword} | Analisis detallado: /docs-debug-agent
```

Prioridad (mayor a menor): pandas > numpy > scikit-learn > keras > tensorflow > pytorch > matplotlib > seaborn > dplyr > ggplot2 > react > n8n > r > python > javascript > css > html

---

## 8. Skills (servidor: `~/server-stack/.claude/skills`)

| Skill | Descripcion |
| --- | --- |
| `/docs-search` | Busqueda en KB con two-step pattern |
| `/docs-add` | Agregar nueva tecnologia al config y recolectar |
| `/docs-fetch` | Fetch real-time de cualquier URL via Firecrawl |
| `/docs-update` | Actualizar documentacion de una tech |
| `/docs-changelog` | Ver cambios recientes con filtro opcional |
| `/docs-load` | Detectar techs en uso y cargar TOC al inicio |
| `/docs-debug-agent` | Lanzar subagente para analisis detallado de errores |
| `/docs-context` | Generar cheatsheet/migration/summary contextual |

Solo existen en sesiones de Claude Code abiertas en el servidor. En el cliente se usan los tools `mcp__docs-kb__*` directamente.

---

## 9. Infraestructura Docker

### Servicios relevantes

| Servicio | Container | Puerto interno | Proposito |
| --- | --- | --- | --- |
| `mcp_docs_kb_http` | `mcp_docs_kb_http_core` | 8765 | MCP server HTTP (codigo montado: `~/server-stack/docs-kb:/docs-kb`; cache fastembed en volumen `mcp_fastembed_cache`) |
| `nginx_firecrawl_proxy` | `nginx_firecrawl_proxy` | 8766 | Auth proxy Bearer token |
| `cloudflared` | `cloudflared` | - | Tunnel HTTPS a internet |
| `firecrawl_api` | `firecrawl_core` | 3002 | Scraping / map para collector y `docs_fetch_live` |
| `firecrawl_playwright` | `firecrawl_playwright` | 3000 | Render de paginas con JavaScript para Firecrawl |

Cambios en `mcp_server.py`: `docker restart mcp_docs_kb_http_core` (no hace falta rebuild). Cambios en `requirements.txt`: `docker compose build mcp_docs_kb_http && docker compose up -d mcp_docs_kb_http`.

### .mcp.json local (servidor Ubuntu)

```json
"docs-kb": {
  "type": "http",
  "url": "http://localhost:8765/mcp"
}
```

### Cliente remoto (Linux)

```bash
claude mcp add --transport http --scope user docs-kb \
  https://mcp-documentacion.adolfo-s-rey-b.com/mcp \
  --header "Authorization: Bearer $DOCS_KB_TOKEN"
```

---

## 10. Actualizacion automatica (GitHub Actions) y cron del servidor

**Recoleccion: GitHub Actions** (`.github/workflows/actualizar-docs.yml`), sin depender del servidor:

- `schedule`: domingos 03:00 UTC (re-descarga paginas con mas de 28 dias; las nuevas siempre) y dia 1 de cada mes 01:00 UTC (ademas `--discover` para encontrar paginas nuevas).
- `workflow_dispatch` manual con entradas `tecnologias` (lista separada por comas), `descubrir`, `max_age_days` y `publicar` (`gh workflow run actualizar-docs.yml -f tecnologias=pandas -f publicar=false`).
- Un job por tecnologia (hasta 10 en paralelo), cada uno con su Firecrawl + Playwright (`.github/firecrawl/docker-compose.yml`, mismas imagenes que el servidor: el Markdown es identico byte a byte). Postgres debe usar base/usuario `postgres` (lo exige `pg_cron`).
- Job `publicar`: junta los artefactos y hace un unico commit `docs: actualizacion automatica FECHA (N archivos)` como `docs-kb-bot`.
- Carga inicial completa: run 42448781365 (2026-11-08, ~2 h 40 min; el job mas largo fue tensorflow, 4.474 paginas), commit `218313e` con 23.931 archivos.

**Excepcion: react y anaconda** (`"recolectar_en": "servidor"` en `config.json`). react.dev y docs.anaconda.com bloquean las IPs de GitHub Actions (en el run 42502728904: 286 scrapes de React con error 500 y el crawl de Anaconda con 1 sola pagina), mientras que desde el servidor se descargan bien (184 y 26 paginas). El workflow las omite salvo que se pidan explicitamente, y el servidor las recolecta una vez al mes y las publica con su deploy key (ver cron abajo). Si el servidor esta caido ese dia, esperan al mes siguiente; las otras 23 tecnologias no dependen de el.

**Servidor: solo sincroniza** (cron instalado el 2026-11-08):

```text
17 * * * * cd /home/adolfo-s-rey-b/server-stack/docs-kb && flock -n /tmp/docs-kb-collector.lock ./sincronizar.sh >> logs/sincronizar.log 2>&1
43 4 2 * * cd /home/adolfo-s-rey-b/server-stack/docs-kb && flock -w 7200 /tmp/docs-kb-collector.lock ./actualizar.sh --tech react,anaconda --discover --max-age-days 28 --no-index
```

La segunda linea (dia 2 de cada mes, 04:43 UTC) es la recoleccion mensual de react y anaconda desde el servidor; `--no-index` porque la siguiente corrida de `sincronizar.sh` reindexa.

`sincronizar.sh` hace `git pull --ff-only`; si cambio `mcp_server.py` reinicia el container; si cambio algo que afecta al indice (`sources/`, `config.json`, `collector.py`) corre `collector.py --index-only`. El commit indexado se guarda en `index/indexed-commit` solo al terminar, y la cache de embeddings se guarda cada 20.000 secciones: si el servidor se reinicia a mitad, la siguiente hora retoma el reindexado sin repetir trabajo. El MCP recarga indice y secciones en caliente.

`actualizar.sh`, `publicar.sh` y `recoleccion_completa.sh` quedan como alternativa manual para recolectar desde el servidor (por ejemplo si una tecnologia falla en Actions); no correrlos a la vez que el workflow. Backups del crontab: `~/backups/crontab-2026-11-07.txt`.

**Disponibilidad del servidor:** estuvo apagado entre 2026-08-15 y 2026-11-04; el 2026-11-08 tuvo dos caidas abruptas (02:10 y 07:20 UTC, sin secuencia de apagado en el journal: corte de energia o cuelgue). La documentacion del repo no depende de el; el MCP si.

---

## 11. Repositorio GitHub (fuente unica de verdad)

- Repo publico: `github.com/adolfo-s-rey-b/docs-kb`. La documentacion se lee directamente en `sources/<tecnologia>/markdown/*.md`; `sources/<tecnologia>/manifest.json` tiene la URL original, titulo y fecha de cada pagina.
- Servidor: `~/server-stack/docs-kb` es un clon. Remoto `git@github-docs-kb:adolfo-s-rey-b/docs-kb.git`; alias SSH `github-docs-kb` -> deploy key `~/.ssh/docs-kb-deploy` (escritura solo en este repo). Autor de commits: noreply de GitHub.
- Quien escribe en `sources/`: el workflow de GitHub Actions (`docs-kb-bot`). El servidor solo lee (`sincronizar.sh`); `publicar.sh` existe para recolecciones manuales desde el servidor.
- No se versionan (`.gitignore`): `.env`, `.venv/`, `index/` (se reconstruye con `--index-only`), `logs/`, `sources/*/html/` (cache para detectar cambios), `sources/*/versions/` (obsoleto), `changelog/` (estado local; el historial publico es el de git).
- Cambios de codigo o documentacion se hacen en un clon (por ejemplo en el cliente) y se hace push; el servidor los recibe en la siguiente corrida de `sincronizar.sh` (cada hora), que reinicia el container si cambia `mcp_server.py`.

---

## 12. Guia de Modificacion

### Agregar tech web

```bash
.venv/bin/python3 collector.py --add "nombre" --map-url "https://..." --filters "ref/,tutorial/"
```

Si `--add` descubre 0 paginas, revisar en el log que estrategias se probaron y fijar `discovery` / `inventory_url` / `sitemap_url` / `crawl_start` en `config.json`; luego `collector.py --tech nombre --discover`.

### Agregar fuente local

Solo para documentacion publicable (se publica en GitHub). Editar `config.json`, agregar entrada con `source_type: "local"`, luego:

```bash
.venv/bin/python3 collector.py --tech nombre
```

### Reconstruir FAISS / cambiar modelo de embeddings

```bash
.venv/bin/python3 collector.py --index-only      # usa EMBED_MODEL (o DOCS_KB_EMBED_MODEL)
```

El servidor detecta el nuevo indice y el modelo desde `embeddings-info.json`.

### Cambiar Bearer token

Ultima rotacion: 2026-11-07 (el token anterior habia estado en texto plano en la documentacion).

1. Respaldo: `cp -p ~/server-stack/nginx/conf.d/mcp-docs-proxy.conf ~/backups/mcp-docs-proxy.conf-FECHA`
2. `openssl rand -hex 32` (generar nuevo token) y reemplazarlo en la linea `set $expected_key "Bearer <token>"` de ese archivo
3. Validar y recargar sin cortar conexiones: `docker exec nginx_firecrawl_proxy nginx -t && docker exec nginx_firecrawl_proxy nginx -s reload`
4. Cliente: actualizar `DOCS_KB_TOKEN` en `.env` y re-registrar: `claude mcp remove docs-kb -s user` + `claude mcp add ...` (ver GuiaMCP.md); reiniciar Claude Code
5. Verificar: token viejo -> 403, token nuevo -> 200 (`./chequeo_remoto.sh`)

### Ajustar limites de contexto

En `mcp_server.py`, modificar `MAX_EXCERPT_CHARS` y `MAX_TOTAL_CHARS`.

### Agregar tool MCP

Definir funcion con `@mcp_app.tool()` en `mcp_server.py`, reiniciar container.

### Registrar patron de error

En `error_hook.py`, agregar al dict `TECH_PATTERNS` y a `PRIORITY_ORDER`.
