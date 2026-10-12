const fs = require('fs');
const path = require('path');
const assert = require('assert');

const filePath = path.join(__dirname, '..', 'python_presentation_03.html');

console.log('Testing Task 1: Presentation 03 Engine Core & Theming...');

// 1. File exists
assert(fs.existsSync(filePath), 'python_presentation_03.html must exist');
const html = fs.readFileSync(filePath, 'utf8');
assert(html.length > 200, 'python_presentation_03.html must not be empty');

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

console.log('✓ Task 1 Verification Passed for Presentation 03!');

console.log('Testing Task 2: Lecture 5 Content & List Memory Diagrams...');

// Lecture 5 Title & Collections
assert(html.toLowerCase().includes('lecture 5') && (html.toLowerCase().includes('sequences') || html.toLowerCase().includes('lists')), 'Must include Lecture 5 title');
assert(html.includes('Collections') || html.includes('collections'), 'Must include Collections overview');

// List indexing & negative indices
assert(html.includes('len(') || html.includes('len'), 'Must include len() function');
assert(html.includes('-1') && html.includes('-2'), 'Must include negative indexing -1 and -2');

// Mutability & IndexError
assert(html.includes('mutable') || html.includes('Mutable'), 'Must include mutability explanation');
assert(html.includes('IndexError') || html.includes('out of range') || html.includes('Out of range'), 'Must include out of range errors');

// Appending and concatenating
assert(html.includes('+=') && html.includes('append'), 'Must include appending with += and append()');
assert(html.includes('+') || html.includes('Concatenat'), 'Must include list concatenation');

// Tuples & Chained indexing
assert(html.includes('immutable') || html.includes('Immutable'), 'Must include tuple immutability');
assert(html.includes('chained indexing') || html.includes('Chained indexing') || html.includes('t[2][-1]') || html.includes('[2][-1]'), 'Must include chained indexing');
assert(html.includes('unpacking') || html.includes('Unpacking'), 'Must include tuple unpacking');

// enumerate
assert(html.includes('enumerate') || html.includes('enumerate('), 'Must include enumerate function');

// Slicing
assert(html.includes('slicing') || html.includes('Slicing'), 'Must include slicing');
assert(html.includes('::-1') || html.includes('[::-1]'), 'Must include reverse slicing');
assert(html.includes('::2') || html.includes('[::2]') || html.includes('step'), 'Must include slicing with step');
assert(html.includes('del ') || html.includes('del'), 'Must include del operator');

// Sorting and searching
assert(html.includes('sort()') && html.includes('sorted('), 'Must distinguish list.sort() and sorted()');
assert(html.includes('index(') && html.includes(' in '), 'Must include index() and in operator');

// List comprehensions, filter & lambda
assert(html.includes('comprehension') || html.includes('comprehensions'), 'Must include list comprehensions');
assert(html.includes('filter(') || html.includes('filter'), 'Must include filter function');
assert(html.includes('lambda') || html.includes('lambda x'), 'Must include lambda expressions');

// 2D lists
assert(html.includes('2d') || html.includes('Two-dimensional') || html.includes('two-dimensional') || html.includes('my_2d_list'), 'Must include 2D lists');

// Vector SVG memory diagram
assert(html.includes('<svg') && (html.includes('Memory') || html.includes('Index') || html.includes('Pointer') || html.includes('0')), 'Must include vector SVG memory diagram');

// Slide count >= 18
const l5Slides = (html.match(/class="slide/g) || []).length;
assert(l5Slides >= 18, `Must have at least 18 slides for L05, currently has ${l5Slides}`);

console.log('✓ Task 2 Verification Passed for Presentation 03!');

