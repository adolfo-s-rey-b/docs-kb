#!/usr/bin/env bash
# publicar.sh — Publica en GitHub los cambios de documentación (sources/) y de config.json.
# Lo llama actualizar.sh (cron) y recoleccion_completa.sh. Push con la deploy key del repo.
set -euo pipefail
cd "$(dirname "$0")"
git pull --rebase --autostash -q origin main
git add -A sources config.json
if git diff --cached --quiet; then
  echo "$(date '+%F %T') sin cambios que publicar"
  exit 0
fi
N=$(git diff --cached --name-only | wc -l)
git commit -q -m "docs: actualización automática $(date -u +%F) ($N archivos)"
git push -q origin main
echo "$(date '+%F %T') publicado: $N archivos"
