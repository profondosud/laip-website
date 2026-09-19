# 🚀 Sistema di Generazione Siti Bozza LAIP

Genera rapidamente siti web di presentazione in 24 ore per i clienti.

## 📁 File

- **TEMPLATE_CLIENTE.md** - Template markdown generico da compilare per ogni cliente
- **genera_sito.py** - Script Python che converte il markdown in HTML finale
- **README.md** - Questo file (istruzioni d'uso)

---

## ⚡ USO VELOCE

### 1️⃣ Copia il template
```bash
cp TEMPLATE_CLIENTE.md pizzeria_mario.md
```

### 2️⃣ Compila i dati del cliente
Apri `pizzeria_mario.md` e compila tutte le sezioni `[...]` con i dati reali del cliente

### 3️⃣ Genera il sito HTML
```bash
python genera_sito.py pizzeria_mario.md
```

Risultato: `pizzeria_mario_20260919_143022.html` (pronto da inviare!)

---

## 📋 Cosa va compilato

### Sezioni OBBLIGATORIE
- `AZIENDA` - Nome dell'azienda
- `SETTORE` - Settore di business
- `TITOLO` - Titolo hero (max 10 parole)
- `SOTTOTITOLO` - Sottotitolo (max 2 righe)
- I 6 `SERVIZIO_*` - Servizi/prodotti
- I 3 `PIANO_*` - Piani prezzi
- I 4 `STEP_*` - Come funziona

### Sezioni OPZIONALI
- FAQ (max 5)
- Contatti (email, telefono, indirizzo)
- SEO (title, description)

---

## 🎨 Personalizzazione

### Cambia il tema
Nel template, modifica:
```
WEBSITE_TEMA: [light/dark]
COLORE_PRIMARIO: [#00d4ff]
```

Opzioni colori:
- `#00d4ff` - Cyan (default LAIP)
- `#ff6b6b` - Rosso
- `#4ecdc4` - Teal
- `#ffd93d` - Giallo

### Cambia le icone
Usa [Font Awesome](https://fontawesome.com/icons) - esempi:
- `fas fa-rocket` - Razzo
- `fas fa-star` - Stella
- `fas fa-heart` - Cuore
- `fas fa-bolt` - Fulmine
- `fas fa-shield-alt` - Scudo
- `fas fa-server` - Server

---

## 📊 Tempo di generazione

| Fase | Tempo |
|------|-------|
| Compilare template | 5-10 min |
| Generare HTML | < 1 sec |
| Testare | 5 min |
| **TOTALE** | **15-20 min** |

---

## 🔄 Flusso Completo

```
1. Cliente richiede sito demo
   ↓
2. Copi TEMPLATE_CLIENTE.md → pizzeria_mario.md
   ↓
3. Compili i dati del cliente
   ↓
4. Esegui: python genera_sito.py pizzeria_mario.md
   ↓
5. Testi il file HTML nel browser
   ↓
6. Invia al cliente (oppure hospa su server)
   ↓
7. Auto-delete dopo 24 ore (da implementare)
```

---

## 💻 Requisiti

- Python 3.6+
- Niente dipendenze esterne (puro Python!)

---

## 📝 Esempio Compilazione

```markdown
# DATI CLIENTE
```
AZIENDA: Pizzeria Mario
SETTORE: Ristorazione
SLOGAN: La vera pizza napoletana
WEBSITE_TEMA: dark
COLORE_PRIMARIO: #ff6b6b
```

# HERO
```
TITOLO: La Vera Pizza Napoletana in Città
SOTTOTITOLO: Dall'impasto alla tavola, ogni pizza è un'arte.
BOTTONE_TESTO: Prenota Un Tavolo
BOTTONE_LINK: #contatti
```
...
```

---

## 🎯 Output

Ogni esecuzione genera:
- **1 file HTML** autonomo (self-contained, nessuna dipendenza)
- **Responsive design** (mobile, tablet, desktop)
- **Dark theme** con accenti in neon
- **Badge rosso** con timer 24 ore
- **Footer LAIP** (branding)

---

## 🔐 Privacy & Sicurezza

- ✅ Zero tracking (niente analytics)
- ✅ Zero cookies
- ✅ Niente backend (file statico HTML)
- ✅ Sicuro da inviare via email

---

## 📞 Support

Per problemi con lo script, controlla:
1. Python versione 3.6+ installato
2. Template markdown compilato correttamente
3. Nessuno spazio vuoto nei dati critici

---

**LAIP © 2026 - AI-Powered Websites**
