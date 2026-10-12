# Unified Python Presentation Deck 05 (Lectures 9 & 10) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a unified, modern dark VS Code styled, 16:9 offline HTML presentation deck (`python_presentation_05.html`) covering Lecture 9 (Files & Exceptions) and Lecture 10 (Intro to Object-Oriented Programming), with 36 slides total, authentic syntax highlighting, 2 custom vector SVGs, and automated E2E testing.

**Architecture:** A single self-contained HTML5/CSS3/Vanilla JS presentation file following the proven architecture of `python_presentation_01.html` through `04.html`. 16:9 aspect ratio container (`1333.33px` by `750px`), auto-transform scaled to window, responsive footer with slide counter and fullscreen button, pure offline zero-CDN styling with VS Code Dark+ syntax tokens.

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript (ES6+), Inline SVG vector diagrams, Node.js test harness.

**Spec:** Curriculum from [L09.ipynb](file:///Users/phanuphong/Library/CloudStorage/OneDrive-catc.or.th/CATC%20Courses/python/Presentation/L09.ipynb) and [L10.ipynb](file:///Users/phanuphong/Library/CloudStorage/OneDrive-catc.or.th/CATC%20Courses/python/Presentation/L10.ipynb).

## Global Constraints
- Target filename: `python_presentation_05.html`.
- Modern Dark theme with VS Code Dark+ syntax highlighting (`#1e1e1e` canvas, `#252526` editor panels, `#569cd6` keywords, `#9cdcfe` identifiers, `#b5cea8` numbers, `#ce9178` strings, `#6a9955` comments, `#dcdcaa` functions, `#4ec9b0` types).
- 16:9 widescreen stage auto-scaled and centered.
- Zero chapter bars, zero persistent header menus.
- Footer branding: `Civil Aviation Training Center (CATC)` with slide counter and fullscreen toggle; NO `"Computer Science"` text.
- Exactly 36 slides: 18 for Lecture 9 + 18 for Lecture 10.
- Fully offline and self-contained (< 250 KB) with zero external fonts, scripts, or CDN dependencies.

## Review Focus
1. Slide 6 vector diagram: File I/O Lifecycle & Stream Buffering rendered with inline SVG and proper contrast.
2. Slide 17 exception flow: Accurate presentation of `try`, `except`, `else` (success path), and `finally` (cleanup).
3. Slide 27 vector diagram: Class Blueprint vs. Instance Heap Objects (`TwitterAccount` blueprint -> `elon` and `biebs` instances).
4. Slide 33 & 34: Magic method `__str__` and object string formatting accurately represented with authentic outputs.
5. All code samples from `L09.ipynb` and `L10.ipynb` formatted in VS Code dark boxes with syntax highlight tokens and output boxes.

---

### Task 1: Scaffolding Deck & Test Suite for Presentation 05

**Files:**
- Create: `tests/verify_presentation_05.js`
- Create: `python_presentation_05.html`

**Interfaces:**
- Consumes: Slide engine, styling tokens, and layout from `python_presentation_04.html`.
- Produces: Base HTML structure, CSS stylesheet, keyboard navigation JS engine, and Task 1 test runner.

- [ ] **Step 1: Write the failing test in `tests/verify_presentation_05.js`**
  - Verify `python_presentation_05.html` exists.
  - Verify `< 250 KB` file size.
  - Verify zero external CDNs / resources.
  - Verify `Civil Aviation Training Center (CATC)` present and `"Computer Science"` absent.
  - Verify presentation engine JS (keyboard listeners, resize handler, hash routing).

- [ ] **Step 2: Run test to verify failure (RED)**
  - Run: `node tests/verify_presentation_05.js`
  - Expected: FAIL with file not found.

- [ ] **Step 3: Implement core presentation container and engine in `python_presentation_05.html`**
  - Scaffold 16:9 stage (`#stage`), VS Code color tokens, keyboard event listener, progress bar, footer with slide counter and fullscreen button.

- [ ] **Step 4: Run test to verify it passes (GREEN)**
  - Run: `node tests/verify_presentation_05.js`
  - Expected: PASS for Task 1.

- [ ] **Step 5: Git commit**
  - Run: `git add tests/verify_presentation_05.js python_presentation_05.html && git commit -m "feat: scaffold presentation 05 engine and test suite"`

---

### Task 2: Lecture 9 Content & File I/O Vector Diagrams (Slides 1–18)

**Files:**
- Modify: `tests/verify_presentation_05.js`
- Modify: `python_presentation_05.html`

**Interfaces:**
- Consumes: Task 1 scaffold.
- Produces: Slides 1 to 18 covering L09 (persistence, text files, context managers, `os` library, JSON serialization/deserialization, exceptions, `try`/`except`/`else`/`finally`), including custom vector SVG diagram in Slide 6.

- [ ] **Step 1: Update `tests/verify_presentation_05.js` with Lecture 9 assertions**
  - Verify all 18 slides for Lecture 9 have unique IDs `slide-1` to `slide-18`.
  - Verify keywords: `with open`, `sample_data.txt`, `os.rename`, `json.dump`, `json.load`, `FileNotFoundError`, `finally`.
  - Verify inline SVG diagram present in Slide 6.

- [ ] **Step 2: Run test to verify failure (RED)**
  - Run: `node tests/verify_presentation_05.js`
  - Expected: FAIL on Lecture 9 assertions.

- [ ] **Step 3: Implement Slides 1 to 18 in `python_presentation_05.html`**
  - Slide 1: Title & Overview (Files & Exceptions).
  - Slide 2: Volatile RAM vs. Persistent Disk Storage.
  - Slide 3: Files as Byte Streams & Encodings.
  - Slide 4: Writing Text Files (`open(..., mode='w')`).
  - Slide 5: The `with` Statement & Context Managers.
  - Slide 6: Vector SVG Diagram: File I/O Lifecycle & Stream Buffering.
  - Slide 7: Reading Text Files (`mode='r'`).
  - Slide 8: Parsing Delimited Rows (`split()` & column formatting).
  - Slide 9: OS File Operations (`os.rename`, `os.remove`).
  - Slide 10: JSON Data Architecture.
  - Slide 11: Complex Nested Dictionaries (`twitter_dict`).
  - Slide 12: Navigating Nested JSON structures (`twitter_dict['twitter'][2]['handle']`).
  - Slide 13: Writing JSON Files (`json.dump`).
  - Slide 14: Reading JSON Files (`json.load`).
  - Slide 15: Introduction to Exceptions & Tracebacks.
  - Slide 16: Catching Errors (`try` / `except FileNotFoundError`).
  - Slide 17: Complete Error Handling Architecture (`try`, `except`, `else`, `finally`).
  - Slide 18: Lecture 9 Key Takeaways & Best Practices.

- [ ] **Step 4: Run test to verify it passes (GREEN)**
  - Run: `node tests/verify_presentation_05.js`
  - Expected: PASS for Tasks 1 & 2.

- [ ] **Step 5: Git commit**
  - Run: `git add tests/verify_presentation_05.js python_presentation_05.html && git commit -m "feat: implement Lecture 9 slides and File I/O vector diagram"`

---

### Task 3: Lecture 10 Content & OOP Memory Model Vector Diagram (Slides 19–36)

**Files:**
- Modify: `tests/verify_presentation_05.js`
- Modify: `python_presentation_05.html`

**Interfaces:**
- Consumes: Tasks 1 & 2 slides.
- Produces: Slides 19 to 36 covering L10 (classes, objects, `__init__`, `self`, methods, object composition, computed properties, simulated privacy `_userid`, `__str__`, `__repr__`, synthesis), including custom vector SVG diagram in Slide 27.

- [ ] **Step 1: Update `tests/verify_presentation_05.js` with Lecture 10 assertions**
  - Verify total slide count equals exactly 36 (`slide-1` to `slide-36`).
  - Verify keywords: `class TwitterAccount`, `__init__`, `self`, `add_follower`, `get_number_followers`, `_userid`, `__str__`.
  - Verify inline SVG diagram present in Slide 27.

- [ ] **Step 2: Run test to verify failure (RED)**
  - Run: `node tests/verify_presentation_05.js`
  - Expected: FAIL on Lecture 10 assertions.

- [ ] **Step 3: Implement Slides 19 to 36 in `python_presentation_05.html`**
  - Slide 19: Title & Overview (Intro to Object-Oriented Programming).
  - Slide 20: Paradigm: "Everything is an Object" in Python.
  - Slide 21: Classes (Blueprints) vs. Objects (Instances).
  - Slide 22: Four Core Motivations of OOP.
  - Slide 23: Defining a Class (`class TwitterAccount`).
  - Slide 24: Instantiation & The `__init__` Constructor.
  - Slide 25: The `self` Parameter Demystified.
  - Slide 26: Accessing & Modifying Instance Attributes.
  - Slide 27: Vector SVG Diagram: Class Blueprint vs. Heap Instances.
  - Slide 28: Adding Instance Methods (`add_follower`).
  - Slide 29: Object Composition: Objects Containing Objects.
  - Slide 30: Computed Methods (`get_number_followers`).
  - Slide 31: Encapsulation & Simulating Private Data (`_userid`).
  - Slide 32: Initializing Internal State (Random User IDs).
  - Slide 33: Magic Methods: The Default String Representation.
  - Slide 34: Implementing Custom `__str__` for Human Readability.
  - Slide 35: `__str__` vs. `__repr__` In-Depth.
  - Slide 36: Curriculum Synthesis & Architecture Matrix (Files + OOP).

- [ ] **Step 4: Run test to verify it passes (GREEN)**
  - Run: `node tests/verify_presentation_05.js`
  - Expected: PASS for all 3 tasks.

- [ ] **Step 5: Git commit**
  - Run: `git add tests/verify_presentation_05.js python_presentation_05.html && git commit -m "feat: implement Lecture 10 slides and OOP memory vector diagram"`

---

### Task 4: End-to-End Verification & Browser Visual Inspection

**Files:**
- Create: `tests/e2e_check_05.js`
- Test: Browser rendering validation

- [ ] **Step 1: Write and run `tests/e2e_check_05.js`**
  - Verify file size is under 250 KB.
  - Verify exactly 36 slide elements.
  - Verify balanced HTML tags and valid SVG definitions.
  - Verify absence of external CDNs and `"Computer Science"` text.

- [ ] **Step 2: Run browser validation using `browser_subagent`**
  - Open `python_presentation_05.html` in browser subagent.
  - Check Slide 1 (L09 Title), Slide 6 (File I/O SVG), Slide 19 (L10 Title), Slide 27 (OOP Memory SVG), Slide 36 (Synthesis).
  - Capture and inspect screenshots.

- [ ] **Step 3: Document and finalize**
  - Commit E2E test suite.
  - Update task checklist artifact.
  - Present final summary to user.
