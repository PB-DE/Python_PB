# Unified Python Lecture Slides (L01 & L02) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single, self-contained, lightweight HTML presentation slide deck (`python_presentation.html`) in the Modern Dark VS Code style that combines all curriculum content from `L01.ipynb` and `L02.ipynb`.

**Architecture:** A pure single-file HTML5/CSS3/Vanilla JS presentation deck. The slide engine uses a minimalist state manager driven by keyboard events and URL hash routing, with centered 16:9 slide views, precise VS Code Dark+ syntax highlighting, and custom embedded vector SVGs for architecture and memory diagrams.

**Tech Stack:** HTML5, CSS3 (Flexbox/Grid, CSS custom properties), Vanilla JavaScript, SVG, Node.js (for automated test assertion), Chrome/Browser for visual verification.

**Spec:** [`docs/superpowers/specs/2026-10-12-python-lecture-slides-design.md`](file:///Users/phanuphong/Library/CloudStorage/OneDrive-catc.or.th/CATC%20Courses/python/Presentation/docs/superpowers/specs/2026-10-12-python-lecture-slides-design.md)

## Global Constraints

- **Single Portable File:** All HTML, CSS, JavaScript, and SVG assets must reside in `python_presentation.html` with zero external dependencies (no CDNs, no web fonts requiring internet).
- **VS Code Dark+ Palette:** Canvas `#1e1e1e`, panel `#252526`, border `#333333`, keywords `#569cd6`, variables/identifiers `#9cdcfe`, numbers `#b5cea8`, strings `#ce9178`, comments `#6a9955`, functions `#dcdcaa`.
- **No Chapter Bar:** No header navigation bars or persistent chapter banners on screen.
- **No Interactive Runner:** Pure slide viewing engine with no Python Wasm/Pyodide execution overhead.
- **Aspect Ratio:** Fixed 16:9 proportional stage auto-centered across all viewport resolutions.

## Review Focus

1. **Missing External Assets in Offline Environment:** Slide deck opened without internet must render all icons, fonts, and diagrams without broken asset boxes.
2. **Keyboard Trapping & Edge Transitions:** Pressing `ArrowLeft` on slide 1 must remain on slide 1 (no out-of-bounds error), and `ArrowRight` on the last slide must gracefully stop at the last slide.
3. **URL Hash Navigation on Direct Load:** Opening `python_presentation.html#slide-22` directly in browser must navigate directly to slide 22 and update the counter accurately.
4. **Code Overflow on Projectors:** Long code lines or multiple lines must not cause vertical or horizontal blowout of the 16:9 slide canvas.
5. **Fullscreen Key Compatibility:** Pressing `F` must toggle fullscreen cleanly across Chrome, Safari, and Firefox without disrupting presentation state.

---

### Task 1: Presentation Engine Core, Theming, and Test Scaffolder

**Files:**
- Create: `tests/verify_presentation.js`
- Create: `python_presentation.html`

**Interfaces:**
- Consumes: None
- Produces: Base HTML shell with `<div id="deck">`, CSS stylesheet with VS Code Dark+ tokens, slide engine `SlideDeck` object with `goTo(index)`, `next()`, `prev()`, and keyboard listener bindings.

- [ ] **Step 1: Write verification script `tests/verify_presentation.js`**
Write a Node.js verification test that checks:
- `python_presentation.html` exists and is non-empty.
- Zero external `<link href="http...>` or `<script src="http...">` tags exist.
- `#deck` container and `.slide` elements are present.
- Keyboard navigation logic (`ArrowRight`, `ArrowLeft`, `Space`, `KeyF`) exists.
- VS Code Dark+ CSS tokens are defined.

- [ ] **Step 2: Run test to verify it fails**
Run: `node tests/verify_presentation.js`  
Expected: FAIL (file does not exist or missing structure).

- [ ] **Step 3: Implement Core Engine in `python_presentation.html`**
Implement the presentation foundation:
- CSS tokens: `--bg: #1e1e1e`, `--code-bg: #252526`, `--text: #d4d4d4`, `--kw: #569cd6`, `--var: #9cdcfe`, `--num: #b5cea8`, `--str: #ce9178`, `--com: #6a9955`.
- 16:9 Stage scaling and layout system (`display: none` / `.active` transition with 120ms fade).
- Slide footer with discreet slide number (`Slide X / Total`) and progress bar.
- Lightweight JavaScript engine (~80 lines): keyboard events, touch events, hash change handler, and fullscreen handler.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation.js`  
Expected: PASS for Task 1 requirements.

- [ ] **Step 5: Commit**
```bash
git add tests/verify_presentation.js python_presentation.html
git commit -m "feat: presentation engine core and VS Code Dark+ theme scaffolding"
```

---

### Task 2: Lecture 1 Content & Embedded Vector Diagrams

**Files:**
- Modify: `tests/verify_presentation.js` (add assertions for L01 topics and diagrams)
- Modify: `python_presentation.html`

**Interfaces:**
- Consumes: Core engine and slide layout from Task 1.
- Produces: 15 complete slides for Lecture 1 (Fundamentals of Computing) with embedded SVGs for Computer Architecture, Shallow vs Deep Memory Copy, and Moore's Law Curve.

- [ ] **Step 1: Update `tests/verify_presentation.js` with L01 content checks**
Add assertions verifying:
- Lecture 1 title slide exists.
- Binary calculation formulas ($1010_2 = 10_{10}$) present.
- Computer Architecture inline `<svg>` exists with CPU, RAM, and Bus components.
- Shallow vs Deep Copy inline `<svg>` exists with memory pointer references.
- Moore's Law exponential curve inline `<svg>` exists.
- NumPy / Matplotlib code snippets for transistor plotting are formatted.

- [ ] **Step 2: Run test to verify it fails**
Run: `node tests/verify_presentation.js`  
Expected: FAIL (L01 slides and SVGs missing).

- [ ] **Step 3: Implement Lecture 1 Slides in `python_presentation.html`**
Transcribe and design all 15 Lecture 1 slides:
- Slide 1: Course Title & Lecture 1 Title (*Fundamentals of Computing* - CATC).
- Slide 2: Representation with Numbers (Speech, images, text, binary reality).
- Slide 3: What is a Number? (Base-10 positional notation).
- Slide 4: Binary Representation (Base-2, bits, 4-bit representation, bit limits).
- Slide 5: Equality vs. Assignment ($x = 2$ vs $x \leftarrow 2$).
- Slide 6: Data Hierarchy (Bit $\to$ Character $\to$ Field $\to$ Record $\to$ Database).
- Slide 7: Basic Computer Architecture (High-resolution inline vector SVG diagram).
- Slide 8: What Do Computers Do? (Voltages, instruction execution, binary arithmetic).
- Slide 9: Moore's Law (Exponential growth, doubling period, cost reduction).
- Slide 10: Levels of Programming Languages (Machine $\to$ Assembly $\to$ High-Level $\to$ Python).
- Slide 11: Shallow vs. Deep Copy (Inline SVG memory pointer diagram).
- Slide 12: Object-Oriented Programming (Objects, attributes, methods, Bank Account).
- Slide 13: Operating Systems (Concurrency, Windows, Linux, macOS, iOS, Android).
- Slide 14: Why Python? (Readability, high-level, batteries included, industry standard).
- Slide 15: Case Study: Plotting Moore's Law with NumPy & Matplotlib (code + SVG curve).

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation.js`  
Expected: PASS for L01 assertions.

- [ ] **Step 5: Commit**
```bash
git add tests/verify_presentation.js python_presentation.html
git commit -m "feat: complete Lecture 1 slides and vector diagrams"
```

---

### Task 3: Lecture 2 Content & VS Code Syntax Token Highlighting

**Files:**
- Modify: `tests/verify_presentation.js` (add assertions for L02 topics, code blocks, and syntax tokens)
- Modify: `python_presentation.html`

**Interfaces:**
- Consumes: Slide engine and theming from Tasks 1 & 2.
- Produces: Title transition slide and 20 complete slides for Lecture 2 (Intro to Python Programming) with accurate syntax tokens and outputs.

- [ ] **Step 1: Update `tests/verify_presentation.js` with L02 assertions**
Add assertions verifying:
- Lecture 2 title transition card exists.
- All code blocks have VS Code Dark+ syntax classes (`.token-kw`, `.token-var`, `.token-num`, `.token-str`, `.token-com`, `.token-fn`).
- Precedence rules and parentheses ambiguity examples (`2 ** 3 ** 4`) present.
- String newline escape example and user input with `type()` present.
- Boolean expressions, `if` branching with indentation note, and `min()`/`max()` present.
- Total slide count $\ge 35$.

- [ ] **Step 2: Run test to verify it fails**
Run: `node tests/verify_presentation.js`  
Expected: FAIL (L02 slides missing).

- [ ] **Step 3: Implement Lecture 2 Slides in `python_presentation.html`**
Transcribe and format all Lecture 2 slides:
- Slide 16: Lecture 2 Transition (*Intro to Python Programming*).
- Slide 17: Expressions & Statements.
- Slide 18: Assignment & Identifiers (`x = 2`).
- Slide 19: Adding Two Integers & PEP 8 Spacing (`x = 45`, `y = 36`, `z = x + y`).
- Slide 20: Variable Naming Rules & Invalid Names (`123_xyz` SyntaxError).
- Slide 21: Data Types & `type()` Function (`int`, `float`).
- Slide 22: Arithmetic Operations: Basic (`+`, `-`, `*`, `/`).
- Slide 23: Arithmetic Operations: Advanced (`**`, `//`, `%`).
- Slide 24: Operator Precedence Rules (Order of operations summary table).
- Slide 25: Parentheses & Associativity (`2 ** 3 ** 4` right-to-left evaluation).
- Slide 26: Strings (`str`), Printing & Newline Escapes (`\n`).
- Slide 27: Obtaining User Input (`input()`, always string type).
- Slide 28: Casting Data Types (`int()` and `float()` conversions).
- Slide 29: Boolean Expressions & Relational Operators (`>`, `<`, `==`, `!=`).
- Slide 30: Conditional Execution (`if` statement, colon, indentation).
- Slide 31: Comments & Documentation (`#`).
- Slide 32: Variables, Values, and Objects (Object model).
- Slide 33: Dynamic Typing in Action (`x / y` produces float).
- Slide 34: Basic Descriptive Statistics (`min()`, `max()`).
- Slide 35: Course Summary & Next Steps.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation.js`  
Expected: PASS for all tests.

- [ ] **Step 5: Commit**
```bash
git add tests/verify_presentation.js python_presentation.html
git commit -m "feat: complete Lecture 2 slides with VS Code Dark+ syntax highlighting"
```

---

### Task 4: End-to-End Verification & Browser Validation

**Files:**
- Create: `tests/e2e_check.js`
- Test: In-browser validation via `browser_subagent`

**Interfaces:**
- Consumes: Complete `python_presentation.html`.
- Produces: Verified presentation with confirmed keyboard responsiveness, correct slide counter progression, hash URL navigation, and clean responsive rendering.

- [ ] **Step 1: Write and run `tests/e2e_check.js`**
Run automated node script verifying:
- HTML5 doctype and syntax closure.
- Slide ID uniqueness (`id="slide-1"` through `id="slide-35"`).
- Zero broken images (`<img src="...">` without inline data).
- File size under 250KB for ultra-fast loading.

- [ ] **Step 2: Run browser validation using `browser_subagent`**
Launch browser subagent to:
- Open `file:///Users/phanuphong/Library/CloudStorage/OneDrive-catc.or.th/CATC Courses/python/Presentation/python_presentation.html`.
- Verify initial slide 1 display and slide counter `1 / 35`.
- Press `ArrowRight` to advance to slide 2, verify slide change and counter update.
- Navigate to slide 7 to verify the Computer Architecture SVG diagram renders crisply.
- Navigate to slide 19 to verify the VS Code Dark+ code box displays properly.
- Verify fullscreen key response.

- [ ] **Step 3: Document and finalize**
Ensure all tests pass and record verification evidence.
