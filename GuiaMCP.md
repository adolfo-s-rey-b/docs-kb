# Guía del MCP docs-kb

**Última actualización:** 2026-11-08

docs-kb es un servidor MCP con la documentación oficial de 25 tecnologías: Python, pandas, numpy, matplotlib, seaborn, scikit-learn, JupyterLab, PyTorch, TensorFlow, Keras, conda, R, tidyverse (dplyr, tidyr, purrr, stringr, lubridate, ggplot2), RStudio, MDN (CSS, HTML, JavaScript), React y n8n. Son unas 24.000 páginas con búsqueda semántica multilingüe.

**Corre en tu equipo** y depende únicamente de GitHub:

- GitHub Actions recolecta la documentación cada semana y la publica en este repo.
- GitHub Actions construye el índice semántico y publica el paquete en el Release [`datos`](https://github.com/adolfo-s-rey-b/docs-kb/releases/tag/datos).
- El plugin descarga ese paquete y lo actualiza solo.

No hay servidor ni token.

---

## 1. Instalación

### Con el plugin de Claude Code (recomendado)

```text
/plugin install docs-kb --marketplace adolfo-s-rey-b/docs-kb
```

En versiones de Claude Code anteriores a la 2.1.275:

```text
/plugin marketplace add adolfo-s-rey-b/docs-kb
/plugin install docs-kb@docs-kb
```

En la primera sesión, el hook de inicio:

1. Descarga `docs-kb-datos.tar.gz` (~150 MB) y verifica su sha256.
2. Crea un entorno Python en `~/.claude/plugins/data/docs-kb-docs-kb/` (`${CLAUDE_PLUGIN_DATA}`) con mcp, fastembed, faiss-cpu y html2text.
3. Descarga el modelo `paraphrase-multilingual-MiniLM-L12-v2` (~220 MB).

Mientras tanto, el MCP responde con un único tool, `docs_status`, que muestra el avance. Cuando termine, **reconecta con `/mcp`**.

**Requisitos:**

- Python 3.10 o superior como `python3`.
- Debian/Ubuntu: el paquete `python3-venv`, o tener [`uv`](https://docs.astral.sh/uv/) instalado (se usa automáticamente si está).
- `curl` no hace falta: la descarga usa la biblioteca estándar de Python.

### Sin plugin

```bash
curl -fsSLO https://raw.githubusercontent.com/adolfo-s-rey-b/docs-kb/main/plugin/docs_kb_local.py
python3 docs_kb_local.py install
claude mcp add --scope user docs-kb -- python3 "$PWD/docs_kb_local.py" serve
```

Datos en `~/.local/share/docs-kb` (o `$DOCS_KB_HOME`). Cualquier cliente MCP puede usar el comando `python3 /ruta/docs_kb_local.py serve` (transporte stdio).

### Comandos de `docs_kb_local.py`

| Comando | Qué hace |
| --- | --- |
| `install [--force]` | Descarga la última versión publicada, prepara el entorno y el modelo |
| `update` | Igual que `install`, pero solo descarga si hay una versión nueva |
| `status` | Versión instalada y versión publicada |
| `serve` | Servidor MCP por stdio. Si pasaron más de 12 h desde la última revisión, lanza un `update` en segundo plano |
| `ensure` | Lo usa el hook de inicio de sesión: instala si falta y, si toca, actualiza |
| `check` | 12 pruebas end-to-end contra el servidor local |
| `uninstall --yes` | Borra los datos locales |

En el plugin, los comandos equivalentes son `/docs-kb:actualizar` y `/docs-kb:estado`.

---

## 2. Actualizaciones

| Qué | Cómo se actualiza |
| --- | --- |
| Documentación e índice | Solo: al iniciar una sesión (como mucho cada 12 h) se compara `version.json` del Release con lo instalado y se descarga la versión nueva. La versión anterior se conserva hasta la siguiente actualización, para no romper una sesión abierta. La nueva se usa al reconectar (`/mcp`) o en la próxima sesión |
| Código del servidor (`mcp_server.py`) | Viene dentro del mismo paquete del Release, así que se actualiza junto con los datos |
| Plugin (lanzador, hook, skill) | Activa *Enable auto-update* para el marketplace `docs-kb` en `/plugin` → *Marketplaces*, o ejecuta `/plugin marketplace update docs-kb`. El plugin no fija `version`, así que sigue los commits del repo |

El paquete se publica cada domingo, tras la recolección semanal, y también cada vez que cambia el código del servidor, del collector o la configuración.

---

## 3. Uso

| Tool | Uso |
| --- | --- |
| `docs_search` | Búsqueda semántica + keyword (`query`, `technology?`, `max_results?`) |
| `docs_get_section` | TOC de una página (sin `section`) o el contenido de una sección (`technology`, `slug`, `section?`) |
| `docs_list_technologies` | Tecnologías con número de páginas y fecha |
| `docs_generate_context` | `cheatsheet`, `summary` o `migration` de una o varias tecnologías |
| `docs_fetch_live` | Página web en vivo convertida a Markdown. En local es una descarga directa, sin JavaScript; con `DOCS_KB_FIRECRAWL_URL` usa tu Firecrawl |
| `docs_changelog` | Cambios recientes, sacados del historial de git del repo (90 días) |
| `docs_version_history` | Versión detectada, cambios registrados y enlace al historial de git |
| `docs_status` | Estado del índice: vectores, modelo, tecnologías |

**Patrón recomendado:** `docs_search` → tomar `tech` y `slug` → `docs_get_section` sin sección (TOC) → `docs_get_section` con la sección.

---

## 4. Verificación

```bash
python3 docs_kb_local.py check     # o: python3 "$CLAUDE_PLUGIN_ROOT/docs_kb_local.py" check
```

Corre 12 pruebas: tools, estado del índice, búsqueda keyword y semántica en español, TOC y sección, summary, cheatsheet, historial de versiones, changelog y fetch en vivo. El código de salida es 0 si todas pasan.

---

## 5. Troubleshooting

| Síntoma | Causa / solución |
| --- | --- |
| El MCP solo tiene `docs_status` y dice "instalando" | Primera instalación en curso. Espera y reconecta con `/mcp`. El log está en `docs-kb.log` del directorio de datos |
| `no se pudo crear el entorno virtual` | Instala `python3-venv` (Debian/Ubuntu) o `uv`, y luego ejecuta `/docs-kb:actualizar` |
| `la descarga no coincide con el sha256 publicado` | El Release se estaba actualizando justo en ese momento. Reintenta en unos minutos |
| `docs_fetch_live` devuelve poco contenido | La página necesita JavaScript. Usa una URL de la documentación estática o configura `DOCS_KB_FIRECRAWL_URL` |
| Quiero empezar de cero | `python3 docs_kb_local.py uninstall --yes`, o desinstalar el plugin (borra `${CLAUDE_PLUGIN_DATA}`), y volver a instalar |
