import json

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
    
    node_str = f'''        <a href="{file_name}" class="deck-node {accent_class}" data-deck="{d_id}" data-phase="{phase}" data-color="{color}" aria-label="Deck {deck_no}: {title} ({lectures}, {total_slides} slides)">
          <div class="node-socket" aria-hidden="true"></div>
          <div class="node-info">
            <div class="node-header-row">
              <span class="deck-tag">Deck {deck_no}</span>
              <span class="node-title">{title}</span>
            </div>
            <div class="node-meta">{lectures} &bull; {subtitle}</div>
          </div>
          <div class="node-action">
            <span class="slide-count-badge">{total_slides} Slides</span>
            <div class="launch-btn">
              <span>Launch</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </div>
        </a>'''
    nodes_html.append(node_str)

nodes_joined = "\n".join(nodes_html)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Programming — CATC Course Portal</title>
  <meta name="description" content="Civil Aviation Training Center (CATC) Python Programming presentation curriculum mind map launcher. 5 widescreen decks, 10 lectures, 179 interactive slides.">

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
      max-width: 600px;
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
      text-decoration: none;
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.25rem;
      transition: background 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
      position: relative;
      box-shadow: var(--shadow-card);
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
    }}

    .node-meta {{
      font-size: 0.8rem;
      color: var(--text-dim);
    }}

    .node-action {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}

    .slide-count-badge {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.75rem;
      color: var(--text-dim);
      font-variant-numeric: tabular-nums;
      white-space: nowrap;
    }}

    .launch-btn {{
      font-size: 0.82rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
      color: var(--text-bright);
      white-space: nowrap;
      transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease;
    }}

    .launch-btn svg {{
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .deck-node:hover .launch-btn svg,
    .deck-node.active-launch .launch-btn svg {{
      transform: translateX(3px);
    }}

    .deck-node.deck-1:hover .launch-btn {{ background: var(--cyan); color: #0b0d13; border-color: var(--cyan); }}
    .deck-node.deck-2:hover .launch-btn {{ background: var(--gold); color: #0b0d13; border-color: var(--gold); }}
    .deck-node.deck-3:hover .launch-btn {{ background: var(--mint); color: #0b0d13; border-color: var(--mint); }}
    .deck-node.deck-4:hover .launch-btn {{ background: var(--purple); color: #0b0d13; border-color: var(--purple); }}
    .deck-node.deck-5:hover .launch-btn {{ background: var(--coral); color: #0b0d13; border-color: var(--coral); }}

    /* Keyboard Shortcuts Bar */
    .shortcuts-hint {{
      margin-top: 2.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      color: var(--text-dim);
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
        align-items: center;
        justify-content: space-between;
        padding: 1.25rem 1.5rem;
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

      <div class="nav-stats" aria-label="Curriculum Statistics">
        <span class="nav-badge">10 Lectures</span>
        <span class="nav-badge">5 Decks</span>
        <span class="nav-badge">179 Slides</span>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <h1 class="hero-title">
      Python Curriculum <span class="hero-title-accent">Mind Map</span>
    </h1>
    <p class="hero-desc">
      Interactive lecture presentation pathway linking directly to the five course slide decks.
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
          <div class="core-desc" id="core-desc">10 Lectures &bull; 5 Decks</div>
        </div>

        <!-- 5 Progressive Deck Nodes (Right) -->
        <nav class="branches-list" aria-label="Course presentation decks">
{nodes_joined}
        </nav>
      </div>

      <!-- Quick Shortcuts Hint -->
      <div class="shortcuts-hint" aria-label="Keyboard Shortcuts">
        <span>Quick Launch: Press</span>
        <kbd class="kbd-chip" data-key="1">1</kbd>
        <span>through</span>
        <kbd class="kbd-chip" data-key="5">5</kbd>
        <span>to launch any deck instantly</span>
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="portal-footer">
    <div class="footer-content">
      <div>&copy; 2026 Civil Aviation Training Center (CATC). Department of Aviation Engineering.</div>
      <div>100% Offline Capable &bull; Standalone HTML5 Presentations</div>
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
            coreDesc.innerHTML = '10 Lectures &bull; 5 Decks';
            if (coreSocket) {{
              coreSocket.style.backgroundColor = 'var(--cyan)';
              coreSocket.style.transform = 'translateY(-50%) scale(1)';
            }}
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
          
          const href = targetNode.getAttribute('href');
          setTimeout(() => {{
            window.location.href = href;
          }}, 120);
        }}
      }}

      // Keyboard shortcuts: 1-5 to launch decks directly
      document.addEventListener('keydown', (e) => {{
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        if (['1', '2', '3', '4', '5'].includes(e.key) && !e.metaKey && !e.ctrlKey && !e.altKey) {{
          launchDeck(e.key);
        }}
      }});

      // Click on keyboard chips
      kbdChips.forEach(chip => {{
        chip.addEventListener('click', () => {{
          launchDeck(chip.dataset.key);
        }});
      }});
    }});
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully!")
