#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
docker compose up --build -d
docker compose ps
printf 'Abrir dashboard: http://localhost:8501\n'
