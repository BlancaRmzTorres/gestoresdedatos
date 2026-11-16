[CmdletBinding()]
param(
    [string]$Archivo = 'datos\personas00.csv',
    [switch]$OmitirPipeline,
    [switch]$SoloVerificar
)
$modo = if ($SoloVerificar) { 'validar' } elseif ($OmitirPipeline) { 'demo' } else { 'completo' }
& "$PSScriptRoot\iniciar.ps1" -Modo $modo -Archivo $Archivo
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
