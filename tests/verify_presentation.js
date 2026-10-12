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

console.log('Testing Task 3: Lecture 2 Content & VS Code Syntax Tokens...');

// Lecture 2 Title & Transition
assert(html.toLowerCase().includes('intro to python programming') || html.toLowerCase().includes('lecture 2'), 'Must include Lecture 2 title');

// Expressions & Variables
assert(html.includes('Expressions') || html.includes('expressions'), 'Must include Expressions');
assert(html.includes('PEP 8') || html.includes('pep-0008') || html.includes('PEP8'), 'Must include PEP 8 spacing note');
assert(html.includes('SyntaxError') && html.includes('123_xyz'), 'Must include invalid variable name SyntaxError example');

// Types & Operations
assert(html.includes('Data types') || html.includes('Data Types'), 'Must include Data types slide');
assert(html.includes('Arithmetic operations') || html.includes('Arithmetic Operations'), 'Must include Arithmetic operations');
assert(html.includes('//') && html.includes('%'), 'Must include floor division and modulus');
assert(html.includes('2417851639229258349412352') || html.includes('2 ** 3 ** 4'), 'Must include exponent associativity');


// Strings, Input, Casting
assert(html.toLowerCase().includes('strings') && html.includes('\\n'), 'Must include strings with newline escape');
assert(html.includes('input('), 'Must include user input() function');
assert(html.includes('int(y)') || html.includes('int('), 'Must include type casting with int()');

// Booleans & Conditionals
assert(html.includes('Boolean expressions') || html.includes('Boolean Expressions'), 'Must include Boolean expressions');
assert(html.includes('bigger than y') && html.includes('smaller than y'), 'Must include conditional if statement');

assert(html.includes('Comments allow you to') || html.includes('Comments'), 'Must include Comments slide');
assert(html.includes('Dynamic typing') || html.includes('Dynamic Typing'), 'Must include Dynamic typing');
assert(html.includes('min(') && html.includes('max('), 'Must include descriptive statistics min/max');

// Slide count >= 35
const totalSlides = (html.match(/class="slide/g) || []).length;
assert(totalSlides >= 35, `Must have at least 35 slides for complete L01 + L02, currently has ${totalSlides}`);

console.log('✓ Task 3 Verification Passed!');


