# docs-kb — Documentación técnica en Markdown

Copia en Markdown de la documentación oficial de 25 tecnologías de ciencia de datos y desarrollo web. Se actualiza automáticamente cada semana y está indexada para búsqueda semántica (también en español) mediante un servidor [MCP](https://modelcontextprotocol.io/).

Todo vive en GitHub: este repositorio es la **fuente única de verdad**, GitHub Actions lo actualiza cada semana y el servidor MCP corre **en tu propio equipo**. No hace falta ningún servidor ni token.

## Instalar el MCP en Claude Code (recomendado)

En Claude Code (v2.1.275 o posterior):

```text
/plugin install docs-kb --marketplace adolfo-s-rey-b/docs-kb
```

O en dos pasos, en versiones anteriores:

```text
/plugin marketplace add adolfo-s-rey-b/docs-kb
/plugin install docs-kb@docs-kb
```

La primera sesión descarga en segundo plano la documentación y el índice semántico desde el [Release `datos`](https://github.com/adolfo-s-rey-b/docs-kb/releases/tag/datos), unos 150 MB. También prepara un entorno Python propio y el modelo de embeddings, unos 220 MB. Todo eso tarda unos minutos y queda en `~/.claude/plugins/data/`. Cuando termine, reconecta con `/mcp`.

**Requisitos:** Python 3.10 o posterior en el `PATH` como `python3`. En Debian/Ubuntu también hace falta `python3-venv`, o [`uv`](https://docs.astral.sh/uv/).

**Actualizaciones:**
- **Documentación e índice:** se actualizan solos. Al iniciar una sesión, el plugin revisa si GitHub publicó una versión nueva (como mucho cada 12 horas) y la descarga en segundo plano. Para forzarlo usa `/docs-kb:actualizar`, y para ver la versión instalada `/docs-kb:estado`.
- **Plugin:** activa *Enable auto-update* para el marketplace `docs-kb` en `/plugin` → *Marketplaces*, o ejecuta `/plugin marketplace update docs-kb`.

Después, Claude usa los tools `docs_search`, `docs_get_section`, `docs_list_technologies`, `docs_generate_context`, `docs_fetch_live`, `docs_changelog`, `docs_version_history` y `docs_status`. La búsqueda es semántica y multilingüe: "combinar tablas por columna común" encuentra `merge`/`join` de pandas o dplyr.

### Sin plugin (cualquier cliente MCP)

```bash
curl -fsSLO https://raw.githubusercontent.com/adolfo-s-rey-b/docs-kb/main/plugin/docs_kb_local.py
python3 docs_kb_local.py install          # descarga datos + entorno + modelo
python3 docs_kb_local.py check            # 12 pruebas end-to-end
claude mcp add --scope user docs-kb -- python3 "$PWD/docs_kb_local.py" serve
```

Para otros clientes MCP, el servidor es el comando `python3 /ruta/docs_kb_local.py serve` (stdio). `python3 docs_kb_local.py update` actualiza, y `serve` también revisa actualizaciones por su cuenta cada 12 horas. Los datos quedan en `~/.local/share/docs-kb`, o en `$DOCS_KB_HOME` si está definido.

## Consultar sin instalar nada

Cada tecnología está en `sources/<tecnología>/markdown/`, con un archivo `.md` por página de la documentación original. `sources/<tecnología>/manifest.json` indica la URL original, el título y la fecha de descarga de cada página. Para buscar en todo el repositorio, usa el buscador de GitHub (tecla `/`) o clónalo y usa `grep`/`rg`.

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
| conda | [sources/conda](sources/conda/markdown) | https://docs.conda.io/projects/conda/en/stable/ |
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

Todo corre en GitHub, sin servidores propios:

1. **Recolección** ([`actualizar-docs.yml`](.github/workflows/actualizar-docs.yml)): cada domingo se vuelven a descargar las páginas con más de 28 días, y el día 1 de cada mes se buscan además páginas nuevas. Cada tecnología corre en su propio job con un [Firecrawl](https://github.com/firecrawl/firecrawl) temporal. `collector.py` descubre las páginas probando, en orden: el sitemap, el inventario Sphinx `objects.inv`, el `sitemap.xml` y un rastreo de enlaces con Playwright. React se toma del Markdown de su repositorio oficial ([reactjs/react.dev](https://github.com/reactjs/react.dev)). Los cambios se publican en un único commit `docs: actualización automática …` de `docs-kb-bot`.
2. **Índice y paquete** ([`datos.yml`](.github/workflows/datos.yml)): después de cada recolección se reconstruye el índice de secciones y los embeddings FAISS, con el modelo multilingüe `paraphrase-multilingual-MiniLM-L12-v2`, cuantizado a 8 bits. Es incremental: solo se calculan las secciones nuevas o modificadas. El paquete del MCP local se publica en el Release [`datos`](https://github.com/adolfo-s-rey-b/docs-kb/releases/tag/datos).
3. **MCP local** ([`plugin/`](plugin)): el plugin descarga ese paquete, verifica su sha256 y lo actualiza solo.

Arquitectura completa y guía de modificación: [SistemaDocumentación.md](SistemaDocumentación.md). Pruebas: `python3 plugin/docs_kb_local.py check` (MCP local) y [ConclusionesSD.md](ConclusionesSD.md) (últimos resultados).

## Licencia

El código, los scripts y los textos propios de este repositorio están bajo la licencia [MIT](LICENSE): `mcp_server.py`, `collector.py`, `plugin/`, los scripts, `config.json` y las guías. La documentación de `sources/` **no** está cubierta por la licencia MIT: conserva la licencia de cada proyecto original (ver [ATTRIBUTION.md](ATTRIBUTION.md)).
