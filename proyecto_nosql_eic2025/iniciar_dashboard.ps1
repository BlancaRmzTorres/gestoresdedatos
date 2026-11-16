# Requiere Docker Desktop instalado y abierto.
$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot
& docker compose up --build -d
if ($LASTEXITCODE -ne 0) { throw "Docker Compose no pudo iniciar el proyecto." }
& docker compose ps
Write-Host "Abrir dashboard: http://localhost:8501"
