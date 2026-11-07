# Conclusiones — Pruebas del Servidor MCP docs-kb

**Última actualización:** 2026-11-07
**Método:** `./chequeo_remoto.sh` (JSON-RPC 2.0 / streamable-http contra el endpoint público HTTPS) y comprobaciones en el servidor (`ssh server`)
**Versión del servidor:** docs-kb v1.27.0

---

## 1. Resumen

| Fecha | Resultado | Estado |
| --- | --- | --- |
| 2026-04-27 | 8 PASS / 1 FAIL / 2 PARCIAL / 1 ERROR | Operativo con bug en `docs_list_technologies`, Firecrawl caído, búsqueda en español irrelevante, 12/28 tecnologías |
| 2026-11-07 (antes de cambios) | 9 PASS / 3 WARN / 0 FAIL | Bug y Firecrawl corregidos; seguían 12/28 tecnologías, búsqueda en español irrelevante, Obsidian congelado desde abril |
| 2026-11-07 (después de cambios) | **12 PASS / 0 WARN / 0 FAIL** | Búsqueda en español funcional, solo documentación técnica; recolección completa de las 25 tecnologías en curso |


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
| Token Bearer en texto plano en 4 archivos | Documentación original | Variable `DOCS_KB_TOKEN` en `.env` (no versionado) |
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

Lanzada el 2026-11-07 a las 18:37 UTC con `recoleccion_completa.sh` (3 grupos en paralelo). Ritmo observado: unas 100 páginas por minuto y 0 fallos en la primera hora.

| Grupo | Tecnologías |
| --- | --- |
| 1 | tensorflow (4474), pytorch (3490), keras (crawl), seaborn (223), tidyverse (185), jupyterlab (55) |
| 2 | numpy (2520), matplotlib (2031), pandas (1756), python (550), scikit-learn (1061) |
| 3 | css (1288), javascript (1346), html (258), n8n (1390), dplyr (131), tidyr (64), purrr (74), stringr (48), lubridate (76), ggplot2 (245), r, react, rstudio, anaconda (crawl) |

*Resultado final: pendiente; se completará al terminar la recolección y la reconstrucción del índice.*

---

## 5. Pendientes

1. Completar la sección 4 con las cifras finales y repetir `./chequeo_remoto.sh`.
2. Reiniciar Claude Code en el cliente para usar los tools nativos `mcp__docs-kb__*`.
3. Opcional: rotar el Bearer token, que estuvo en texto plano (procedimiento en SistemaDocumentación.md §12).
4. Opcional: definir una licencia para el código del repositorio (`mcp_server.py`, `collector.py`, scripts). Hoy no tiene ninguna.
5. Acceso de terceros al MCP: por ahora es solo del mantenedor. Si se abre, conviene emitir tokens por persona y evaluar restringir `docs_fetch_live`.
