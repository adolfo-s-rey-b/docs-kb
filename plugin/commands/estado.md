---
description: Muestra la versión instalada de docs-kb, la publicada en GitHub y si hay una actualización
---

Ejecuta con la herramienta Bash:

```bash
DOCS_KB_HOME="${CLAUDE_PLUGIN_DATA}" python3 "${CLAUDE_PLUGIN_ROOT}/docs_kb_local.py" status
```

Resume el resultado para el usuario en una o dos líneas. Si hay una actualización disponible, sugiere `/docs-kb:actualizar`.
