# 📝 TEXT REVIEW AGENT - Planning Document

## Overview
**Text Review Agent** è il workflow automatico per **revisioni E generazione** di copy, testo discorsivo e contenuti dei siti LAIP e SWITCH UP usando **markdownlint** + **ChatGPT**.

Modalità:
- **REVISIONE**: Migliora testo esistente
- **GENERAZIONE**: Crea nuovo testo da zero con stile specifico (discorsivo, serio, descrittivo, etc.)

Ogni richiesta segue lo STESSO processo strutturato per qualità, coerenza e persuasività.

---

## 🔧 MARKDOWNLINT CONFIGURATION

### Installation
```bash
npm install -g markdownlint-cli
# or
npm install markdownlint-cli --save-dev
```

### Rules Attivi (.markdownlint.json)
```json
{
  "MD001": true,
  "MD003": {"style": "consistent"},
  "MD004": {"style": "consistent"},
  "MD005": true,
  "MD007": {"indent": 2},
  "MD009": true,
  "MD010": true,
  "MD011": true,
  "MD012": {"maximum": 1},
  "MD013": {"line_length": 120},
  "MD014": true,
  "MD018": true,
  "MD019": true,
  "MD020": true,
  "MD021": true,
  "MD022": true,
  "MD023": true,
  "MD024": false,
  "MD025": true,
  "MD026": {"punctuation": ".,;:!?"},
  "MD027": true,
  "MD028": true,
  "MD029": {"style": "ordered"},
  "MD030": {"ul_single": 1, "ol_single": 1},
  "MD031": true,
  "MD032": true,
  "MD033": true,
  "MD034": true,
  "MD035": true,
  "MD036": true,
  "MD037": true,
  "MD038": true,
  "MD039": true,
  "MD040": true,
  "MD041": true,
  "MD042": true,
  "MD043": true,
  "MD044": false,
  "MD045": true,
  "MD046": {"style": "consistent"},
  "MD047": true,
  "MD048": true
}
```

### What Markdownlint Checks
✅ Heading hierarchy (MD001)
✅ List consistency (MD004, MD005, MD029)
✅ Link format (MD011, MD034)
✅ Line length (MD013 - max 120 chars)
✅ Punctuation consistency (MD026)
✅ Spacing issues (MD012, MD027, MD028)
✅ Code block format (MD040)
✅ No trailing spaces (MD009, MD010)

---

## 🔄 WORKFLOW AUTOMATICO

### Step 1: RICHIESTA REVISIONE TESTO (Marco)
```
"Migliora il copy della sezione hero di LAIP"
"Rivedi il tono della pagina partners"
"Rendi più persuasivo il testo pricing"
"Controlla grammatica e coerenza"
```

### Step 2: ANALISI RICHIESTA (Text Review Agent)
✅ Tipo di revisione (copy, tono, grammatica, persuasività, struttura)
✅ Sezione interessata (hero, pricing, benefits, partners)
✅ Sito interessato (LAIP o SWITCH UP)
✅ Scope: Singolo paragrafo vs sezione vs intero sito

### Step 3: MARKDOWNLINT CHECK
Eseguo markdownlint su:
- Formattazione markdown
- Consistenza liste/heading
- Lunghezza linee
- Spaziatura
- Punteggiatura

```bash
markdownlint <file> --config .markdownlint.json
```

### Step 4: CHATGPT ANALYSIS
Cito ChatGPT per:
- Miglioramento copy e tono
- Persuasività e call-to-action
- Clarità e readability
- Coerenza con brand voice

### Step 5: TEXT GENERATION
Genero:
- Versione rivista del testo
- Varianti alternative (A/B)
- Note su cambiamenti

### Step 6: IMPLEMENTATION
Implemento nel sito (index.html, switchup.html, partners.html)

### Step 7: VERSIONING
Salvo versione in text-assets/ con timestamp

---

## 📚 PROMPT LIBRARY

### 📄 PROMPTS COPY/COPYWRITING

#### Revisione Testi Esistenti
```
"Migliora il testo '[TESTO_ATTUALE]' per la sezione [SEZIONE] mantenendo [TONO]. Focus su [BENEFIT]"

"Riscrivi in modo più persuasivo: '[TESTO]'. Aggiungi urgenza/valore senza risultare forzato"

"Semplifica questo testo per aumentare readability: '[TESTO]'"

"Crea 3 varianti di headline per [SEZIONE] che comunichino [MESSAGGIO]"

"Rendi questo CTA più convincente: '[TESTO_ATTUALE]'"
```

#### Generazione Nuovi Testi da Zero
```
"Crea un testo [STILE] per la sezione [SEZIONE] di [SITO]. Tema: [TEMA]. Lunghezza: [LUNGHEZZA]. Tono: [TONO]"

"Scrivi una descrizione discorsiva per [ELEMENTO]. Stile narrativo, conversazionale. Include: [PUNTI CHIAVE]"

"Genera versione formale/seria di questa descrizione: '[RIFERIMENTO]'. Tono professionale, credibilità"

"Crea 3 varianti di copy per [ELEMENTO]: (1) Discorsiva, (2) Seria/Formale, (3) Sarcastica/Casual"

"Scrivi una bio/descrizione per [SOGGETTO]. Tono: [TONO]. Lunghezza: [LUNGHEZZA]. Focus su: [ASPETTI]"
```

### 💬 PROMPTS TONO/VOCE
```
"Analizza il tono attuale di questo testo e suggerisci come renderlo più [AGGETTIVO]: '[TESTO]'"

"Uniforma il tono di questi 3 paragrafi: [PARAGRAFI]. Brand voice: [STILE]"

"Questo testo suona troppo [AGGETTIVO]. Riscrivilo in modo più [AGGETTIVO_TARGET]"
```

### ✨ PROMPTS PERSUASIVITÀ
```
"Migliora la persuasività di questo pitch: '[TESTO]'. Focus su pain points e solutions"

"Aggiungi social proof/credibilità a questo testo: '[TESTO]'"

"Questa sezione non convincente. Riscrivila evidenziando: [BENEFICI CHIAVE]"

"Crea versione più persuasiva della call-to-action: '[TESTO_ATTUALE]'"
```

### 📊 PROMPTS CHIAREZZA/STRUTTURA
```
"Analizza la leggibilità di questo testo. Quali frasi sono troppo lunghe? '[TESTO]'"

"Struttura questo contenuto con heading/list per migliore readability: '[TESTO]'"

"Migliora la scansione visiva di questa sezione senza cambiare significato: '[TESTO]'"

"Rimuovi il jargon tecnico e semplifica: '[TESTO]'"
```

### 🌍 PROMPTS LOCALIZZAZIONE
```
"Traduci questo testo in [LINGUA] mantenendo tono e persuasività: '[TESTO]'"

"Adatta questo testo per pubblico [TARGET] (es. motorsport enthusiasts): '[TESTO]'"

"Usa linguaggio più tecnico per [AUDIENCE] in questa sezione: '[TESTO]'"
```

---

## 🎨 STILI DI GENERAZIONE TESTO

### Discorsivo (Narrative)
✅ Conversazionale, amichevole
✅ Racconta una storia
✅ Personal touch, relatable
✅ Emozioni e connessione umana
✅ Adatto per: Hero, benefits, testimonials

**Prompt Base:**
```
"Scrivi in stile discorsivo/narrativo: [TEMA]. Tono caldo, amichevole, conversazionale. 
Come se stessi parlando con un amico. Includi: [PUNTI CHIAVE]. Lunghezza: [LUNGHEZZA]"
```

### Serio/Formale (Professional)
✅ Credibilità e autorità
✅ Linguaggio tecnico/professionale
✅ Focus su fatti e risultati
✅ Tono confidenziale, esperto
✅ Adatto per: Pricing, features, technical specs

**Prompt Base:**
```
"Scrivi in stile formale/professionale: [TEMA]. Tono serio, autorevole, competente.
Enfatizza credibilità e expertise. Includi: [PUNTI CHIAVE]. Lunghezza: [LUNGHEZZA]"
```

### Descrittivo (Descriptive)
✅ Dettagli vividi
✅ Immagini mentali
✅ Uso di aggettivi evocativi
✅ Coinvolgimento sensoriale
✅ Adatto per: Product descriptions, visual sections

**Prompt Base:**
```
"Scrivi descrizione vivida di: [SOGGETTO]. Stile descrittivo, evocativo. 
Usa aggettivi forti, crea immagini mentali. Lunghezza: [LUNGHEZZA]"
```

### Persuasivo (Persuasive)
✅ Convince all'azione
✅ Urgenza e valore
✅ Call-to-action implicita
✅ Focus su benefici
✅ Adatto per: CTA, pricing, value propositions

**Prompt Base:**
```
"Scrivi testo persuasivo su: [TEMA]. Stile convincente, focus su benefici.
Aggiungi urgenza (senza esagerare) e valore chiaro. Includi CTA. Lunghezza: [LUNGHEZZA]"
```

### Casual/Sarcastico (Casual/Witty)
✅ Tono leggero, divertente
✅ Sarcasmo intelligente
✅ Conversazione naturale
✅ Personalità forte
✅ Adatto per: Social copy, testimonials, fun sections

**Prompt Base:**
```
"Scrivi in tono casual/sarcastico su: [TEMA]. Tono divertente, intelligente, personale.
Sarcasmo ok se appropriato. Mantieni professionalità. Lunghezza: [LUNGHEZZA]"
```

---

## 📁 ASSET ORGANIZATION

```
C:\Users\marco\Documents\set up\
├── text-assets/                     # NUOVA CARTELLA
│   ├── markdownlint/
│   │   └── .markdownlint.json       # Config file
│   ├── prompts/                     # Prompt library salvati
│   │   ├── copy-prompts.txt
│   │   ├── tone-prompts.txt
│   │   ├── persuasion-prompts.txt
│   │   ├── clarity-prompts.txt
│   │   └── localization-prompts.txt
│   ├── generated/                   # Testo generato/rivisto
│   │   ├── LAIP/
│   │   │   ├── hero-copy-v2.txt
│   │   │   ├── pricing-text-v3.txt
│   │   │   └── ...
│   │   └── SWITCHUP/
│   │       └── ...
│   ├── reports/                     # Markdownlint reports
│   │   ├── 2026-09-30-laip-full.txt
│   │   └── ...
│   └── versions/                    # Version history
│       └── YYYY-MM-DD-description/
├── GRAPHIC_AGENT_PLANNING.md
├── TEXT_REVIEW_AGENT_PLANNING.md
├── CLAUDE.md
├── index.html                       # LAIP
├── partners.html                    # LAIP Partners
└── switchup.html                    # SWITCH UP
```

---

## ✅ CHECKLIST PER OGNI REVISIONE

### Pre-Revisione
- [ ] Identificato tipo di revisione (copy, tono, grammatica, persuasività, struttura)
- [ ] Selezionata sezione/elemento
- [ ] Verificato contesto e audience
- [ ] Preparato testo per markdownlint

### Markdownlint Check
- [ ] Eseguito markdownlint
- [ ] Risolti warning/errori formali
- [ ] Verificata lunghezza linee (max 120 chars)
- [ ] Controllata punteggiatura consistente

### ChatGPT Enhancement
- [ ] Generato prompt appropriato
- [ ] Creato versioni alternative (A/B)
- [ ] Verificato tono coerente
- [ ] Controllato persuasività/chiarezza

### Post-Revisione
- [ ] Salvato asset con timestamp in text-assets/
- [ ] Aggiornato il sito
- [ ] Verificato preview (desktop, mobile)
- [ ] Testato leggibilità (readability score)
- [ ] Documentato la modifica nel version log

---

## 🚀 WORKFLOW RAPIDO (Da Ricordare)

### Quando Marco chiede revisione O generazione testo:
```
REVISIONE TESTO ESISTENTE:
1️⃣  ANALIZZA: Tipo di revisione?
2️⃣  MARKDOWNLINT: Esegui check formale
3️⃣  SELEZIONA: Prompt template dalla library
4️⃣  CHATGPT: "Usa questo prompt per migliorare..."
5️⃣  GENERA: Varianti testo rivisto
6️⃣  IMPLEMENTA: Nel sito
7️⃣  SALVA: In text-assets/ con timestamp
8️⃣  MOSTRA: Preview aggiornato

GENERAZIONE NUOVO TESTO:
1️⃣  ANALIZZA: Quale stile? (Discorsivo/Serio/Descrittivo/Persuasivo/Casual)
2️⃣  SELEZIONA: Stile + Prompt template appropriato
3️⃣  CHATGPT: "Genera testo [STILE] per [SEZIONE]..."
4️⃣  GENERA: Testo nuovo da zero (o 3 varianti se richieste)
5️⃣  SALVA: In text-assets/generated con timestamp
6️⃣  IMPLEMENTA: Nel sito
7️⃣  MOSTRA: Preview con nuovo testo
```

---

## 💾 VERSION LOG

### Template Entry:
```
📅 YYYY-MM-DD | [SITE] | [TIPO REVISIONE]
Richiesta: "[DESCRIZIONE]"
Elemento: [SEZIONE]
Asset: text-assets/generated/[SITE]/[FILE]
Markdownlint: ✅ Passed / ❌ [N] issues fixed
ChatGPT Prompt: [CATEGORIA]
Status: ✅ Implementato
```

---

## 🎯 WORKFLOW EXAMPLES

### Esempio 1: Migliorare Copy Hero
```
Marco: "Migliora il copy della sezione hero di LAIP"

Agent Process:
1. Tipo: Copy enhancement
2. Markdownlint: Esegui check su hero section
3. Prompt: "Migliora persuasività della headline hero"
4. ChatGPT: Genera 3 versioni alternative
5. Asset: Salva in text-assets/generated/LAIP/
6. Implementa: Aggiorna index.html hero section
7. Mostra: Preview con nuovo copy
```

### Esempio 2: Revisione Tono Pagina
```
Marco: "Rivedi il tono della pagina partners"

Agent Process:
1. Tipo: Tone review
2. Markdownlint: Check su partners.html
3. Prompt: "Uniforma tono a brand voice professionale ma amichevole"
4. ChatGPT: Riscrive sezioni con tono inconsistente
5. Asset: Salva versione rivista
6. Implementa: Aggiorna partners.html
7. Mostra: Preview con tono uniforme
```

### Esempio 3: Aumentare Persuasività Pricing
```
Marco: "Rendi più persuasivo il testo pricing"

Agent Process:
1. Tipo: Persuasion enhancement
2. Markdownlint: Controlla punteggiatura/struttura pricing
3. Prompt: "Aggiungi urgenza/value proposition alle plan descriptions"
4. ChatGPT: Riscrive CTA pricing con focus su benefici
5. Asset: Genera pricing-copy-v2.txt
6. Implementa: Aggiorna sezione pricing
7. Mostra: Preview con nuovo pricing copy
```

### Esempio 4: Generare Testo Discorsivo per Hero
```
Marco: "Crea un testo discorsivo per la hero section di LAIP"

Agent Process:
1. Tipo: Text generation (narrative style)
2. Stile: Discorsivo - conversazionale, storytelling
3. Prompt: "Scrivi hero copy discorsivo per sito vendita website AI. Tono caldo, narrativo. 
           Includi: problema, soluzione, valore. Lunghezza: 150 parole"
4. ChatGPT: Genera testo narrativo con storytelling
5. Asset: Salva hero-narrative-v1.txt
6. Implementa: Aggiorna hero section
7. Mostra: Preview con nuovo hero text discorsivo
```

### Esempio 5: Generare 3 Varianti Stile Diverso
```
Marco: "Crea 3 versioni della sezione benefits: una discorsiva, una seria, una persuasiva"

Agent Process:
1. Tipo: Multi-style text generation
2. Stili: Narrative + Professional + Persuasive
3. Prompt: "Genera 3 varianti di copy per benefits LAIP:
           (1) Stile discorsivo - narrativo, amichevole
           (2) Stile serio - professionale, credibilità
           (3) Stile persuasivo - urgenza, value focus
           Includi: [BENEFIT POINTS]. Lunghezza: 100 parole each"
4. ChatGPT: Genera 3 versioni distinte
5. Asset: Salva benefits-narrative.txt, benefits-professional.txt, benefits-persuasive.txt
6. Implementa: Mostra preview di tutti e 3
7. Utente sceglie: Quale variante preferisci? (A/B/C)
```

### Esempio 6: Generare Descrizione Prodotto Descrittiva
```
Marco: "Scrivi una descrizione del nostro servizio in stile descrittivo e vivido"

Agent Process:
1. Tipo: Text generation (descriptive style)
2. Stile: Descrittivo - vivido, evocativo, immagini mentali
3. Prompt: "Scrivi descrizione vivida del servizio 'siti web AI' per LAIP.
           Stile descrittivo, aggettivi forti, coinvolgimento sensoriale.
           Lunghezza: 200 parole"
4. ChatGPT: Genera testo descrittivo con immagini mentali forti
5. Asset: Salva service-description-vivid.txt
6. Implementa: Aggiorna sezione servizio
7. Mostra: Preview con descrizione vivida
```

---

## 🔍 MARKDOWNLINT VS CHATGPT

| Aspetto | Markdownlint | ChatGPT |
|---------|-------------|---------|
| **Controlla** | Formato/struttura markdown | Tono/persuasività/chiarezza |
| **Esegue** | Automatico su file | Su richiesta con prompt |
| **Tipo Error** | Formale (sintassi) | Stilistico (qualità) |
| **Output** | Report di errori | Testo rivisto |
| **Integrazione** | CLI tool | API + prompt templates |

---

## 📝 NOTE IMPORTANTI

✅ **REVISIONE + GENERAZIONE**: Non solo migliora testi, ma crea testi nuovi da zero
✅ **5 Stili Disponibili**: Discorsivo, Serio, Descrittivo, Persuasivo, Casual
✅ **Markdownlint sempre eseguito** per controllo formale
✅ **ChatGPT sempre referenziato** per creatività e qualità
✅ **Niente domande** - agisco automaticamente su richiesta
✅ **Versioning** di tutte le versioni testo generate
✅ **Multi-varianti**: Genero 3 versioni stili diversi quando richiesto (A/B/C testing)
✅ **Readability focused** - testo semplice, persuasivo, chiaro

### Comandi Tipici che Capisco
- "Crea un testo discorsivo per..."
- "Scrivi una descrizione seria/formale di..."
- "Genera 3 varianti copy: una discorsiva, una seria, una persuasiva"
- "Rivedi il tono di questa sezione"
- "Migliora questo copy in modo più persuasivo"
- "Crea una descrizione vivida di..."
- "Scrivi in tono casual/sarcastico su..."

---

**Text Review Agent Potenziato** 📝✨
Revisione testi + Generazione testi nuovi con stili specifici!
