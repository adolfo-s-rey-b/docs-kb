# Sistema de Documentacion docs-kb

**Ultima actualizacion:** 2026-11-08

> Repositorio publico y fuente unica de verdad: [github.com/adolfo-s-rey-b/docs-kb](https://github.com/adolfo-s-rey-b/docs-kb). **Desde 2026-11-08 todo depende solo de GitHub**: GitHub Actions recolecta la documentacion, construye el indice y publica el paquete del MCP local (Release `datos`), que cada usuario instala con el plugin de Claude Code. El servidor propio (secciones marcadas *legado*) ya no es necesario. docs-kb contiene **solo documentacion tecnica publica**: ningun contenido personal.

---

## 1. Proposito

Documentacion tecnica oficial de 25 tecnologias para Claude Code (y cualquier cliente MCP). Protege la ventana de contexto devolviendo solo las secciones relevantes. La busqueda semantica multilingue (FAISS) hace que una consulta en espanol encuentre la documentacion en ingles aunque los terminos sean distintos.

**Acceso:**

- **MCP local (principal):** plugin `docs-kb@docs-kb` (`/plugin install docs-kb --marketplace adolfo-s-rey-b/docs-kb`) o `python3 plugin/docs_kb_local.py serve` (stdio). Sin token. Ver GuiaMCP.md
- **Lectura directa:** `sources/<tecnologia>/markdown/*.md` en GitHub
- **Legado:** `https://mcp-documentacion.adolfo-s-rey-b.com/mcp` (servidor propio, Bearer token), que se desconectara

---

## 2. Arquitectura

```text
[Documentacion tecnica publica de 25 tecnologias]        [reactjs/react.dev (markdown)]
         |                                                         |
         v Firecrawl + Playwright (efimeros, uno por job)          v API de GitHub (source_type: github)
    +-----------------------------------------------------------------------------------+
    |  GitHub Actions: actualizar-docs.yml (domingos 03:00 UTC; dia 1 01:00 + discover)  |
    |  - 1 job por tecnologia: collector.py --tech T --max-age-days 28 --no-index       |
    |  - Descubre paginas: map -> objects.inv -> sitemap -> crawl BFS                   |
    |  - Job publicar: un commit "docs: actualizacion automatica" (docs-kb-bot) en main |
    +-----------------------------------------------------------------------------------+
                 |
                 v github.com/adolfo-s-rey-b/docs-kb   (fuente unica de verdad: sources/)
                 |
    +-----------------------------------------------------------------------------------+
    |  GitHub Actions: datos.yml (tras cada recoleccion, o push de codigo/config)       |
    |  - collector.py --index-only: section-index + FAISS SQ8 (incremental: cache de    |
    |    embeddings del Release anterior)                                               |
    |  - changelog desde git, paquete docs-kb-datos.tar.gz + version.json (sha256)      |
    +-----------------------------------------------------------------------------------+
                 |
                 v Release "datos": docs-kb-datos.tar.gz (~100 MB), version.json, embeddings-cache.npz
                 |
    +-----------------------------------------------------------------------------------+
    |  Equipo del usuario: plugin docs-kb (Claude Code) / docs_kb_local.py              |
    |  - hook SessionStart (async): instala o actualiza (cada <=12 h) en segundo plano  |
    |  - serve: venv propio -> mcp_server.py por stdio (8 tools); mientras se instala,  |
    |    un MCP minimo (solo stdlib) informa el avance                                  |
    |  - datos en ${CLAUDE_PLUGIN_DATA} (o ~/.local/share/docs-kb)                       |
    +-----------------------------------------------------------------------------------+
```

El servidor propio (legado) hacia lo mismo que el ultimo bloque, pero remoto: era un clon del repo con `sincronizar.sh` y servia `mcp_server.py` por streamable-http (Docker :8765 -> nginx :8766 con Bearer token -> Cloudflare Tunnel).

---

## 2b. MCP local: plugin y paquete

| Pieza | Donde | Que hace |
| --- | --- | --- |
| Marketplace | `.claude-plugin/marketplace.json` | El repo es un marketplace de Claude Code (`docs-kb`); el plugin esta en `./plugin` y Claude Code copia solo esa carpeta |
| Plugin | `plugin/.claude-plugin/plugin.json` | Declara el MCP `docs-kb` (`python3 ${CLAUDE_PLUGIN_ROOT}/docs_kb_local.py serve`, `DOCS_KB_HOME=${CLAUDE_PLUGIN_DATA}`). Sin `version`: sigue los commits del repo |
| Hook | `plugin/hooks/hooks.json` | `SessionStart` (`startup`, `async`): `docs_kb_local.py ensure` |
| Comandos y skill | `plugin/commands/`, `plugin/skills/docs-kb/` | `/docs-kb:actualizar`, `/docs-kb:estado`; la skill explica a Claude cuando y como consultar |
| Lanzador | `plugin/docs_kb_local.py` | Solo stdlib. `install`/`update`/`status`/`serve`/`ensure`/`check`/`uninstall`. Descarga `version.json` y el paquete desde `https://github.com/adolfo-s-rey-b/docs-kb/releases/download/datos/` (sin API ni token), verifica sha256, extrae en `versiones/<commit>/` y cambia `actual` de forma atomica (conserva la version anterior). Crea `venv/` con `requirements-local.txt` (usa `uv` si existe) y descarga el modelo a `modelos/` |
| Paquete | Release `datos` | `mcp_server.py`, `config.json`, `requirements-local.txt`, `LICENSE`, `ATTRIBUTION.md`, `sources/*/markdown`, `sources/*/manifest.json`, `index/` (FAISS SQ8, meta, section-index, tech-map) y `changelog/` (90 dias, desde git) |

**Versiones fijadas** (`requirements-local.txt`): `fastembed==0.8.0`, la version con la que se calcula el indice (asi las consultas producen embeddings comparables); `mcp>=1.27,<2`, porque mcp 2.x renombro FastMCP.

**En local:**

- `docs_fetch_live` descarga la pagina directamente y la convierte con html2text. No renderiza JavaScript; con `DOCS_KB_FIRECRAWL_URL` usa un Firecrawl propio.
- `docs_changelog` lee el changelog generado desde git.
- Los logs del servidor van a stderr, porque stdout es el canal MCP.

**Prueba end-to-end:** `python3 docs_kb_local.py check` (12 pruebas por stdio). Resultados del 2026-11-08: 12/12, tanto con la instalacion directa como con el plugin instalado desde el marketplace.

---

## 3. Estructura de Directorios

```text
docs-kb/
+-- mcp_server.py              # MCP server (8 tools, HTTP + stdio)
+-- collector.py               # Recolector (web, FAISS, compression)
+-- error_hook.py              # PostToolUse hook para errores
+-- config.json                # 25 tecnologias configuradas
+-- .github/workflows/actualizar-docs.yml  # Recoleccion semanal en GitHub Actions (mecanismo principal)
+-- .github/workflows/datos.yml            # Indice + paquete del MCP local -> Release "datos"
+-- .github/scripts/                       # changelog_desde_git.py, empaquetar.py
+-- .claude-plugin/marketplace.json        # El repo como marketplace de Claude Code
+-- plugin/                                # Plugin docs-kb: MCP local (docs_kb_local.py), hook, comandos, skill
+-- requirements-local.txt                 # Dependencias fijadas del MCP local
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

**Web (via Firecrawl, en GitHub Actions), 23:**
python, pandas, numpy, matplotlib, seaborn, scikit-learn, keras, tensorflow, pytorch, r,
tidyverse, dplyr, tidyr, purrr, stringr, lubridate, ggplot2, rstudio, css, html,
javascript, n8n, jupyterlab

**Repositorio GitHub (`source_type: "github"`), 1:** react, desde el Markdown de [reactjs/react.dev](https://github.com/reactjs/react.dev) (`src/content/learn`, `src/content/reference`; CC-BY-4.0). react.dev bloquea los runners de GitHub, pero su fuente es publica.

**Congelada (`"recolectar_en": "congelada"`), 1:** anaconda. docs.anaconda.com bloquea los runners de GitHub y no publica su fuente; se conservan las 26 paginas recolectadas el 2026-11-08 y el workflow no la actualiza.

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

### Fuente repositorio GitHub (`source_type: "github"`)

Para documentacion publicada como Markdown en un repo publico:

```json
"react": {"source_type": "github", "repo": "reactjs/react.dev", "ref": "main", "path": "src/content",
          "include": ["learn/", "reference/"], "doc_base_url": "https://react.dev/"}
```

- Una sola llamada a la API (`git/trees/<ref>?recursive=1`) lista los archivos. Solo se descargan, desde `raw.githubusercontent.com`, los que cambiaron segun su sha de blob.
- El slug y la URL replican el sitio: `learn/foo.md` -> `learn-foo` -> `https://react.dev/learn/foo`.
- Se eliminan las paginas que ya no existen.
- Usa `GH_TOKEN`/`GITHUB_TOKEN` si estan definidos.
- El indice de secciones toma el `title` del frontmatter y quita las anclas MDX (`{/*x*/}`) y los componentes sueltos (`<InlineToc />`).

### Indice FAISS

`DOCS_KB_FAISS_INDEX=flat` (por defecto) crea `IndexFlatL2` exacto en float32. `sq8` crea `IndexScalarQuantizer` de 8 bits, unas 4 veces mas chico (165k vectores: ~63 MB en lugar de ~250 MB), con la misma API; es el que usa el paquete local. La cache de embeddings (`index/embeddings-cache.npz`) se guarda en float16.

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

## 7. Error Hook (error_hook.py) — legado (servidor)

**Tipo:** PostToolUse hook, matcher: Bash
**Interprete:** System Python (sin venv)

Output al detectar error:

```text
NOTA: Error detectado en {tech}.
Busqueda rapida: /docs-search {tech} {keyword} | Analisis detallado: /docs-debug-agent
```

Prioridad (mayor a menor): pandas > numpy > scikit-learn > keras > tensorflow > pytorch > matplotlib > seaborn > dplyr > ggplot2 > react > n8n > r > python > javascript > css > html

---

## 8. Skills del servidor (`~/server-stack/.claude/skills`) — legado

El plugin trae su propia skill (`plugin/skills/docs-kb`) y comandos (`/docs-kb:actualizar`, `/docs-kb:estado`).


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

## 9. Infraestructura Docker — legado (servidor propio)

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

**Indice y paquete: GitHub Actions** (`.github/workflows/datos.yml`): corre como job `datos` al final de `actualizar-docs.yml`, y tambien en un push que cambie `mcp_server.py`, `collector.py`, `config.json`, `requirements-local.txt` o los scripts, o a mano. Hace lo siguiente:

1. Descarga del Release la cache de embeddings (`embeddings-cache.npz`, float16).
2. `DOCS_KB_FAISS_INDEX=sq8 collector.py --index-only`: solo codifica las secciones nuevas o modificadas.
3. Genera el changelog desde git y empaqueta.
4. Sube al Release `datos` el paquete y la cache, y `version.json` al final, para que ningun cliente vea una version que todavia no esta subida.

Primera publicacion: `bb4b28c` (2026-11-08, 99 MB, 162.933 vectores; la cache se sembro con los embeddings del servidor). Tras pasar React a la fuente GitHub: `3396873` (24.116 paginas, 165.212 vectores).

**Servidor propio — legado, solo sincroniza** (cron instalado el 2026-11-08; ya no hace falta para nada, el MCP local lo reemplaza):

```text
17 * * * * cd /home/adolfo-s-rey-b/server-stack/docs-kb && flock -n /tmp/docs-kb-collector.lock ./sincronizar.sh >> logs/sincronizar.log 2>&1
```

(La recoleccion mensual de react y anaconda desde el servidor se retiro el 2026-11-08: react viene de GitHub y anaconda esta congelada.)

`sincronizar.sh` hace `git pull --ff-only`; si cambio `mcp_server.py` reinicia el container; si cambio algo que afecta al indice (`sources/`, `config.json`, `collector.py`) corre `collector.py --index-only`. El commit indexado se guarda en `index/indexed-commit` solo al terminar, y la cache de embeddings se guarda cada 20.000 secciones: si el servidor se reinicia a mitad, la siguiente hora retoma el reindexado sin repetir trabajo. El MCP recarga indice y secciones en caliente.

`actualizar.sh`, `publicar.sh` y `recoleccion_completa.sh` quedan como alternativa manual para recolectar desde el servidor (por ejemplo si una tecnologia falla en Actions); no correrlos a la vez que el workflow. Backups del crontab: `~/backups/crontab-2026-11-07.txt`.

**Disponibilidad del servidor:** estuvo apagado entre 2026-08-15 y 2026-11-04, y el 2026-11-08 se desconecto fisicamente dos veces (02:10 y 07:20 UTC; desconexiones intencionales, no fallas). La documentacion del repo no depende del servidor; el MCP remoto si. Todo lo del servidor se retoma solo al volver (sincronizacion cada hora, cache de embeddings con checkpoints).

---

## 11. Repositorio GitHub (fuente unica de verdad)

- Repo publico: `github.com/adolfo-s-rey-b/docs-kb`. La documentacion se lee directamente en `sources/<tecnologia>/markdown/*.md`; `sources/<tecnologia>/manifest.json` tiene la URL original, titulo y fecha de cada pagina.
- Servidor: `~/server-stack/docs-kb` es un clon. Remoto `git@github-docs-kb:adolfo-s-rey-b/docs-kb.git`; alias SSH `github-docs-kb` -> deploy key `~/.ssh/docs-kb-deploy` (escritura solo en este repo). Autor de commits: noreply de GitHub.
- Quien escribe en `sources/`: el workflow de GitHub Actions (`docs-kb-bot`). El servidor (legado) solo lee.
- Release `datos` (tag fijo, assets reemplazados en cada publicacion): `docs-kb-datos.tar.gz`, `version.json`, `embeddings-cache.npz`. URLs estables: `https://github.com/adolfo-s-rey-b/docs-kb/releases/download/datos/<asset>`.
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
