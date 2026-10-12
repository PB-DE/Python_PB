# Unified Python Lecture Slides (L05 & L06) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single, self-contained, lightweight HTML presentation slide deck (`python_presentation_03.html`) in the established Modern Dark VS Code style that combines all curriculum content from `L05.ipynb` (Sequences: Lists & Tuples) and `L06.ipynb` (Dictionaries & Sets).

**Architecture:** Identical presentation engine to `python_presentation_01.html` and `python_presentation_02.html`: pure single-file HTML5/CSS3/Vanilla JS with 16:9 widescreen stage, VS Code Dark+ syntax highlighting, discreet progress bar and slide counter, zero persistent headers, and custom embedded vector SVGs for memory layout and set Venn diagrams.

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript, SVG, Node.js (automated verification), Chrome/Browser subagent.

## Global Constraints

- **File Name:** Output file must be `python_presentation_03.html`.
- **Zero External Dependencies:** 100% self-contained offline deck with no CDN or remote font dependencies.
- **VS Code Dark+ Palette:** Canvas `#1e1e1e`, code background `#252526`, border `#333333`, keywords `#569cd6`, variables `#9cdcfe`, numbers `#b5cea8`, strings `#ce9178`, comments `#6a9955`, functions `#dcdcaa`.
- **Footer:** `Civil Aviation Training Center (CATC)` (clean branding without "Computer Science").
- **Navigation:** Arrow keys, Space, PageUp/PageDown, Home, End, `F` for fullscreen, URL hash navigation.
- **Total Slides:** Exactly 36 slides (18 for Lecture 5 + 18 for Lecture 6).

---

### Task 1: Scaffolding Deck & Test Suite for Presentation 03

**Files:**
- Create: `tests/verify_presentation_03.js`
- Create: `python_presentation_03.html`

- [ ] **Step 1: Write `tests/verify_presentation_03.js`**
Assert file existence, zero CDN links, `#deck` container, VS Code Dark+ CSS tokens, keyboard event listeners, and footer text `Civil Aviation Training Center (CATC)` (no "Computer Science").

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_03.js`
Expected: FAIL (file does not exist).

- [ ] **Step 3: Implement core structure in `python_presentation_03.html` (GREEN)**
Set up the identical engine and stylesheet with title slide for Lectures 5 & 6.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_03.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit Task 1 changes.

---

### Task 2: Lecture 5 Content & List Memory Diagrams

**Files:**
- Modify: `tests/verify_presentation_03.js` (add assertions for L05 topics)
- Modify: `python_presentation_03.html`

- [ ] **Step 1: Update `tests/verify_presentation_03.js` with L05 assertions**
Assert Lecture 5 topics: indexing `[]`, `len()`, negative indices (`-1`, `-2`), mutability, `IndexError`, appending (`+=`, `append()`, `insert()`), contiguous memory SVG diagram, tuples immutability & chained indexing, tuple unpacking, `enumerate()`, slicing (`[start:stop]`, step `[::2]`, reverse `[::-1]`), `del` operator, in-place function modifications, sorting (`list.sort()` vs `sorted()`), searching (`index()` & `in`), list comprehensions (`[i**2 for i in range(1,11) if i%2==0]`), `filter()`, `lambda` expressions, and 2D lists (matrices). Slide count >= 18.

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_03.js`
Expected: FAIL (L05 content missing).

- [ ] **Step 3: Implement Lecture 5 Slides in `python_presentation_03.html` (GREEN)**
Assemble slides 1 through 18 for Lecture 5 with VS Code code boxes and vector memory diagram SVG.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_03.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit Task 2 changes.

---

### Task 3: Lecture 6 Content & Venn Diagram of Set Operations

**Files:**
- Modify: `tests/verify_presentation_03.js` (add assertions for L06 topics)
- Modify: `python_presentation_03.html`

- [ ] **Step 1: Update `tests/verify_presentation_03.js` with L06 assertions**
Assert Lecture 6 topics: dictionaries, key immutability rules, tuple keys, lookup & assignment, dynamic retyping (`presidents['Trump']=[45,47]`), `pop()`, `clear()`, `.get()` safe lookup vs `in`, iterating with `.items()` / `.keys()` / `.values()`, dict comprehensions (`{number: number**2}`), sets uniqueness & `in`, set type casting, subset check (`<`, `.issubset()`), set Venn diagram SVG, union (`|`, `.union()`), intersection (`&`, `.intersection()`), difference (`-`, `.difference()`), set modifications (`add()`, `remove()`, `discard()`), set comprehensions, and collection comparison synthesis. Total slides >= 35.

- [ ] **Step 2: Run test to verify failure (RED)**
Run: `node tests/verify_presentation_03.js`
Expected: FAIL (L06 content missing).

- [ ] **Step 3: Implement Lecture 6 Slides in `python_presentation_03.html` (GREEN)**
Assemble slides 19 through 36 with code blocks, outputs, and vector Venn diagram SVG. Total slides = 36.

- [ ] **Step 4: Run test to verify it passes**
Run: `node tests/verify_presentation_03.js`
Expected: PASS.

- [ ] **Step 5: Git commit**
Commit Task 3 changes.

---

### Task 4: End-to-End Verification & Browser Validation

**Files:**
- Create: `tests/e2e_check_03.js`
- Test: In-browser validation via `browser_subagent`

- [ ] **Step 1: Write and run `tests/e2e_check_03.js`**
Assert well-formed HTML, exactly 36 unique slide IDs, file size < 250 KB, zero broken local images, balanced tags, and zero CDNs.

- [ ] **Step 2: Run browser validation using `browser_subagent`**
Verify initial load, arrow key navigation, counter updates (`1 / 36` to `36 / 36`), and clean rendering of vector memory and Venn diagrams in Chrome.

- [ ] **Step 3: Document and finalize**
Ensure all test suites pass and record verification evidence.
