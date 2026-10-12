const fs = require('fs');
const path = require('path');
const assert = require('assert');

const filePath = path.join(__dirname, '..', 'python_presentation_04.html');

console.log('Testing Task 1: Presentation 04 Engine Core & Theming...');

// 1. File exists
assert(fs.existsSync(filePath), 'python_presentation_04.html must exist');
const html = fs.readFileSync(filePath, 'utf8');
assert(html.length > 200, 'python_presentation_04.html must not be empty');

// 2. Zero external dependencies
assert(!html.includes('http://') && !html.includes('https://'), 'Must not contain external HTTP/HTTPS CDN references');

// 3. Structure
assert(html.includes('id="deck"'), 'Must have #deck container');
assert(html.includes('class="slide'), 'Must have .slide elements');
assert(html.includes('id="progress"'), 'Must have progress bar');
assert(html.includes('id="counter"'), 'Must have slide counter');

// 4. Clean Footer (No "Computer Science")
assert(html.includes('Civil Aviation Training Center (CATC)'), 'Must include CATC in footer');
assert(!html.includes('Computer Science'), 'Must NOT include "Computer Science" anywhere');

// 5. VS Code Dark+ CSS tokens
assert(html.includes('--bg: #1e1e1e') || html.includes('--bg:#1e1e1e'), 'Must have #1e1e1e background');
assert(html.includes('--code-bg: #252526') || html.includes('--code-bg:#252526'), 'Must have #252526 code background');

// 6. Navigation
assert(html.includes('ArrowRight') && html.includes('ArrowLeft'), 'Must support arrow keys');
assert(html.includes('KeyF') || html.includes('fullscreen'), 'Must support fullscreen');

console.log('✓ Task 1 Verification Passed for Presentation 04!');
