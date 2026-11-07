#!/usr/bin/env bash
# Recolección completa de docs-kb en 3 grupos paralelos (sitios distintos por grupo),
# una sola reconstrucción del índice al final y publicación en GitHub (publicar.sh).
# Uso (en el servidor): setsid nohup ./recoleccion_completa.sh > logs/recoleccion-$(date +%F).out 2>&1 &
set -u
cd "$(dirname "$0")"
PY=.venv/bin/python3
exec 9>/tmp/docs-kb-collector.lock
flock -n 9 || { echo "Otra recolección está en curso (lock)"; exit 1; }
G1="tensorflow,pytorch,keras,seaborn,tidyverse,jupyterlab"
G2="numpy,matplotlib,pandas,python,scikit-learn"
G3="css,javascript,html,n8n,dplyr,tidyr,purrr,stringr,lubridate,ggplot2,r,react,rstudio,anaconda"
echo "$(date '+%F %T') inicio"
for G in "$G1" "$G2" "$G3"; do
  $PY collector.py --tech "$G" --discover --max-age-days 7 --no-index &
done
wait
echo "$(date '+%F %T') recolección terminada; reconstruyendo índice"
$PY collector.py --index-only
echo "$(date '+%F %T') publicando en GitHub"
./publicar.sh
echo "$(date '+%F %T') fin"
