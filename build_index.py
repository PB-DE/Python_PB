import json
import os
from build_labs import build_all_labs

# Ensure all 5 lab HTML files are compiled from their markdown source
build_all_labs()

with open('decks_data.json', 'r', encoding='utf-8') as f:
    decks = json.load(f)

# Colors, accents, and aviation flight phases for the 5 decks
deck_accents = {
    1: {"color": "#38bdf8", "rgb": "56, 189, 248", "class": "deck-1", "phase": "Phase 1: Pre-Flight Systems"},
    2: {"color": "#facc15", "rgb": "250, 204, 21", "class": "deck-2", "phase": "Phase 2: Algorithmic Takeoff"},
    3: {"color": "#34d399", "rgb": "52, 211, 153", "class": "deck-3", "phase": "Phase 3: Data Navigation"},
    4: {"color": "#c084fc", "rgb": "192, 132, 252", "class": "deck-4", "phase": "Phase 4: Tensor Vectoring"},
    5: {"color": "#fb7185", "rgb": "251, 113, 133", "class": "deck-5", "phase": "Phase 5: Approach & Architecture"}
}

# Fallback / canonical lab sheets mapping
lab_sheets_fallback = {
    1: {
        "html_file": "version 03/Lab_01_Exercise_L01_L02.html",
        "md_file": "version 03/Lab_01_Exercise_L01_L02.md",
        "filename": "Lab_01_Exercise_L01_L02.html",
        "title": "Laboratory Exercise 1: Computing Foundations & Python Basics"
    },
    2: {
        "html_file": "version 03/Lab_02_Exercise_L03_L04.html",
        "md_file": "version 03/Lab_02_Exercise_L03_L04.md",
        "filename": "Lab_02_Exercise_L03_L04.html",
        "title": "Laboratory Exercise 2: Algorithms, Control Flow & Modular Functions"
    },
    3: {
        "html_file": "version 03/Lab_03_Exercise_L05_L06.html",
        "md_file": "version 03/Lab_03_Exercise_L05_L06.md",
        "filename": "Lab_03_Exercise_L05_L06.html",
        "title": "Laboratory Exercise 3: Data Structures — Sequences, Mappings & Sets"
    },
    4: {
        "html_file": "version 03/Lab_04_Exercise_L07_L08.html",
        "md_file": "version 03/Lab_04_Exercise_L07_L08.md",
        "filename": "Lab_04_Exercise_L07_L08.html",
        "title": "Laboratory Exercise 4: Numerical Computing with NumPy & Text Processing"
    },
    5: {
        "html_file": "version 03/Lab_05_Exercise_L09_L10.html",
        "md_file": "version 03/Lab_05_Exercise_L09_L10.md",
        "filename": "Lab_05_Exercise_L09_L10.html",
        "title": "Laboratory Exercise 5: Data Persistence, Exception Handling & Object-Oriented Programming"
    }
}

JUPYTER_URL = "https://jupyter.org/try-jupyter/lab/"
JUPYTER_SVG = '<svg class="jupyter-icon" width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7.157 22.201A1.784 1.799 0 0 1 5.374 24a1.784 1.799 0 0 1-1.784-1.799 1.784 1.799 0 0 1 1.784-1.799 1.784 1.799 0 0 1 1.783 1.799zM20.582 1.427a1.415 1.427 0 0 1-1.415 1.428 1.415 1.427 0 0 1-1.416-1.428A1.415 1.427 0 0 1 19.167 0a1.415 1.427 0 0 1 1.415 1.427zM4.992 3.336A1.047 1.056 0 0 1 3.946 4.39a1.047 1.056 0 0 1-1.047-1.055A1.047 1.056 0 0 1 3.946 2.28a1.047 1.056 0 0 1 1.046 1.056zm7.336 1.517c3.769 0 7.06 1.38 8.768 3.424a9.363 9.363 0 0 0-3.393-4.547 9.238 9.238 0 0 0-5.377-1.728A9.238 9.238 0 0 0 6.95 3.73a9.363 9.363 0 0 0-3.394 4.547c1.713-2.04 5.004-3.424 8.772-3.424zm.001 13.295c-3.768 0-7.06-1.381-8.768-3.425a9.363 9.363 0 0 0 3.394 4.547A9.238 9.238 0 0 0 12.33 21a9.238 9.238 0 0 0 5.377-1.729 9.363 9.363 0 0 0 3.393-4.547c-1.712 2.044-5.003 3.425-8.772 3.425Z"/></svg>'
EXTERNAL_SVG = '<svg class="ext-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>'

# Generate node cards HTML
nodes_html = []
for deck in decks:
    d_id = deck['id']
    deck_no = deck.get('deck_number', f"0{d_id}")
    file_name = deck.get('file', f"python_presentation_{deck_no}.html")
    title = deck.get('title', '')
    subtitle = deck.get('subtitle', '')
    lectures = deck.get('lectures_label', '')
    total_slides = deck.get('total_slides', '')
    deck_meta = deck_accents.get(d_id, {})
    accent_class = deck_meta.get('class', f"deck-{d_id}")
    phase = deck_meta.get('phase', '')
    color = deck_meta.get('color', '#38bdf8')
    
    lab_meta = deck.get('lab_sheet') or lab_sheets_fallback.get(d_id, {})
    lab_html_file = (lab_meta.get('html_file') or lab_meta.get('file', '')).replace(' ', '%20')
    lab_md_file = lab_meta.get('md_file', '').replace(' ', '%20')
    lab_title = lab_meta.get('title', f"Laboratory Exercise {deck_no}")
    
    node_str = f'''        <div class="deck-node {accent_class}" data-deck="{d_id}" data-phase="{phase}" data-color="{color}" data-href="{file_name}" role="article" aria-label="Deck {deck_no}: {title} ({lectures}, {total_slides} slides)">
          <div class="node-socket" aria-hidden="true"></div>
          <a href="{file_name}" class="node-main-link" aria-label="Launch Deck {deck_no}: {title}">
            <div class="node-info">
              <div class="node-header-row">
                <span class="deck-tag">Deck {deck_no}</span>
                <span class="node-title">{title}</span>
              </div>
              <div class="node-meta">{lectures} &bull; {subtitle}</div>
            </div>
          </a>
          <div class="node-action">
            <span class="slide-count-badge">{total_slides} Slides</span>
            <div class="action-buttons">
              <a href="{lab_html_file}" class="lab-btn" target="_blank" rel="noopener" title="Open {lab_title} (HTML style)" aria-label="Open Lab Sheet {deck_no} (HTML)">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                <span>Lab Sheet</span>
              </a>
              <a href="{file_name}" class="launch-btn" aria-label="Launch Deck {deck_no} presentation">
                <span>Launch</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </a>
            </div>
          </div>
        </div>'''
    nodes_html.append(node_str)

nodes_joined = "\n".join(nodes_html)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Programming — CATC Course Portal</title>
  <meta name="description" content="Civil Aviation Training Center (CATC) Python Programming presentation curriculum mind map launcher. 5 widescreen decks, 10 lectures, 179 interactive slides, 5 interactive HTML laboratory sheets, and online JupyterLab workspace.">

  <style>
    :root {{
      --bg: #0b0d13;
      --bg-surface: #12151f;
      --bg-card: #181d2a;
      --bg-card-hover: #1f2637;
      --border: #242c3d;
      --border-light: rgba(255, 255, 255, 0.08);
      --border-focus: #38bdf8;
      --text: #cbd5e1;
      --text-bright: #ffffff;
      --text-dim: #94a3b8;
      
      /* Theme accents */
      --cyan: #38bdf8;
      --cyan-rgb: 56, 189, 248;
      --gold: #facc15;
      --gold-rgb: 250, 204, 21;
      --mint: #34d399;
      --mint-rgb: 52, 211, 153;
      --purple: #c084fc;
      --purple-rgb: 192, 132, 252;
      --coral: #fb7185;
      --coral-rgb: 251, 113, 133;
      --jupyter: #f37626;
      --jupyter-rgb: 243, 118, 38;
      
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -2px rgba(0, 0, 0, 0.3);
      --shadow-card: 0 4px 14px rgba(0, 0, 0, 0.35);
      --shadow-hover: 0 12px 28px -6px rgba(0, 0, 0, 0.55);
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
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow-x: hidden;
      font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }}

    /* Browser Surfaces Theming */
    ::selection {{
      background: rgba(56, 189, 248, 0.28);
      color: #ffffff;
    }}

    :focus-visible {{
      outline: 2px solid var(--cyan);
      outline-offset: 3px;
    }}

    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}

    ::-webkit-scrollbar-track {{
      background: var(--bg);
    }}

    ::-webkit-scrollbar-thumb {{
      background: var(--border);
      border-radius: 4px;
    }}

    ::-webkit-scrollbar-thumb:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}

    /* Sticky Navigation Header */
    header.portal-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 13, 19, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-light);
    }}

    .nav-container {{
      max-width: 1200px;
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
      width: 38px;
      height: 38px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: var(--shadow-sm);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
    }}

    .brand:hover .brand-logo {{
      transform: rotate(-12deg) scale(1.05);
      box-shadow: 0 8px 16px -2px rgba(0, 0, 0, 0.5);
    }}

    .brand:active .brand-logo {{
      transform: rotate(-18deg) scale(0.97);
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .brand-title {{
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--text-bright);
      letter-spacing: -0.015em;
      line-height: 1.2;
    }}

    .brand-subtitle {{
      font-size: 0.72rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 600;
    }}

    .nav-stats {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .nav-badge {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-dim);
      font-size: 0.75rem;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-sm);
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-variant-numeric: tabular-nums;
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    .nav-jupyter-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.35rem 0.8rem;
      border-radius: var(--radius-sm);
      background: rgba(243, 118, 38, 0.12);
      border: 1px solid rgba(243, 118, 38, 0.4);
      color: #ff9e58;
      font-size: 0.78rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
      white-space: nowrap;
    }}

    .nav-jupyter-btn svg.jupyter-icon {{
      color: #f37626;
      transition: transform 0.2s ease;
    }}

    .nav-jupyter-btn svg.ext-icon {{
      opacity: 0.7;
      transition: transform 0.2s ease, opacity 0.2s ease;
    }}

    .nav-jupyter-btn:hover {{
      background: #f37626;
      border-color: #f37626;
      color: #ffffff;
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(243, 118, 38, 0.4);
    }}

    .nav-jupyter-btn:hover svg.jupyter-icon {{
      color: #ffffff;
      transform: rotate(15deg);
    }}

    .nav-jupyter-btn:hover svg.ext-icon {{
      opacity: 1;
      transform: translate(1px, -1px);
    }}

    .nav-jupyter-btn:active {{
      transform: translateY(0);
    }}

    /* Main Section */
    main {{
      flex: 1;
      max-width: 1200px;
      margin: 0 auto;
      padding: 3.5rem 1.5rem 4rem;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }}

    .hero-title {{
      font-size: clamp(2.1rem, 4vw, 3rem);
      font-weight: 800;
      line-height: 1.15;
      color: var(--text-bright);
      margin-bottom: 0.75rem;
      letter-spacing: -0.025em;
      text-align: center;
      text-wrap: balance;
    }}

    .hero-title-accent {{
      color: var(--cyan);
    }}

    .hero-desc {{
      font-size: 1.02rem;
      color: var(--text-dim);
      max-width: 640px;
      margin: 0 auto 3.25rem;
      line-height: 1.6;
      text-align: center;
      text-wrap: balance;
    }}

    /* Mind Map Workspace Wrapper */
    .mindmap-wrapper {{
      width: 100%;
      max-width: 1080px;
      padding: 0.5rem 0;
      position: relative;
    }}

    .mindmap-container {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 4rem;
      align-items: center;
      position: relative;
    }}

    /* SVG Connecting Curves */
    .connector-svg {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }}

    .branch-path {{
      transition: stroke-opacity 0.25s ease, stroke-width 0.25s ease;
    }}

    /* Signal databus pulse animation */
    .branch-path.active {{
      stroke-opacity: 1 !important;
      stroke-width: 2.5 !important;
      stroke-dasharray: 8 6 !important;
      animation: signalFlow 0.65s linear infinite;
    }}

    @keyframes signalFlow {{
      to {{
        stroke-dashoffset: -28;
      }}
    }}

    /* Core Root Node (Left) */
    .core-node {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.85rem 1.35rem;
      text-align: center;
      position: relative;
      box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.45);
      z-index: 2;
      transition: border-color 0.25s ease;
    }}

    .core-socket {{
      position: absolute;
      right: -7px;
      top: 50%;
      transform: translateY(-50%);
      width: 14px;
      height: 14px;
      background: var(--cyan);
      border-radius: 50%;
      border: 2.5px solid var(--bg);
      z-index: 3;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.25s ease;
    }}

    .core-badge {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.7rem;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
      margin-bottom: 0.45rem;
      transition: color 0.2s ease;
    }}

    .core-title {{
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--text-bright);
      line-height: 1.2;
      margin-bottom: 0.45rem;
      letter-spacing: -0.015em;
    }}

    .core-desc {{
      font-size: 0.78rem;
      color: var(--text-dim);
      font-variant-numeric: tabular-nums;
      transition: color 0.2s ease;
    }}

    .core-action {{
      margin-top: auto;
      padding-top: 0.4rem;
    }}

    .core-jupyter-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      width: 100%;
      padding: 0.58rem 0.85rem;
      border-radius: var(--radius-sm);
      background: rgba(243, 118, 38, 0.12);
      border: 1px solid rgba(243, 118, 38, 0.35);
      color: #ff9e58;
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }}

    .core-jupyter-btn svg.jupyter-icon {{
      color: #f37626;
      transition: transform 0.2s ease;
    }}

    .core-jupyter-btn svg.ext-icon {{
      opacity: 0.7;
      transition: transform 0.2s ease, opacity 0.2s ease;
    }}

    .core-jupyter-btn:hover {{
      background: #f37626;
      border-color: #f37626;
      color: #ffffff;
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(243, 118, 38, 0.4);
    }}

    .core-jupyter-btn:hover svg.jupyter-icon {{
      color: #ffffff;
      transform: rotate(15deg);
    }}

    .core-jupyter-btn:hover svg.ext-icon {{
      opacity: 1;
      transform: translate(1px, -1px);
    }}

    .core-jupyter-btn:active {{
      transform: translateY(0);
    }}

    /* Branches List (Right) */
    .branches-list {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
      z-index: 2;
    }}

    /* Deck Node Card */
    .deck-node {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.05rem 1.35rem;
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.25rem;
      transition: background 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
      position: relative;
      box-shadow: var(--shadow-card);
      cursor: pointer;
    }}

    /* Connection Socket on Left of each card */
    .node-socket {{
      position: absolute;
      left: -6px;
      top: 50%;
      transform: translateY(-50%);
      width: 12px;
      height: 12px;
      border-radius: 50%;
      border: 2px solid var(--bg);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 3;
    }}

    .deck-1 .node-socket {{ background: var(--cyan); }}
    .deck-2 .node-socket {{ background: var(--gold); }}
    .deck-3 .node-socket {{ background: var(--mint); }}
    .deck-4 .node-socket {{ background: var(--purple); }}
    .deck-5 .node-socket {{ background: var(--coral); }}

    /* Hover and Focus States */
    .deck-node:hover,
    .deck-node.active-launch {{
      background: var(--bg-card-hover);
      box-shadow: var(--shadow-hover);
    }}

    .deck-node:hover .node-socket,
    .deck-node.active-launch .node-socket {{
      transform: translateY(-50%) scale(1.35);
    }}

    .deck-node.deck-1:hover, .deck-node.deck-1.active-launch {{ border-color: var(--cyan); }}
    .deck-node.deck-2:hover, .deck-node.deck-2.active-launch {{ border-color: var(--gold); }}
    .deck-node.deck-3:hover, .deck-node.deck-3.active-launch {{ border-color: var(--mint); }}
    .deck-node.deck-4:hover, .deck-node.deck-4.active-launch {{ border-color: var(--purple); }}
    .deck-node.deck-5:hover, .deck-node.deck-5.active-launch {{ border-color: var(--coral); }}

    .node-main-link {{
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      flex: 1;
      min-width: 0;
      border-radius: var(--radius-sm);
    }}

    .node-main-link:focus-visible {{
      outline: 2px solid var(--cyan);
      outline-offset: 4px;
    }}

    .node-info {{
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }}

    .node-header-row {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }}

    .deck-tag {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.74rem;
      font-weight: 700;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      font-variant-numeric: tabular-nums;
    }}

    .deck-1 .deck-tag {{ background: rgba(var(--cyan-rgb), 0.14); color: var(--cyan); border: 1px solid rgba(var(--cyan-rgb), 0.2); }}
    .deck-2 .deck-tag {{ background: rgba(var(--gold-rgb), 0.14); color: var(--gold); border: 1px solid rgba(var(--gold-rgb), 0.2); }}
    .deck-3 .deck-tag {{ background: rgba(var(--mint-rgb), 0.14); color: var(--mint); border: 1px solid rgba(var(--mint-rgb), 0.2); }}
    .deck-4 .deck-tag {{ background: rgba(var(--purple-rgb), 0.14); color: var(--purple); border: 1px solid rgba(var(--purple-rgb), 0.2); }}
    .deck-5 .deck-tag {{ background: rgba(var(--coral-rgb), 0.14); color: var(--coral); border: 1px solid rgba(var(--coral-rgb), 0.2); }}

    .node-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-bright);
      letter-spacing: -0.01em;
      transition: color 0.15s ease;
    }}

    .deck-node:hover .node-title {{
      color: #ffffff;
    }}

    .node-meta {{
      font-size: 0.8rem;
      color: var(--text-dim);
    }}

    .node-action {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-shrink: 0;
    }}

    .action-buttons {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .slide-count-badge {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.75rem;
      color: var(--text-dim);
      font-variant-numeric: tabular-nums;
      white-space: nowrap;
    }}

    .lab-btn {{
      font-size: 0.8rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.42rem 0.72rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      color: var(--text);
      white-space: nowrap;
      text-decoration: none;
      transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease, transform 0.15s ease, box-shadow 0.2s ease;
      cursor: pointer;
    }}

    .lab-btn svg {{
      color: var(--text-dim);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), color 0.2s ease;
      flex-shrink: 0;
    }}

    .lab-btn:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.25);
      color: var(--text-bright);
      transform: translateY(-1px);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35);
    }}

    .lab-btn:hover svg {{
      color: var(--text-bright);
      transform: translateY(1px);
    }}

    .lab-btn:active {{
      transform: translateY(0);
    }}

    .deck-node.deck-1 .lab-btn:hover {{ border-color: rgba(var(--cyan-rgb), 0.5); color: var(--cyan); background: rgba(var(--cyan-rgb), 0.1); }}
    .deck-node.deck-1 .lab-btn:hover svg {{ color: var(--cyan); }}

    .deck-node.deck-2 .lab-btn:hover {{ border-color: rgba(var(--gold-rgb), 0.5); color: var(--gold); background: rgba(var(--gold-rgb), 0.1); }}
    .deck-node.deck-2 .lab-btn:hover svg {{ color: var(--gold); }}

    .deck-node.deck-3 .lab-btn:hover {{ border-color: rgba(var(--mint-rgb), 0.5); color: var(--mint); background: rgba(var(--mint-rgb), 0.1); }}
    .deck-node.deck-3 .lab-btn:hover svg {{ color: var(--mint); }}

    .deck-node.deck-4 .lab-btn:hover {{ border-color: rgba(var(--purple-rgb), 0.5); color: var(--purple); background: rgba(var(--purple-rgb), 0.1); }}
    .deck-node.deck-4 .lab-btn:hover svg {{ color: var(--purple); }}

    .deck-node.deck-5 .lab-btn:hover {{ border-color: rgba(var(--coral-rgb), 0.5); color: var(--coral); background: rgba(var(--coral-rgb), 0.1); }}
    .deck-node.deck-5 .lab-btn:hover svg {{ color: var(--coral); }}

    /* Keep launch button clean when hovering on lab button */
    .deck-node:has(.lab-btn:hover) .launch-btn {{
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-bright);
      border-color: var(--border);
    }}
    .deck-node:has(.lab-btn:hover) .launch-btn svg {{
      transform: none;
    }}

    /* Keyboard Shortcuts Bar */
    .shortcuts-hint {{
      margin-top: 2.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      color: var(--text-dim);
      flex-wrap: wrap;
    }}

    .kbd-chip {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.74rem;
      font-weight: 700;
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      color: var(--cyan);
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.35);
      cursor: pointer;
      user-select: none;
      transition: background 0.15s ease, border-color 0.15s ease, transform 0.15s ease, color 0.15s ease;
    }}

    .kbd-chip:hover {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--cyan);
      transform: translateY(-1px);
    }}

    .kbd-chip.active {{
      background: rgba(56, 189, 248, 0.3);
      border-color: var(--cyan);
      transform: translateY(1px);
    }}

    .hint-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      color: var(--text-bright);
      font-weight: 600;
      font-size: 0.76rem;
    }}

    .hint-badge svg {{
      color: var(--cyan);
    }}

    .hint-jupyter-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: rgba(243, 118, 38, 0.12);
      border: 1px solid rgba(243, 118, 38, 0.35);
      padding: 0.16rem 0.55rem;
      border-radius: 4px;
      color: #ff9e58;
      font-weight: 600;
      font-size: 0.76rem;
      text-decoration: none;
      transition: all 0.15s ease;
    }}

    .hint-jupyter-link svg.jupyter-icon {{
      color: #f37626;
    }}

    .hint-jupyter-link svg.ext-icon {{
      opacity: 0.7;
    }}

    .hint-jupyter-link:hover {{
      background: #f37626;
      border-color: #f37626;
      color: #ffffff;
      transform: translateY(-1px);
    }}

    .hint-jupyter-link:hover svg.jupyter-icon {{
      color: #ffffff;
    }}

    .hint-jupyter-link:hover svg.ext-icon {{
      opacity: 1;
    }}

    /* Footer */
    footer.portal-footer {{
      margin-top: auto;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-light);
      padding: 1.75rem 1.5rem;
      color: var(--text-dim);
      font-size: 0.82rem;
    }}

    .footer-content {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .footer-links {{
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      flex-wrap: wrap;
    }}

    .footer-jupyter-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      color: #ff9e58;
      text-decoration: none;
      font-weight: 600;
      transition: color 0.15s ease;
    }}

    .footer-jupyter-link svg.jupyter-icon {{
      color: #f37626;
    }}

    .footer-jupyter-link svg.ext-icon {{
      opacity: 0.7;
    }}

    .footer-jupyter-link:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}

    .footer-jupyter-link:hover svg.jupyter-icon {{
      color: #ffffff;
    }}

    .footer-divider {{
      opacity: 0.35;
    }}

    @media (max-width: 850px) {{
      .mindmap-container {{
        grid-template-columns: 1fr;
        gap: 2rem;
      }}
      .connector-svg,
      .core-socket,
      .node-socket {{
        display: none;
      }}
      .core-node {{
        text-align: left;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        padding: 1.25rem 1.5rem;
        gap: 1rem;
      }}
      .core-action {{
        margin-top: 0;
        padding-top: 0;
        width: 100%;
      }}
      .core-jupyter-btn {{
        width: 100%;
      }}
    }}

    @media (max-width: 720px) {{
      .deck-node {{
        flex-direction: column;
        align-items: stretch;
        gap: 0.85rem;
      }}
      .node-action {{
        width: 100%;
        justify-content: space-between;
      }}
    }}

    @media (max-width: 600px) {{
      .portal-nav .nav-container {{
        flex-direction: column;
        align-items: flex-start;
        gap: 0.75rem;
      }}
      .nav-actions {{
        width: 100%;
        justify-content: space-between;
      }}
    }}

    @media (max-width: 480px) {{
      .node-action {{
        flex-direction: column;
        align-items: stretch;
        gap: 0.65rem;
      }}
      .action-buttons {{
        width: 100%;
        justify-content: stretch;
      }}
      .action-buttons .lab-btn,
      .action-buttons .launch-btn {{
        flex: 1;
        justify-content: center;
      }}
      .nav-actions {{
        flex-direction: column;
        align-items: stretch;
        gap: 0.6rem;
      }}
      .nav-jupyter-btn {{
        justify-content: center;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Header -->
  <header class="portal-nav">
    <div class="nav-container">
      <a href="#" class="brand" aria-label="CATC Python Course Portal Home">
        <div class="brand-logo" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 19 21 12 17 5 21 12 2"></polygon>
          </svg>
        </div>
        <div class="brand-text">
          <span class="brand-title">Python Course Portal</span>
          <span class="brand-subtitle">Civil Aviation Training Center (CATC)</span>
        </div>
      </a>

      <div class="nav-actions">
        <div class="nav-stats" aria-label="Curriculum Statistics">
          <span class="nav-badge">10 Lectures</span>
          <span class="nav-badge">5 Decks</span>
          <span class="nav-badge">5 Lab Sheets</span>
          <span class="nav-badge">179 Slides</span>
        </div>
        <a href="{JUPYTER_URL}" target="_blank" rel="noopener noreferrer" class="nav-jupyter-btn" title="Open online JupyterLab sandbox in your browser">
          {JUPYTER_SVG}
          <span>Try JupyterLab</span>
          {EXTERNAL_SVG}
        </a>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <h1 class="hero-title">
      Python Curriculum <span class="hero-title-accent">Mind Map</span>
    </h1>
    <p class="hero-desc">
      Interactive lecture presentation pathway linking directly to the five course slide decks and laboratory exercise sheets.
    </p>

    <!-- Mind Map Workspace -->
    <div class="mindmap-wrapper">
      <div class="mindmap-container">
        <!-- SVG Branch Connectors -->
        <svg id="connector-svg" class="connector-svg" aria-hidden="true"></svg>

        <!-- Course Core Hub (Left) -->
        <div class="core-node" id="core-node">
          <div class="core-socket" aria-hidden="true"></div>
          <div>
            <div class="core-badge" id="core-badge">Course Core</div>
            <div class="core-title">Python Programming</div>
          </div>
          <div class="core-desc" id="core-desc">10 Lectures &bull; 5 Decks &bull; 5 Labs</div>
          <div class="core-action">
            <a href="{JUPYTER_URL}" target="_blank" rel="noopener noreferrer" class="core-jupyter-btn" title="Open online JupyterLab sandbox (runs in browser)">
              {JUPYTER_SVG}
              <span>Try JupyterLab</span>
              {EXTERNAL_SVG}
            </a>
          </div>
        </div>

        <!-- 5 Progressive Deck Nodes (Right) -->
        <nav class="branches-list" aria-label="Course presentation decks">
{nodes_joined}
        </nav>
      </div>

      <!-- Quick Shortcuts Hint -->
      <div class="shortcuts-hint" aria-label="Keyboard Shortcuts and Course Materials">
        <span>Quick Launch: Press</span>
        <kbd class="kbd-chip" data-key="1">1</kbd>
        <span>through</span>
        <kbd class="kbd-chip" data-key="5">5</kbd>
        <span>to launch decks &bull;</span>
        <kbd class="kbd-chip" data-key="j" title="Press J to open JupyterLab in a new tab">J</kbd>
        <span>or</span>
        <a href="{JUPYTER_URL}" target="_blank" rel="noopener noreferrer" class="hint-jupyter-link" title="Open online JupyterLab sandbox in browser">
          {JUPYTER_SVG}
          <span>Try JupyterLab</span>
          {EXTERNAL_SVG}
        </a>
        <span>&bull; Click</span>
        <span class="hint-badge"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg> Lab Sheet</span>
        <span>to view interactive HTML exercises</span>
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="portal-footer">
    <div class="footer-content">
      <div>&copy; 2026 Civil Aviation Training Center (CATC). Department of Aviation Engineering.</div>
      <div class="footer-links">
        <a href="{JUPYTER_URL}" target="_blank" rel="noopener noreferrer" class="footer-jupyter-link" title="Open online JupyterLab sandbox in browser">
          {JUPYTER_SVG}
          <span>Try JupyterLab Online</span>
          {EXTERNAL_SVG}
        </a>
        <span class="footer-divider">&bull;</span>
        <span>100% Offline Capable &bull; Standalone HTML5 Presentations &amp; Materials</span>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const svg = document.getElementById('connector-svg');
      const coreSocket = document.querySelector('.core-socket');
      const nodeSockets = document.querySelectorAll('.node-socket');
      const nodes = document.querySelectorAll('.deck-node');
      const coreBadge = document.getElementById('core-badge');
      const coreDesc = document.getElementById('core-desc');
      const kbdChips = document.querySelectorAll('.kbd-chip');
      const colors = ['#38bdf8', '#facc15', '#34d399', '#c084fc', '#fb7185'];

      function drawConnectors() {{
        if (!svg || window.innerWidth <= 850) {{
          if (svg) svg.innerHTML = '';
          return;
        }}
        const container = document.querySelector('.mindmap-container');
        if (!container || !coreSocket || nodeSockets.length === 0) return;

        const contRect = container.getBoundingClientRect();
        const coreRect = coreSocket.getBoundingClientRect();

        const startX = coreRect.left + (coreRect.width / 2) - contRect.left;
        const startY = coreRect.top + (coreRect.height / 2) - contRect.top;

        let paths = '';

        nodeSockets.forEach((sock, i) => {{
          const sockRect = sock.getBoundingClientRect();
          const endX = sockRect.left + (sockRect.width / 2) - contRect.left;
          const endY = sockRect.top + (sockRect.height / 2) - contRect.top;
          
          const deltaX = endX - startX;
          const cp1X = startX + (deltaX * 0.45);
          const cp2X = startX + (deltaX * 0.55);

          paths += `<path id="path-${{i + 1}}" d="M ${{startX}} ${{startY}} C ${{cp1X}} ${{startY}}, ${{cp2X}} ${{endY}}, ${{endX}} ${{endY}}" 
            fill="none" stroke="${{colors[i]}}" stroke-width="2" stroke-opacity="0.32" stroke-dasharray="6,4" class="branch-path"/>`;
        }});

        svg.setAttribute('width', contRect.width);
        svg.setAttribute('height', contRect.height);
        svg.setAttribute('viewBox', `0 0 ${{contRect.width}} ${{contRect.height}}`);
        svg.innerHTML = paths;
      }}

      // Interactive hover illumination & avionics telemetry feedback
      nodes.forEach((node, i) => {{
        node.addEventListener('mouseenter', () => {{
          const p = document.getElementById(`path-${{i + 1}}`);
          if (p) {{
            p.classList.add('active');
          }}
          if (coreBadge && coreDesc) {{
            const d = node.dataset.deck;
            const phase = node.dataset.phase;
            const color = node.dataset.color;
            coreBadge.textContent = `Deck 0${{d}} • Engaged`;
            coreBadge.style.color = color;
            coreDesc.textContent = phase;
            if (coreSocket) {{
              coreSocket.style.backgroundColor = color;
              coreSocket.style.transform = 'translateY(-50%) scale(1.2)';
            }}
          }}
        }});

        node.addEventListener('mouseleave', () => {{
          const p = document.getElementById(`path-${{i + 1}}`);
          if (p) {{
            p.classList.remove('active');
          }}
          if (coreBadge && coreDesc) {{
            coreBadge.textContent = 'Course Core';
            coreBadge.style.color = 'var(--cyan)';
            coreDesc.innerHTML = '10 Lectures &bull; 5 Decks &bull; 5 Labs';
            if (coreSocket) {{
              coreSocket.style.backgroundColor = 'var(--cyan)';
              coreSocket.style.transform = 'translateY(-50%) scale(1)';
            }}
          }}
        }});

        // Click card background to launch deck (unless clicking lab sheet link)
        node.addEventListener('click', (e) => {{
          if (e.target.closest('.lab-btn')) {{
            return;
          }}
          if (e.target.closest('a')) {{
            return;
          }}
          const href = node.dataset.href;
          if (href) {{
            node.classList.add('active-launch');
            setTimeout(() => {{
              window.location.href = href;
            }}, 120);
          }}
        }});
      }});

      // Draw initial connectors and bind resize
      drawConnectors();
      window.addEventListener('resize', drawConnectors);

      function launchDeck(key) {{
        const targetNode = document.querySelector(`.deck-node.deck-${{key}}`);
        const targetKbd = document.querySelector(`.kbd-chip[data-key="${{key}}"]`);
        if (targetNode) {{
          targetNode.classList.add('active-launch');
          if (targetKbd) targetKbd.classList.add('active');
          const p = document.getElementById(`path-${{key}}`);
          if (p) p.classList.add('active');
          
          const href = targetNode.dataset.href || targetNode.getAttribute('href');
          setTimeout(() => {{
            window.location.href = href;
          }}, 120);
        }}
      }}

      // Keyboard shortcuts: 1-5 to launch decks directly, J for JupyterLab
      document.addEventListener('keydown', (e) => {{
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        if (['1', '2', '3', '4', '5'].includes(e.key) && !e.metaKey && !e.ctrlKey && !e.altKey) {{
          launchDeck(e.key);
        }} else if ((e.key === 'j' || e.key === 'J') && !e.metaKey && !e.ctrlKey && !e.altKey) {{
          const kbdJ = document.querySelector('.kbd-chip[data-key="j"]');
          if (kbdJ) kbdJ.classList.add('active');
          window.open('{JUPYTER_URL}', '_blank', 'noopener,noreferrer');
          if (kbdJ) setTimeout(() => kbdJ.classList.remove('active'), 250);
        }}
      }});

      // Click on keyboard chips
      kbdChips.forEach(chip => {{
        chip.addEventListener('click', () => {{
          const key = chip.dataset.key;
          if (key === 'j') {{
            window.open('{JUPYTER_URL}', '_blank', 'noopener,noreferrer');
          }} else {{
            launchDeck(key);
          }}
        }});
      }});
    }});
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully with interactive HTML lab sheet links!")
