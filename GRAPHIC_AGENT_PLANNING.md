# 🎨 GRAPHIC AGENT - Planning Document

## Overview
**Graphic Agent** è il workflow automatico per gestire TUTTI i cambiamenti grafici nei siti LAIP e SWITCH UP usando ChatGPT come riferimento principale.

Ogni richiesta grafica segue lo STESSO processo strutturato per massimizzare velocità e coerenza.

---

## 📋 DESIGN SYSTEM

### Colori
- **LAIP**: Azzurro luminoso (#0099FF) + Dark background (#0a0a0a)
- **SWITCH UP**: Verde neon (#22FF00 / #B8FF00) + Dark background (#070908)
- **Neutri**: Grigio (#2a2a2a), Bianco (#fff), Testo scuro (#1a1a1a)

### Tipografia
- **Headings**: Barlow Condensed (700, 800)
- **Body**: Inter (400, 500, 600)
- **Hero/Special**: Lora (per effetto premium)

### Spacing & Grid
- Mobile first responsive
- Breakpoints: 600px, 768px, 1024px, 1200px
- Gap standard: 2rem, 3rem
- Padding sezioni: 5rem 2rem

### Animazioni
- Transizioni: 0.3s ease
- Fade in/out: @keyframes fadeIn/fadeOut
- Glow effects: drop-shadow per icone/logo
- No lag: max 60fps, CSS3 only

---

## 🔄 WORKFLOW AUTOMATICO

### Step 1: RICHIESTA GRAFICA (Marco)
```
"Ingrandisci il logo header"
"Cambia colore pulsanti"
"Crea intro animation per LAIP"
```

### Step 2: ANALISI RICHIESTA (Graphic Agent)
✅ Tipo di modifica (logo, colore, animazione, layout, copy)
✅ Sezione interessata (hero, header, buttons, carousel)
✅ Sito interessato (LAIP o SWITCH UP)
✅ Impatto responsive (mobile, tablet, desktop)

### Step 3: PROMPT GENERATION
Seleziono il prompt template giusto dalla Prompt Library

### Step 4: CHATGPT REFERENCE
Cito ChatGPT per:
- Idee di design
- Codice CSS/animazioni
- Copywriting
- Ottimizzazioni estetiche

### Step 5: ASSET GENERATION
Genero:
- File CSS/HTML modificato
- Immagini (DALL-E se necessario)
- Screenshot preview

### Step 6: IMPLEMENTATION
Implemento nel sito e mostro il risultato

### Step 7: VERSIONING
Salvo la versione in asset folder con timestamp

---

## 📚 PROMPT LIBRARY

### 🔵 PROMPTS LOGO/BRANDING
```
"Creare versione ingrandita del logo [SITE] da [DIM_ATTUALE]px a [DIM_NUOVA]px mantenendo proporzioni. Mantenere chiarezza e leggibilità"

"Suggerisci animazione intro per il logo [SITE] con effetti neon in [COLORE]. Usare CSS @keyframes con glow effect"

"Crea versione responsive del logo per mobile, tablet, desktop con font-size differenti"
```

### 🎨 PROMPTS COLORI/STYLING
```
"Migliora la palette colore per la sezione [SEZIONE] nel sito [SITE]. Colori primari: [COLORI]. Suggerisci contrasti e sfumature"

"Crea gradient background per [ELEMENTO] usando colori [COLORI] con effetto professionale ma moderno"

"Suggerisci miglioramenti estetici per i pulsanti CTA mantenendo stile [SITE]"
```

### ✨ PROMPTS ANIMAZIONI
```
"Codice CSS per animazione [TIPO] su [ELEMENTO]. Durata: [MS]ms. Effetto: [EFFETTO]. 60fps, no lag"

"Crea @keyframes per animazione di fade-in del testo hero con delay progressivo tra elementi"

"Suggerisci animazioni micro-interazioni per hover su bottoni e link nel design [SITE]"
```

### 📐 PROMPTS LAYOUT/RESPONSIVE
```
"Ottimizza layout per mobile/tablet/desktop della sezione [SEZIONE]. Breakpoints: 600px, 768px, 1024px, 1200px"

"Suggerisci miglioramenti di spacing e padding per la sezione [SEZIONE] per migliore UX"

"Analizza layout attuale e proponi ottimizzazioni di grid/flexbox per [SEZIONE]"
```

### ✍️ PROMPTS COPYWRITING
```
"Riscrivi il testo '[TESTO_ATTUALE]' in modo più persuasivo e conciso per [CONTESTO]"

"Suggerisci 3 varianti di tagline per [SEZIONE] che comunichino [MESSAGGIO]"

"Migliora la copy della sezione [SEZIONE] con focus su benefici, non features"
```

### 🖼️ PROMPTS IMMAGINI (DALL-E)
```
"Genera immagine di [DESCRIZIONE] nello stile [STILE]. Risoluzione: [DIM]. Colori dominanti: [COLORI]"

"Crea hero image per sito motorsport con tema [TEMA]. Includi: [ELEMENTI]. Style: moderno, profesionale"

"Genera background pattern [TIPO] con colori [COLORI] in stile [STILE]"
```

---

## 📁 ASSET ORGANIZATION

```
C:\Users\marco\Documents\set up\
├── images/                          # Immagini siti
│   ├── logo-switchup.png
│   ├── pilots-photo.png
│   └── screenshots/
├── graphic-assets/                  # NUOVA CARTELLA
│   ├── prompts/                     # Prompt library salvati
│   │   ├── logo-prompts.txt
│   │   ├── color-prompts.txt
│   │   ├── animation-prompts.txt
│   │   └── layout-prompts.txt
│   ├── generated/                   # Asset generati
│   │   ├── LAIP/
│   │   │   ├── intro-animation-v1.css
│   │   │   ├── hero-logo-v2.png
│   │   │   └── ...
│   │   └── SWITCHUP/
│   │       └── ...
│   ├── colors/                      # Color palettes
│   │   ├── laip-palette.json
│   │   └── switchup-palette.json
│   ├── fonts/                       # Typography specs
│   │   └── font-specifications.json
│   └── versions/                    # Version history
│       └── YYYY-MM-DD-change-description/
├── index.html                       # LAIP
├── partners.html                    # LAIP Partners
└── switchup.html                    # SWITCH UP
```

---

## ✅ CHECKLIST PER OGNI MODIFICA GRAFICA

### Pre-Modifica
- [ ] Analizzato tipo di richiesta (logo, colore, animazione, layout, copy)
- [ ] Identificata sezione e sito interessati
- [ ] Verificato design system (colori, font, spacing)
- [ ] Considerato impatto responsive (mobile, tablet, desktop)

### Durante Modifica
- [ ] Generato prompt ChatGPT appropriato
- [ ] Creato asset/codice
- [ ] Testato su tutti i breakpoint
- [ ] Verificato performance (no lag, 60fps)
- [ ] Controllato contrasto colori (accessibilità)

### Post-Modifica
- [ ] Salvato asset con timestamp in graphic-assets/
- [ ] Aggiornato il sito
- [ ] Verificato preview (desktop, tablet, mobile)
- [ ] Testato animazioni e interazioni
- [ ] Documentato la modifica nel version log

---

## 🚀 WORKFLOW RAPIDO (Da Ricordare)

### Quando Marco chiede cambio grafico:
```
1️⃣  ANALIZZA: Tipo di richiesta?
2️⃣  SELEZIONA: Prompt template dalla library
3️⃣  CHATGPT: "Usa questo prompt per generare..."
4️⃣  GENERA: Asset/codice
5️⃣  IMPLEMENTA: Nel sito
6️⃣  SALVA: In graphic-assets/ con timestamp
7️⃣  MOSTRA: Preview aggiornato
```

---

## 💾 VERSION LOG

### Template Entry:
```
📅 YYYY-MM-DD | [SITE] | [TIPO MODIFICA]
Richiesta: "[DESCRIZIONE]"
Cambio: [ELEMENTO]
Asset: graphic-assets/generated/[SITE]/[FILE]
ChatGPT Prompt: [CATEGORIA]
Status: ✅ Implementato
```

---

## 🎯 WORKFLOW EXAMPLES

### Esempio 1: Ingrandire Logo
```
Marco: "Ingrandisci il logo SWITCH UP nell'header"

Agent Process:
1. Tipo: Logo sizing
2. Prompt Template: "Creare versione ingrandita del logo..."
3. ChatGPT: "Migliora il logo da 90px a 160px mantenendo proporzioni"
4. Asset: Modifica inline style in index.html
5. Salva: graphic-assets/versions/2026-09-30-logo-resize/
6. Mostra: Preview dell'header aggiornato
```

### Esempio 2: Nuova Animazione
```
Marco: "Crea intro animation per LAIP come quella di SWITCH UP"

Agent Process:
1. Tipo: Animation/Intro
2. Prompt Template: "Codice CSS per animazione..."
3. ChatGPT: "Crea @keyframes per fade-in del logo con glow effect"
4. Asset: Nuovo CSS @keyframes + HTML overlay
5. Salva: graphic-assets/generated/LAIP/intro-animation.css
6. Mostra: Preview dell'animazione
```

### Esempio 3: Cambio Colori
```
Marco: "Cambia il colore dei pulsanti in azzurro"

Agent Process:
1. Tipo: Color update
2. Prompt Template: "Migliora palette colore..."
3. ChatGPT: "Suggerisci variante azzurra per CTA buttons"
4. Asset: Aggiorna CSS color variables
5. Salva: graphic-assets/colors/laip-palette-v2.json
6. Mostra: Preview con nuovi colori
```

---

## 📝 NOTE IMPORTANTI

✅ **Ogni richiesta grafica** usa QUESTO workflow
✅ **Niente domande** - agisco automaticamente
✅ **ChatGPT sempre referenziato** per coerenza
✅ **Versioning** di tutti gli asset generati
✅ **Preview sempre mostrato** prima di finire
✅ **Performance first** - animazioni 60fps, no lag
✅ **Responsive by default** - mobile, tablet, desktop

---

**Graphic Agent Attivo e Pronto** 🎨✨
Ogni richiesta grafica = Workflow automatico completo!
