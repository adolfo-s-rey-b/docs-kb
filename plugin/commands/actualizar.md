---
description: Actualiza la documentación local de docs-kb a la última versión publicada en GitHub
---

Ejecuta con la herramienta Bash:

```bash
DOCS_KB_HOME="${CLAUDE_PLUGIN_DATA}" python3 "${CLAUDE_PLUGIN_ROOT}/docs_kb_local.py" update
```

Informa al usuario el resultado (versión, páginas y tecnologías). Si se descargó una versión nueva, indícale que reconecte el servidor con `/mcp` para empezar a usarla. Si falla, muestra las últimas líneas de `${CLAUDE_PLUGIN_DATA}/docs-kb.log`.
