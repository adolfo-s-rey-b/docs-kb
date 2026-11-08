---
name: docs-kb
description: Consultar la documentación oficial de Python, pandas, numpy, matplotlib, seaborn, scikit-learn, JupyterLab, PyTorch, TensorFlow, Keras, Anaconda, R y sus manuales, tidyverse (dplyr, tidyr, purrr, stringr, lubridate, ggplot2), RStudio, CSS, HTML, JavaScript (MDN), React y n8n con el MCP docs-kb. Úsala cuando el usuario pregunte cómo se usa una función, parámetro, clase o concepto de esas tecnologías, o cuando haya un error de alguna de ellas, antes de responder de memoria.
---

# Documentación técnica con docs-kb

El servidor MCP `docs-kb` de este plugin tiene la documentación oficial completa (unas 24.000 páginas) indexada localmente, con búsqueda semántica multilingüe: una pregunta en español encuentra la documentación en inglés.

## Patrón de consulta

1. `docs_search(query, technology?)`: busca y devuelve fragmentos con `[tecnología] slug > sección`. Con `technology` (por ejemplo `pandas` o `dplyr`) los resultados son más precisos.
2. `docs_get_section(technology, slug)`: sin `section` devuelve la tabla de contenidos de la página.
3. `docs_get_section(technology, slug, section)`: devuelve el contenido completo de esa sección.

Otros tools:

- `docs_list_technologies`: lista las tecnologías indexadas.
- `docs_generate_context(technologies, context_type)`: genera un `cheatsheet`, un `summary` o `migration` notes.
- `docs_fetch_live(url, query?)`: trae una página web en vivo (sin JavaScript) cuando algo no está en la base.
- `docs_changelog(days?)`: muestra los cambios recientes de la documentación.
- `docs_version_history(technology)`: muestra la versión actual y el historial.
- `docs_status`: muestra el estado del índice.

Cita la tecnología y la página (`slug`) de donde sale la información.

## Si el servidor responde "instalando"

La primera vez el plugin descarga la documentación y el índice desde GitHub (unos 150 MB) y prepara su entorno Python, lo que toma unos minutos. Mientras tanto solo existe `docs_status`, que muestra el avance. Cuando termine, el usuario debe reconectar con `/mcp`.

Actualización manual: `/docs-kb:actualizar`. Estado: `/docs-kb:estado`. La actualización también es automática: al iniciar una sesión se revisa si GitHub publicó una versión nueva, a lo sumo cada 12 horas.
