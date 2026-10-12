const fs = require('fs');
const path = require('path');
const assert = require('assert');

const filePath = path.join(__dirname, '..', 'python_presentation.html');

console.log('Testing Task 1: Presentation Engine Core & Styling...');

// Check file exists
assert(fs.existsSync(filePath), 'python_presentation.html must exist');
const html = fs.readFileSync(filePath, 'utf8');
assert(html.length > 200, 'python_presentation.html must not be empty');

// Check no external network dependencies
assert(!html.includes('http://') && !html.includes('https://'), 'Must not contain external HTTP/HTTPS CDN references');

// Check structure
assert(html.includes('id="deck"'), 'Must have #deck container');
assert(html.includes('class="slide'), 'Must have .slide elements');
assert(html.includes('class="progress-bar"') || html.includes('id="progress"'), 'Must have progress bar indicator');
assert(html.includes('class="slide-counter"') || html.includes('id="counter"'), 'Must have slide counter');

// Check VS Code Dark+ CSS tokens
assert(html.includes('--bg: #1e1e1e') || html.includes('--bg:#1e1e1e'), 'Must have VS Code Dark+ canvas background #1e1e1e');
assert(html.includes('--code-bg: #252526') || html.includes('--code-bg:#252526'), 'Must have VS Code Dark+ code background #252526');
assert(html.includes('--token-kw: #569cd6') || html.includes('--kw: #569cd6'), 'Must define VS Code keyword token color #569cd6');

// Check JS engine features
assert(html.includes('ArrowRight') && html.includes('ArrowLeft'), 'Must support ArrowRight and ArrowLeft keys');
assert(html.includes('Space'), 'Must support Space key');
assert(html.includes('KeyF') || html.includes('fullscreen'), 'Must support KeyF / fullscreen API');
assert(html.includes('location.hash') || html.includes('hashchange'), 'Must support URL hash navigation');

console.log('✓ Task 1 Verification Passed!');
