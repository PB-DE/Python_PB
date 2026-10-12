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

console.log('Testing Task 2: Lecture 1 Content & SVG Diagrams...');

// L01 Title & topics
assert(html.includes('Fundamentals of computing') || html.includes('Fundamentals of Computing'), 'Must include Lecture 1 title');
assert(html.includes('Representation with numbers') || html.includes('Representation with Numbers'), 'Must include Representation with numbers slide');
assert(html.includes('1010') && html.includes('2<sup>3</sup>'), 'Must include binary conversion formula');
assert(html.includes('Equality versus assignment') || html.includes('Equality versus Assignment'), 'Must include Equality vs assignment');
assert(html.includes('Data hierarchy') || html.includes('Data Hierarchy'), 'Must include data hierarchy');
assert(html.includes('Moore&#39;s Law') || html.includes("Moore's Law"), "Must include Moore's law slide");
assert(html.toLowerCase().includes('levels of programming languages'), 'Must include programming languages levels');
assert(html.toLowerCase().includes('object-oriented programming'), 'Must include OOP slide');
assert(html.toLowerCase().includes('operating systems'), 'Must include operating systems');
assert(html.includes('Why Python?'), 'Must include Why Python');


// Inline SVGs
assert(html.includes('<svg') && html.includes('CPU') && html.includes('RAM'), 'Must have inline vector SVG for Computer Architecture');
assert(html.includes('Shallow') && html.includes('Deep') && html.includes('<svg'), 'Must have inline vector SVG for Shallow vs Deep Copy');
assert(html.includes('transistors') && html.includes('<svg') && html.includes('path'), "Must have inline vector SVG for Moore's Law curve");

// NumPy code for plotting
assert(html.includes('numpy') && html.includes('matplotlib.pyplot') && html.includes('n_transistors'), 'Must include Moore law plotting code');


// Count slides >= 15
const slideMatches = html.match(/class="slide/g) || [];
assert(slideMatches.length >= 15, `Must have at least 15 slides, currently has ${slideMatches.length}`);

console.log('✓ Task 2 Verification Passed!');

