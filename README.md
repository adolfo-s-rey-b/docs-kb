# docs-kb — Documentación técnica en Markdown

Copia en Markdown de la documentación oficial de 25 tecnologías de ciencia de datos y desarrollo web. Se actualiza automáticamente cada semana y está indexada para búsqueda semántica (también en español) mediante un servidor [MCP](https://modelcontextprotocol.io/).

Este repositorio es la **fuente única de verdad**: el servidor MCP lee exactamente lo que hay aquí, y aquí publica cada actualización.

## Cómo consultarla

**Directamente en GitHub.** Cada tecnología está en `sources/<tecnología>/markdown/`, con un archivo `.md` por página de la documentación original. `sources/<tecnología>/manifest.json` indica la URL original, el título y la fecha de descarga de cada página. Para buscar en todo el repositorio, usa el buscador de GitHub (tecla `/`) o clónalo y usa `grep`/`rg`.

**Desde un asistente con MCP** (Claude Code u otro cliente compatible). El servidor ofrece búsqueda semántica: una consulta como "combinar tablas por columna común" encuentra `merge`/`join` de pandas o dplyr. Tiene 8 herramientas (`docs_search`, `docs_get_section`, `docs_list_technologies`…). Por ahora el endpoint público exige un token y su uso está limitado al mantenedor. Detalles de conexión: [GuiaMCP.md](GuiaMCP.md).

## Tecnologías

| Tecnología | Carpeta | Documentación original |
| --- | --- | --- |
| Python | [sources/python](sources/python/markdown) | https://docs.python.org/3/ |
| pandas | [sources/pandas](sources/pandas/markdown) | https://pandas.pydata.org/docs/ |
| NumPy | [sources/numpy](sources/numpy/markdown) | https://numpy.org/doc/stable/ |
| Matplotlib | [sources/matplotlib](sources/matplotlib/markdown) | https://matplotlib.org/stable/ |
| seaborn | [sources/seaborn](sources/seaborn/markdown) | https://seaborn.pydata.org/ |
| scikit-learn | [sources/scikit-learn](sources/scikit-learn/markdown) | https://scikit-learn.org/stable/ |
| JupyterLab | [sources/jupyterlab](sources/jupyterlab/markdown) | https://jupyterlab.readthedocs.io/en/stable/ |
| PyTorch | [sources/pytorch](sources/pytorch/markdown) | https://docs.pytorch.org/docs/stable/ |
| TensorFlow | [sources/tensorflow](sources/tensorflow/markdown) | https://www.tensorflow.org/ |
| Keras | [sources/keras](sources/keras/markdown) | https://keras.io/ |
| Anaconda | [sources/anaconda](sources/anaconda/markdown) | https://docs.anaconda.com/ |
| R (manuales) | [sources/r](sources/r/markdown) | https://cran.r-project.org/doc/manuals/ |
| tidyverse | [sources/tidyverse](sources/tidyverse/markdown) | https://www.tidyverse.org/ |
| dplyr | [sources/dplyr](sources/dplyr/markdown) | https://dplyr.tidyverse.org/ |
| tidyr | [sources/tidyr](sources/tidyr/markdown) | https://tidyr.tidyverse.org/ |
| purrr | [sources/purrr](sources/purrr/markdown) | https://purrr.tidyverse.org/ |
| stringr | [sources/stringr](sources/stringr/markdown) | https://stringr.tidyverse.org/ |
| lubridate | [sources/lubridate](sources/lubridate/markdown) | https://lubridate.tidyverse.org/ |
| ggplot2 | [sources/ggplot2](sources/ggplot2/markdown) | https://ggplot2.tidyverse.org/ |
| RStudio IDE | [sources/rstudio](sources/rstudio/markdown) | https://docs.posit.co/ide/ |
| CSS (MDN) | [sources/css](sources/css/markdown) | https://developer.mozilla.org/en-US/docs/Web/CSS |
| HTML (MDN) | [sources/html](sources/html/markdown) | https://developer.mozilla.org/en-US/docs/Web/HTML |
| JavaScript (MDN) | [sources/javascript](sources/javascript/markdown) | https://developer.mozilla.org/en-US/docs/Web/JavaScript |
| React | [sources/react](sources/react/markdown) | https://react.dev/ |
| n8n | [sources/n8n](sources/n8n/markdown) | https://docs.n8n.io/ |

Los derechos de cada documentación pertenecen a sus autores. Las licencias están en [ATTRIBUTION.md](ATTRIBUTION.md).

## Cómo se mantiene

- **Recolección:** `collector.py` encuentra todas las páginas de cada sitio. Prueba, en orden: el sitemap vía Firecrawl, el inventario Sphinx `objects.inv`, el `sitemap.xml` y, como último recurso, un rastreo de enlaces con Playwright. Luego las convierte a Markdown con [Firecrawl](https://github.com/firecrawl/firecrawl).
- **Actualización:** cada domingo se vuelven a descargar las páginas con más de 28 días. El día 1 de cada mes se buscan además páginas nuevas. Los cambios se publican aquí como commits `docs: actualización automática …`.
- **Índice:** el servidor construye un índice de secciones y embeddings FAISS con el modelo multilingüe `paraphrase-multilingual-MiniLM-L12-v2`. El índice no se versiona; se regenera con `collector.py --index-only`.

Arquitectura completa, operación del servidor y guía de modificación: [SistemaDocumentación.md](SistemaDocumentación.md). Pruebas: [ChequeoSD.md](ChequeoSD.md) (servidor), `chequeo_remoto.sh` (cliente) y [ConclusionesSD.md](ConclusionesSD.md) (últimos resultados).

## Montar tu propia instancia

1. Clona el repo e instala las dependencias: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`.
2. Levanta Firecrawl, y opcionalmente su servicio de Playwright, y ajusta `firecrawl_url` en `config.json`.
3. Indexa la documentación incluida: `.venv/bin/python3 collector.py --index-only`.
4. Inicia el servidor: `.venv/bin/python3 mcp_server.py --transport streamable-http --port 8765`, o con Docker usando `Dockerfile.http`.
5. Conéctalo: `claude mcp add --transport http docs-kb http://localhost:8765/mcp`.

## Licencia

El código, los scripts y los textos propios de este repositorio están bajo la licencia [MIT](LICENSE): `mcp_server.py`, `collector.py`, los scripts `.sh`, `config.json` y las guías. La documentación de `sources/` **no** está cubierta por la licencia MIT: conserva la licencia de cada proyecto original (ver [ATTRIBUTION.md](ATTRIBUTION.md)).
