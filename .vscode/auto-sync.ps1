# Sync automatico con GitHub (Windows).
# Ogni 20 secondi scarica le modifiche caricate dall'altro socio.
# Non tocca mai i file che stai modificando: se arrivano cambi proprio su quelli, aspetta.

Set-Location (Split-Path -Parent $PSScriptRoot)
$interval = 20

function Say($msg) { Write-Host ("[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $msg) }

Say "Sync automatico attivo: controllo GitHub ogni $interval secondi. Chiudi questo terminale per fermarlo."

while ($true) {
    git fetch --quiet origin 2>$null
    $behind = git rev-list --count 'HEAD..@{u}' 2>$null

    if ($LASTEXITCODE -eq 0 -and [int]$behind -gt 0) {
        $gitDir = git rev-parse --git-dir
        if ((Test-Path "$gitDir/MERGE_HEAD") -or (Test-Path "$gitDir/rebase-merge") -or (Test-Path "$gitDir/rebase-apply")) {
            Say "C'e' un merge o un rebase in corso: riprovo piu' tardi."
        }
        else {
            $incoming = @(git diff --name-only 'HEAD...@{u}')
            $mine = @(git status --porcelain | ForEach-Object { $_.Substring(3).Trim('"') })
            $overlap = @($incoming | Where-Object { $mine -contains $_ })

            if ($overlap.Count -gt 0) {
                Say ("Nuove modifiche su file che stai cambiando anche tu ({0}). Salva e fai commit: poi le scarico." -f ($overlap -join ', '))
            }
            else {
                $log = git log --format='   - %an: %s' 'HEAD..@{u}'
                git merge --no-edit '@{u}' *> $null
                if ($LASTEXITCODE -eq 0) {
                    Say "Aggiornato con $behind modifiche:"
                    $log | ForEach-Object { Write-Host $_ }
                }
                else {
                    git merge --abort *> $null
                    Say "Le modifiche vanno in conflitto con i tuoi commit: serve un git pull a mano."
                }
            }
        }
    }
    Start-Sleep -Seconds $interval
}
