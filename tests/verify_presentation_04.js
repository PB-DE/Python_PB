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

console.log('Testing Task 2: Lecture 7 Content & NumPy Vector Diagrams...');

// Lecture 7 Title & ndarray
assert(html.toLowerCase().includes('lecture 7') && html.toLowerCase().includes('numpy'), 'Must include Lecture 7 title');
assert(html.includes('import numpy as np') || html.includes('numpy as np'), 'Must include NumPy import statement');
assert(html.includes('ndarray') || html.includes('numpy.ndarray'), 'Must include ndarray class');

// 1D vs 2D arrays & attributes
assert(html.includes('.dtype') || html.includes('dtype'), 'Must include dtype attribute');
assert(html.includes('.shape') || html.includes('shape'), 'Must include shape attribute');
assert(html.includes('.ndim') || html.includes('ndim'), 'Must include ndim attribute');
assert(html.includes('.size') || html.includes('size'), 'Must include size attribute');

// Iteration: row vs flat
assert(html.includes('.flat') || html.includes('flat'), 'Must include flat iterator');

// Creation utilities & ranges
assert(html.includes('np.zeros') || html.includes('zeros('), 'Must include np.zeros');
assert(html.includes('np.ones') || html.includes('ones('), 'Must include np.ones');
assert(html.includes('np.full') || html.includes('full('), 'Must include np.full');
assert(html.includes('np.arange') || html.includes('arange('), 'Must include np.arange');
assert(html.includes('np.linspace') || html.includes('linspace('), 'Must include np.linspace');

// Reshaping
assert(html.includes('reshape(') || html.includes('.reshape'), 'Must include reshape method');

// Arithmetic & Boolean operations
assert(html.includes('broadcasting') || html.includes('Broadcasting') || html.includes('Element-wise') || html.includes('element-wise'), 'Must include element-wise operations');
assert(html.includes('axis=0') && html.includes('axis=1'), 'Must include axis=0 and axis=1 reductions');

// Indexing and slicing
assert(html.includes('[1, 2]') || html.includes('[1,2]') || html.includes('[:, 0:2]') || html.includes('[:,-1]'), 'Must include multidimensional slicing');

// Transpose
assert(html.includes('transpose') || html.includes('.T'), 'Must include transpose');

// Vector memory layout SVG
assert(html.includes('<svg') && (html.includes('List') || html.includes('list')) && (html.includes('NumPy') || html.includes('ndarray')), 'Must include vector SVG comparing Python list vs NumPy ndarray');

// Slide count >= 18
const l7Slides = (html.match(/class="slide/g) || []).length;
assert(l7Slides >= 18, `Must have at least 18 slides for L07, currently has ${l7Slides}`);

console.log('✓ Task 2 Verification Passed for Presentation 04!');

