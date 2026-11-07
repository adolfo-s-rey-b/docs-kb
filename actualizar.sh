#!/usr/bin/env bash
# actualizar.sh — Corre collector.py con los argumentos dados y publica el resultado en GitHub.
# Usado por cron (siempre bajo flock -n /tmp/docs-kb-collector.lock).
cd "$(dirname "$0")"
.venv/bin/python3 collector.py "$@" >> logs/collector.log 2>&1
./publicar.sh >> logs/publicar.log 2>&1
