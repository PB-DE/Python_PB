import json

with open('decks_data.json', 'r', encoding='utf-8') as f:
    decks = json.load(f)

json_data_str = json.dumps(decks, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Programming — CATC Course Portal</title>
  <meta name="description" content="Civil Aviation Training Center (CATC) Python Programming presentation decks and curriculum portal. 5 widescreen decks, 10 comprehensive lectures, 179 interactive slides.">
  
  <!-- Modern Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #0b0d13;
      --bg-surface: #12151f;
      --bg-card: #181d2a;
      --bg-card-hover: #202738;
      --border: #242c3d;
      --border-light: rgba(255, 255, 255, 0.08);
      --border-focus: #38bdf8;
      --text: #cbd5e1;
      --text-bright: #ffffff;
      --text-muted: #818cf8;
      --text-dim: #94a3b8;
      
      /* Theme accents */
      --cyan: #38bdf8;
      --blue: #2563eb;
      --gold: #facc15;
      --mint: #34d399;
      --purple: #c084fc;
      --coral: #fb7185;
      --code-bg: #0f131c;
      
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-xl: 24px;
      --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -2px rgba(0, 0, 0, 0.3);
      --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      background-color: var(--bg);
      color: var(--text);
      font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow-x: hidden;
    }}

    /* Background Ambient Glowing Lights */
    .ambient-glow {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }}
    .glow-1 {{
      position: absolute;
      top: -150px;
      left: 15%;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, rgba(56, 189, 248, 0.12) 0%, rgba(37, 99, 235, 0.05) 50%, transparent 70%);
      filter: blur(60px);
    }}
    .glow-2 {{
      position: absolute;
      top: 40%;
      right: -100px;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(192, 132, 252, 0.1) 0%, rgba(251, 113, 133, 0.04) 50%, transparent 70%);
      filter: blur(70px);
    }}
    .glow-3 {{
      position: absolute;
      bottom: -100px;
      left: 30%;
      width: 700px;
      height: 500px;
      background: radial-gradient(circle, rgba(52, 211, 153, 0.08) 0%, transparent 70%);
      filter: blur(80px);
    }}

    /* Header Nav */
    header.portal-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 13, 19, 0.88);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-bottom: 1px solid var(--border-light);
    }}

    .nav-container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0.85rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      text-decoration: none;
    }}

    .brand-logo {{
      width: 40px;
      height: 40px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, #007acc 0%, #38bdf8 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba(56, 189, 248, 0.35);
      color: #fff;
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .brand-title {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 1.15rem;
      color: var(--text-bright);
      letter-spacing: -0.01em;
      line-height: 1.2;
    }}

    .brand-subtitle {{
      font-size: 0.72rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 600;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .nav-link {{
      color: var(--text);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      transition: all 0.2s ease;
    }}

    .nav-link:hover {{
      color: var(--text-bright);
      background: var(--bg-card);
    }}

    .search-btn-trigger {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-dim);
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }}

    .search-btn-trigger:hover {{
      border-color: var(--cyan);
      color: var(--text-bright);
    }}

    .kbd-shortcut {{
      background: var(--border);
      color: var(--text);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
    }}

    /* Main Container */
    main {{
      position: relative;
      z-index: 1;
      max-width: 1280px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 4rem;
      width: 100%;
    }}

    /* Hero Section */
    .hero {{
      text-align: center;
      padding: 2rem 0 3.5rem;
      max-width: 920px;
      margin: 0 auto;
    }}

    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      color: var(--cyan);
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      margin-bottom: 1.25rem;
      text-transform: uppercase;
    }}

    .hero-badge .pulse-dot {{
      width: 7px;
      height: 7px;
      background-color: var(--cyan);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--cyan);
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0% {{ opacity: 0.4; transform: scale(0.9); }}
      50% {{ opacity: 1; transform: scale(1.2); }}
      100% {{ opacity: 0.4; transform: scale(0.9); }}
    }}

    .hero-title {{
      font-family: 'Outfit', sans-serif;
      font-size: clamp(2.2rem, 5vw, 3.4rem);
      font-weight: 800;
      line-height: 1.15;
      color: var(--text-bright);
      margin-bottom: 1rem;
      letter-spacing: -0.025em;
    }}

    .gradient-text {{
      background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-desc {{
      font-size: 1.125rem;
      color: var(--text);
      max-width: 780px;
      margin: 0 auto 2.25rem;
      line-height: 1.65;
    }}

    /* Stat Cards Bar */
    .stats-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}

    .stat-item {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1rem;
      text-align: center;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .stat-item:hover {{
      transform: translateY(-3px);
      border-color: rgba(255, 255, 255, 0.15);
    }}

    .stat-num {{
      font-family: 'Outfit', sans-serif;
      font-size: 2rem;
      font-weight: 800;
      color: var(--text-bright);
      line-height: 1.1;
      margin-bottom: 0.25rem;
    }}

    .stat-label {{
      font-size: 0.8rem;
      color: var(--text-dim);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    /* Global Search & Filter Bar */
    .filter-section {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 1.25rem 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
    }}

    .search-input-wrap {{
      position: relative;
      margin-bottom: 1rem;
    }}

    .search-icon {{
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      pointer-events: none;
      width: 20px;
      height: 20px;
    }}

    .search-input {{
      width: 100%;
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.85rem 2.85rem 0.85rem 2.85rem;
      color: var(--text-bright);
      font-size: 0.95rem;
      outline: none;
      transition: all 0.2s ease;
      font-family: inherit;
    }}

    .search-input:focus {{
      border-color: var(--cyan);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
    }}

    .search-clear-btn {{
      position: absolute;
      right: 0.85rem;
      top: 50%;
      transform: translateY(-50%);
      background: transparent;
      border: none;
      color: var(--text-dim);
      cursor: pointer;
      display: none;
      font-size: 1.1rem;
      padding: 0.25rem;
    }}

    .search-clear-btn:hover {{
      color: var(--text-bright);
    }}

    .filter-pills {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.5rem;
    }}

    .filter-label {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-right: 0.35rem;
    }}

    .pill {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }}

    .pill:hover {{
      color: var(--text-bright);
      background: var(--bg-card-hover);
      border-color: rgba(255, 255, 255, 0.15);
    }}

    .pill.active {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--cyan);
      color: var(--cyan);
      font-weight: 600;
    }}

    /* Search Results Live Panel */
    #search-results-panel {{
      display: none;
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border);
      max-height: 400px;
      overflow-y: auto;
    }}

    .search-result-count {{
      font-size: 0.85rem;
      color: var(--text-dim);
      margin-bottom: 0.75rem;
    }}

    .search-results-list {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}

    .search-result-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding: 0.65rem 0.9rem;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      text-decoration: none;
      color: var(--text);
      transition: all 0.15s ease;
    }}

    .search-result-item:hover {{
      background: var(--bg-card-hover);
      border-color: var(--cyan);
      transform: translateX(4px);
      color: var(--text-bright);
    }}

    .res-left {{
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
    }}

    .res-eyebrow {{
      font-size: 0.72rem;
      color: var(--cyan);
      font-weight: 600;
    }}

    .res-title {{
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-bright);
    }}

    .res-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      background: var(--code-bg);
      border: 1px solid var(--border);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      color: var(--text-muted);
      white-space: nowrap;
    }}

    /* Deck Cards Section */
    .section-title-wrap {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.5rem;
    }}

    .section-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-bright);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .decks-container {{
      display: flex;
      flex-direction: column;
      gap: 2rem;
      margin-bottom: 3.5rem;
    }}

    /* Individual Deck Card */
    .deck-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      overflow: hidden;
      position: relative;
      box-shadow: var(--shadow-sm);
      transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }}

    .deck-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: rgba(255, 255, 255, 0.18);
    }}

    /* Card Top Color Accent Bar */
    .deck-top-bar {{
      height: 4px;
      width: 100%;
    }}

    .deck-content {{
      padding: 1.75rem 2rem;
    }}

    .deck-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }}

    .deck-header-info {{
      flex: 1;
      min-width: 280px;
    }}

    .deck-badges {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.65rem;
      flex-wrap: wrap;
    }}

    .badge-deck-no {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 0.75rem;
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}

    .badge-lectures {{
      font-size: 0.78rem;
      font-weight: 600;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-bright);
    }}

    .badge-slides-count {{
      font-size: 0.78rem;
      font-weight: 500;
      color: var(--text-dim);
    }}

    .deck-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--text-bright);
      line-height: 1.25;
      margin-bottom: 0.4rem;
    }}

    .deck-subtitle {{
      font-size: 0.95rem;
      color: var(--text);
      line-height: 1.5;
    }}

    /* Dual Lecture Split Modules */
    .deck-lectures-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
      margin: 1.5rem 0;
    }}

    .lecture-box {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: border-color 0.2s ease;
    }}

    .lecture-box:hover {{
      border-color: rgba(255, 255, 255, 0.15);
    }}

    .lec-eyebrow {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.35rem;
    }}

    .lec-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--text-bright);
      margin-bottom: 0.75rem;
      line-height: 1.3;
    }}

    .lec-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
    }}

    .lec-jump-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--code-bg);
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: var(--radius-sm);
      text-decoration: none;
      transition: all 0.2s ease;
    }}

    .lec-jump-btn:hover {{
      background: var(--bg-surface);
      color: var(--text-bright);
      border-color: var(--cyan);
    }}

    /* Topic Tags & Notebooks */
    .deck-footer-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border);
      flex-wrap: wrap;
    }}

    .deck-tags-list {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      flex: 1;
      min-width: 250px;
    }}

    .topic-tag {{
      font-size: 0.75rem;
      background: var(--code-bg);
      border: 1px solid var(--border);
      color: var(--text-dim);
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      transition: color 0.15s ease;
    }}

    .topic-tag:hover {{
      color: var(--text-bright);
      border-color: rgba(255, 255, 255, 0.15);
    }}

    .deck-actions-group {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #0284c7 0%, #007acc 100%);
      color: #ffffff;
      font-weight: 600;
      font-size: 0.9rem;
      padding: 0.6rem 1.25rem;
      border-radius: var(--radius-md);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35);
      transition: all 0.2s ease;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }}

    .btn-primary:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(2, 132, 199, 0.5);
      filter: brightness(1.1);
    }}

    .btn-secondary {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-bright);
      font-weight: 600;
      font-size: 0.85rem;
      padding: 0.6rem 1rem;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }}

    .btn-secondary:hover {{
      background: var(--bg-card-hover);
      border-color: rgba(255, 255, 255, 0.2);
    }}

    /* Slide Outline Accordion Drawer */
    .deck-outline-drawer {{
      display: none;
      background: var(--code-bg);
      border-top: 1px solid var(--border);
      padding: 1.5rem 2rem;
    }}

    .deck-outline-drawer.open {{
      display: block;
      animation: fadeIn 0.25s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(-6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .outline-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }}

    .outline-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-bright);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .outline-slides-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 0.65rem;
    }}

    .outline-slide-link {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.55rem 0.8rem;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      text-decoration: none;
      color: var(--text);
      font-size: 0.82rem;
      transition: all 0.15s ease;
    }}

    .outline-slide-link:hover {{
      background: var(--bg-card-hover);
      border-color: var(--cyan);
      color: var(--text-bright);
      transform: translateX(3px);
    }}

    .slide-num-pill {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      color: var(--cyan);
      min-width: 32px;
      text-align: center;
    }}

    /* Syllabus Curriculum Matrix Table */
    .syllabus-section {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 2rem;
      margin-bottom: 3.5rem;
      box-shadow: var(--shadow-sm);
    }}

    .table-container {{
      overflow-x: auto;
      margin-top: 1.25rem;
    }}

    .syllabus-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }}

    .syllabus-table th {{
      background: var(--bg-card);
      color: var(--text-bright);
      font-weight: 600;
      padding: 0.9rem 1rem;
      border-bottom: 2px solid var(--border);
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .syllabus-table td {{
      padding: 0.9rem 1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }}

    .syllabus-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}

    .lecture-badge-pill {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 0.75rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      white-space: nowrap;
    }}

    /* Keyboard Shortcuts Guide Card */
    .shortcuts-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }}

    .shortcut-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .key-cap {{
      background: var(--code-bg);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-bottom: 3px solid rgba(255, 255, 255, 0.3);
      border-radius: 6px;
      color: var(--text-bright);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.75rem;
      display: inline-block;
      text-align: center;
      min-width: 45px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
    }}

    .key-info {{
      display: flex;
      flex-direction: column;
    }}

    .key-action {{
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--text-bright);
    }}

    .key-desc {{
      font-size: 0.75rem;
      color: var(--text-dim);
    }}

    /* Footer */
    footer.portal-footer {{
      margin-top: auto;
      background: var(--bg-surface);
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      color: var(--text-dim);
      font-size: 0.875rem;
    }}

    .footer-content {{
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
    }}

    .footer-left {{
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }}

    .footer-links {{
      display: flex;
      gap: 1rem;
    }}

    .footer-link {{
      color: var(--text-dim);
      text-decoration: none;
      transition: color 0.15s ease;
    }}

    .footer-link:hover {{
      color: var(--cyan);
    }}

    /* Notebook Pill */
    .nb-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.2rem 0.5rem;
      background: rgba(250, 204, 21, 0.1);
      border: 1px solid rgba(250, 204, 21, 0.25);
      border-radius: 4px;
      color: var(--gold);
      font-size: 0.75rem;
      font-family: 'JetBrains Mono', monospace;
      text-decoration: none;
      transition: all 0.2s ease;
    }}

    .nb-pill:hover {{
      background: rgba(250, 204, 21, 0.2);
      border-color: var(--gold);
      color: #fff;
    }}

    /* Responsive adjustments */
    @media (max-width: 768px) {{
      .deck-lectures-grid {{
        grid-template-columns: 1fr;
      }}
      .deck-content {{
        padding: 1.25rem 1.25rem;
      }}
      .stats-bar {{
        grid-template-columns: 1fr 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Ambient Light Orbs -->
  <div class="ambient-glow">
    <div class="glow-1"></div>
    <div class="glow-2"></div>
    <div class="glow-3"></div>
  </div>

  <!-- Top Sticky Header -->
  <header class="portal-nav">
    <div class="nav-container">
      <a href="#top" class="brand">
        <div class="brand-logo">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="4 17 10 11 4 5"></polyline>
            <line x1="12" y1="19" x2="20" y2="19"></line>
          </svg>
        </div>
        <div class="brand-text">
          <span class="brand-title">Python Course Portal</span>
          <span class="brand-subtitle">Civil Aviation Training Center (CATC)</span>
        </div>
      </a>

      <div class="nav-links">
        <a href="#decks" class="nav-link">Slide Decks</a>
        <a href="#syllabus" class="nav-link">Curriculum</a>
        <a href="#shortcuts" class="nav-link">Shortcuts</a>
        <button class="search-btn-trigger" id="search-trigger-btn" aria-label="Search curriculum">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <span>Search</span>
          <span class="kbd-shortcut">⌘K</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main id="top">
    
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-badge">
        <span class="pulse-dot"></span>
        CATC Department of Aviation Engineering
      </div>
      <h1 class="hero-title">
        Modern Python Programming<br>
        <span class="gradient-text">Interactive Curriculum Decks</span>
      </h1>
      <p class="hero-desc">
        A comprehensive, 10-lecture university course curriculum in computer science and scientific Python, packaged into five 16:9 widescreen interactive presentation decks with direct code demonstrations.
      </p>

      <!-- Stat Counters -->
      <div class="stats-bar">
        <div class="stat-item">
          <div class="stat-num" style="color: var(--cyan);">5</div>
          <div class="stat-label">Slide Decks</div>
        </div>
        <div class="stat-item">
          <div class="stat-num" style="color: var(--mint);">10</div>
          <div class="stat-label">Lectures (+ Lab 11)</div>
        </div>
        <div class="stat-item">
          <div class="stat-num" style="color: var(--gold);">179</div>
          <div class="stat-label">Interactive Slides</div>
        </div>
        <div class="stat-item">
          <div class="stat-num" style="color: var(--coral);">100%</div>
          <div class="stat-label">Offline Capable</div>
        </div>
      </div>
    </section>

    <!-- Global Instant Search & Filter Section -->
    <section class="filter-section" id="search-section">
      <div class="search-input-wrap">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input 
          type="text" 
          id="global-search" 
          class="search-input" 
          placeholder="Search 179 slides (e.g. slicing, regex, json, broadcasting, oop, pep 8, binary)..."
          autocomplete="off"
        >
        <button class="search-clear-btn" id="search-clear" title="Clear search">✕</button>
      </div>

      <div class="filter-pills">
        <span class="filter-label">Filter:</span>
        <button class="pill active" data-filter="all">All Decks (5)</button>
        <button class="pill" data-filter="deck-1">Deck 1: Foundations</button>
        <button class="pill" data-filter="deck-2">Deck 2: Logic &amp; Functions</button>
        <button class="pill" data-filter="deck-3">Deck 3: Collections &amp; Sets</button>
        <button class="pill" data-filter="deck-4">Deck 4: NumPy &amp; Regex</button>
        <button class="pill" data-filter="deck-5">Deck 5: Files &amp; OOP</button>
      </div>

      <!-- Live Search Results Dropdown/Panel -->
      <div id="search-results-panel">
        <div class="search-result-count" id="result-count">0 matching slides found</div>
        <div class="search-results-list" id="results-list"></div>
      </div>
    </section>

    <!-- Presentation Decks List -->
    <section id="decks">
      <div class="section-title-wrap">
        <h2 class="section-title">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--cyan)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
            <line x1="8" y1="21" x2="16" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
          </svg>
          Interactive Lecture Slide Decks
        </h2>
      </div>

      <div class="decks-container" id="decks-container">
        <!-- Deck Cards will be rendered dynamically -->
      </div>
    </section>

    <!-- Syllabus Table Section -->
    <section class="syllabus-section" id="syllabus">
      <div class="section-title-wrap">
        <h2 class="section-title">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
          </svg>
          Complete Course Syllabus &amp; Lecture Roadmap
        </h2>
      </div>
      <p style="color: var(--text-dim); font-size: 0.95rem;">
        Ten structured curriculum lectures covering computing principles to production-grade object-oriented system engineering.
      </p>

      <div class="table-container">
        <table class="syllabus-table">
          <thead>
            <tr>
              <th>Lecture</th>
              <th>Presentation Deck</th>
              <th>Primary Curriculum Domain</th>
              <th>Slide Range</th>
              <th>Notebook Lab</th>
              <th>Launch</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid var(--cyan);">Lecture 1</span></td>
              <td><strong>Deck 01</strong></td>
              <td>Fundamentals of Computing (Architecture, Binary Representation, Moore's Law)</td>
              <td>Slides 1 – 15</td>
              <td><a href="L01.ipynb" class="nb-pill">L01.ipynb</a></td>
              <td><a href="python_presentation_01.html#slide-1" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid var(--cyan);">Lecture 2</span></td>
              <td><strong>Deck 01</strong></td>
              <td>Intro to Python Programming (Expressions, Variables, Types, Operators &amp; PEP 8)</td>
              <td>Slides 16 – 35</td>
              <td><a href="L02.ipynb" class="nb-pill">L02.ipynb</a></td>
              <td><a href="python_presentation_01.html#slide-16" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(250, 204, 21, 0.15); color: var(--gold); border: 1px solid var(--gold);">Lecture 3</span></td>
              <td><strong>Deck 02</strong></td>
              <td>Control Statements &amp; Program Development (Algorithms, Selection, Iteration, Statistics)</td>
              <td>Slides 1 – 18</td>
              <td><a href="L03.ipynb" class="nb-pill">L03.ipynb</a></td>
              <td><a href="python_presentation_02.html#slide-1" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(250, 204, 21, 0.15); color: var(--gold); border: 1px solid var(--gold);">Lecture 4</span></td>
              <td><strong>Deck 02</strong></td>
              <td>Functions &amp; Modular Architecture (Inputs/Outputs, Random Simulation, Scope, References)</td>
              <td>Slides 19 – 36</td>
              <td><a href="L04.ipynb" class="nb-pill">L04.ipynb</a></td>
              <td><a href="python_presentation_02.html#slide-19" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(52, 211, 153, 0.15); color: var(--mint); border: 1px solid var(--mint);">Lecture 5</span></td>
              <td><strong>Deck 03</strong></td>
              <td>Sequences: Lists and Tuples (Indexing, Slicing, In-place Mutation, Comprehensions, 2D)</td>
              <td>Slides 1 – 18</td>
              <td><a href="L05.ipynb" class="nb-pill">L05.ipynb</a></td>
              <td><a href="python_presentation_03.html#slide-1" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(52, 211, 153, 0.15); color: var(--mint); border: 1px solid var(--mint);">Lecture 6</span></td>
              <td><strong>Deck 03</strong></td>
              <td>Dictionaries and Sets (Hash Tables, Key-Value Mappings, Set Algebra, Venn Operations)</td>
              <td>Slides 19 – 36</td>
              <td><a href="L06.ipynb" class="nb-pill">L06.ipynb</a></td>
              <td><a href="python_presentation_03.html#slide-19" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(192, 132, 252, 0.15); color: var(--purple); border: 1px solid var(--purple);">Lecture 7</span></td>
              <td><strong>Deck 04</strong></td>
              <td>NumPy Arrays: Numerical Computing (Multidimensional Tensors, Vectorization, Broadcasting)</td>
              <td>Slides 1 – 18</td>
              <td><a href="L07.ipynb" class="nb-pill">L07.ipynb</a></td>
              <td><a href="python_presentation_04.html#slide-1" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(192, 132, 252, 0.15); color: var(--purple); border: 1px solid var(--purple);">Lecture 8</span></td>
              <td><strong>Deck 04</strong></td>
              <td>Strings &amp; Regular Expressions (f-string Formatting, Token Pipelines, Regex Automata)</td>
              <td>Slides 19 – 36</td>
              <td><a href="L08.ipynb" class="nb-pill">L08.ipynb</a></td>
              <td><a href="python_presentation_04.html#slide-19" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(251, 113, 133, 0.15); color: var(--coral); border: 1px solid var(--coral);">Lecture 9</span></td>
              <td><strong>Deck 05</strong></td>
              <td>Files &amp; Exceptions (Stream I/O, Persistent Storage, JSON Dictionaries, Defensive try-catch)</td>
              <td>Slides 1 – 18</td>
              <td><a href="L09.ipynb" class="nb-pill">L09.ipynb</a></td>
              <td><a href="python_presentation_05.html#slide-1" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(251, 113, 133, 0.15); color: var(--coral); border: 1px solid var(--coral);">Lecture 10</span></td>
              <td><strong>Deck 05</strong></td>
              <td>Intro to Object-Oriented Programming (Classes, Constructors, Encapsulation &amp; Magic Methods)</td>
              <td>Slides 19 – 36</td>
              <td><a href="L10.ipynb" class="nb-pill">L10.ipynb</a></td>
              <td><a href="python_presentation_05.html#slide-19" class="lec-jump-btn">Launch ↗</a></td>
            </tr>
            <tr>
              <td><span class="lecture-badge-pill" style="background: rgba(255, 255, 255, 0.1); color: var(--text-bright); border: 1px solid rgba(255, 255, 255, 0.2);">Lab 11</span></td>
              <td><strong>Supplementary</strong></td>
              <td>Pandas Dataframes, Tabular Analytics &amp; Aviation Data Visualization</td>
              <td>Hands-on Lab</td>
              <td><a href="L11.ipynb" class="nb-pill">L11.ipynb</a></td>
              <td><span style="font-size: 0.8rem; color: var(--text-dim);">Jupyter Lab</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Keyboard Shortcuts Guide -->
    <section class="syllabus-section" id="shortcuts">
      <div class="section-title-wrap">
        <h2 class="section-title">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--mint)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="4" width="20" height="16" rx="2"></rect>
            <path d="M6 8h.001"></path>
            <path d="M10 8h.001"></path>
            <path d="M14 8h.001"></path>
            <path d="M18 8h.001"></path>
            <path d="M8 12h.001"></path>
            <path d="M12 12h.001"></path>
            <path d="M16 12h.001"></path>
            <path d="M7 16h10"></path>
          </svg>
          Slide Deck Keyboard Navigation
        </h2>
      </div>
      <p style="color: var(--text-dim); font-size: 0.95rem;">
        When viewing any presentation deck, use these keyboard shortcuts for smooth presentation control:
      </p>

      <div class="shortcuts-grid">
        <div class="shortcut-card">
          <span class="key-cap">→</span>
          <div class="key-info">
            <span class="key-action">Next Slide</span>
            <span class="key-desc">Also Space or PageDown</span>
          </div>
        </div>
        <div class="shortcut-card">
          <span class="key-cap">←</span>
          <div class="key-info">
            <span class="key-action">Previous Slide</span>
            <span class="key-desc">Also PageUp</span>
          </div>
        </div>
        <div class="shortcut-card">
          <span class="key-cap">Home</span>
          <div class="key-info">
            <span class="key-action">First Slide</span>
            <span class="key-desc">Jump to deck beginning</span>
          </div>
        </div>
        <div class="shortcut-card">
          <span class="key-cap">End</span>
          <div class="key-info">
            <span class="key-action">Last Slide</span>
            <span class="key-desc">Jump to curriculum summary</span>
          </div>
        </div>
        <div class="shortcut-card">
          <span class="key-cap">F</span>
          <div class="key-info">
            <span class="key-action">Fullscreen</span>
            <span class="key-desc">Toggle projector mode</span>
          </div>
        </div>
        <div class="shortcut-card">
          <span class="key-cap">Esc</span>
          <div class="key-info">
            <span class="key-action">Exit Fullscreen</span>
            <span class="key-desc">Return to window view</span>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="portal-footer">
    <div class="footer-content">
      <div class="footer-left">
        <strong style="color: var(--text-bright);">Civil Aviation Training Center (CATC) • Thailand</strong>
        <span>Department of Aviation Engineering &bull; Python Programming Curriculum</span>
      </div>
      <div class="footer-links">
        <a href="#top" class="footer-link">Back to Top ↑</a>
        <a href="https://docs.python.org/3/" target="_blank" rel="noopener" class="footer-link">Python Docs ↗</a>
      </div>
    </div>
  </footer>

  <!-- Embedded Decks JSON Data -->
  <script>
    const DECKS_DATA = {json_data_str};
  </script>

  <!-- Portal Interactive Script -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const container = document.getElementById('decks-container');
      const searchInput = document.getElementById('global-search');
      const searchClear = document.getElementById('search-clear');
      const searchPanel = document.getElementById('search-results-panel');
      const resultsList = document.getElementById('results-list');
      const resultCount = document.getElementById('result-count');
      const filterPills = document.querySelectorAll('.filter-pills .pill');
      const searchTriggerBtn = document.getElementById('search-trigger-btn');

      // Accent gradients per deck
      const deckGradients = [
        'linear-gradient(90deg, #38bdf8 0%, #007acc 100%)',
        'linear-gradient(90deg, #facc15 0%, #eab308 100%)',
        'linear-gradient(90deg, #34d399 0%, #059669 100%)',
        'linear-gradient(90deg, #c084fc 0%, #9333ea 100%)',
        'linear-gradient(90deg, #fb7185 0%, #e11d48 100%)'
      ];

      // Render Deck Cards
      function renderDecks(filter = 'all') {{
        container.innerHTML = '';

        DECKS_DATA.forEach((deck, idx) => {{
          const deckFilterKey = `deck-${{deck.id}}`;
          if (filter !== 'all' && filter !== deckFilterKey) return;

          const card = document.createElement('article');
          card.className = 'deck-card';
          card.id = `deck-card-${{deck.id}}`;

          const grad = deckGradients[idx % deckGradients.length];

          // Slides outline generation
          const outlineSlidesHtml = deck.slides.map(s => `
            <a href="${{deck.file}}#${{s.id}}" class="outline-slide-link" title="${{s.eyebrow ? s.eyebrow + ' • ' : ''}}${{s.title}}">
              <span class="slide-num-pill">${{s.num}}</span>
              <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${{s.title}}</span>
            </a>
          `).join('');

          // Notebooks pills html
          const notebooksHtml = deck.notebooks.map(nb => `
            <a href="${{nb}}" class="nb-pill" title="Open Jupyter Notebook ${{nb}}">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              ${{nb}}
            </a>
          `).join(' ');

          // Tags html
          const tagsHtml = deck.tags.map(t => `<span class="topic-tag">${{t}}</span>`).join('');

          card.innerHTML = `
            <div class="deck-top-bar" style="background: ${{grad}};"></div>
            <div class="deck-content">
              <div class="deck-header">
                <div class="deck-header-info">
                  <div class="deck-badges">
                    <span class="badge-deck-no" style="background: rgba(255, 255, 255, 0.08); color: ${{deck.badge_color}}; border: 1px solid ${{deck.badge_color}}44;">DECK ${{deck.deck_number}}</span>
                    <span class="badge-lectures">${{deck.lectures_label}}</span>
                    <span class="badge-slides-count">&bull; ${{deck.total_slides}} Widescreen Slides</span>
                  </div>
                  <h3 class="deck-title">${{deck.title}}</h3>
                  <p class="deck-subtitle">${{deck.subtitle}}</p>
                </div>
              </div>

              <!-- Dual Lecture Split Modules -->
              <div class="deck-lectures-grid">
                <div class="lecture-box">
                  <div>
                    <div class="lec-eyebrow">${{deck.part1.lecture}}</div>
                    <h4 class="lec-title">${{deck.part1.title}}</h4>
                  </div>
                  <div class="lec-meta">
                    <span style="font-size: 0.78rem; color: var(--text-dim);">Starts at Slide ${{deck.part1.slide}}</span>
                    <a href="${{deck.file}}#${{deck.part1.id}}" class="lec-jump-btn">
                      Jump to ${{deck.part1.lecture}} ↗
                    </a>
                  </div>
                </div>

                <div class="lecture-box">
                  <div>
                    <div class="lec-eyebrow" style="color: var(--gold);">${{deck.part2.lecture}}</div>
                    <h4 class="lec-title">${{deck.part2.title}}</h4>
                  </div>
                  <div class="lec-meta">
                    <span style="font-size: 0.78rem; color: var(--text-dim);">Starts at Slide ${{deck.part2.slide}}</span>
                    <a href="${{deck.file}}#${{deck.part2.id}}" class="lec-jump-btn">
                      Jump to ${{deck.part2.lecture}} ↗
                    </a>
                  </div>
                </div>
              </div>

              <!-- Footer with tags, notebooks, and action buttons -->
              <div class="deck-footer-row">
                <div style="display: flex; flex-direction: column; gap: 0.6rem; flex: 1; min-width: 260px;">
                  <div class="deck-tags-list">
                    ${{tagsHtml}}
                  </div>
                  <div style="display: flex; align-items: center; gap: 0.4rem; flex-wrap: wrap;">
                    <span style="font-size: 0.75rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600;">Labs:</span>
                    ${{notebooksHtml}}
                  </div>
                </div>

                <div class="deck-actions-group">
                  <button class="btn-secondary toggle-outline-btn" data-deck="${{deck.id}}">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
                    <span>View Outline (${{deck.total_slides}})</span>
                  </button>
                  <a href="${{deck.file}}" class="btn-primary">
                    <span>Launch Presentation</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                  </a>
                </div>
              </div>
            </div>

            <!-- Expandable Slide Outline Drawer -->
            <div class="deck-outline-drawer" id="outline-drawer-${{deck.id}}">
              <div class="outline-header">
                <div class="outline-title">Deck ${{deck.deck_number}} &bull; Complete Slide Outline (${{deck.total_slides}} Slides)</div>
                <button class="btn-secondary close-outline-btn" data-deck="${{deck.id}}" style="padding: 0.25rem 0.6rem; font-size: 0.78rem;">
                  Close ✕
                </button>
              </div>
              <div class="outline-slides-grid">
                ${{outlineSlidesHtml}}
              </div>
            </div>
          `;

          container.appendChild(card);
        }});

        // Attach event listeners for outline buttons
        document.querySelectorAll('.toggle-outline-btn').forEach(btn => {{
          btn.addEventListener('click', (e) => {{
            const deckId = btn.getAttribute('data-deck');
            const drawer = document.getElementById(`outline-drawer-${{deckId}}`);
            if (drawer) {{
              const isOpen = drawer.classList.contains('open');
              drawer.classList.toggle('open');
              btn.innerHTML = isOpen ? 
                `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line></svg><span>View Outline</span>` :
                `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"></polyline></svg><span>Hide Outline</span>`;
            }}
          }});
        }});

        document.querySelectorAll('.close-outline-btn').forEach(btn => {{
          btn.addEventListener('click', () => {{
            const deckId = btn.getAttribute('data-deck');
            const drawer = document.getElementById(`outline-drawer-${{deckId}}`);
            if (drawer) drawer.classList.remove('open');
            const toggleBtn = document.querySelector(`.toggle-outline-btn[data-deck="${{deckId}}"]`);
            if (toggleBtn) {{
              toggleBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line></svg><span>View Outline</span>`;
            }}
          }});
        }});
      }}

      // Live Instant Search across all slides
      function handleSearch() {{
        const query = searchInput.value.trim().toLowerCase();

        if (query.length > 0) {{
          searchClear.style.display = 'block';
        }} else {{
          searchClear.style.display = 'none';
          searchPanel.style.display = 'none';
          return;
        }}

        const matches = [];

        DECKS_DATA.forEach(deck => {{
          deck.slides.forEach(slide => {{
            const matchTitle = slide.title.toLowerCase().includes(query);
            const matchEyebrow = slide.eyebrow.toLowerCase().includes(query);
            const matchDeck = deck.title.toLowerCase().includes(query);

            if (matchTitle || matchEyebrow || matchDeck) {{
              matches.push({{
                deckTitle: deck.title,
                deckNum: deck.deck_number,
                file: deck.file,
                slideNum: slide.num,
                slideId: slide.id,
                title: slide.title,
                eyebrow: slide.eyebrow
              }});
            }}
          }});
        }});

        resultCount.textContent = `${{matches.length}} matching slide${{matches.length === 1 ? '' : 's'}} found for "${{query}}"`;
        
        if (matches.length > 0) {{
          resultsList.innerHTML = matches.slice(0, 20).map(m => `
            <a href="${{m.file}}#${{m.slideId}}" class="search-result-item">
              <div class="res-left">
                <span class="res-eyebrow">Deck ${{m.deckNum}} &bull; ${{m.eyebrow || 'Lecture Slide'}}</span>
                <span class="res-title">${{m.title}}</span>
              </div>
              <span class="res-badge">Slide ${{m.slideNum}} ↗</span>
            </a>
          `).join('');

          if (matches.length > 20) {{
            resultsList.innerHTML += `<div style="text-align: center; color: var(--text-dim); font-size: 0.8rem; padding: 0.5rem;">+ ${{matches.length - 20}} more results. Refine your query.</div>`;
          }}
        }} else {{
          resultsList.innerHTML = `<div style="padding: 1.5rem; text-align: center; color: var(--text-dim); font-size: 0.9rem;">No matching slides found. Try searching for "loop", "regex", "array", "function", or "class".</div>`;
        }}

        searchPanel.style.display = 'block';
      }}

      searchInput.addEventListener('input', handleSearch);

      searchClear.addEventListener('click', () => {{
        searchInput.value = '';
        searchInput.focus();
        handleSearch();
      }});

      // Category Pill Filters
      filterPills.forEach(pill => {{
        pill.addEventListener('click', () => {{
          filterPills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          const filter = pill.getAttribute('data-filter');
          renderDecks(filter);
        }});
      }});

      // Keyboard Shortcut ⌘K / /
      document.addEventListener('keydown', (e) => {{
        if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {{
          e.preventDefault();
          searchInput.focus();
          searchInput.select();
        }} else if (e.key === '/' && document.activeElement !== searchInput) {{
          e.preventDefault();
          searchInput.focus();
          searchInput.select();
        }} else if (e.key === 'Escape') {{
          if (document.activeElement === searchInput) {{
            searchInput.blur();
          }}
          searchPanel.style.display = 'none';
        }}
      }});

      searchTriggerBtn.addEventListener('click', () => {{
        searchInput.focus();
        searchInput.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      }});

      // Initial render
      renderDecks('all');
    }});
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated index.html successfully!')
