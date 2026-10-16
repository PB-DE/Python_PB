# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary users are Civil Aviation Training Center (CATC) aviation students and instructors:
- **Instructors:** Presenting technical lectures and coding demonstrations in classroom and lecture hall settings via projectors or large displays.
- **Students:** Reviewing course materials, exploring programming syntax, and practicing exercises during class and offline self-study on laptops and personal devices.

## Product Purpose

Provide an integrated, rapid curriculum portal and standalone widescreen presentation slide decks covering the 10-lecture CATC Python Programming syllabus (179 interactive slides across 5 unified decks). Success means friction-free offline classroom presentation, immediate responsiveness, high visual clarity for code and diagrams, and zero runtime dependency hurdles for students.

## Positioning

Curriculum-tailored aviation computing education delivered as 100% self-contained, offline-first HTML slide decks and portal that require no external build servers or internet access, featuring authentic VS Code Dark+ syntax rendering and fluid keyboard/touch navigation.

## Operating Context

- **Classroom Delivery:** Projected in lecture halls with varying ambient lighting and screen resolutions; demands immediate legibility and clean full-viewport presentation.
- **Student Self-Study:** Used on student laptops, tablets, and mobile devices, frequently in disconnected or bandwidth-constrained environments.
- **Curriculum Synchronization:** Jupyter notebooks (`L01.ipynb` through `L11.ipynb`) serve as the source curriculum; metadata is indexed in `decks_data.json` and rendered via `build_index.py`.

## Capabilities and Constraints

- **Capabilities:**
  - Full keyboard navigation (`Right Arrow`/`Space`/`PageDown`, `Left Arrow`/`PageUp`, `Home`, `End`, `F` fullscreen).
  - Touch swipe gestures for tablets and touch displays.
  - Direct URL hash linking (`#slide-XX`) for bookmarking and sharing specific slides.
  - Portal curriculum hub with search, lecture filters, and direct slide deck launchers.
  - High-resolution SVG diagrams (CPU/Memory architecture, Moore's Law curve, object reference pointers).
- **Constraints:**
  - Standalone & offline-first: Zero CDN or external network dependencies; works entirely offline.
  - No heavy execution runtime: Lightweight vanilla HTML5/CSS3/JavaScript with no bulky Wasm or compilation overhead inside the slides.
  - Distraction-free viewport: No persistent navigation headers or breadcrumbs eating vertical presentation space during lectures.

## Brand Commitments

- **Institution:** Civil Aviation Training Center (CATC).
- **Course:** Python Programming.
- **Tone:** Professional, technical, structured, and modern instructional design upholding aviation training standards.

## Evidence on Hand

- Canonical lecture notebooks: `L01.ipynb` through `L11.ipynb`
- Presentation decks: `python_presentation_01.html` through `python_presentation_05.html`
- Portal index: `index.html` and generator `build_index.py`
- Structured slide metadata: `decks_data.json`
- Design specifications: `docs/superpowers/specs/2026-10-12-python-lecture-slides-design.md`
- Verification suite: `tests/` (Playwright / e2e verification scripts)

## Product Principles

1. **Zero-Dependency Resilience:** Must function completely offline on any student or classroom device without network requests or external dependencies.
2. **Content-First Classroom Readability:** Every slide is engineered for high contrast and immediate readability on standard projection systems.
3. **Exact Curriculum Fidelity:** Presentation slides and portal index directly mirror and faithfully represent the underlying CATC course notebooks.
4. **Instant Lightweight Performance:** Fast loading, fluid slide transitions, and low hardware footprint across all devices.

## Accessibility & Inclusion

High-contrast code and typography optimized for both projector viewing and personal devices. Fully navigable via standard keyboard controls, screen-agnostic layout scaling, and touch support.
