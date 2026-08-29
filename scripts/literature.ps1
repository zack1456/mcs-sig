$ErrorActionPreference = "Stop"

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repositoryRoot ".venv\Scripts\python.exe"

if (Test-Path -LiteralPath $venvPython) {
    & $venvPython (Join-Path $PSScriptRoot "literature.py") @args
    exit $LASTEXITCODE
}

$pythonLauncher = Get-Command py -ErrorAction SilentlyContinue
if ($pythonLauncher) {
    & $pythonLauncher.Source -3 (Join-Path $PSScriptRoot "literature.py") @args
    exit $LASTEXITCODE
}

$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCommand) {
    & $pythonCommand.Source (Join-Path $PSScriptRoot "literature.py") @args
    exit $LASTEXITCODE
}

Write-Error "Python was not found. Ask a maintainer to help install Python or create the intake note for you."
