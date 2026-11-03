#!/usr/bin/env python3
"""
build_labs.py
Compiles CATC Python Course Laboratory Exercise Markdown files (version 03/Lab_*.md)
into standalone, 100% offline-first, beautifully styled HTML documents.
"""

import os
import re
import html
import mistune

LAB_METADATA = {
    1: {
        "deck_no": "01",
        "lectures": "Lectures 1 & 2",
        "title": "Laboratory Exercise 1: Computing Foundations & Python Basics",
        "color": "#38bdf8",
        "color_rgb": "56, 189, 248",
        "md_file": "version 03/Lab_01_Exercise_L01_L02.md",
        "html_file": "version 03/Lab_01_Exercise_L01_L02.html",
        "presentation_file": "../python_presentation_01.html"
    },
    2: {
        "deck_no": "02",
        "lectures": "Lectures 3 & 4",
        "title": "Laboratory Exercise 2: Algorithms, Control Flow & Modular Functions",
        "color": "#facc15",
        "color_rgb": "250, 204, 21",
        "md_file": "version 03/Lab_02_Exercise_L03_L04.md",
        "html_file": "version 03/Lab_02_Exercise_L03_L04.html",
        "presentation_file": "../python_presentation_02.html"
    },
    3: {
        "deck_no": "03",
        "lectures": "Lectures 5 & 6",
        "title": "Laboratory Exercise 3: Data Structures — Sequences, Mappings & Sets",
        "color": "#34d399",
        "color_rgb": "52, 211, 153",
        "md_file": "version 03/Lab_03_Exercise_L05_L06.md",
        "html_file": "version 03/Lab_03_Exercise_L05_L06.html",
        "presentation_file": "../python_presentation_03.html"
    },
    4: {
        "deck_no": "04",
        "lectures": "Lectures 7 & 8",
        "title": "Laboratory Exercise 4: Numerical Computing with NumPy & Text Processing",
        "color": "#c084fc",
        "color_rgb": "192, 132, 252",
        "md_file": "version 03/Lab_04_Exercise_L07_L08.md",
        "html_file": "version 03/Lab_04_Exercise_L07_L08.html",
        "presentation_file": "../python_presentation_04.html"
    },
    5: {
        "deck_no": "05",
        "lectures": "Lectures 9 & 10",
        "title": "Laboratory Exercise 5: Data Persistence, Exception Handling & Object-Oriented Programming",
        "color": "#fb7185",
        "color_rgb": "251, 113, 133",
        "md_file": "version 03/Lab_05_Exercise_L09_L10.md",
        "html_file": "version 03/Lab_05_Exercise_L09_L10.html",
        "presentation_file": "../python_presentation_05.html"
    }
}

def extract_braced(s, start_idx):
    if start_idx >= len(s) or s[start_idx] != '{':
        return None, start_idx
    depth = 0
    content = []
    for i in range(start_idx, len(s)):
        if s[i] == '{':
            depth += 1
            if depth > 1:
                content.append('{')
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return ''.join(content), i + 1
            else:
                content.append('}')
        else:
            content.append(s[i])
    return None, len(s)

def parse_fractions(s):
    idx = 0
    while True:
        pos = s.find(r'\frac', idx)
        if pos == -1:
            break
        first_brace = pos + 5
        while first_brace < len(s) and s[first_brace].isspace():
            first_brace += 1
        if first_brace >= len(s) or s[first_brace] != '{':
            idx = pos + 5
            continue
        num, end_num = extract_braced(s, first_brace)
        if num is None:
            idx = pos + 5
            continue
        second_brace = end_num
        while second_brace < len(s) and s[second_brace].isspace():
            second_brace += 1
        if second_brace >= len(s) or s[second_brace] != '{':
            idx = end_num
            continue
        den, end_den = extract_braced(s, second_brace)
        if den is None:
            idx = end_num
            continue
        num_html = parse_fractions(num)
        den_html = parse_fractions(den)
        replacement = f'<span class="frac"><span class="num">{num_html}</span><span class="den">{den_html}</span></span>'
        s = s[:pos] + replacement + s[end_den:]
        idx = pos + len(replacement)
    return s

def format_latex(latex_str):
    s = latex_str.strip()
    if s.startswith('$$') and s.endswith('$$'):
        s = s[2:-2].strip()
    elif s.startswith(r'\(') and s.endswith(r'\)'):
        s = s[2:-2].strip()
    elif s.startswith('$') and s.endswith('$'):
        s = s[1:-1].strip()

    s = s.replace(r'\%', '%')
    s = s.replace(r'\_', '_')
    s = s.replace(r'\qquad', '&emsp;&emsp;')
    s = s.replace(r'\quad', '&emsp;')
    s = s.replace(r'\left(', '(').replace(r'\right)', ')')
    s = s.replace(r'\times', '&times;')
    s = s.replace(r'\ge', '&ge;')
    s = s.replace(r'\le', '&le;')
    s = s.replace(r'\Delta', '&Delta;')
    s = s.replace(r'\theta', '&theta;')
    s = s.replace(r'\rightarrow', '&rarr;')
    s = s.replace(r'\sum', '&sum;')

    # sqrt
    while r'\sqrt' in s:
        pos = s.find(r'\sqrt')
        brace_pos = pos + 5
        while brace_pos < len(s) and s[brace_pos].isspace():
            brace_pos += 1
        if brace_pos < len(s) and s[brace_pos] == '{':
            content, end_pos = extract_braced(s, brace_pos)
            if content is not None:
                sub_formatted = format_latex(content)
                rep = f'<span class="sqrt-wrap">&radic;<span class="radicand">{sub_formatted}</span></span>'
                s = s[:pos] + rep + s[end_pos:]
                continue
        break

    # fractions
    s = parse_fractions(s)

    # text
    while r'\text' in s:
        pos = s.find(r'\text')
        brace_pos = pos + 5
        while brace_pos < len(s) and s[brace_pos].isspace():
            brace_pos += 1
        if brace_pos < len(s) and s[brace_pos] == '{':
            content, end_pos = extract_braced(s, brace_pos)
            if content is not None:
                rep = f'<span class="math-text">{content}</span>'
                s = s[:pos] + rep + s[end_pos:]
                continue
        break

    # superscripts
    s = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', s)
    s = re.sub(r'\^([0-9a-zA-Z])', r'<sup>\1</sup>', s)

    # subscripts
    s = re.sub(r'\_\{([^}]+)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'\_([0-9a-zA-Z])', r'<sub>\1</sub>', s)

    return s

def highlight_python_safe(code_text):
    lines = []
    for line in code_text.split('\n'):
        in_single = False
        in_double = False
        comment_idx = -1
        for i, char in enumerate(line):
            if char == "'" and not in_double:
                in_single = not in_single
            elif char == '"' and not in_single:
                in_double = not in_double
            elif char == '#' and not in_single and not in_double:
                comment_idx = i
                break

        if comment_idx != -1:
            code_part = line[:comment_idx]
            comment_part = '<span class="token-com">' + html.escape(line[comment_idx:]) + '</span>'
        else:
            code_part = line
            comment_part = ''

        tokens = []
        last_idx = 0
        for m in re.finditer(r'(\"[^\"]*\"|\'[^\']*\')', code_part):
            if m.start() > last_idx:
                tokens.append(('code', code_part[last_idx:m.start()]))
            tokens.append(('str', m.group(0)))
            last_idx = m.end()
        if last_idx < len(code_part):
            tokens.append(('code', code_part[last_idx:]))

        rendered_code = []
        for t_type, t_val in tokens:
            if t_type == 'str':
                rendered_code.append(f'<span class="token-str">{html.escape(t_val)}</span>')
            else:
                s = html.escape(t_val)
                kw_pattern = r'\b(def|return|if|elif|else|while|for|in|import|from|as|class|try|except|with|True|False|None|break|continue|pass|and|or|not|is|lambda)\b'
                s = re.sub(kw_pattern, r'<span class="token-kw">\1</span>', s)
                fn_pattern = r'\b(print|input|len|type|int|float|str|bool|min|max|sum|range|sorted|list|dict|set|tuple|bin|round|open)\b(?=\s*\()'
                s = re.sub(fn_pattern, r'<span class="token-fn">\1</span>', s)
                s = re.sub(r'\b(0b[01]+|\d+(\.\d+)?)\b', r'<span class="token-num">\1</span>', s)
                rendered_code.append(s)

        lines.append(''.join(rendered_code) + comment_part)
    return '\n'.join(lines)

class LabRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        lang = info.strip().split()[0] if info else 'text'
        if lang == 'python':
            highlighted = highlight_python_safe(code)
            badge_label = 'Python 3'
        else:
            highlighted = html.escape(code)
            badge_label = 'Terminal Output' if lang in ['text', 'shell', 'bash'] else lang.upper()

        return f'''<div class="code-card">
  <div class="code-card-header">
    <div class="code-lang-meta">
      <span class="code-dot"></span>
      <span class="code-lang-label">{badge_label}</span>
    </div>
    <button class="copy-code-btn" onclick="copyCode(this)" title="Copy code snippet" aria-label="Copy code">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
      <span>Copy</span>
    </button>
  </div>
  <pre><code class="language-{lang}">{highlighted}</code></pre>
</div>'''

    def heading(self, text, level, **attrs):
        pts_match = re.search(r'\((\d+)\s*Points?\)', text, re.IGNORECASE)
        pts_badge = ""
        if pts_match:
            pts_val = pts_match.group(1)
            pts_badge = f' <span class="pts-badge">{pts_val} Pts</span>'
            clean_text = re.sub(r'\s*\(\d+\s*Points?\)', '', text, flags=re.IGNORECASE)
        else:
            clean_text = text

        slug = re.sub(r'[^a-zA-Z0-9]+', '-', clean_text).strip('-').lower()
        if level == 1:
            return f'<h1 id="{slug}" class="lab-main-title">{clean_text}</h1>'
        elif level == 2:
            return f'<div class="part-header-wrapper"><h2 id="{slug}" class="lab-part-heading"><span>{clean_text}</span>{pts_badge}</h2></div>'
        elif level == 3:
            return f'<h3 id="{slug}" class="lab-task-heading"><span>{clean_text}</span>{pts_badge}</h3>'
        return f'<h{level} id="{slug}">{text}</h{level}>'

    def table(self, text):
        return f'<div class="table-container"><table class="lab-table">{text}</table></div>'

def render_lab_body(md_text):
    math_store = {}
    math_counter = 0

    # 1. Extract block math
    def repl_block_math(m):
        nonlocal math_counter
        key = f"XYZMATHBLOCK{math_counter}XYZ"
        math_counter += 1
        formatted = format_latex(m.group(0))
        math_store[key] = f'<div class="math-block" role="region" aria-label="Mathematical Formula">{formatted}</div>'
        return f"\n\n{key}\n\n"

    md_text = re.sub(r'\$\$[\s\S]*?\$\$', repl_block_math, md_text)

    # 2. Extract inline math
    def repl_inline_math(m):
        nonlocal math_counter
        key = f"XYZMATHINLINE{math_counter}XYZ"
        math_counter += 1
        formatted = format_latex(m.group(0))
        math_store[key] = f'<span class="math-inline">{formatted}</span>'
        return key

    md_text = re.sub(r'\$[^\$\n]+?\$', repl_inline_math, md_text)

    # 3. Mistune render
    renderer = LabRenderer()
    md = mistune.create_markdown(renderer=renderer, plugins=['table', 'task_lists', 'url', 'strikethrough'])
    html_out = md(md_text)

    # 4. Restore math
    for key, val in math_store.items():
        if "BLOCK" in key:
            html_out = html_out.replace(f'<p>{key}</p>', val)
            html_out = html_out.replace(key, val)
        else:
            html_out = html_out.replace(key, val)

    # 5. Transform fill blanks
    blank_idx = 0
    def repl_blank(m):
        nonlocal blank_idx
        b_id = f"blank_{blank_idx}"
        blank_idx += 1
        return f'<span class="fill-blank" contenteditable="true" spellcheck="false" data-blank-id="{b_id}" data-placeholder="Click to type..."></span>'

    html_out = re.sub(r'(?:\\?_{4,})+', repl_blank, html_out)

    # 6. Preserve print page break
    html_out = html_out.replace('&lt;div style=&quot;page-break-after: always;&quot;&gt;&lt;/div&gt;', '<div class="print-page-break" style="page-break-after: always;"></div>')
    html_out = html_out.replace('<div style="page-break-after: always;"></div>', '<div class="print-page-break" style="page-break-after: always;"></div>')

    return html_out

def build_lab_html(lab_id, meta):
    md_path = meta["md_file"]
    with open(md_path, "r", encoding="utf-8") as f:
        raw_md = f.read()

    body_content = render_lab_body(raw_md)
    deck_no = meta["deck_no"]
    title = meta["title"]
    lectures = meta["lectures"]
    accent_color = meta["color"]
    accent_rgb = meta["color_rgb"]
    md_filename = os.path.basename(md_path)
    presentation_file = meta["presentation_file"]

    toc_items = []
    for match in re.finditer(r'<h2 id="([^"]+)" class="lab-part-heading"><span>([^<]+)</span>', body_content):
        slug = match.group(1)
        heading_text = match.group(2).strip()
        toc_items.append(f'<a href="#{slug}" class="toc-pill">{heading_text}</a>')

    toc_html = '\n        '.join(toc_items) if toc_items else ''

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — CATC Course Portal</title>
  <meta name="description" content="Civil Aviation Training Center (CATC) Python Programming — {title} ({lectures}). Standalone offline HTML lab sheet with interactive student blanks, syntax-highlighted code blocks, and print stylesheet.">

  <style>
    :root {{
      --bg: #0b0d13;
      --bg-surface: #12151f;
      --bg-card: #181d2a;
      --bg-card-hover: #1f2637;
      --border: #242c3d;
      --border-light: rgba(255, 255, 255, 0.08);
      --border-focus: {accent_color};
      --text: #cbd5e1;
      --text-bright: #ffffff;
      --text-dim: #94a3b8;
      
      --accent: {accent_color};
      --accent-rgb: {accent_rgb};
      --cyan: #38bdf8;
      
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
      --shadow-card: 0 4px 14px rgba(0, 0, 0, 0.35);

      /* VS Code Dark+ Syntax Tokens */
      --token-kw: #569cd6;
      --token-var: #9cdcfe;
      --token-num: #b5cea8;
      --token-str: #ce9178;
      --token-com: #6a9955;
      --token-fn: #dcdcaa;
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
      line-height: 1.7;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }}

    ::selection {{
      background: rgba(var(--accent-rgb), 0.35);
      color: #ffffff;
    }}

    :focus-visible {{
      outline: 2px solid var(--accent);
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

    /* Top Sticky Navigation Header */
    header.lab-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 13, 19, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-light);
    }}

    .nav-container {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .nav-left {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      color: var(--text-dim);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      padding: 0.35rem 0.65rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      background: var(--bg-surface);
      transition: color 0.15s ease, background 0.15s ease, border-color 0.15s ease;
    }}

    .back-btn:hover {{
      color: var(--text-bright);
      border-color: rgba(255, 255, 255, 0.25);
      background: rgba(255, 255, 255, 0.05);
    }}

    .nav-title-group {{
      display: flex;
      flex-direction: column;
    }}

    .nav-badge-row {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .deck-badge {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.1rem 0.45rem;
      border-radius: 4px;
      background: rgba(var(--accent-rgb), 0.15);
      color: var(--accent);
      border: 1px solid rgba(var(--accent-rgb), 0.3);
    }}

    .nav-page-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-bright);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 420px;
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .action-btn {{
      font-size: 0.82rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
      color: var(--text);
      text-decoration: none;
      white-space: nowrap;
      cursor: pointer;
      transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
    }}

    .action-btn:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.25);
      color: var(--text-bright);
    }}

    .action-btn.primary {{
      background: rgba(var(--accent-rgb), 0.12);
      border-color: rgba(var(--accent-rgb), 0.35);
      color: var(--accent);
    }}

    .action-btn.primary:hover {{
      background: var(--accent);
      border-color: var(--accent);
      color: #0b0d13;
    }}

    /* Table of Contents Jump Bar */
    .lab-toc {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-light);
      padding: 0.5rem 1.5rem;
    }}

    .toc-container {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      overflow-x: auto;
      scrollbar-width: thin;
      padding-bottom: 2px;
    }}

    .toc-label {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      white-space: nowrap;
      margin-right: 0.35rem;
    }}

    .toc-pill {{
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-dim);
      text-decoration: none;
      padding: 0.2rem 0.6rem;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border);
      white-space: nowrap;
      transition: color 0.15s ease, border-color 0.15s ease, background 0.15s ease;
    }}

    .toc-pill:hover {{
      color: var(--text-bright);
      border-color: var(--accent);
      background: rgba(var(--accent-rgb), 0.08);
    }}

    /* Main Container */
    main.lab-content {{
      flex: 1;
      max-width: 900px;
      margin: 0 auto;
      padding: 2.75rem 1.5rem 5rem;
      width: 100%;
    }}

    /* Document Main Title */
    .lab-main-title {{
      font-size: clamp(1.8rem, 3.5vw, 2.35rem);
      font-weight: 800;
      color: var(--text-bright);
      line-height: 1.25;
      letter-spacing: -0.02em;
      margin-bottom: 1.5rem;
      border-bottom: 2px solid var(--border);
      padding-bottom: 1rem;
    }}

    /* Section Headings */
    .part-header-wrapper {{
      margin-top: 3rem;
      margin-bottom: 1.25rem;
      border-left: 4px solid var(--accent);
      padding-left: 1rem;
    }}

    .lab-part-heading {{
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--text-bright);
      letter-spacing: -0.015em;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .lab-task-heading {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-bright);
      margin-top: 1.85rem;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      border-bottom: 1px dashed var(--border);
      padding-bottom: 0.4rem;
    }}

    .pts-badge {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 0.15rem 0.55rem;
      border-radius: 4px;
      background: rgba(var(--accent-rgb), 0.14);
      color: var(--accent);
      border: 1px solid rgba(var(--accent-rgb), 0.28);
      font-variant-numeric: tabular-nums;
      flex-shrink: 0;
    }}

    p {{
      margin-bottom: 1.1rem;
      color: var(--text);
    }}

    ul, ol {{
      margin-bottom: 1.25rem;
      padding-left: 1.6rem;
    }}

    li {{
      margin-bottom: 0.5rem;
    }}

    hr {{
      border: 0;
      border-top: 1px solid var(--border);
      margin: 2.5rem 0;
    }}

    strong {{
      color: var(--text-bright);
      font-weight: 700;
    }}

    /* Inline Code */
    code:not([class*="language-"]) {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.88em;
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--cyan);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
    }}

    /* Code Card Component */
    .code-card {{
      background: #181d2a;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin: 1.25rem 0;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}

    .code-card-header {{
      background: #12151f;
      border-bottom: 1px solid var(--border);
      padding: 0.45rem 0.85rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .code-lang-meta {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .code-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--accent);
    }}

    .code-lang-label {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .copy-code-btn {{
      font-size: 0.72rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-dim);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      cursor: pointer;
      transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
    }}

    .copy-code-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--border);
      color: var(--text-bright);
    }}

    .code-card pre {{
      padding: 1rem 1.15rem;
      margin: 0;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #d4d4d4;
    }}

    /* VS Code Syntax Colors */
    .token-kw {{ color: var(--token-kw); font-weight: 600; }}
    .token-var {{ color: var(--token-var); }}
    .token-num {{ color: var(--token-num); }}
    .token-str {{ color: var(--token-str); }}
    .token-com {{ color: var(--token-com); font-style: italic; }}
    .token-fn {{ color: var(--token-fn); }}

    /* Table Component */
    .table-container {{
      width: 100%;
      overflow-x: auto;
      margin: 1.25rem 0;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--bg-card);
    }}

    .lab-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }}

    .lab-table th {{
      background: var(--bg-surface);
      color: var(--text-bright);
      font-weight: 700;
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border);
      letter-spacing: -0.01em;
    }}

    .lab-table td {{
      padding: 0.7rem 1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: var(--text);
    }}

    .lab-table tr:last-child td {{
      border-bottom: 0;
    }}

    .lab-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}

    /* Mathematical Formulas */
    .math-block {{
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.15rem 1.5rem;
      margin: 1.35rem 0;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      font-family: "Cambria Math", "STIX Two Math", "KaTeX_Math", "Times New Roman", serif;
      font-size: 1.2rem;
      color: var(--accent);
      overflow-x: auto;
    }}

    .math-inline {{
      font-family: "Cambria Math", "STIX Two Math", "KaTeX_Math", "Times New Roman", serif;
      font-size: 1.05em;
      color: var(--accent);
      padding: 0 0.2em;
    }}

    .frac {{
      display: inline-flex;
      flex-direction: column;
      vertical-align: middle;
      text-align: center;
      padding: 0 0.35em;
      font-size: 0.92em;
      line-height: 1.15;
    }}

    .num {{
      border-bottom: 1.5px solid currentColor;
      padding-bottom: 2px;
    }}

    .den {{
      padding-top: 2px;
    }}

    .sqrt-wrap {{
      display: inline-flex;
      align-items: baseline;
      padding: 0 0.2em;
    }}

    .radicand {{
      border-top: 1.5px solid currentColor;
      padding-top: 1px;
      margin-left: 1px;
    }}

    .math-text {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-style: normal;
      font-size: 0.92em;
      color: var(--text-bright);
    }}

    /* Interactive Fill Blanks */
    .fill-blank {{
      display: inline-block;
      min-width: 140px;
      border-bottom: 1.5px dashed var(--accent);
      padding: 0 0.4rem;
      margin: 0 0.2rem;
      color: var(--text-bright);
      background: rgba(var(--accent-rgb), 0.06);
      border-radius: 2px;
      outline: none;
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 0.95em;
      transition: background 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
      cursor: text;
    }}

    .fill-blank:empty::before {{
      content: attr(data-placeholder);
      color: var(--text-dim);
      font-style: italic;
      font-size: 0.85em;
      pointer-events: none;
    }}

    .fill-blank:focus {{
      background: rgba(var(--accent-rgb), 0.18);
      border-bottom-style: solid;
      box-shadow: 0 0 0 2px rgba(var(--accent-rgb), 0.25);
    }}

    .print-page-break {{
      height: 0;
      margin: 0;
      padding: 0;
      border: 0;
    }}

    /* Floating Save Status Toast */
    .save-toast {{
      position: fixed;
      bottom: 1.5rem;
      right: 1.5rem;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 0.5rem 0.85rem;
      font-size: 0.78rem;
      color: var(--text-dim);
      box-shadow: var(--shadow-card);
      display: flex;
      align-items: center;
      gap: 0.4rem;
      opacity: 0;
      transform: translateY(10px);
      transition: opacity 0.25s ease, transform 0.25s ease;
      pointer-events: none;
      z-index: 90;
    }}

    .save-toast.visible {{
      opacity: 1;
      transform: translateY(0);
    }}

    .save-toast-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--accent);
    }}

    /* Footer */
    footer.lab-footer {{
      margin-top: auto;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-light);
      padding: 1.75rem 1.5rem;
      color: var(--text-dim);
      font-size: 0.82rem;
    }}

    .footer-content {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .nav-page-title {{
        display: none;
      }}
      main.lab-content {{
        padding: 1.75rem 1rem 4rem;
      }}
    }}

    /* PRINT STYLESHEET (Clean white ink-friendly handout for printing/PDF) */
    @media print {{
      @page {{
        size: A4 portrait;
        margin: 15mm 15mm 20mm 15mm;
      }}

      body {{
        background: #ffffff !important;
        color: #111111 !important;
        font-size: 10pt;
        line-height: 1.5;
      }}

      header.lab-nav,
      nav.lab-toc,
      .copy-code-btn,
      .save-toast,
      footer.lab-footer {{
        display: none !important;
      }}

      main.lab-content {{
        padding: 0 !important;
        max-width: 100% !important;
      }}

      .lab-main-title {{
        color: #000000 !important;
        font-size: 18pt !important;
        border-bottom: 2px solid #333333 !important;
        margin-bottom: 12pt !important;
        padding-bottom: 6pt !important;
      }}

      .part-header-wrapper {{
        border-left: 4px solid #333333 !important;
        margin-top: 18pt !important;
        margin-bottom: 8pt !important;
      }}

      .lab-part-heading {{
        color: #000000 !important;
        font-size: 13pt !important;
      }}

      .lab-task-heading {{
        color: #111111 !important;
        font-size: 11pt !important;
        border-bottom: 1px solid #cccccc !important;
        margin-top: 12pt !important;
      }}

      .pts-badge {{
        background: #eeeeee !important;
        color: #222222 !important;
        border: 1px solid #999999 !important;
      }}

      .code-card {{
        background: #f8f9fa !important;
        border: 1px solid #cccccc !important;
        box-shadow: none !important;
        break-inside: avoid;
      }}

      .code-card-header {{
        background: #eeeeee !important;
        border-bottom: 1px solid #cccccc !important;
      }}

      .code-card pre {{
        color: #222222 !important;
        font-size: 8.5pt !important;
      }}

      .token-kw {{ color: #0000bb !important; font-weight: bold; }}
      .token-var {{ color: #222222 !important; }}
      .token-num {{ color: #098658 !important; }}
      .token-str {{ color: #a31515 !important; }}
      .token-com {{ color: #008000 !important; font-style: italic; }}
      .token-fn {{ color: #795e26 !important; }}

      .table-container {{
        background: #ffffff !important;
        border: 1px solid #333333 !important;
        break-inside: avoid;
      }}

      .lab-table th {{
        background: #f0f0f0 !important;
        color: #000000 !important;
        border-bottom: 1px solid #333333 !important;
      }}

      .lab-table td {{
        border-bottom: 1px solid #dddddd !important;
        color: #111111 !important;
      }}

      .math-block {{
        background: #fdfdfd !important;
        border: 1px solid #cccccc !important;
        color: #111111 !important;
        font-size: 11pt !important;
        break-inside: avoid;
      }}

      .math-inline {{
        color: #111111 !important;
      }}

      .fill-blank {{
        background: transparent !important;
        border-bottom: 1.5px solid #222222 !important;
        color: #000000 !important;
        min-width: 120px !important;
      }}

      .fill-blank:empty::before {{
        display: none !important;
      }}

      .print-page-break {{
        page-break-after: always !important;
        break-after: page !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="lab-nav">
    <div class="nav-container">
      <div class="nav-left">
        <a href="../index.html" class="back-btn" title="Return to Course Mind Map Portal">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"></polyline></svg>
          <span>Portal</span>
        </a>
        <div class="nav-title-group">
          <div class="nav-badge-row">
            <span class="deck-badge">Deck {deck_no}</span>
            <span class="deck-badge" style="background: rgba(255,255,255,0.06); color: var(--text-dim); border-color: var(--border);">{lectures}</span>
          </div>
          <span class="nav-page-title">{title}</span>
        </div>
      </div>

      <div class="nav-actions">
        <a href="{presentation_file}" class="action-btn" title="Launch companion presentation slides">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
          <span>Slides</span>
        </a>
        <button onclick="window.print()" class="action-btn primary" title="Print document or save as PDF">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          <span>Print / PDF</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Table of Contents Quick Navigation -->
  <nav class="lab-toc" aria-label="Table of Contents Quick Jump">
    <div class="toc-container">
      <span class="toc-label">Jump to:</span>
      {toc_html}
    </div>
  </nav>

  <!-- Main Document Content -->
  <main class="lab-content">
{body_content}
  </main>

  <!-- Auto-Save Toast Feedback -->
  <div id="save-toast" class="save-toast" aria-live="polite">
    <div class="save-toast-dot"></div>
    <span>Answer autosaved</span>
  </div>

  <!-- Footer -->
  <footer class="lab-footer">
    <div class="footer-content">
      <div>&copy; 2026 Civil Aviation Training Center (CATC). Department of Aviation Engineering.</div>
      <div>100% Offline Capable &bull; Standalone HTML5 Laboratory Sheets (Source: Markdown)</div>
    </div>
  </footer>

  <script>
    // Copy code snippet helper
    function copyCode(btn) {{
      const card = btn.closest('.code-card');
      const code = card.querySelector('code');
      if (code) {{
        navigator.clipboard.writeText(code.innerText).then(() => {{
          const original = btn.innerHTML;
          btn.innerHTML = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> <span style="color:#34d399">Copied!</span>';
          setTimeout(() => {{
            btn.innerHTML = original;
          }}, 1800);
        }}).catch(err => console.error('Copy failed:', err));
      }}
    }}

    // LocalStorage Auto-Save for student fill blanks
    document.addEventListener('DOMContentLoaded', () => {{
      const storageKey = 'catc_lab_0{deck_no}_answers';
      const blanks = document.querySelectorAll('.fill-blank');
      const toast = document.getElementById('save-toast');
      let toastTimer = null;

      // Restore saved answers
      try {{
        const saved = JSON.parse(localStorage.getItem(storageKey) || '{{}}');
        blanks.forEach(b => {{
          const id = b.dataset.blankId;
          if (id && saved[id]) {{
            b.innerText = saved[id];
          }}
        }});
      }} catch (e) {{
        console.warn('LocalStorage access restricted:', e);
      }}

      // Auto-save on input
      function saveAnswers() {{
        try {{
          const state = {{}};
          blanks.forEach(b => {{
            const id = b.dataset.blankId;
            if (id && b.innerText.trim()) {{
              state[id] = b.innerText;
            }}
          }});
          localStorage.setItem(storageKey, JSON.stringify(state));
          
          if (toast) {{
            toast.classList.add('visible');
            clearTimeout(toastTimer);
            toastTimer = setTimeout(() => {{
              toast.classList.remove('visible');
            }}, 1400);
          }}
        }} catch (e) {{
          console.warn('Could not save to localStorage:', e);
        }}
      }}

      blanks.forEach(b => {{
        b.addEventListener('input', saveAnswers);
      }});
    }});
  </script>
</body>
</html>
'''
    return full_html

def build_all_labs():
    print("Building all 5 CATC Laboratory Exercise HTML documents from Markdown sources...")
    for lab_id, meta in sorted(LAB_METADATA.items()):
        html_content = build_lab_html(lab_id, meta)
        out_path = meta["html_file"]
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  [OK] Generated {out_path} ({len(html_content)} bytes)")
    print("All 5 laboratory exercise HTML documents compiled successfully!")

if __name__ == "__main__":
    build_all_labs()
