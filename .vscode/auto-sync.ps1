# Auto-sync script - esegui ogni 20 secondi
$repoPath = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $repoPath

# Primo avvio
if (-not (Test-Path "$repoPath\.sync-status")) {
    Write-Host "[SYNC] Sync automatico attivo - Andrea può iniziare a caricare modifiche" -ForegroundColor Green
    "started" | Out-File "$repoPath\.sync-status" -NoNewline
}

# Fetch e pull
$before = git rev-parse HEAD
git fetch origin 2>$null
git reset --hard origin/main 2>$null
$after = git rev-parse HEAD

if ($before -ne $after) {
    Write-Host "[SYNC] ✓ Aggiornamento da GitHub" -ForegroundColor Cyan
    git log --oneline -1
} else {
    Write-Host "[SYNC] Nessuna modifica" -ForegroundColor Gray
}
