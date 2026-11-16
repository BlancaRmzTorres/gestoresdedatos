# Ejecutar: powershell -NoProfile -ExecutionPolicy Bypass -File .\iniciar.ps1 -Modo demo
[CmdletBinding()]
param(
    [ValidateSet('demo', 'completo', 'validar')][string]$Modo = 'demo',
    [string]$Archivo = 'datos\personas00.csv',
    [switch]$SinInstalar
)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

function Ejecutar([string]$Programa, [string[]]$Argumentos) {
    & $Programa @Argumentos
    if ($LASTEXITCODE -ne 0) {
        throw "El comando $Programa devolvio codigo $LASTEXITCODE."
    }
}
try {
    $pythonLocal = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
    if (-not (Test-Path -LiteralPath $pythonLocal -PathType Leaf)) {
        $py = Get-Command 'py' -ErrorAction SilentlyContinue
        if ($py) {
            Write-Host 'Creando entorno virtual con py -3...'
            & $py.Source -3 -m venv '.venv'
            if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear el entorno. Instala Python 3.11 a 3.14.' }
        } else {
            $python = Get-Command 'python' -ErrorAction SilentlyContinue
            if (-not $python) { throw 'No se encontro Python. Instala Python 3.11 a 3.14.' }
            Write-Host 'Creando entorno virtual con python...'
            Ejecutar -Programa $python.Source -Argumentos @('-m','venv','.venv')
        }
    }
    if (-not (Test-Path -LiteralPath $pythonLocal -PathType Leaf)) {
        throw 'No se pudo encontrar .venv\Scripts\python.exe.'
    }
    if (-not $SinInstalar) {
        Ejecutar -Programa $pythonLocal -Argumentos @('-m','pip','install','-r','requirements.txt')
    }
    Ejecutar -Programa $pythonLocal -Argumentos @('iniciar.py','--modo',$Modo,'--archivo',$Archivo)
} catch {
    Write-Error "No se pudo completar: $_"
    exit 1
}
