# Sync automatico con GitHub (Windows). Parte da solo aprendo la cartella in VS Code.
# Ogni 20 secondi controlla GitHub e scarica le modifiche nuove.
#
# Due modalita':
#   mirror  la cartella diventa sempre uguale a GitHub. Prima di sovrascrivere mette al
#           sicuro le modifiche locali (git stash) e i commit non caricati (branch backup-*).
#           E' la modalita' di chi guarda il sito mentre l'altro lavora (Marko).
#   safe    scarica solo se non tocca file che stai modificando. Non cancella mai niente.
#           E' la modalita' di chi lavora sul sito (Andrea).
# Scelta: "git config laip.sync.mode mirror|safe" (solo su quel computer). Se non e'
# impostata: mirror per Marco Paonessa, safe per tutti gli altri.

$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo
$interval = 20

function Say($msg, $color = 'Gray') { Write-Host ("[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $msg) -ForegroundColor $color }

$mode = git config --get laip.sync.mode
if (-not $mode) {
    $who = "$(git config --get user.name) $(git config --get user.email)"
    $mode = if ($who -match 'paonessa') { 'mirror' } else { 'safe' }
}

Say "Sync automatico attivo in $repo (modalita' $mode, ogni $interval secondi). Chiudi questo terminale per fermarlo." 'Green'

while ($true) {
    git fetch --quiet origin 2>$null
    $behind = git rev-list --count 'HEAD..@{u}' 2>$null

    if ($LASTEXITCODE -eq 0 -and [int]$behind -gt 0) {
        $gitDir = git rev-parse --git-dir
        $busy = (Test-Path "$gitDir/MERGE_HEAD") -or (Test-Path "$gitDir/rebase-merge") -or (Test-Path "$gitDir/rebase-apply")
        $log = git log --format='   - %an: %s' 'HEAD..@{u}'

        if ($mode -eq 'mirror') {
            if ($busy) { git merge --abort *> $null; git rebase --abort *> $null }
            $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
            if (git status --porcelain) {
                git stash push -u -m "auto-backup $stamp" *> $null
                Say "Modifiche locali salvate nello stash 'auto-backup $stamp' (git stash list)." 'Yellow'
            }
            if ([int](git rev-list --count '@{u}..HEAD') -gt 0) {
                git branch "backup-$stamp" *> $null
                Say "Commit non caricati salvati nel branch backup-$stamp." 'Yellow'
            }
            git reset --hard --quiet '@{u}'
            Say "Aggiornato a GitHub ($behind modifiche):" 'Cyan'
            $log | ForEach-Object { Write-Host $_ }
        }
        elseif ($busy) {
            Say "C'e' un merge o un rebase in corso: riprovo piu' tardi." 'Yellow'
        }
        else {
            $incoming = @(git diff --name-only 'HEAD...@{u}')
            $mine = @(git status --porcelain | ForEach-Object { $_.Substring(3).Trim('"') })
            $overlap = @($incoming | Where-Object { $mine -contains $_ })

            if ($overlap.Count -gt 0) {
                Say ("Nuove modifiche su file che stai cambiando anche tu ({0}). Fai commit: poi le scarico." -f ($overlap -join ', ')) 'Yellow'
            }
            else {
                git merge --no-edit '@{u}' *> $null
                if ($LASTEXITCODE -eq 0) {
                    Say "Aggiornato con $behind modifiche:" 'Cyan'
                    $log | ForEach-Object { Write-Host $_ }
                }
                else {
                    git merge --abort *> $null
                    Say "Le modifiche vanno in conflitto con i tuoi commit: serve un git pull a mano." 'Red'
                }
            }
        }
    }
    Start-Sleep -Seconds $interval
}
