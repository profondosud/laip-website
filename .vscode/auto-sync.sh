#!/usr/bin/env bash
# Sync automatico con GitHub (Mac / Linux).
# Ogni 20 secondi scarica le modifiche caricate dall'altro socio.
# Non tocca mai i file che stai modificando: se arrivano cambi proprio su quelli, aspetta.

cd "$(dirname "$0")/.." || exit 1
interval=20

say() { echo "[$(date +%H:%M:%S)] $*"; }

say "Sync automatico attivo: controllo GitHub ogni $interval secondi. Chiudi questo terminale per fermarlo."

while true; do
    git fetch --quiet origin 2>/dev/null
    behind=$(git rev-list --count 'HEAD..@{u}' 2>/dev/null || echo 0)

    if [ "$behind" -gt 0 ]; then
        git_dir=$(git rev-parse --git-dir)
        if [ -f "$git_dir/MERGE_HEAD" ] || [ -d "$git_dir/rebase-merge" ] || [ -d "$git_dir/rebase-apply" ]; then
            say "C'è un merge o un rebase in corso: riprovo più tardi."
        else
            overlap=$(comm -12 \
                <(git diff --name-only 'HEAD...@{u}' | sort) \
                <(git status --porcelain | cut -c4- | tr -d '"' | sort))
            if [ -n "$overlap" ]; then
                say "Nuove modifiche su file che stai cambiando anche tu ($(echo $overlap)). Salva e fai commit: poi le scarico."
            else
                log=$(git log --format='   - %an: %s' 'HEAD..@{u}')
                if git merge --no-edit '@{u}' >/dev/null 2>&1; then
                    say "Aggiornato con $behind modifiche:"
                    echo "$log"
                else
                    git merge --abort >/dev/null 2>&1
                    say "Le modifiche vanno in conflitto con i tuoi commit: serve un git pull a mano."
                fi
            fi
        fi
    fi
    sleep "$interval"
done
