# Unified Python Lecture Slides (L07 & L08) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single, self-contained, lightweight HTML presentation slide deck (`python_presentation_04.html`) in the established Modern Dark VS Code style that combines all curriculum content from `L07.ipynb` (NumPy Arrays) and `L08.ipynb` (Strings & Regular Expressions).

**Architecture:** Identical presentation engine to `python_presentation_01.html`, `python_presentation_02.html`, and `python_presentation_03.html`: pure single-file HTML5/CSS3/Vanilla JS with 16:9 widescreen stage, VS Code Dark+ syntax highlighting, discreet progress bar and slide counter, zero persistent headers, and custom embedded vector SVGs for memory layout and string processing pipelines.

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript, SVG, Node.js (automated verification), Chrome/Browser subagent.

## Global Constraints

- **File Name:** Output file must be `python_presentation_04.html`.
- **Zero External Dependencies:** 100% self-contained offline deck with no CDN or remote font dependencies.
- **VS Code Dark+ Palette:** Canvas `#1e1e1e`, code background `#252526`, border `#333333`, keywords `#569cd6`, variables `#9cdcfe`, numbers `#b5cea8`, strings `#ce9178`, comments `#6a9955`, functions `#dcdcaa`.
- **Footer:** `Civil Aviation Training Center (CATC)` (clean branding without "Computer Science").
- **Navigation:** Arrow keys, Space, PageUp/PageDown, Home, End, `F` for fullscreen, URL hash navigation.
- **Total Slides:** Exactly 36 slides (18 for Lecture 7 + 18 for Lecture 8).

---

### Task 1: Scaffolding Deck & Test Suite for Presentation 04

**Files:**
- Create: `tests/verify_presentation_04.js`
- Create: `python_presentation_04.html`

- [ ] **Step 1: Write `tests/verify_presentation_04.js`**
Assert file existence, zero CDN links, `#deck` container, VS Code Dark+ CSS tokens, keyboard event listeners, and footer text `Civil Aviation Training Center (CATC)` (no "Computer Science").

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_04.js`
Expected: FAIL (file does not exist).

- [ ] **Step 3: Implement core structure in `python_presentation_04.html` (GREEN)**
Set up the identical engine and stylesheet with title slide for Lectures 7 & 8.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_04.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit message: `feat: scaffold Presentation 04 engine and test suite`

---

### Task 2: Lecture 7 Content & NumPy Vector Memory Diagrams (Slides 1–18)

**Files:**
- Modify: `tests/verify_presentation_04.js`
- Modify: `python_presentation_04.html`

- [ ] **Step 1: Update `tests/verify_presentation_04.js` with L07 assertions**
Add assertions for:
- Lecture 7 title & topics
- 1D vs 2D arrays (`np.array`)
- `dtype`, `ndim`, `shape`, `size`
- Vector SVG memory diagram (Python List vs NumPy ndarray)
- Array generators: `zeros`, `ones`, `full`, `arange`, `linspace`
- `.reshape()`
- Element-wise arithmetic & scalar broadcasting
- Relational operators & boolean masks
- Aggregations: `.sum()`, `axis=0`, `axis=1`
- Multidimensional slicing (`arr[0:2, :]`, `arr[:, -1]`)
- Transpose (`np.transpose(arr)`, `.T`)
- Slide count >= 18

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_04.js`
Expected: FAIL.

- [ ] **Step 3: Implement Lecture 7 slides with VS Code code boxes and vector memory diagram SVG (GREEN)**
Add slides 2 through 18 with accurate output boxes and embedded vector diagram.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_04.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit message: `feat: complete Lecture 7 slides and vector memory diagram`

---

### Task 3: Lecture 8 Content & String Tokenization/Regex Pipeline (Slides 19–36)

**Files:**
- Modify: `tests/verify_presentation_04.js`
- Modify: `python_presentation_04.html`

- [ ] **Step 1: Update `tests/verify_presentation_04.js` with L08 assertions**
Add assertions for:
- Lecture 8 title & Strings
- f-strings formatting (`:d`, `:c`, `:.2f`, `:.2e`, `:10f`)
- Immutability, concatenation, repetition (`*`)
- `.strip()`, `.lower()`, `.upper()`
- `.count()`, `.find()`, `in`
- `.replace()`
- `.split()`, `.join()`
- Vector SVG for Tokenization & Join pipeline
- `.splitlines()`
- `import re`, `re.fullmatch()`, zip codes, twitter handles, character classes
- Total slide count === 36

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_04.js`
Expected: FAIL.

- [ ] **Step 3: Implement Lecture 8 slides and vector diagram (GREEN)**
Add slides 19 through 36 with accurate code examples and vector pipeline diagram.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_04.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit message: `feat: complete Lecture 8 slides with regex and tokenization pipeline`

---

### Task 4: End-to-End Verification & Browser Validation

**Files:**
- Create: `tests/e2e_check_04.js`
- Test: `python_presentation_04.html`

- [ ] **Step 1: Write and run `tests/e2e_check_04.js`**
Verify:
- File size < 250 KB
- Exactly 36 slides with balanced `<section>` tags
- Zero external CDNs/fonts
- Zero broken images
- At least 2 inline SVGs
- Clean branding in footer

- [ ] **Step 2: Run browser validation using `browser_subagent`**
Verify:
- Initial load on slide 1
- Navigation to slide 6 (NumPy memory layout)
- Navigation to slide 19 (Lecture 8 title)
- Navigation to slide 30 (String tokenization pipeline)
- Navigation to slide 36 (Summary matrix and counter `36 / 36`)

- [ ] **Step 3: Document and finalize**
Commit message: `test: add E2E verification suite for presentation 04`
Update task checklist and present results to user.
