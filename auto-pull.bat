@echo off
REM Auto-pull updates from GitHub every 20 seconds
REM Esegui questo file per ricevere automaticamente le modifiche

title LAIP Website - Auto Pull Updates
color 0A
echo.
echo ========================================
echo   LAIP - Auto Pull Updates
echo ========================================
echo.
echo Questo script aggiorna automaticamente il sito
echo ogni 20 secondi quando l'altra persona fa modifiche.
echo.
echo Premi CTRL+C per fermare.
echo ========================================
echo.

:loop
echo [%date% %time%] Checking for updates...
git pull origin main
echo.
timeout /t 20 /nobreak
goto loop
