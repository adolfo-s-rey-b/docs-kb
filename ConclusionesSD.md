# Conclusiones — Pruebas del Servidor MCP docs-kb

**Última actualización:** 2026-11-08 (MCP local)
**Método:** `./chequeo_remoto.sh` (JSON-RPC 2.0 / streamable-http contra el endpoint público HTTPS) y comprobaciones en el servidor (`ssh server`)
**Versión del servidor:** docs-kb v1.27.0

---

## 1. Resumen

| Fecha | Resultado | Estado |
| --- | --- | --- |
| 2026-04-27 | 8 PASS / 1 FAIL / 2 PARCIAL / 1 ERROR | Operativo con bug en `docs_list_technologies`, Firecrawl caído, búsqueda en español irrelevante, 12/28 tecnologías |
| 2026-11-07 (antes de cambios) | 9 PASS / 3 WARN / 0 FAIL | Bug y Firecrawl corregidos; seguían 12/28 tecnologías, búsqueda en español irrelevante, Obsidian congelado desde abril |
| 2026-11-07 (después de cambios) | 12 PASS / 0 WARN / 0 FAIL | Búsqueda en español funcional, solo documentación técnica; recolección completa de las 25 tecnologías en curso |
| **2026-11-08 (final)** | **12 PASS / 0 WARN / 0 FAIL** | **25/25 tecnologías recolectadas, 24.115 páginas, 163.003 vectores**; GitHub Actions recolecta y el servidor solo sincroniza |


---

## 2. Problemas encontrados en la revisión del 2026-11-07 y su solución

| Problema | Causa raíz | Solución |
| --- | --- | --- |
| 16/28 tecnologías nunca recolectadas (pandas, python, numpy, react…) | Firecrawl self-hosted `/v1/map` solo conoce sitemaps; esos sitios no tienen → 0 URLs | Descubrimiento multi-estrategia: map → Sphinx `objects.inv` → `sitemap.xml` → crawl con Playwright |
| Las tecnologías recolectadas tenían pocas páginas (20–40) | `max_pages` y `map_filters` restrictivos | Sin límite (`max_pages: 0`), sin `map_filters` (salvo tensorflow y r), alcance por `doc_base_url`; ~22.900 páginas descubiertas en 21 tecnologías + 4 por crawl |
| Páginas con JavaScript no se renderizaban | Firecrawl corría sin playwright-service | Servicio `firecrawl_playwright` agregado |
| Búsqueda semántica en español devolvía notas personales | Modelo solo inglés (`all-MiniLM-L6-v2`), embeddings solo del título, y keywords (`por`, `de`…) con score fijo +10 | Modelo `paraphrase-multilingual-MiniLM-L12-v2`, embeddings de título de página + heading + contenido, stopwords y score proporcional |
| Headings con basura `[](https://…)` | Conversión de anclas de Firecrawl | Limpieza en el índice de secciones |
| Índice desactualizado tras el cron | FAISS se cargaba solo al iniciar el container | Recarga en caliente por mtime |
| Cron semanal re-scrapeaba todo y sin lock | Diseño original | `--max-age-days 28` semanal, `--discover` mensual, `flock`, publicación en GitHub |
| Log duplicaba cada línea | Handler a stdout + redirección del cron al mismo archivo | stdout solo en terminal |
| Tools nativos `mcp__docs-kb__*` nunca aparecían en el cliente | La guía usaba `~/.claude/mcp.json`, que Claude Code no lee | `claude mcp add --scope user` |
| Health-checks documentados daban 406 | Faltaba `Accept: application/json, text/event-stream` y `initialize` | Comandos corregidos + `chequeo_remoto.sh` |
| Token Bearer en texto plano en 4 archivos | Documentación original | Variable `DOCS_KB_TOKEN` en `.env` (no versionado); token **rotado** el 2026-11-07 (el anterior devuelve 403) |
| El código del repositorio no tenía licencia | — | Licencia MIT para el código; `sources/` conserva las licencias originales (ATTRIBUTION.md) |
| Contenido personal en el índice (vault de Obsidian, stack Docker, skills) | Fuentes locales configuradas | Retirado del config, `sources/`, índice y changelog; docs-kb solo contiene documentación técnica pública |

---

## 3. Resultados de las 12 pruebas (2026-11-07, después de cambios)

| # | Prueba | Estado | Observación |
| --- | --- | --- | --- |
| 1 | 8 tools registrados | ✅ PASS | 8/8 |
| 2 | `docs_status` | ✅ PASS | FAISS activo, modelo multilingüe |
| 3 | `docs_list_technologies` | ✅ PASS | Bug de abril (`NoneType.__format__`) corregido |
| 4 | Búsqueda keyword `str_detect` | ✅ PASS | 5 resultados de stringr |
| 5 | Búsqueda semántica en español | ✅ PASS | "combinar tablas por columna comun" → tidyr/dplyr (antes: notas personales sin relación con la consulta) |
| 6 | TOC `articles-stringr` | ✅ PASS | Headings limpios (`Tasks`) |
| 7 | Sección específica | ✅ PASS | Usa la primera sección real del TOC ("Basic usage" no existe) |
| 8 | `docs_generate_context` summary | ✅ PASS | Prueba cambiada de Obsidian a numpy |
| 9 | Cheatsheet pandas | ✅ PASS | En abril estaba vacío (pandas no recolectado) |
| 10 | `docs_version_history` | ✅ PASS | |
| 11 | `docs_changelog` | ✅ PASS | |
| 12 | `docs_fetch_live` | ✅ PASS | Firecrawl operativo (en abril estaba caído) |

---

## 4. Recolección completa

**Cronología**

| Cuándo (UTC) | Qué pasó |
| --- | --- |
| 2026-11-07 18:37 | Recolección completa en el servidor (`recoleccion_completa.sh`, 3 grupos en paralelo) |
| 2026-11-08 02:10 | Desconexión física del servidor (intencional), con ~19.600 páginas descargadas y sin publicar. Iba por PyTorch |
| 2026-11-08 04:55 | Como el servidor no respondía, lancé la carga completa en GitHub Actions (run 42448781365, 25 jobs, 10 en paralelo) |
| 2026-11-08 06:25 / 07:20 / 14:25 | El servidor arranca, se vuelve a desconectar a las 07:20 y arranca de nuevo a las 14:25 |
| 2026-11-08 07:35 | Actions publica el commit `218313e` (`docs-kb-bot`, 23.931 archivos). El job más largo fue tensorflow (2 h 38 min) |
| 2026-11-08 17:00 | El servidor descarta su copia local, sincroniza con el repo y reindexa con el parser de secciones corregido |
| 2026-11-08 18:12 | El servidor publica react (184 páginas) y anaconda (26) con su deploy key (commit `8b4b62a`) |
| 2026-11-08 18:17 | Reindexado incremental: 160.905 embeddings reutilizados de la caché y solo 250 nuevos. Índice al día: 163.003 vectores |
| 2026-11-08 18:52 | `./chequeo_remoto.sh`: 12/12 PASS |

**Documentación publicada** (repo `sources/`, **24.115 páginas** de Markdown en 25 tecnologías, ~290 MB):

| Tecnología | Páginas | MB | Descubrimiento |
| --- | --- | --- | --- |
| tensorflow | 4.474 | 36 | map |
| pytorch | 3.490 | 42 | map |
| numpy | 2.520 | 18 | inventory |
| matplotlib | 2.031 | 27 | inventory |
| pandas | 1.756 | 13 | inventory |
| n8n | 1.390 | 11 | map |
| keras | 1.360 | 22 | crawl |
| javascript | 1.341 | 15 | sitemap (MDN) |
| css | 1.287 | 21 | sitemap (MDN) |
| rstudio | 1.275 | 13 | crawl |
| scikit-learn | 1.061 | 21 | inventory |
| python | 550 | 28 | inventory |
| html | 258 | 4 | sitemap (MDN) |
| ggplot2 | 244 | 3 | map |
| seaborn | 223 | 2 | inventory |
| tidyverse | 185 | 1 | map |
| dplyr | 131 | 2 | map |
| lubridate | 76 | 1 | map |
| purrr | 74 | 1 | map |
| tidyr | 64 | 1 | map |
| jupyterlab | 55 | 2 | inventory |
| stringr | 48 | 1 | map |
| r | 12 | 6 | crawl |
| react | 184 | 0,7 | crawl, desde el servidor |
| anaconda | 26 | 0,2 | crawl, desde el servidor |

Total: 23.905 páginas de las 23 tecnologías recolectadas por GitHub Actions, más 210 de react y anaconda desde el servidor = **24.115 páginas**.

**React y Anaconda** se recolectan desde el servidor porque react.dev y docs.anaconda.com bloquean las IPs de GitHub Actions. En Actions dieron 286 scrapes de React con error 500 y un crawl de Anaconda con 1 sola página; desde el servidor se habían descargado 184 y 26. Quedan marcadas con `"recolectar_en": "servidor"` y se recolectan una vez al mes (cron del día 2).

**Índice de secciones:** con el parser original solo 9.166 de 23.906 páginas tenían secciones (numpy: 63 de 2.520), porque Firecrawl renderiza los títulos de Sphinx y pkgdown como setext y con anclas permalink. Con el parser corregido se indexan 22.494 páginas (94 %) y 162.753 secciones.

**Otros errores corregidos durante la recolección**
- Snapshots de versión espurios (~3 GB; 105 en matplotlib), por detectar la versión página por página.
- Las páginas sin cambios no actualizaban `last_fetched`.
- La caché de embeddings ahora es reanudable (checkpoints cada 20.000 secciones), por la inestabilidad del servidor.

---

## 5. MCP local: todo depende de GitHub (2026-11-08)

Como el servidor propio se va a desconectar, docs-kb pasó a funcionar solo con GitHub:

| Pieza | Resultado |
| --- | --- |
| Recolección | GitHub Actions, semanal. React se toma ahora del Markdown de [reactjs/react.dev](https://github.com/reactjs/react.dev): react.dev bloquea los runners, pero su fuente es pública. Run 42516933791: 181 páginas, 4 obsoletas eliminadas. Anaconda queda **congelada** (26 páginas): bloquea los runners y no publica su fuente |
| Índice y paquete | `datos.yml`: índice FAISS SQ8 incremental (165.212 vectores) y Release `datos` con `docs-kb-datos.tar.gz` (~101 MB), `version.json` y la caché de embeddings. La primera construcción reutilizó 161.032 embeddings sembrados desde el servidor y solo calculó 53 |
| Plugin / marketplace | `/plugin install docs-kb --marketplace adolfo-s-rey-b/docs-kb`. Añadir el marketplace tarda 6,5 s (el repo comprimido pesa 41 MB) y Claude Code copia solo `plugin/` |
| Instalación local | 46 s desde cero en Python 3.14: paquete, entorno y modelo. Mientras se instala, el MCP responde con un servidor mínimo que informa el avance |
| Prueba end-to-end (`docs_kb_local.py check`) | **12/12 PASS**, tanto con instalación directa como con el plugin desde el marketplace. Init en 2–3 s y consultas en menos de 0,7 s |

Problemas encontrados y corregidos en el camino:

- **mcp 2.x** renombró `FastMCP` y rompía las instalaciones nuevas: se fijó `mcp<2`.
- `fastembed` quedó fijado en 0.8.0, la versión del índice; una instalación nueva había bajado la 0.9.1.
- El servidor escribía logs en stdout, que en modo stdio es el canal MCP: ahora van a stderr.
- El directorio de datos del plugin no coincidía entre el hook y el MCP.

---

## 6. Retiro del servidor y cambio a conda (2026-11-08)

**Servidor retirado.** Se borró del servidor todo lo de docs-kb:

- el container `mcp_docs_kb_http_core`, su imagen y el volumen de fastembed;
- `firecrawl_playwright`, que se había agregado para docs-kb;
- `~/server-stack/docs-kb` (1,4 GB);
- el proxy `mcp-docs-proxy.conf` de nginx y la regla `mcp-documentacion` del túnel;
- el cron, la deploy key (también revocada en GitHub) y el alias SSH;
- las skills `/docs-*`, el hook `error_hook.py`, la entrada de `.mcp.json`, los permisos y la memoria de docs-kb;
- la documentación del stack, las cachés y los respaldos de docs-kb.

Se mantuvo Firecrawl, que también usan flujos de n8n, junto con nginx y el resto del stack. El cambio se coordinó con la sesión de Obsidian, que comparte nginx y el túnel.

**En el cliente**, se quitó el registro del MCP remoto (`claude mcp remove docs-kb -s user`) y se borró `.env`, porque el token ya no sirve. También salieron del repo los archivos que solo servían al servidor: `sincronizar.sh`, `actualizar.sh`, `publicar.sh`, `recoleccion_completa.sh`, `Dockerfile.http`, `requirements.txt`, `error_hook.py`, `chequeo_remoto.sh`, `ChequeoSD.md` y `.env.example`. Por último, `mcp_server.py` ya no acepta el dominio viejo.

**Anaconda → conda.** docs.anaconda.com bloquea los runners de GitHub y no publica su fuente. Se reemplazó por la documentación de conda (docs.conda.io, Sphinx). Su `objects.inv` descubre 80 páginas: guía de usuario y comandos.

---

## 7. Pendientes

1. El registro DNS `mcp-documentacion.adolfo-s-rey-b.com` sigue existiendo en Cloudflare. El túnel ya responde 404 para ese nombre. Se puede borrar desde el panel de Cloudflare (DNS), porque `cloudflared` no borra registros.
2. **conda incompleta (24 de ~80 páginas).** docs.conda.io también bloquea los runners de GitHub tras unas 12 páginas, aun con 3 s de pausa (`SCRAPE_ALL_ENGINES_FAILED`). El cortacircuitos detiene la tecnología y cada corrida semanal agrega unas 12 páginas más. Para tenerla completa de una vez, se podría añadir al collector soporte para reStructuredText y tomarla de `conda/conda` (`docs/source`, 106 archivos `.rst`) con la fuente GitHub.
3. Verificar la primera corrida programada del workflow, el domingo 2026-11-15 a las 03:00 UTC: debe publicar y encadenar `datos.yml`.
