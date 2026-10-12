# Design Document: Unified Python Lecture Slides (L01 & L02)

**Date:** 2026-10-12  
**Target File:** `python_presentation.html`  
**Course:** Python Programming — Civil Aviation Training Center (CATC)  

---

## 1. Intent & Purpose

Create a unified, fast, and lightweight HTML presentation slide deck derived directly from the course lecture notebooks:
- **Lecture 1 (`L01.ipynb`):** *Fundamentals of Computing* (data representation, binary systems, computer architecture, Moore's law, programming language hierarchy, why Python).
- **Lecture 2 (`L02.ipynb`):** *Intro to Python Programming* (expressions, variables, data types, arithmetic operators & precedence, strings, user input, type casting, booleans, conditionals, comments, dynamic typing, built-in stats).

The slides will be used in classroom lectures and for student distribution. The presentation must look clean, professional, and modern, offering maximum readability on projectors and laptops.

---

## 2. Key Decisions (Confirmed by User)

1. **Unified Presentation:** All content from Lecture 1 and Lecture 2 combined into a single, continuous presentation deck.
2. **Visual Style:** Modern Dark IDE theme matching the authentic **VS Code Dark+** color palette (`#1e1e1e` slide background, `#252526` code containers, syntax colors: `#569cd6` keywords, `#9cdcfe` identifiers, `#b5cea8` numbers, `#ce9178` strings, `#6a9955` comments).
3. **No Chapter Bar:** No persistent top header or chapter navigation bars that consume screen real estate. The entire viewport is dedicated to slide content.
4. **No Heavy Interactive Features:** No live Python runtime (Pyodide/Wasm) or heavy interactive sandboxes. Slides remain lightweight, pure, and fast.
5. **Self-Contained & Fast:** Everything bundled into a single standalone HTML file (`python_presentation.html`) that works completely offline with zero external network requests.

---

## 3. Goals, Non-Goals & Anti-Goals

### Goals
- **Complete Content Coverage:** Accurate transcription of all lecture topics, definitions, tables, code snippets, outputs, and exercises from `L01.ipynb` and `L02.ipynb`.
- **VS Code Dark+ High-Fidelity Code:** Code snippets styled with precise syntax token highlighting and formatted output blocks.
- **Embedded Visuals & Diagrams:**
  - Crisp SVG diagram for *Computer Architecture* (CPU, ALU, Control Unit, Memory, Storage, I/O, Bus).
  - Clean memory reference diagram for *Shallow vs. Deep Copy* (`X = 3.14156`, `Y = X`).
  - High-resolution SVG / vector curve for *Moore's Law Plot* (transistors vs. time).
- **Lightweight Presentation Engine:**
  - Keyboard navigation: `Right Arrow` / `Space` / `PageDown` (Next), `Left Arrow` / `PageUp` (Previous), `Home` (First slide), `End` (Last slide), `F` (Toggle Fullscreen).
  - Touch / Swipe support for tablets or touch displays.
  - Slide URL hash linking (e.g., `#slide-15`) allowing instant resumption or sharing of specific slides.
  - Minimal UI overlay: discreet slide counter (`15 / 48`) and a razor-thin progress bar at the top or bottom edge.

### Non-Goals
- Live interactive code compilation or evaluation inside the slide.
- Video playback or audio narration plugins.

### Anti-Goals
- Bloated slide frameworks (no multi-megabyte external node dependencies or CDN-reliant scripts that break offline in lecture halls).
- Visual clutter (no persistent navigation breadcrumbs, floating menus, or animated slide backgrounds that distract from lecture content).

---

## 4. Slide Content Breakdown

### Part I: Lecture 1 — Fundamentals of Computing
1. **Title Slide:** Course Title, Lecture 1: Fundamentals of Computing (CATC).
2. **Representation with Numbers:** Speech, images, text, and everything represented as numbers.
3. **What is a Number?:** Decimal base-10 sequence of digits, positional notation ($1979 = 1\times 10^3 + \dots$).
4. **Binary Representation:** Base-2 representation, bits $\in \{0, 1\}$, 4-bit numbers ($1010_2 = 10_{10}$), bit capacity formula.
5. **Equality vs. Assignment:** Mathematical equivalence ($x = 2 \iff 2 = x$) vs. procedural assignment ($x \leftarrow 2$, invalid $2 \leftarrow x$).
6. **Data Hierarchy:** Bit $\to$ Character $\to$ Field $\to$ Record $\to$ Database table.
7. **Basic Computer Architecture:** Vector diagram showing CPU (ALU, Control Unit), Main Memory (RAM), Secondary Storage, and Bus lines.
8. **What Do Computers Do?:** Physical voltage manipulation, instructions, arithmetic, logical comparisons, universal computing.
9. **Moore's Law:** Transistor doubling every ~2 years, exponential curve, cost reduction over time.
10. **Levels of Programming Languages:** Machine language $\to$ Assembly language $\to$ High-level compiled/interpreted languages $\to$ Where Python fits.
11. **Shallow vs. Deep Copy:** Memory references, variable binding, object pointers in memory.
12. **Object-Oriented Programming (OOP):** Objects, reusable software components, attributes, methods (Bank Account example).
13. **Operating Systems:** Resource management, concurrency, desktop (Windows, macOS, Linux) and mobile (Android, iOS).
14. **Why Python?:** Readability, high-level ergonomics, free & open-source, massive library ecosystem, stepping stone for computer science.
15. **Moore's Law Case Study:** Plotting exponential growth with NumPy and Matplotlib (code, array calculation $2^{t/2}$, and the exponential graph).

### Part II: Section Transition
16. **Lecture 2 Title Slide:** Lecture 2: Intro to Python Programming.

### Part III: Lecture 2 — Intro to Python Programming
17. **Expressions & Statements:** Syntax, statements as computer instructions, expression evaluation.
18. **Variables & Assignment:** Identifiers, assignment symbol `=`, integer literals.
19. **Adding Two Integers & PEP 8:** `x = 45`, `y = 36`, `z = x + y`, recommended spacing style (PEP 8).
20. **Variable Naming Rules:** Case sensitivity (`X` vs `x`), permitted characters (letters, digits, underscores), invalid names starting with digits (`123_xyz` SyntaxError).
21. **Data Types & `type()` Function:** Dynamic typing, inspecting variable types (`int`, `float`).
22. **Arithmetic Operations I:** Addition (`+`), subtraction (`-`), multiplication (`*`), floating-point division (`/`).
23. **Arithmetic Operations II:** Exponentiation (`**`), floor division (`//`), modulus (`%`).
24. **Operator Precedence Rules:** PEMDAS / Python precedence (parentheses, exponents right-to-left, multiplication/division/modulus, addition/subtraction).
25. **Associativity & Parentheses:** Right-to-left exponentiation (`2 ** 3 ** 4` = $2^{81}$ vs `(2 ** 3) ** 4`), disambiguating expressions.
26. **Strings (`str`):** Character sequences, single vs. double quotes, `print()` function, newline escape sequences (`\n`).
27. **User Input:** `input()` function, prompt strings, why input returns strings.
28. **Type Casting:** Converting strings to numbers using `int()` and `float()`.
29. **Boolean Expressions:** `bool` type (`True`, `False`), relational comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`).
30. **Conditional Execution (`if`):** State-dependent branching, colon `:` requirement, mandatory 4-space indentation.
31. **Comments & Documentation:** `#` single-line and inline comments, self-documenting code.
32. **Variables, Values, and Objects:** Pointers to objects, values, and types in memory.
33. **Dynamic Typing in Action:** Type mutation on reassignment and operations (`x = 10`, `y = 3`, `z = x / y` produces `float`).
34. **Basic Descriptive Statistics:** Built-in `min()` and `max()` functions across multiple values.
35. **Summary & Conclusion:** Key takeaways from Lectures 1 & 2, preparation for Lecture 3.

---

## 5. Technical Architecture & Implementation Details

- **Single HTML File:** Contains CSS in `<style>`, markup in `<div id="deck">`, and minimal vanilla script in `<script>`.
- **Display Mode:** Flexbox/Grid centering at 16:9 aspect ratio with auto-scaling to fill any display without distortion.
- **Styling Architecture:**
  - CSS Variables for color palette and typography.
  - System font stack prioritizing crisp sans-serif: `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`.
  - Monospace font stack for code: `'Cascadia Code', 'Fira Code', 'JetBrains Mono', 'Consolas', monospace`.
- **Keyboard Handling:**
  - Keydown listener for `ArrowRight`, `Space`, `PageDown`, `Enter` $\to$ `nextSlide()`.
  - Keydown listener for `ArrowLeft`, `PageUp`, `Backspace` $\to$ `prevSlide()`.
  - Keydown listener for `KeyF` $\to$ toggle browser fullscreen API.
  - Keydown listener for `Home` / `End` $\to$ jump to slide 1 / final slide.
  - Hash change listener for browser back/forward and direct links.
- **Embedded Graphics:**
  - All diagrams (Computer Architecture, Shallow vs Deep Memory, Moore's Law Curve) coded as inline `<svg>` with theme matching so there are zero missing image files.

---

## 6. What is Left to the Builder

- Implementing the slide navigation state machine and transition effects (fade/slide).
- Fine-tuning responsive SVG coordinate boxes for computer architecture and memory pointer diagrams.
- Ensuring strict compliance with VS Code Dark+ color hex values across all code tokens.
