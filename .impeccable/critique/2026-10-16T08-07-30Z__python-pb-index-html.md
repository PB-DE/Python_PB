---
target: Python_PB/index.html
total_score: 35
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 1
target_identity: "file:/Users/phanuphong/Library/CloudStorage/OneDrive-catc.or.th/CATC Courses/python/Presentation/Python_PB/Python_PB/index.html"
timestamp: 2026-10-16T08-07-30Z
slug: python-pb-index-html
closed: true
---
⚠️ DEGRADED: single-context (no general sub-agent tool exposed in environment)

#### Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Search result count updates dynamically, but outline drawer open/closed state lacks aria-expanded announcements. |
| 2 | Match System / Real World | 4 | Academic computing and Python syllabus terminology align cleanly with university curriculum expectations. |
| 3 | User Control and Freedom | 3 | Search can be cleared with Escape or '✕'; outline drawers toggle; but no quick jump-to-top or filter reset button when query active. |
| 4 | Consistency and Standards | 4 | Unified card architecture, consistent badge tokenization, and standardized action buttons across all 5 decks. |
| 5 | Error Prevention | 4 | Search is non-destructive filter-as-you-type; empty query states offer helpful recovery guidance. |
| 6 | Recognition Rather Than Recall | 4 | All 179 slides are indexed and searchable with instant title/eyebrow previews; shortcuts card provides explicit reference. |
| 7 | Flexibility and Efficiency | 4 | Keyboard accelerators (⌘K, /, Esc), direct URL deep-linking to `#slide-XX`, and topic tags enable rapid access. |
| 8 | Aesthetic and Minimalist Design | 2 | Heavy AI aesthetic markers: 3 large viewport blur orbs, zero-offset cyan glow shadows, gradient headings, and decorative pulsing dot. |
| 9 | Error Recovery | 3 | Clear suggestion prompts when search query matches zero slides; no fallback state for missing deck files. |
| 10 | Help and Documentation | 4 | Explicit presentation shortcuts reference card and complete syllabus roadmap table. |
| **Total** | | **35/40** | **Good** |

#### Design Specificity Verdict

**LLM assessment**: The portal establishes a solid, clean organizational structure for the CATC Python Programming curriculum (5 decks, 10 lectures, 179 slides, syllabus table, keyboard shortcuts). However, its visual identity is category-interchangeable with generic developer tooling or AI template sites. Beyond literal text strings ("Civil Aviation Training Center (CATC)"), the aesthetic uses generic dark-mode tropes (ambient blur orbs, cyan glow boxes, gradient text) rather than visual cues reflecting aviation engineering, flight data systems, or technical avionics computing.

**Deterministic scan**: The Impeccable detector surfaced 7 findings across 4 antipatterns:
- `dark-glow` (3 instances): Viewport-sized glowing ambient background orbs (`filter: blur(60-80px)`), colored `#38bdf8` shadow on brand logo, zero-offset cyan glow on pulse dot.
- `gradient-text` (2 instances): Gradient text on hero heading (`.gradient-text`).
- `pulsing-dot` (1 instance): Infinite pulsing animation on `.pulse-dot` simulating ungrounded live streaming telemetry.
- `overused-font` (1 instance): Primary font family is `Inter`, which blends into category sameness.

**Visual inspection**: Live browser inspection confirmed responsive scaling and functional drawer accordions. The drawer expands smoothly and the search modal instantly filters all 179 slides. The ambient glow orbs create slight background turbidity on lower-contrast displays and add GPU composite layer overhead.

#### Overall Impression

The portal excels at information architecture and speed — the 10-lecture syllabus matrix, searchable 179-slide index, and direct deep-linking are exceptionally functional. The primary opportunity is stripping away generic AI-generated aesthetic clichés (glowing blur spheres, text gradients, fake pulse dots) and replacing them with a crisp, authoritative aviation engineering design language.

#### What's Working

1. **Curriculum Matrix & Direct Deep-Linking:** The syllabus roadmap and outline drawers link directly into presentation slide anchors (`#slide-XX`), giving instructors and students instant access to exact lecture moments.
2. **Instant Universal Slide Search:** Real-time search indexing all 179 slides with `⌘K` / `/` hotkey binding delivers superb navigation speed.
3. **Structured Information Architecture:** Clear hierarchical progression from hero stats to deck cards, syllabus table, and keyboard shortcuts guide.

#### Priority Issues

- **[P1] AI-Aesthetic Tells: Ambient Glowing Orbs & Colored Glow Shadows**
  - *Why it matters:* Three massive viewport-sized background blur circles (`filter: blur(60-80px)`) and zero-offset cyan glow shadows (`box-shadow: 0 0 8px var(--cyan)`) give the interface a generic "AI landing page" template sheen rather than a serious, authoritative aviation engineering training instrument. The blur filters also introduce unnecessary GPU composite layers.
  - *Fix:* Remove the ambient glowing orbs (`.ambient-glow`, `.glow-1`, `.glow-2`, `.glow-3`) and colored halo shadows. Replace with crisp, high-contrast dark surface elevation tokens (`--bg-surface`, `--bg-card`, crisp 1px borders) suited for lecture projectors.
  - *Suggested command:* `/impeccable quieter`

- **[P2] Generic Identity & Missed Aviation Domain Specificity**
  - *Why it matters:* Beyond the text strings "Civil Aviation Training Center (CATC)" and "Department of Aviation Engineering", the visual presentation contains no domain cues relating to flight computing, telemetry, or avionics systems. The default font choice (Inter) and gradient text accent reinforce a generic SaaS template vibe.
  - *Fix:* Incorporate subtle aviation engineering precision aesthetics (e.g. flight telemetry grid lines, monospaced data readout badges, aircraft instrumentation accents) and replace gradient headings with clean, solid high-contrast typography.
  - *Suggested command:* `/impeccable bolder`

- **[P2] Accessibility Gaps: Missing ARIA Attributes on Interactive Accordions and Search**
  - *Why it matters:* The "View Outline" buttons toggle expandable drawers without setting `aria-expanded="false/true"` or `aria-controls`. The search trigger and live search results container lack `aria-live="polite"` or `role="region"`, creating an obstacle for keyboard-only and screen-reader students (Sam).
  - *Fix:* Add `aria-expanded` and `aria-controls` to `.toggle-outline-btn`, tie drawers to IDs via `aria-labelledby`, and mark `#search-results-panel` with `aria-live="polite"`.
  - *Suggested command:* `/impeccable harden`

- **[P3] Search Results Keyboard Traversal**
  - *Why it matters:* Power users (Alex) can trigger search via `⌘K` or `/`, but must use a mouse to select a result from the list because `ArrowDown`/`ArrowUp` key navigation through the search items is not implemented.
  - *Fix:* Implement arrow key navigation (`ArrowDown`/`ArrowUp`/`Enter`) within `#results-list` so users can search and launch slides entirely from the keyboard.
  - *Suggested command:* `/impeccable polish`

#### Persona Red Flags

- **Alex (Power User)**: Can trigger search with `⌘K` or `/`, but cannot arrow down to navigate search results; must reach for mouse to launch a matched slide.
- **Jordan (First-Timer)**: Each deck card contains 5 competing clickable targets (Launch Deck, Jump Lecture A, Jump Lecture B, Lab .ipynb links, View Outline), causing initial visual paralysis on what to click first.
- **Sam (Accessibility-Dependent User)**: Drawer expanders lack `aria-expanded` state; search results panel does not announce live update counts to screen readers.
- **Capt. Somchai (CATC Aviation Instructor)**: Needs an instant "Presentation Mode / Today's Lecture" quick-launch toggle on classroom displays without navigating curriculum metadata.

#### Minor Observations

- Pulsing dot in hero badge simulates fake live streaming telemetry.
- Tiny `font-size: 0.72rem` on eyebrow labels may be hard to read from the back of large lecture halls.

#### Questions to Consider

- "What if the portal hero offered an instant 'Today's Lecture' widget that auto-highlights the current active week?"
- "How might the visual language reflect aviation telemetry data displays rather than standard web SaaS styling?"
- "Could the 5 competing CTAs on deck cards be distilled into one clear primary action with secondary disclosures?"
