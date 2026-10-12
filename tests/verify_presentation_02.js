const fs = require('fs');
const path = require('path');
const assert = require('assert');

const filePath = path.join(__dirname, '..', 'python_presentation_02.html');

console.log('Testing Task 1: Presentation 02 Engine Core & Theming...');

// 1. File exists
assert(fs.existsSync(filePath), 'python_presentation_02.html must exist');
const html = fs.readFileSync(filePath, 'utf8');
assert(html.length > 200, 'python_presentation_02.html must not be empty');

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

console.log('✓ Task 1 Verification Passed for Presentation 02!');

console.log('Testing Task 2: Lecture 3 Content & Flowcharts...');

// Lecture 3 Title & Overview
assert(html.toLowerCase().includes('lecture 3') && html.toLowerCase().includes('control statements'), 'Must include Lecture 3 title');
assert(html.includes('Algorithms') || html.includes('algorithms'), 'Must include Algorithms slide');
assert(html.includes('Pseudocode') || html.includes('pseudocode'), 'Must include Pseudocode slide');

// Selection statements
assert(html.includes('Selection statements') || html.includes('if elif else'), 'Must include selection statements');
assert(html.includes('Condition is True') && html.includes('Loquacious D'), 'Must include truthiness evaluation');
assert(html.includes('Suite indentation') || html.includes('suite'), 'Must include suite indentation');
assert(html.includes("'even' if") || html.includes('"even" if'), 'Must include ternary conditional expression');
assert(html.includes('Logic error') || html.includes('logic error'), 'Must include logic vs syntax error');

// Loops
assert(html.includes('while price_of_netflix') || html.includes('Netflix'), 'Must include while loop Netflix case study');
assert(html.includes('0.2f') && html.includes('{year'), 'Must include f-string formatting slide');
assert(html.includes('range(6)') || html.includes('range('), 'Must include for loop and range()');
assert(html.includes('my_first_list') || html.includes('[-3, 2, -5, 4, 0]'), 'Must include iterables and lists');
assert(html.includes('+=') && html.includes('*='), 'Must include augmented expressions');

// Fibonacci & Refinement
assert(html.includes('Fibonacci') || html.includes('fibonacci'), 'Must include Fibonacci case study');
assert(html.includes('Initialization') && html.includes('Processing') && html.includes('Termination'), 'Must include 3 stages of algorithms');
assert(html.includes('first refinement') || html.includes('second refinement') || html.includes('refinement'), 'Must include algorithm refinement');

// break, continue, boolean ops, stats
assert(html.includes('break') && html.includes('continue'), 'Must include break and continue statements');
assert(html.includes('Boolean operators') || (html.includes('and') && html.includes('or') && html.includes('not')), 'Must include boolean operators');
assert(html.includes('statistics.mean') && html.includes('statistics.median') && html.includes('statistics.mode'), 'Must include central tendency statistics');

// Inline SVG Flowchart
assert(html.includes('<svg') && (html.includes('Condition') || html.includes('True') || html.includes('False')), 'Must include inline vector SVG flowchart');

// Slide count >= 18
const l3Slides = (html.match(/class="slide/g) || []).length;
assert(l3Slides >= 18, `Must have at least 18 slides for L03, currently has ${l3Slides}`);

console.log('✓ Task 2 Verification Passed for Presentation 02!');

