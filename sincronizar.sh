#!/usr/bin/env bash
# sincronizar.sh — Trae del repositorio la documentación publicada por GitHub Actions
# (.github/workflows/actualizar-docs.yml) y reconstruye el índice del MCP.
# Uso en el servidor (cron cada hora, bajo flock): ./sincronizar.sh >> logs/sincronizar.log 2>&1
#
# Reanudable: el commit indexado se guarda en index/indexed-commit solo al terminar el
# reindexado. Si el servidor se reinicia a mitad, la siguiente corrida lo retoma (la caché
# de embeddings se guarda por tramos, así que no se repite el trabajo ya hecho).
set -uo pipefail
cd "$(dirname "$0")"

OLD=$(git rev-parse HEAD)
if ! git pull --ff-only -q origin main; then
  echo "$(date '+%F %T') ERROR: git pull --ff-only falló (¿cambios locales o archivos sin versionar en el servidor?)"
  exit 1
fi
NEW=$(git rev-parse HEAD)

if [ "$OLD" != "$NEW" ]; then
  echo "$(date '+%F %T') $(git diff --name-only "$OLD" "$NEW" | wc -l) archivos cambiados ($OLD..$NEW)"
  if git diff --name-only "$OLD" "$NEW" | grep -qx 'mcp_server.py'; then
    docker restart mcp_docs_kb_http_core > /dev/null && echo "$(date '+%F %T') mcp_server.py cambió: container reiniciado"
  fi
fi

INDEXED=$(cat index/indexed-commit 2>/dev/null || true)
if [ "$INDEXED" = "$NEW" ]; then
  [ "$OLD" = "$NEW" ] && echo "$(date '+%F %T') sin cambios"
  exit 0
fi

# Reindexar si nunca se indexó, si el commit indexado no existe, o si cambió algo que afecta al índice
if [ -z "$INDEXED" ] || ! git cat-file -e "${INDEXED}^{commit}" 2>/dev/null \
   || git diff --name-only "$INDEXED" "$NEW" | grep -qE '^(sources/|config\.json$|collector\.py$)'; then
  echo "$(date '+%F %T') reindexando (indexado: ${INDEXED:-ninguno} -> $NEW)"
  if ! .venv/bin/python3 collector.py --index-only; then
    echo "$(date '+%F %T') ERROR: collector.py --index-only falló"
    exit 1
  fi
  echo "$(date '+%F %T') índice reconstruido"
fi
mkdir -p index && echo "$NEW" > index/indexed-commit
