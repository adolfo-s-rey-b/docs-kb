# Sistema de Documentación docs-kb

**Última actualización:** 2026-11-08

> Repositorio público y fuente única de verdad: [github.com/adolfo-s-rey-b/docs-kb](https://github.com/adolfo-s-rey-b/docs-kb). **docs-kb depende solo de GitHub.** GitHub Actions recolecta la documentación, construye el índice y publica el paquete del MCP local en el Release `datos`. Cada usuario instala ese MCP con el plugin de Claude Code. No hay servidor propio: el que existía se retiró el 2026-11-08. docs-kb contiene **solo documentación técnica pública**, nada personal.

---

## 1. Propósito

Documentación técnica oficial de 25 tecnologías para Claude Code y cualquier cliente MCP. Devuelve solo las secciones relevantes, para cuidar la ventana de contexto. La búsqueda semántica multilingüe (FAISS) encuentra documentación en inglés desde una consulta en español, aunque los términos no coincidan.

**Acceso:**

- **MCP local:** con el plugin `docs-kb@docs-kb` (`/plugin install docs-kb --marketplace adolfo-s-rey-b/docs-kb`) o con `python3 plugin/docs_kb_local.py serve` (stdio). No necesita token. Ver [GuiaMCP.md](GuiaMCP.md).
- **Lectura directa:** `sources/<tecnología>/markdown/*.md` en GitHub.

---

## 2. Arquitectura

```text
[Documentación técnica pública de 25 tecnologías]        [reactjs/react.dev (markdown)]
         |                                                         |
         v Firecrawl + Playwright (efímeros, uno por job)          v API de GitHub (source_type: github)
    +-----------------------------------------------------------------------------------+
    |  GitHub Actions: actualizar-docs.yml (domingos 03:00 UTC; día 1 01:00 + discover)  |
    |  - 1 job por tecnología: collector.py --tech T --max-age-days 28 --no-index       |
    |  - Descubre páginas: map -> objects.inv -> sitemap -> crawl BFS                   |
    |  - Job publicar: un commit "docs: actualización automática" (docs-kb-bot) en main |
    +-----------------------------------------------------------------------------------+
                 |
                 v github.com/adolfo-s-rey-b/docs-kb   (fuente única de verdad: sources/)
                 |
    +-----------------------------------------------------------------------------------+
    |  GitHub Actions: datos.yml (tras cada recolección, o push de código/config)       |
    |  - collector.py --index-only: section-index + FAISS SQ8 (incremental: caché de    |
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
    |    un MCP mínimo (solo stdlib) informa el avance                                  |
    |  - datos en ${CLAUDE_PLUGIN_DATA} (o ~/.local/share/docs-kb)                       |
    +-----------------------------------------------------------------------------------+
```

---

## 3. MCP local: plugin y paquete

| Pieza | Dónde | Qué hace |
| --- | --- | --- |
| Marketplace | `.claude-plugin/marketplace.json` | Convierte el repo en un marketplace de Claude Code llamado `docs-kb`. El plugin está en `./plugin` y Claude Code copia solo esa carpeta |
| Plugin | `plugin/.claude-plugin/plugin.json` | Declara el MCP `docs-kb`: `python3 ${CLAUDE_PLUGIN_ROOT}/docs_kb_local.py serve`, con `DOCS_KB_HOME=${CLAUDE_PLUGIN_DATA}`. No fija `version`, así que sigue los commits del repo |
| Hook | `plugin/hooks/hooks.json` | `SessionStart` (`startup`, `async`): ejecuta `docs_kb_local.py ensure` |
| Comandos y skill | `plugin/commands/`, `plugin/skills/docs-kb/` | `/docs-kb:actualizar` y `/docs-kb:estado`. La skill le explica a Claude cuándo y cómo consultar |
| Lanzador | `plugin/docs_kb_local.py` | Ver la descripción debajo de la tabla |
| Paquete | Release `datos` | `mcp_server.py`, `config.json`, `requirements-local.txt`, `LICENSE`, `ATTRIBUTION.md`, `sources/*/markdown`, `sources/*/manifest.json`, `index/` (FAISS SQ8, meta, section-index, tech-map) y `changelog/` (90 días, generado desde git) |

**El lanzador** (`docs_kb_local.py`) usa solo la biblioteca estándar. Comandos: `install`, `update`, `status`, `serve`, `ensure`, `check` y `uninstall`. Al instalar o actualizar:

1. Descarga `version.json` y el paquete desde `https://github.com/adolfo-s-rey-b/docs-kb/releases/download/datos/`, sin API ni token.
2. Verifica el sha256.
3. Extrae en `versiones/<commit>/` y cambia `actual` de forma atómica. Conserva la versión anterior.
4. Crea `venv/` con `requirements-local.txt` (usa `uv` si está instalado).
5. Descarga el modelo a `modelos/`.

**Versiones fijadas** en `requirements-local.txt`:

- `fastembed==0.8.0`: es la versión con la que se calcula el índice, así las consultas producen embeddings comparables.
- `mcp>=1.27,<2`: mcp 2.x renombró FastMCP.

**Diferencias del modo local:**

- `docs_fetch_live` descarga la página directamente y la convierte con html2text. No renderiza JavaScript. Con `DOCS_KB_FIRECRAWL_URL` usa un Firecrawl propio.
- `docs_changelog` lee el changelog generado desde git.
- Los logs del servidor van a stderr, porque stdout es el canal MCP.

**Prueba end-to-end:** `python3 docs_kb_local.py check` (12 pruebas por stdio). El 2026-11-08 dio 12/12 con la instalación directa y con el plugin instalado desde el marketplace.

---

## 4. Estructura del repositorio

```text
docs-kb/
+-- .claude-plugin/marketplace.json        # El repo como marketplace de Claude Code
+-- plugin/                                # Plugin docs-kb: docs_kb_local.py, hook, comandos, skill
+-- .github/workflows/actualizar-docs.yml  # Recolección semanal (GitHub Actions)
+-- .github/workflows/datos.yml            # Índice + paquete del MCP local -> Release "datos"
+-- .github/firecrawl/docker-compose.yml   # Firecrawl + Playwright efímeros para los jobs
+-- .github/scripts/                       # changelog_desde_git.py, empaquetar.py
+-- mcp_server.py                          # Servidor MCP (8 tools; stdio, o streamable-http en localhost)
+-- collector.py                           # Recolector (web, GitHub, local) + índice (secciones, FAISS)
+-- config.json                            # 25 tecnologías
+-- requirements-local.txt                 # Dependencias fijadas del MCP local / CI
+-- sources/<tech>/markdown/*.md           # Documentación (generada; no editar a mano)
+-- sources/<tech>/manifest.json           # URL original, título, hash y fecha de cada página
+-- README.md, GuiaMCP.md, SistemaDocumentación.md, ConclusionesSD.md, ATTRIBUTION.md, LICENSE
```

No se versionan (`.gitignore`):

- `.venv/`
- `index/`: se reconstruye con `collector.py --index-only`.
- `logs/` y `dist/`
- `sources/*/html/`: caché para detectar cambios.
- `sources/*/versions/`: obsoleto.
- `changelog/`: en el paquete se genera desde git.

---

## 5. Tecnologías configuradas (25)

**Web, vía Firecrawl en GitHub Actions (24):**
python, pandas, numpy, matplotlib, seaborn, scikit-learn, keras, tensorflow, pytorch, r,
tidyverse, dplyr, tidyr, purrr, stringr, lubridate, ggplot2, rstudio, css, html,
javascript, n8n, jupyterlab, conda

**Repositorio GitHub (`source_type: "github"`, 1):** react. Se toma el Markdown de [reactjs/react.dev](https://github.com/reactjs/react.dev) (`src/content/learn`, `src/content/reference`; CC-BY-4.0). react.dev bloquea los runners de GitHub, pero su fuente es pública.

**conda** reemplazó a Anaconda el 2026-11-08. docs.anaconda.com bloquea los runners de GitHub y no publica su fuente. La documentación de conda ([docs.conda.io](https://docs.conda.io/projects/conda/en/stable/), sitio Sphinx) cubre entornos y paquetes y se descubre con `objects.inv`.

El campo `"recolectar_en": "congelada"` sigue disponible para conservar una tecnología sin recolectarla.

La fuente y la licencia de cada tecnología están en `ATTRIBUTION.md`. **No hay fuentes personales:** las notas de Obsidian, el stack Docker y las skills de OpenClaw se retiraron el 2026-11-07.

---

## 6. MCP Server (mcp_server.py)

**Transportes:**

- stdio: `python3 mcp_server.py`. Es el que usa el plugin.
- streamable-http: `python3 mcp_server.py --transport streamable-http --port 8765`. Por la protección contra DNS rebinding, solo acepta `localhost`.

### 8 tools

| Tool | Descripción | Parámetros clave |
| --- | --- | --- |
| `docs_search` | Búsqueda semántica + keyword | `query`, `technology?`, `max_results?`, `version?` |
| `docs_list_technologies` | Lista todas las tecnologías con estadísticas | - |
| `docs_get_section` | TOC o sección específica | `technology`, `slug`, `section?`, `version?` |
| `docs_changelog` | Cambios recientes | `technology?`, `days?` |
| `docs_fetch_live` | Página en vivo: Firecrawl si `FIRECRAWL_URL` está definido; si no, descarga directa + html2text | `url`, `query?` |
| `docs_status` | Estado de la KB, incluido el modelo de embeddings | - |
| `docs_version_history` | Versión actual, cambios registrados y enlace al historial de git | `technology` |
| `docs_generate_context` | Cheatsheet, migration o summary | `technologies`, `context_type?` |

### Búsqueda en 3 fases

1. **Semántica (FAISS):**
   - Modelo `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (384d, más de 50 idiomas).
   - Cada vector codifica `"{tech} {página}: {heading}. {primeros 300 caracteres de la sección}"`.
   - Los vectores están normalizados, así que se usa similitud coseno, con un score de 0 a 12.
   - Con filtro `technology` busca 40 veces más profundo antes de filtrar. Sin filtro, devuelve como máximo 2 resultados por tecnología.
2. **Headings:** busca términos en `section-index.json`, ignorando stopwords (es/en) y palabras de hasta 2 letras. El score va de 4 a 12, proporcional a la fracción de términos encontrados, con +5 si la sección también salió en la fase semántica.
3. **Full-text:** grep sobre los archivos Markdown. Solo se usa si las fases anteriores dan pocos resultados.

El modelo se lee de `index/embeddings-info.json`, que escribe el collector, así el servidor siempre usa el mismo modelo que el índice. Se puede reemplazar con la variable `DOCS_KB_EMBED_MODEL`.

El índice FAISS y `section-index.json` se recargan en caliente cuando cambia su mtime.

### Caché y límites

- Caché LRU de 200 entradas para `docs_search` y `docs_get_section`. Se invalida cuando cambia `section-index.json`.
- `MAX_EXCERPT_CHARS = 800` por resultado y `MAX_TOTAL_CHARS = 4000` por llamada.

---

## 7. Collector (collector.py)

**Dónde corre:** en GitHub Actions. La recolección solo necesita `requests` (con `--no-index` no se cargan fastembed ni FAISS). El índice usa `requirements-local.txt`.

`--time-budget-min N` detiene la descarga de forma ordenada antes del límite de 6 h de cada job, y el manifest se guarda cada 50 páginas.

### CLI

```bash
python collector.py --tech pandas                       # una tecnología (o lista: --tech a,b)
python collector.py --tech pandas --discover            # re-descubrir páginas
python collector.py --all --discover --dry-run          # solo contar páginas, sin descargar
python collector.py --all --max-age-days 28             # re-descargar solo páginas con >28 días
python collector.py --tech a,b --no-index               # sin reconstruir el índice
python collector.py --index-only                        # índice de secciones + FAISS
python collector.py --add "fastapi" --map-url "https://..." --filters "tutorial/,ref/"
python collector.py --report | --check | --compress     # ESTADO.md, versiones, resúmenes LLM
```

### Descubrimiento de páginas

Firecrawl self-hosted `/v1/map` solo devuelve URLs de sitemaps. Por eso `discover_pages()` prueba varias estrategias en orden y usa la primera que dé URLs que pasen `map_filters` y `exclude_patterns`. Además exige que cada URL esté bajo `doc_base_url` (mismo dominio y prefijo de ruta).

| Estrategia | Cómo funciona | Usada por |
| --- | --- | --- |
| `map` | Firecrawl `/v1/map` (`limit` 100000) | sitios pkgdown (dplyr, tidyr, stringr…), n8n, tensorflow, pytorch, tidyverse |
| `inventory` | Sphinx `objects.inv`: todas las páginas, primero las narrativas y la API de primer nivel | pandas, numpy, python, matplotlib, seaborn, scikit-learn, jupyterlab, conda |
| `sitemap` | `sitemap.xml`, índices y `.gz` leídos directamente | MDN (css, html, javascript) |
| `crawl` | BFS sobre los `links` de `firecrawl_scrape` (página renderizada con Playwright) | rstudio, r, keras |

**Cobertura completa:**

- Todas las tecnologías web tienen `max_pages: 0`, es decir, sin límite.
- No usan `map_filters`, salvo `tensorflow` (`api_docs/python/`, `guide/`, `tutorials/`) y `r` (lista de manuales).
- Se mantienen los `exclude_patterns`: release notes, índices y páginas de comunidad.

Opciones por tecnología: `discovery`, `inventory_url`, `sitemap_url`, `crawl_start`, `crawl_depth` (6) y `crawl_max_fetch` (3000).

### Fuente repositorio GitHub (`source_type: "github"`)

```json
"react": {"source_type": "github", "repo": "reactjs/react.dev", "ref": "main", "path": "src/content",
          "include": ["learn/", "reference/"], "doc_base_url": "https://react.dev/"}
```

- Una sola llamada a `git/trees/<ref>?recursive=1` lista los archivos. Solo se descargan, desde `raw.githubusercontent.com`, los que cambiaron según su sha de blob.
- El slug y la URL replican el sitio: `learn/foo.md` → `learn-foo` → `https://react.dev/learn/foo`.
- Las páginas que ya no existen se eliminan. Usa `GH_TOKEN`/`GITHUB_TOKEN` si están definidos.

### Índice de secciones e índice FAISS

- **Formatos de título que reconoce:**
  - `# Título`.
  - Títulos con ancla permalink: `Título[#](url "Link to this heading")` de Sphinx y `Usage[](url#ref-usage)` de pkgdown.
  - Subrayados setext (`=====` / `-----`), aunque haya una línea en blanco de por medio.
  - Definiciones de API de Sphinx: `firma[#](url "Link to this definition")`.
  - El `title` del frontmatter YAML.
- **Lo que limpia o ignora:** las anclas MDX (`{/*x*/}`), los componentes sueltos (`<InlineToc />`) y los bloques de código.
- **Cobertura:** ~94 % de las páginas tiene secciones.
- **Tipo de índice:** `DOCS_KB_FAISS_INDEX=flat` (por defecto) crea `IndexFlatL2` exacto; `sq8` crea `IndexScalarQuantizer` de 8 bits, unas 4 veces más chico y con la misma API. El paquete local usa `sq8`.
- **Caché de embeddings:** `index/embeddings-cache.npz`, en float16, con claves `sha1(texto)` y checkpoints cada 20.000 secciones. Solo se codifican las secciones nuevas o modificadas.

### Versiones

La versión de cada tecnología es la que aparece en más páginas de la corrida, con un umbral: al menos 3 páginas y mayoría. Cada cambio se registra en `manifest.json["version_history"]`. El contenido anterior queda en el **historial de git** (`docs_version_history` enlaza a `commits/main/sources/<tech>`). No se hacen copias en `versions/`.

### Fuentes locales

`source_type: "local"` está soportado, pero no hay ninguna configurada. Todo lo que se agregue queda público, así que no debe usarse para contenido personal.

---

## 8. Actualización automática (GitHub Actions)

**Recolección** (`.github/workflows/actualizar-docs.yml`):

- `schedule`: domingos a las 03:00 UTC re-descarga las páginas con más de 28 días (las nuevas siempre). El día 1 de cada mes a la 01:00 UTC además corre `--discover`.
- `workflow_dispatch` acepta `tecnologias`, `descubrir`, `max_age_days` y `publicar`. Ejemplo: `gh workflow run actualizar-docs.yml -f tecnologias=pandas -f publicar=false`.
- Hay un job por tecnología, hasta 10 en paralelo. Cada uno levanta su Firecrawl + Playwright con `.github/firecrawl/docker-compose.yml`. Postgres debe usar la base y el usuario `postgres`, porque `pg_cron` lo exige.
- El job `publicar` hace un único commit con todo, como `docs-kb-bot`. Al final se llama a `datos.yml`.

**Índice y paquete** (`.github/workflows/datos.yml`): también corre cuando un push cambia `mcp_server.py`, `collector.py`, `config.json`, `requirements-local.txt` o los scripts, y a mano. Pasos:

1. Descarga la caché de embeddings del Release.
2. Corre `DOCS_KB_FAISS_INDEX=sq8 collector.py --index-only`.
3. Genera el changelog desde git.
4. Empaqueta y sube el paquete y la caché.
5. Sube `version.json` al final, para que ningún cliente vea una versión que todavía no terminó de subirse.

**Historial:**

- Carga inicial completa: run 42448781365 (2026-11-08), commit `218313e` con 23.931 archivos.
- Primer paquete: `bb4b28c` (99 MB, 162.933 vectores). La caché se sembró con los embeddings que ya tenía el servidor.
- Después de pasar React a la fuente GitHub: `3396873` (24.116 páginas, 165.212 vectores).

---

## 9. Guía de modificación

- **Agregar una tecnología web:** agregar la entrada en `config.json` (`display_name`, `doc_base_url`, `exclude_patterns`, `max_pages: 0` y, si hace falta, `discovery`, `inventory_url`, `sitemap_url` o `crawl_start`), y luego `gh workflow run actualizar-docs.yml -f tecnologias=<tech> -f descubrir=true`. Para probar el descubrimiento sin descargar: `python collector.py --tech <tech> --discover --dry-run`.
- **Quitar una tecnología:** borrarla de `config.json` y borrar `sources/<tech>/` (`git rm -r --sparse sources/<tech>` en un clon parcial). El push dispara `datos.yml`.
- **Cambiar el servidor MCP o el collector:** push a `main`. `datos.yml` publica un paquete nuevo y los clientes lo toman en menos de 12 h (o con `/docs-kb:actualizar`).
- **Cambiar el modelo de embeddings:** cambiar `EMBED_MODEL` en `collector.py` y `DEFAULT_EMBED_MODEL` en `mcp_server.py`. La caché se invalida sola porque guarda el modelo. Ajustar también `requirements-local.txt`.
- **Límites de contexto:** `MAX_EXCERPT_CHARS` y `MAX_TOTAL_CHARS` en `mcp_server.py`.
- **Agregar un tool MCP:** una función con `@mcp_app.tool()` en `mcp_server.py`, y actualizar `docs_kb_local.py check`.

---

## 10. Historia: servidor propio (retirado)

Hasta el 2026-11-08, docs-kb corría en un servidor propio:

- Container Docker con streamable-http en `:8765`, detrás de nginx con Bearer token y de un Cloudflare Tunnel (`mcp-documentacion.adolfo-s-rey-b.com`).
- Un cron que recolectaba y reindexaba.

Se reemplazó por el esquema solo-GitHub de este documento. El 2026-11-08 se borró del servidor todo lo de docs-kb:

- el container, la imagen y el volumen;
- el código y los datos (1,4 GB);
- el proxy de nginx y la regla del túnel;
- el cron, la deploy key, las skills y el hook;
- la entrada MCP y la documentación del stack.

Firecrawl, que también usa n8n, se mantuvo.
