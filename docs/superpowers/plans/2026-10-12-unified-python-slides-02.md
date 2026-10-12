# Unified Python Lecture Slides (L03 & L04) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single, self-contained, lightweight HTML presentation slide deck (`python_presentation_02.html`) in the established Modern Dark VS Code style that combines all curriculum content from `L03.ipynb` and `L04.ipynb`.

**Architecture:** Identical presentation engine to `python_presentation_01.html`: pure single-file HTML5/CSS3/Vanilla JS with 16:9 widescreen stage, VS Code Dark+ syntax highlighting, discreet progress bar and slide counter, zero persistent headers, and custom embedded vector SVGs for algorithmic flowcharts and variable scope diagrams.

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript, SVG, Node.js (automated verification), Chrome/Browser subagent.

**Spec:** Follows established design in [`docs/superpowers/specs/2026-10-12-python-lecture-slides-design.md`](file:///Users/phanuphong/Library/CloudStorage/OneDrive-catc.or.th/CATC%20Courses/python/Presentation/docs/superpowers/specs/2026-10-12-python-lecture-slides-design.md).

## Global Constraints

- **File Name:** Output file must be `python_presentation_02.html`.
- **Zero External Dependencies:** 100% self-contained offline deck with no CDN or remote font dependencies.
- **VS Code Dark+ Palette:** Canvas `#1e1e1e`, code background `#252526`, border `#333333`, keywords `#569cd6`, variables `#9cdcfe`, numbers `#b5cea8`, strings `#ce9178`, comments `#6a9955`, functions `#dcdcaa`.
- **Footer:** `Civil Aviation Training Center (CATC)` (clean branding without "Computer Science").
- **Navigation:** Arrow keys, Space, PageUp/PageDown, Home, End, `F` for fullscreen, URL hash navigation.

---

### Task 1: Scaffolding Deck & Test Suite for Presentation 02

**Files:**
- Create: `tests/verify_presentation_02.js`
- Create: `python_presentation_02.html`

- [ ] **Step 1: Write `tests/verify_presentation_02.js`**
Assert file existence, zero CDN links, `#deck` container, VS Code Dark+ CSS tokens, keyboard event listeners, and footer text `Civil Aviation Training Center (CATC)`.

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_02.js`
Expected: FAIL (file does not exist).

- [ ] **Step 3: Implement core structure in `python_presentation_02.html` (GREEN)**
Set up the identical engine and stylesheet with title slide for Lecture 3 & 4.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_02.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit Task 1 changes.

---

### Task 2: Lecture 3 Content & Flowchart Diagrams

**Files:**
- Modify: `tests/verify_presentation_02.js` (add assertions for L03 topics)
- Modify: `python_presentation_02.html`

- [ ] **Step 1: Update `tests/verify_presentation_02.js` with L03 assertions**
Assert Lecture 3 topics: algorithms & pseudocode, selection statements (`if`, `if-else`, `if-elif-else`), truthiness, indentation suite, ternary expressions, `while` loop with f-string formatting, `for` loops & `range()`, lists & iterables, augmented assignment (`+=`, `*=`), Fibonacci algorithm development (requirements, 3 stages, refinements), `break` and `continue`, boolean operators (`and`, `or`, `not`), `statistics` module (mean, median, mode), and inline vector flowchart SVG.

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_02.js`
Expected: FAIL (L03 content missing).

- [ ] **Step 3: Implement Lecture 3 Slides in `python_presentation_02.html` (GREEN)**
Assemble slides 1 through 18 for Lecture 3 with VS Code code boxes and vector flowchart.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_02.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit Task 2 changes.

---

### Task 3: Lecture 4 Content & Scope Diagrams

**Files:**
- Modify: `tests/verify_presentation_02.js` (add assertions for L04 topics)
- Modify: `python_presentation_02.html`

- [ ] **Step 1: Update `tests/verify_presentation_02.js` with L04 assertions**
Assert Lecture 4 topics: functions definition (`def`), inputs & return values, `get_pi()` without arguments, `get_bmi()` with multiple arguments, `random` module & pseudo-random generation (`random()`, `randrange()`), dice simulation, returning multiple values with tuples and unpacking, Python modules & Standard Library, `math.sqrt()`, default parameter values (`h=1.7`), keyword arguments, object methods (`upper()`), variable scope (local vs global, `NameError`), modifying globals & `global` keyword, pass-by-reference object model, and inline vector scope diagram. Total slides $\ge 35$.

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_02.js`
Expected: FAIL (L04 content missing).

- [ ] **Step 3: Implement Lecture 4 Slides in `python_presentation_02.html` (GREEN)**
Assemble slides 19 through 36 with full code blocks, outputs, and scope diagram.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_02.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit Task 3 changes.

---

### Task 4: End-to-End Verification & Browser Validation

**Files:**
- Create: `tests/e2e_check_02.js`
- Test: In-browser validation via `browser_subagent`

- [ ] **Step 1: Write and run `tests/e2e_check_02.js`**
Assert well-formed HTML, 36 unique slide IDs, file size < 250 KB, zero missing images, and zero CDNs.

- [ ] **Step 2: Run browser validation using `browser_subagent`**
Verify initial load, arrow key navigation, counter updates, and clean diagram rendering in Chrome.

- [ ] **Step 3: Document and finalize**
Ensure all tests pass and record verification evidence.
