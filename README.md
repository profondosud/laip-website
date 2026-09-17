# LAIP - Professional Websites with AI

Professional website for LAIP, founded by two professional motorcycle racers bringing motorsport DNA to web development.

## 🚀 Features

- **Professional Dark Theme** - Pure black background with neon cyan accents
- **Animated Intro** - Logo with lightbulb glow effect (dim to bright)
- **Hero Section** - Founders photo with animated logo passing underneath
- **Matrix Background** - Binary code falling animation
- **Responsive Design** - Mobile-first approach
- **Racing + AI DNA** - Velocity, precision, innovation

## 🎨 Design Elements

- Color scheme: Dark (#040812) with neon cyan (#00d4ff, #00f0ff)
- Logo: LAIP with circuit patterns and racing stripe
- Typography: Modern system fonts
- Animations: Smooth transitions and effects

## 📝 How to Edit

### Local Setup
```bash
git clone https://github.com/profondosud/laip-website.git
cd laip-website
```

### Opening the Site
Simply open `index.html` in your browser:
- Double-click `index.html` to view locally
- Or use Live Server extension in VS Code

### Making Changes

**Images:**
- Trailer intro image: `index.html` line ~507 (trailerImage)
- Founders photo: `index.html` line ~646 (heroImage)  
- Logo: Multiple locations (navbar, trailer, overlay)

**Text:**
- Hero section: Around line 635
- Feature cards: Around line 750
- Footer content: Around line 800

**Colors:**
Edit CSS variables at the top of `<style>` section:
```css
:root {
    --primary: #00d4ff;
    --primary-bright: #00f0ff;
    --dark: #040812;
    --darker: #010204;
    --white: #ffffff;
}
```

### Updating Images

To replace images, convert them to base64:
1. Open image in any online base64 converter
2. Copy the base64 string
3. Replace in HTML: `data:image/jpeg;base64,<BASE64_STRING>`

## 🔄 Sync automatico in VS Code

Aprendo la cartella in VS Code parte da solo il task **"Sync automatico con GitHub"**
(`.vscode/tasks.json`). Ogni 20 secondi scarica le modifiche caricate dall'altro socio:
i file si aggiornano nell'editor senza fare nulla.

- La prima volta VS Code chiede il permesso per le attività automatiche: rispondi **Consenti**.
- Non tocca mai i file che stai modificando: se arrivano cambi proprio su quelli, lo scrive nel terminale e aspetta il tuo commit.
- Con l'estensione **Live Server** (consigliata da VS Code) il browser si ricarica da solo a ogni aggiornamento.
- Per fermarlo: chiudi il terminale "Sync automatico con GitHub".

## 📤 Pushing Changes

After editing:
```bash
git add .
git commit -m "Update: description of changes"
git push origin main
```

## 👥 Collaboration

- Pull latest changes: `git pull origin main`
- Create feature branches: `git checkout -b feature/your-feature`
- Make a Pull Request for review before merging

## 📱 Responsive Breakpoints

- Desktop: Full width
- Tablet: Grid adjusts
- Mobile: Single column layout

## 🔧 Tech Stack

- Pure HTML5
- CSS3 (Flexbox, Grid, Animations)
- Vanilla JavaScript
- Base64 embedded images (no external dependencies)

## 📄 Files

- `index.html` - Main website file
- `.claude/` - Additional resources and images
- `README.md` - This file

## 🎯 Quick Start for Collaborators

1. Clone: `git clone https://github.com/profondosud/laip-website.git`
2. Open: Double-click `index.html`
3. Edit: Make changes to HTML/CSS
4. Test: Refresh browser to see changes
5. Push: `git add . && git commit -m "Your message" && git push`

---

Built with racing precision and AI innovation 🏁⚡
