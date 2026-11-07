#!/usr/bin/env bash
# sincronizar.sh — Trae del repositorio la documentación publicada por GitHub Actions
# (.github/workflows/actualizar-docs.yml) y reconstruye el índice del MCP.
# Uso en el servidor (cron, bajo flock): ./sincronizar.sh >> logs/sincronizar.log 2>&1
# El reindexado es incremental (caché de embeddings) y el MCP lo recarga en caliente.
set -uo pipefail
cd "$(dirname "$0")"

OLD=$(git rev-parse HEAD)
if ! git pull --ff-only -q origin main; then
  echo "$(date '+%F %T') ERROR: git pull --ff-only falló (¿cambios locales en el servidor?)"
  exit 1
fi
NEW=$(git rev-parse HEAD)
if [ "$OLD" = "$NEW" ]; then
  echo "$(date '+%F %T') sin cambios"
  exit 0
fi

CHANGED=$(git diff --name-only "$OLD" "$NEW")
echo "$(date '+%F %T') $(echo "$CHANGED" | wc -l) archivos cambiados ($OLD..$NEW)"

if echo "$CHANGED" | grep -qx 'mcp_server.py'; then
  docker restart mcp_docs_kb_http_core > /dev/null && echo "$(date '+%F %T') mcp_server.py cambió: container reiniciado"
fi

if echo "$CHANGED" | grep -qE '^(sources/|config\.json$|collector\.py$)'; then
  .venv/bin/python3 collector.py --index-only
  echo "$(date '+%F %T') índice reconstruido"
fi
