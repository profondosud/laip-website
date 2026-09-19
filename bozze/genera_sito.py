#!/usr/bin/env python3
"""
Generatore di siti web bozza da template Markdown
Legge TEMPLATE_CLIENTE.md e genera HTML completo pronto per il cliente
"""

import os
import sys
import re
from datetime import datetime, timedelta

def leggi_template(file_md):
    """Legge il file markdown e estrae i dati"""
    dati = {}
    with open(file_md, 'r', encoding='utf-8') as f:
        contenuto = f.read()

    # Estrae i dati tra i blocchi ```
    blocchi = re.findall(r'```\n(.*?)\n```', contenuto, re.DOTALL)

    for blocco in blocchi:
        linee = blocco.strip().split('\n')
        for linea in linee:
            if ':' in linea:
                chiave, valore = linea.split(':', 1)
                chiave = chiave.strip()
                valore = valore.strip()
                # Gestisci liste (features)
                if chiave.endswith('_FEATURES'):
                    if chiave not in dati:
                        dati[chiave] = []
                    if valore.startswith('- '):
                        dati[chiave].append(valore[2:])
                else:
                    dati[chiave] = valore

    return dati

def genera_html(dati):
    """Genera il file HTML dal dizionario dati"""

    # Calcola scadenza 24 ore
    ora_scadenza = (datetime.now() + timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S')

    # Estrae i colori e il tema
    colore_primario = dati.get('COLORE_PRIMARIO', '#00d4ff')
    tema = dati.get('WEBSITE_TEMA', 'dark')

    # Se tema è light, usa colori invertiti, altrimenti dark come LAIP
    if tema == 'light':
        bg_color = '#ffffff'
        text_color = '#1a1a1a'
        card_bg = '#f5f5f5'
        card_border = '#e0e0e0'
    else:
        bg_color = '#040812'
        text_color = '#e5e7eb'
        card_bg = '#0a0e1a'
        card_border = 'rgba(0, 212, 255, 0.2)'

    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dati.get('SEO_TITLE', dati.get('AZIENDA', 'Sito Web'))}</title>
    <meta name="description" content="{dati.get('SEO_DESCRIPTION', 'Scopri i nostri servizi')}">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary: {colore_primario};
            --dark: {bg_color};
            --text: {text_color};
            --card-bg: {card_bg};
            --card-border: {card_border};
        }}

        html {{ scroll-behavior: smooth; }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--dark);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            letter-spacing: -0.02em;
        }}

        nav {{
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(4, 8, 18, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 2rem;
            z-index: 100;
            border-bottom: 1px solid rgba(0, 212, 255, 0.1);
        }}

        nav a {{
            color: var(--text);
            text-decoration: none;
            margin-right: 2rem;
            transition: color 0.3s;
        }}

        nav a:hover {{
            color: var(--primary);
        }}

        main {{
            padding-top: 60px;
            position: relative;
            z-index: 1;
        }}

        section {{
            padding: 4rem 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }}

        .hero {{
            text-align: center;
            padding: 6rem 2rem !important;
            min-height: 60vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}

        .hero h1 {{
            font-size: clamp(2rem, 5vw, 4rem);
            margin-bottom: 1rem;
            color: var(--primary);
        }}

        .hero p {{
            font-size: 1.2rem;
            max-width: 600px;
            margin-bottom: 2rem;
            opacity: 0.9;
        }}

        .btn {{
            display: inline-block;
            background: var(--primary);
            color: var(--dark);
            padding: 0.8rem 2rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            font-size: 1rem;
        }}

        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0, 212, 255, 0.4);
        }}

        section h2 {{
            font-size: clamp(1.8rem, 4vw, 2.5rem);
            margin-bottom: 3rem;
            text-align: center;
            color: var(--primary);
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }}

        .card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 2rem;
            border-radius: 8px;
            transition: all 0.3s;
            text-align: center;
        }}

        .card:hover {{
            transform: translateY(-5px);
            border-color: var(--primary);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.1);
        }}

        .card i {{
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }}

        .card h3 {{
            margin-bottom: 0.5rem;
        }}

        .price-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }}

        .price-card {{
            background: var(--card-bg);
            border: 2px solid var(--card-border);
            padding: 2rem;
            border-radius: 8px;
            text-align: center;
            position: relative;
        }}

        .price-card h3 {{
            margin-bottom: 1rem;
        }}

        .price-card .price {{
            font-size: 2.5rem;
            color: var(--primary);
            margin: 1rem 0;
            font-weight: 800;
        }}

        .price-card ul {{
            list-style: none;
            text-align: left;
            margin: 1.5rem 0;
        }}

        .price-card li {{
            padding: 0.5rem 0;
            border-bottom: 1px solid var(--card-border);
        }}

        .price-card li:before {{
            content: "✓ ";
            color: var(--primary);
            font-weight: bold;
            margin-right: 0.5rem;
        }}

        .timeline {{
            position: relative;
            padding: 2rem 0;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: var(--primary);
            transform: translateX(-50%);
        }}

        .timeline-item {{
            margin-bottom: 3rem;
            position: relative;
        }}

        .timeline-item:nth-child(odd) {{
            text-align: right;
            padding-right: 52%;
        }}

        .timeline-item:nth-child(even) {{
            text-align: left;
            padding-left: 52%;
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            background: var(--dark);
            border: 3px solid var(--primary);
            border-radius: 50%;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
        }}

        .timeline-content {{
            background: var(--card-bg);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 3px solid var(--primary);
        }}

        .faq-item {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            margin-bottom: 1rem;
            border-radius: 8px;
            overflow: hidden;
        }}

        .faq-item input {{
            display: none;
        }}

        .faq-item label {{
            display: block;
            padding: 1.5rem;
            cursor: pointer;
            font-weight: 600;
            color: var(--text);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .faq-item label:hover {{
            background: rgba(0, 212, 255, 0.05);
        }}

        .faq-item label::after {{
            content: "+";
            font-weight: bold;
            color: var(--primary);
        }}

        .faq-item input:checked + label::after {{
            content: "−";
        }}

        .faq-item input:checked ~ .faq-content {{
            max-height: 500px;
            padding: 1rem 1.5rem;
        }}

        .faq-content {{
            max-height: 0;
            overflow: hidden;
            transition: all 0.3s;
        }}

        .contact-form {{
            max-width: 600px;
            margin: 2rem auto;
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 8px;
            border: 1px solid var(--card-border);
        }}

        .form-group {{
            margin-bottom: 1.5rem;
        }}

        .form-group label {{
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }}

        .form-group input,
        .form-group textarea {{
            width: 100%;
            padding: 0.8rem;
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid var(--card-border);
            border-radius: 4px;
            color: var(--text);
            font-family: inherit;
        }}

        .form-group textarea {{
            resize: vertical;
            min-height: 120px;
        }}

        footer {{
            background: rgba(0, 0, 0, 0.3);
            padding: 2rem;
            text-align: center;
            border-top: 1px solid var(--card-border);
            margin-top: 4rem;
        }}

        .demo-badge {{
            position: fixed;
            top: 80px;
            right: 20px;
            background: rgba(255, 0, 0, 0.9);
            color: white;
            padding: 0.8rem 1.5rem;
            border-radius: 4px;
            font-weight: 600;
            z-index: 99;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.7; }}
        }}

        @media (max-width: 768px) {{
            nav {{
                flex-wrap: wrap;
            }}

            .timeline::before {{
                left: 0;
            }}

            .timeline-item {{
                padding-left: 30px !important;
                padding-right: 0 !important;
                text-align: left !important;
            }}

            .timeline-item::before {{
                left: 0;
            }}

            .timeline-content {{
                border-left: 3px solid var(--primary);
            }}

            .grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="demo-badge">🔴 DEMO - Scade: {ora_scadenza}</div>

    <nav>
        <a href="#hero">{dati.get('AZIENDA', 'Home')}</a>
        <a href="#about">Chi Siamo</a>
        <a href="#servizi">Servizi</a>
        <a href="#prezzi">Prezzi</a>
        <a href="#come">Come Funziona</a>
        <a href="#faq">FAQ</a>
        <a href="#contatti">Contatti</a>
    </nav>

    <main>
        <!-- HERO -->
        <section id="hero" class="hero">
            <h1>{dati.get('TITOLO', 'Benvenuto')}</h1>
            <p>{dati.get('SOTTOTITOLO', 'Scopri i nostri servizi')}</p>
            <a href="{dati.get('BOTTONE_LINK', '#servizi')}" class="btn">{dati.get('BOTTONE_TESTO', 'Scopri di Più')}</a>
        </section>

        <!-- ABOUT -->
        <section id="about">
            <h2>Chi Siamo</h2>
            <p style="max-width: 800px; margin: 0 auto; text-align: center; font-size: 1.1rem; line-height: 1.8;">
                {dati.get('PARAGRAFO_1', '')}
            </p>
        </section>

        <!-- SERVIZI -->
        <section id="servizi">
            <h2>I Nostri Servizi</h2>
            <div class="grid">
"""

    # Aggiungi i servizi
    for i in range(1, 7):
        icon = dati.get(f'SERVIZIO_{i}_ICONA', 'fas fa-star')
        titolo = dati.get(f'SERVIZIO_{i}_TITOLO', f'Servizio {i}')
        testo = dati.get(f'SERVIZIO_{i}_TESTO', 'Descrizione')
        html += f"""                <div class="card">
                    <i class="{icon}"></i>
                    <h3>{titolo}</h3>
                    <p>{testo}</p>
                </div>
"""

    html += """            </div>
        </section>

        <!-- PREZZI -->
        <section id="prezzi">
            <h2>I Nostri Prezzi</h2>
            <div class="price-grid">
"""

    # Aggiungi i piani prezzi
    for i in range(1, 4):
        nome = dati.get(f'PIANO_{i}_NOME', f'Piano {i}')
        prezzo = dati.get(f'PIANO_{i}_PREZZO', '€ 0')
        desc = dati.get(f'PIANO_{i}_DESCRIZIONE', '')
        features = dati.get(f'PIANO_{i}_FEATURES', [])

        html += f"""                <div class="price-card">
                    <h3>{nome}</h3>
                    <p>{desc}</p>
                    <div class="price">{prezzo}</div>
                    <ul>
"""
        for feature in features[:6]:
            html += f"                        <li>{feature}</li>\n"

        html += """                    </ul>
                    <a href="#contatti" class="btn">Scegli Questo Piano</a>
                </div>
"""

    html += """            </div>
        </section>

        <!-- TIMELINE -->
        <section id="come">
            <h2>Come Funziona</h2>
            <div class="timeline">
"""

    for i in range(1, 5):
        step_titolo = dati.get(f'STEP_{i}_TITOLO', f'Step {i}')
        step_testo = dati.get(f'STEP_{i}_TESTO', 'Descrizione')

        html += f"""                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Step {i}: {step_titolo}</h3>
                        <p>{step_testo}</p>
                    </div>
                </div>
"""

    html += """            </div>
        </section>

        <!-- FAQ -->
        <section id="faq">
            <h2>Domande Frequenti</h2>
"""

    for i in range(1, 6):
        domanda = dati.get(f'DOMANDA_{i}', f'Domanda {i}?')
        risposta = dati.get(f'RISPOSTA_{i}', 'Risposta')

        html += f"""            <div class="faq-item">
                <input type="checkbox" id="faq{i}">
                <label for="faq{i}">{domanda}</label>
                <div class="faq-content">
                    <p>{risposta}</p>
                </div>
            </div>
"""

    html += f"""        </section>

        <!-- CONTATTI -->
        <section id="contatti">
            <h2>Contatti</h2>
            <div class="contact-form">
                <div class="form-group">
                    <label>Nome</label>
                    <input type="text" placeholder="Il tuo nome">
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" placeholder="La tua email">
                </div>
                <div class="form-group">
                    <label>Telefono</label>
                    <input type="tel" placeholder="Il tuo telefono">
                </div>
                <div class="form-group">
                    <label>Messaggio</label>
                    <textarea placeholder="Il tuo messaggio"></textarea>
                </div>
                <button class="btn" style="width: 100%;">Invia Messaggio</button>
            </div>
            <div style="text-align: center; margin-top: 3rem; opacity: 0.8;">
                <p><strong>Email:</strong> {dati.get('EMAIL', 'info@azienda.it')}</p>
                <p><strong>Telefono:</strong> {dati.get('TELEFONO', '+39 XXX XXX XXX')}</p>
                <p><strong>Città:</strong> {dati.get('CITTÀ', 'Italia')}</p>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 {dati.get('AZIENDA', 'Azienda')}. Sito web creato con <strong>LAIP</strong> - AI-Powered Websites</p>
        <p style="font-size: 0.9rem; margin-top: 1rem; opacity: 0.7;">
            Questo è un sito di presentazione in fase demo. Valido per 24 ore.
        </p>
    </footer>
</body>
</html>
"""

    return html

def main():
    if len(sys.argv) < 2:
        print("❌ Uso: python genera_sito.py <file_markdown>")
        print("📝 Esempio: python genera_sito.py pizzeria_mario.md")
        sys.exit(1)

    file_md = sys.argv[1]

    if not os.path.exists(file_md):
        print(f"❌ File non trovato: {file_md}")
        sys.exit(1)

    print(f"📖 Leggo il template: {file_md}")
    dati = leggi_template(file_md)

    print("🏗️  Genero l'HTML...")
    html = genera_html(dati)

    # Crea il nome del file di output
    nome_azienda = dati.get('AZIENDA', 'sito').lower().replace(' ', '_')
    data_ora = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_output = f"{nome_azienda}_{data_ora}.html"

    with open(nome_output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Sito generato: {nome_output}")
    print(f"📊 Dimensione: {len(html) / 1024:.1f} KB")
    print(f"⏱️  Valido per 24 ore")

if __name__ == '__main__':
    main()
