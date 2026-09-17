# STANDARD-SITO.md — Anatomia di un sito TeamHero

> Documento di riferimento trasversale. NON è il `CLAUDE.md` di un singolo sito:
> descrive come **deve essere fatto** un sito nuovo, sia nel setup infrastrutturale
> sia nella struttura tecnica. Da consultare **ogni volta che si crea un sito nuovo**.
> Posizione consigliata nel filesystem: `SITI INTERNET/_standard/STANDARD-SITO.md`.
> Lingua di lavoro: italiano.

---

## Come si usa questo documento

Quando crei un sito nuovo, segui in ordine:

1. **PARTE A — Setup infrastruttura**: i passaggi "una tantum" fuori dal codice (repo, Vercel, email, video, env). È una checklist: spunta man mano.
2. **PARTE B — Blueprint tecnico**: come deve essere fatto il codice (stack, struttura cartelle, bot, FAQ, palette). È la specifica di riferimento.
3. Alla fine genera il `CLAUDE.md` del nuovo sito (vedi PARTE C).

Stack standard deciso: **Next.js** (App Router, TypeScript). I siti legacy in HTML statico (es. adattivia, teamhero) restano come sono finché funzionano — si migrano a Next.js solo in occasione di un redesign o di una modifica strutturale, mai "solo per uniformare".

---

# PARTE A — Setup infrastruttura (checklist)

Ordine consigliato: GitHub → progetto locale → Vercel → email → (video se servono) → variabili d'ambiente.

## A.1 Repository GitHub

- [ ] Crea il repo sotto l'account/org **`mbtt-teamhero`**.
- [ ] **Convenzione nome**: `sito_<nome>` (es. `sito_cirmo`, `sito_adattivia`). La cartella locale usa lo stesso nome.
- [ ] Repo **privato**.
- [ ] Branch principale: **`main`**.
- [ ] NON committare mai: `.env*`, `node_modules`, `.vercel`. Verificare che siano nel `.gitignore` (Next.js lo genera già corretto).

**Autenticazione (importante, una volta sola per il PC):**
Il push da VS Code NON richiede token nei file. L'autenticazione la gestisce **Git Credential Manager** col login browser. Se un `git push` fallisce con *"Password authentication is not supported"*:
- Controlla l'URL del remote: `git remote -v`. Se contiene un token (`x-access-token:...@github.com` o `<userid>@github.com`), ripuliscilo:
  `git remote set-url origin https://github.com/mbtt-teamhero/sito_<nome>.git`
- Forza il login pulito: `git credential-manager github login` → "Sign in with your browser".
- Se persiste, rimuovi le voci GitHub vecchie da *Gestione credenziali di Windows* e riprova.

## A.2 Progetto locale (Next.js)

- [ ] Crea il progetto: `npx create-next-app@latest sito_<nome>` (TypeScript: sì, App Router: sì, Tailwind: opzionale — vedi nota stile in B.5).
- [ ] Collega il remote: `git remote add origin https://github.com/mbtt-teamhero/sito_<nome>.git`
- [ ] Primo commit + push su `main`.
- [ ] Copia in radice questo standard come riferimento, e genera il `CLAUDE.md` del sito (PARTE C).

## A.3 Vercel

- [ ] Su **vercel.com**, importa il repo GitHub (New Project → Import). Vercel rileva Next.js e configura build da solo.
- [ ] **Nome progetto Vercel**: coerente col repo (`sito-<nome>`). Annota l'URL `.vercel.app` assegnato.
- [ ] Deploy automatico: ogni `push` su `main` → build e deploy automatici. Nessun comando manuale.
- [ ] Dominio custom (se previsto): Project → Settings → Domains → aggiungi `nome.it` o sottodominio. Segui le istruzioni DNS.
- [ ] Le **variabili d'ambiente** si impostano qui (A.6), MAI nel codice. Valgono dal deploy successivo al salvataggio.

## A.4 Email / lead (due opzioni documentate)

Scegli **una** delle due in base al sito. Regola pratica: **Resend** se vuoi controllo pieno e template server-side; **EmailJS + Google Sheet** se vuoi anche accumulare i lead in un foglio e l'invio è lato client.

### Opzione 1 — Resend (consigliata per nuovi siti Next.js)
- [ ] Crea account su **resend.com**.
- [ ] Verifica il dominio mittente (es. `send.<nome>.it`): aggiungi i record DKIM/SPF/MX indicati da Resend al DNS.
- [ ] Crea una **API key**.
- [ ] Definisci l'indirizzo `from` (es. `noreply@send.<nome>.it`).
- [ ] L'invio avviene **server-side** in una route handler (`app/api/contact/route.ts`) che legge `RESEND_API_KEY` dall'env. (Riferimento reale: `sito_cirmo`.)

### Opzione 2 — EmailJS + Google Sheet (lead-capture con archivio)
- [ ] Account su **emailjs.com** → service + template + public key (le chiavi EmailJS sono pubbliche per natura, possono stare lato client).
- [ ] Template con variabili attese (es. `{{timestamp}}`, `{{chi}}`, `{{riepilogo}}`).
- [ ] Webhook Google Sheet (Apps Script) per salvare i lead; l'URL del webhook va in env `GOOGLE_SHEET_WEBHOOK` e l'invio passa per una route server-side (`app/api/save-lead/route.ts`). (Riferimento reale: `sito_teamhero`.)
- [ ] Imposta restrizioni anti-abuso lato dashboard EmailJS.

## A.5 Immagini e video (Cloudflare R2)

**Immagini e video NON vanno nel repo git.** Asset pesanti appesantiscono il repo, rallentano i push e non hanno senso in un sistema di versioning del codice. Si ospitano su **Cloudflare R2** — storage senza costi di egress, CDN globale inclusa — e si referenziano nel codice con URL assoluti.

**Cosa va su R2:**
- Video (hero, demo, manifesto, ecc.) — desktop e mobile se servono entrambe le versioni.
- Immagini di contenuto (foto, gallery, immagini hero, foto profilo, loghi partner).
- Qualsiasi asset binario pesante (PDF, file scaricabili).

**Cosa resta nel repo/`public/`:**
- Favicon, icone SVG leggere, loghi piccoli usati nel codice Next.js via `next/image`.
- Asset strettamente legati al codice (es. og-image generata dinamicamente).

**Procedura setup bucket (una volta per sito):**

- [ ] Accedi alla **dashboard Cloudflare** → **R2**. Al primo uso Cloudflare richiede un metodo di pagamento (piano gratuito generoso: ~10GB storage, egress gratuito).
- [ ] **Crea un bucket**: nome `<nome>-media` (es. `cirmo-media`, `teamhero-media`). Un bucket per sito.
- [ ] **Rendi pubblico tramite dominio custom** (i bucket R2 sono privati di default): Bucket → **Settings** → **Public access > Custom Domains** → **Connect Domain** → inserisci `media.<nome>.it` → Cloudflare crea il record DNS → conferma. Stato: *Initializing* → *Active* in pochi minuti.
- [ ] **Non usare** l'URL `*.r2.dev` in produzione: ha rate limit stretti. Sempre dominio custom.
- [ ] Nel codice referenziare gli asset con URL assoluti: `https://media.<nome>.it/hero.mp4`, `https://media.<nome>.it/foto-marco.webp`.

**Come caricare gli asset (due metodi):**

**Dashboard Cloudflare** (consigliato per upload occasionali): R2 → bucket → **Upload** → trascina i file. Semplice, nessun comando.

**Wrangler da terminale** (consigliato per upload multipli o automatizzati):
```bash
# Setup una tantum (vale per tutti i siti, tutto il PC):
npm install -g wrangler
wrangler login   # apre il browser per autenticarsi con Cloudflare

# Upload singolo file:
wrangler r2 object put <nome>-media/nome-file.mp4 --file="C:\percorso\file.mp4"

# Lista contenuto bucket:
wrangler r2 object list <nome>-media
```
Il `wrangler login` si fa **una volta sola** per PC — le credenziali restano in `~/.wrangler/config`. Non va nei file del progetto, non nel repo.

> Nota: il dominio custom deve essere su Cloudflare (stesso account del bucket). Se il dominio non è ancora gestito da Cloudflare, va prima aggiunto come zona.

## A.6 Sistema di health-check (monitoraggio automatico via Vercel Cron)

Ogni sito in produzione ha un controllo automatico giornaliero che verifica che sia "in salute" e, se qualcosa è rotto, **apre da solo una issue su GitHub** — così te ne accorgi senza dover guardare, e senza tenere nessun PC acceso. (Riferimento reale: `sito_teamhero`.)

**Principio architetturale fondamentale:** i controlli girano **DENTRO Vercel** (via Cron), NON da uno script esterno. È una scelta obbligata, non un'opzione: un probe esterno che sonda il sito da un datacenter viene **bloccato con HTTP 403** dalla protezione anti-DDoS di Vercel (sul piano Hobby non è scavalcabile dall'esterno, nemmeno col Protection Bypass). Il Cron invece invoca la funzione dall'interno, non attraversa il firewall, è gratis ed è incluso in Hobby.

> Lezione appresa su teamhero: NON costruire script esterni (tipo routine che fanno fetch del sito). Falliscono. Usare sempre il Cron interno.

**File del sistema** (da replicare nel nuovo sito):

| File | Ruolo |
|---|---|
| `lib/checks.js` | La logica dei controlli, condivisa. Il "cuore" del sistema. |
| `app/api/health/route.ts` | Endpoint per verifica manuale dal browser. Protetto da token (`HEALTH_TOKEN`). |
| `app/api/health-cron/route.ts` | Eseguito dal Cron Vercel. Fa i check; se KO apre/aggiorna una issue su GitHub. |
| `vercel.json` | Definisce il Cron: path `/api/health-cron`, schedule giornaliero (es. `0 6 * * *` = 06:00 UTC). |

**Cosa controllare** (adattare per sito): la home risponde 200 e contiene un testo atteso; le pagine privacy/cookie sono raggiungibili; il bot risponde (chiave Anthropic valida + modello esistente); il servizio email è raggiungibile; le env critiche (es. webhook lead) sono configurate.

**Setup:**
- [ ] Porta `lib/checks.js`, `api/health` e `api/health-cron` nel nuovo sito, adattando le stringhe attese (testo home, path policy, ecc.).
- [ ] Aggiungi il Cron in `vercel.json` (schedule giornaliero; su Hobby max 2 cron, frequenza giornaliera).
- [ ] Imposta su Vercel le env del sistema: `HEALTH_TOKEN` (protegge `/api/health`), `GITHUB_TOKEN` (fine-grained, solo questo repo, permesso **Issues: Read & write**, per aprire le issue), `CRON_SECRET` (protegge l'endpoint cron; Vercel la invia in automatico).
- [ ] Verifica manuale quando vuoi: `https://<dominio>/api/health?token=<HEALTH_TOKEN>` → JSON con i check e `ok: true/false`.
- [ ] Gli allarmi compaiono come **issue GitHub** con label `health` nel repo del sito. Le chiudi tu a mano quando il problema è risolto.

**Manutenzione e sicurezza:**
- I segreti (`HEALTH_TOKEN`, `GITHUB_TOKEN`, `CRON_SECRET`) stanno SOLO su Vercel, mai hardcoded nel codice. Leggere sempre da `process.env` senza fallback in chiaro.
- Il `GITHUB_TOKEN` fine-grained **scade**: alla scadenza il cron non apre più issue (il check gira comunque). Rigenerarlo su GitHub e aggiornarlo su Vercel; segnare in calendario la scadenza.
- Per aggiungere/togliere un controllo si modifica solo `lib/checks.js` (logica condivisa tra endpoint manuale e cron).

> Limite Hobby: cron a frequenza **giornaliera** (orario approssimativo). Per frequenza oraria serve Vercel Pro, oppure spostare il probe su una GitHub Action schedulata (che, girando da GitHub, non è soggetta allo stesso blocco di Vercel sul probe esterno — ma resta più complessa del cron interno).

## A.7 Variabili d'ambiente — regole

- Le chiavi vere stanno **solo** su Vercel (Settings → Environment Variables) e in un **password manager** come backup. MAI nel codice, MAI in file versionati.
- In locale, per i test, si usa `.env.local` (già ignorato da git). I valori si recuperano dal password manager o da Vercel.
- Nel repo si tiene `.env.example` con i **nomi** delle variabili e nessun valore.
- Nel codice si legge sempre da `process.env.NOME` **senza fallback in chiaro** (niente `|| "valore"`).

Variabili tipiche (a seconda delle feature attivate):

| Variabile | Quando serve |
|---|---|
| `ANTHROPIC_API_KEY` | bot chat |
| `ANTHROPIC_MODEL` | opzionale, override modello bot |
| `RESEND_API_KEY` | email via Resend (opzione 1) |
| `GOOGLE_SHEET_WEBHOOK` | lead su Sheet (opzione 2) |
| `HEALTH_TOKEN` | protegge `/api/health` (health-check, A.6) |
| `GITHUB_TOKEN` | il cron apre le issue di allarme (A.6) |
| `CRON_SECRET` | protegge `/api/health-cron` (A.6) |

---

# PARTE B — Blueprint tecnico

## B.1 Stack standard

- **Next.js** (App Router) + **TypeScript** + **React**.
- Styling: CSS globale con variabili in `:root` (palette e token), oppure Tailwind se preferito. Coerenza prima di tutto: un solo approccio per sito.
- **Serverless**: route handlers Next.js in `app/api/<endpoint>/route.ts`.
- **Hosting**: Vercel (build automatica, zero-config).
- Niente segreti hardcoded, niente `node_modules` versionati.

## B.2 Struttura cartelle di riferimento

```
sito_<nome>/
├── app/
│   ├── layout.tsx              # layout root: <html lang>, metadata SEO/OG, font, JSON-LD
│   ├── page.tsx                # home (lingua default)
│   ├── globals.css             # palette in :root, stili globali
│   ├── components/             # componenti riusabili (Nav, Footer, ChatWidget, ...)
│   ├── data/                   # contenuti: translations/*.json, faq, ecc.
│   ├── api/
│   │   ├── chat/route.ts       # proxy bot → Anthropic (se bot attivo)
│   │   ├── contact/route.ts    # invio email (Resend) o
│   │   └── save-lead/route.ts  # invio lead (EmailJS+Sheet)
│   └── <lang>/page.tsx         # pagine per lingua (solo se multilingua)
├── public/                     # immagini, favicon, asset statici
├── .env.example                # nomi env, niente valori
├── CLAUDE.md                   # contesto del sito (PARTE C)
└── package.json
```

## B.3 Bot chat — incluso SOLO se serve

Il bot non è obbligatorio. Si include quando il sito fa lead-capture o assistenza. **Segue la lingua del sito**: la pagina passa la lingua corrente e il bot risponde in quella lingua.

Principi (riferimenti reali: `sito_cirmo` multilingua, `sito_teamhero` con rami conversazionali):

- **Proxy server-side**: il widget chiama `POST /api/chat`; la route inoltra ad Anthropic. La **API key resta solo server-side**, mai nel client.
- **Lingua**: la route costruisce un system prompt con l'istruzione di lingua + i contenuti localizzati. Per siti multilingua, il widget passa `?lang=<lang>`; per siti monolingua, lingua fissa.
- **Contenuti dalle FAQ**: il bot risponde attingendo alle **FAQ del sito** (vedi B.4). Le FAQ sono la fonte di verità del bot: stesse risposte in chat e in pagina.
- **Scope ristretto**: il system prompt limita il bot agli argomenti del sito/prodotto; fuori scope → messaggio di cortesia.
- **Lead capture (se previsto)**: a dati raccolti e consenso privacy dato, il modello emette un blocco delimitato (es. `[DATI_COMPLETI]...[/DATI_COMPLETI]` o `[SEND_LEAD]...`), il client lo estrae, lo rimuove dal testo mostrato, e invia via email/Sheet. Il formato del blocco deve restare allineato tra prompt e parser.
- **Modello**: stringa versionata esplicita (es. `claude-haiku-4-5` per chat leggere). Mai alias generici.

## B.4 FAQ a fine pagina

- Ogni sito ha una sezione **FAQ in fondo alla pagina** (prima del footer).
- Le FAQ sono in un file dati strutturato (es. `app/data/faq` o dentro le translations), così sono **riusabili sia in pagina sia dal bot**.
- Multilingua: una versione FAQ per lingua.
- Regola: il bot non inventa: se la domanda è coperta dalle FAQ, usa quelle; altrimenti risponde nei limiti dello scope.

## B.5 Palette, font, convenzioni

- Palette definita in `:root` di `globals.css` con variabili semantiche (`--bg`, `--text`, `--accent`, ecc.). Ogni sito ha la sua identità, ma la **struttura** dei token è la stessa.
- Font via `next/font/google` (es. su teamhero: Fraunces per i titoli, Outfit per il corpo).
- Nav fissa, footer con link legali (Privacy, Cookie), CTA che apre il bot (se presente).
- Reveal-on-scroll e micro-animazioni opzionali, ma coerenti.

## B.6 Pagine legali e compliance (obbligatorie prima del go-live)

- [ ] **Privacy Policy** (`/privacy-policy`).
- [ ] **Cookie Policy** (`/cookie-policy`) + cookie banner (es. CookieYes).
- [ ] Se il bot raccoglie dati: **consenso privacy esplicito** prima di salvare qualsiasi contatto.
- [ ] I link legali nel footer NON devono restare `#` placeholder al go-live.

---

# PARTE C — Generare il CLAUDE.md del nuovo sito

Quando il sito ha una struttura iniziale, genera il suo `CLAUDE.md` con Claude Code (lavorando nella cartella del sito). Prompt:

```
Analizza la cartella `sito_<nome>`: struttura reale, file presenti (componenti,
route in app/api, css, config) e contenuto. Genera un `CLAUDE.md` nella radice
che serva da contesto permanente: cos'è il sito, stack reale, struttura file,
palette/font dedotti dal CSS, come funziona il bot e le serverless (se presenti),
flusso di deploy, pending. Aggiungi come sezione finale la regola di manutenzione:
"Quando si introduce una modifica strutturale, aggiornare questo CLAUDE.md e
includerlo nel commit con messaggio `docs: update CLAUDE.md`."
NON inserire token/chiavi/segreti. Segna come "DA DEFINIRE" ciò che non è deducibile.
```

---

# Checklist sintetica (da spuntare a ogni nuovo sito)

- [ ] Repo `mbtt-teamhero/sito_<nome>` privato, branch `main`
- [ ] Progetto Next.js + push iniziale
- [ ] Progetto Vercel collegato, deploy automatico verificato
- [ ] Email configurata (Resend **oppure** EmailJS+Sheet)
- [ ] Sistema health-check via Vercel Cron (lib/checks + api/health + api/health-cron + vercel.json)
- [ ] Immagini e video su Cloudflare R2 con dominio custom (`media.<nome>.it`)
- [ ] Env impostate su Vercel + `.env.example` nel repo + password manager
- [ ] Bot configurato (solo se serve), con lingua del sito e FAQ come fonte
- [ ] Sezione FAQ a fine pagina
- [ ] Privacy + Cookie policy + banner + consenso bot
- [ ] `CLAUDE.md` del sito generato
- [ ] Nessun segreto nel codice (verificato)

---

## Regola di manutenzione di questo standard

Questo documento evolve. Aggiornarlo quando:
- cambia lo stack o un servizio (es. si sostituisce un provider email),
- si introduce una nuova convenzione valida per tutti i siti,
- si chiarisce un punto rimasto aperto.

Lo standard descrive il modello "a regime". I siti reali possono divergere finché
non vengono allineati: documentare le divergenze nel `CLAUDE.md` del singolo sito.

— *TeamHero · making change powerful*
