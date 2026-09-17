# Auto-pull updates from GitHub every 20 seconds
# Esegui: powershell -ExecutionPolicy Bypass -File auto-pull.ps1

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  LAIP - Auto Pull Updates" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Questo script aggiorna automaticamente il sito" -ForegroundColor Green
Write-Host "ogni 20 secondi quando l'altra persona fa modifiche." -ForegroundColor Green
Write-Host ""
Write-Host "Premi CTRL+C per fermare." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$counter = 0

while ($true) {
    $counter++
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] Check #$counter - Downloading updates..." -ForegroundColor Cyan

    Set-Location "C:\Users\marco\Documents\set up"
    git pull origin main

    Write-Host ""
    Write-Host "Next check in 20 seconds..." -ForegroundColor Yellow
    Start-Sleep -Seconds 20
    Write-Host ""
}
