# Claude Code Project Config

## Project Context
- **Projects**: LAIP (AI website seller), SWITCH UP (Motorsport AI website seller)
- **Deployment**: GitHub Pages (automatic), Vercel Cloud
- **Tech**: HTML/CSS/JavaScript, no frameworks
- **Focus**: Graphic design workflow through ChatGPT + DALL-E

---

## Agents Overview

| Agent | Status | Trigger | Workflow |
|-------|--------|---------|----------|
| **Graphic Agent** 🎨 | ✅ ACTIVE | Richieste grafiche | GRAPHIC_AGENT_PLANNING.md |
| **Text Review Agent** 📝 | ✅ ACTIVE | Revisioni/generazioni testo | TEXT_REVIEW_AGENT_PLANNING.md |

---

## Authorization
**Auto-execute all changes** - No permission prompts needed for:
- CSS modifications
- Logo/image updates
- Animation changes
- Layout adjustments
- Color/styling updates
- Text generation & revisions

Never ask "Do you authorize this change?" — Just implement it.

---

## Graphic Agent
**STATUS**: ✅ **ACTIVE**

### Activation
- Triggered by: Any graphic design request
- Workflow: Automatic (see GRAPHIC_AGENT_PLANNING.md)
- ChatGPT: Always referenced for ideas/code
- Auto-implementation: Yes, no prompts

### Deactivation
Change STATUS above to: `❌ DISABLED`
Then ask for changes directly without workflow.

### Typical Requests
- Logo sizing/positioning
- Color/accent updates
- New animations/transitions
- Layout reorganization
- Copy improvements
- Background effects

---

## Text Review Agent
**STATUS**: ✅ **ACTIVE**

### Activation
- Triggered by: Any text/copy revision request
- Workflow: Automatic (see TEXT_REVIEW_AGENT_PLANNING.md)
- Markdownlint: Formal checks on all text
- ChatGPT: Copy enhancement & persuasivity
- Auto-implementation: Yes, no prompts

### Deactivation
Change STATUS above to: `❌ DISABLED`
Then ask for changes directly without workflow.

### Typical Requests
- Copy/headline improvement
- Tone/voice consistency
- Persuasivity enhancement
- Grammar/clarity review
- Readability optimization
- A/B text variants

---

## Design System Reference
- **LAIP Colors**: Azzurro (#0099FF) + Dark (#0a0a0a)
- **SWITCH UP Colors**: Verde (#B8FF00) + Dark (#070908)
- **Fonts**: Barlow Condensed (headings), Inter (body), Lora (hero)
- **Breakpoints**: 600px, 768px, 1024px, 1200px
- **Performance**: 60fps, CSS3 only, no lag

---

## File Structure
```
C:\Users\marco\Documents\set up\
├── index.html                      # LAIP main
├── partners.html                   # LAIP partners
├── switchup.html                   # SWITCH UP
├── CLAUDE.md                       # This file (config)
├── GRAPHIC_AGENT_PLANNING.md       # Graphic Agent workflow
├── TEXT_REVIEW_AGENT_PLANNING.md   # Text Review Agent workflow
├── images/                         # Logos, screenshots
├── graphic-assets/                 # Generated graphic assets
└── text-assets/                    # Generated text assets
```

---

## Notes
- GitHub Pages deployment is automatic on push to main
- Always test responsive design (mobile/tablet/desktop)
- Version assets in graphic-assets/ with timestamps
- No backwards compatibility needed — just change the code
