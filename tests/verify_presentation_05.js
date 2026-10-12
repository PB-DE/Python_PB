const fs = require('fs');
const path = require('path');
const assert = require('assert');

const filePath = path.join(__dirname, '..', 'python_presentation_05.html');

console.log('Testing Task 1: Presentation 05 Engine Core & Theming...');

// 1. File exists
assert(fs.existsSync(filePath), 'python_presentation_05.html must exist');
const html = fs.readFileSync(filePath, 'utf8');
assert(html.length > 200, 'python_presentation_05.html must not be empty');

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

console.log('✓ Task 1 Verification Passed for Presentation 05!');

console.log('Testing Task 2: Lecture 9 Content & File I/O Vector Diagrams...');

// Check all 18 slides for Lecture 9
for (let i = 1; i <= 18; i++) {
  assert(html.includes(`id="slide-${i}"`), `Must contain slide-${i}`);
}

// Title and fundamentals
assert(html.toLowerCase().includes('lecture 9') && html.toLowerCase().includes('files'), 'Must include Lecture 9 and files in title');
assert(html.includes('fibonacci') || html.includes('Volatile'), 'Must contrast volatile memory with persistent storage');
assert(html.includes('sample_data.txt'), 'Must reference sample_data.txt');
assert(html.includes("mode='w'") || html.includes('mode="w"'), 'Must include write mode');
assert(html.includes("mode='r'") || html.includes('mode="r"'), 'Must include read mode');
assert(html.includes('with open'), 'Must include with open context manager');

// Slide 6 vector diagram
assert(html.includes('<svg') && html.includes('Stream Buffer'), 'Must include inline SVG File I/O lifecycle diagram in slide 6');

// Parsing and OS
assert(html.includes('line.split()'), 'Must include line.split() for line tokenization');
assert(html.includes('os.rename'), 'Must include os.rename');
assert(html.includes('os.remove') || html.includes('os library'), 'Must include os file operations');

// JSON processing
assert(html.includes('twitter_dict'), 'Must include twitter_dict');
assert(html.includes('Barack Obama') && html.includes('Elon Musk'), 'Must include twitter sample data');
assert(html.includes("twitter_dict['twitter'][2]['handle']") || html.includes("['twitter'][2]['handle']"), 'Must demonstrate nested navigation');
assert(html.includes('json.dump'), 'Must demonstrate json.dump');
assert(html.includes('json.load'), 'Must demonstrate json.load');
assert(html.includes('twitter_top5.json'), 'Must reference twitter_top5.json');

// Exceptions
assert(html.includes('FileNotFoundError'), 'Must demonstrate FileNotFoundError');
assert((html.includes('try:') || html.includes('try</span>:')) && html.includes('except'), 'Must demonstrate try-except block');
assert((html.includes('else:') || html.includes('else</span>:')) && (html.includes('finally:') || html.includes('finally</span>:')), 'Must demonstrate complete try-except-else-finally architecture');

console.log('✓ Task 2 Verification Passed for Presentation 05!');

console.log('Testing Task 3: Lecture 10 Content & OOP Memory Model Vector Diagram...');

// Check all 36 slides
for (let i = 1; i <= 36; i++) {
  assert(html.includes(`id="slide-${i}"`), `Must contain slide-${i}`);
}

// Lecture 10 title & paradigm
assert(html.toLowerCase().includes('lecture 10') && (html.toLowerCase().includes('object-oriented') || html.toLowerCase().includes('oop')), 'Must include Lecture 10 OOP in title');
assert(html.includes('Everything is an object') || html.includes('everything is an object'), 'Must include "Everything is an object" paradigm');
assert(html.includes('class TwitterAccount') || html.includes('TwitterAccount'), 'Must define TwitterAccount class');

// Constructor & self
assert(html.includes('__init__'), 'Must include __init__ constructor');
assert(html.includes('self.name') || html.includes('self.handle'), 'Must bind instance attributes via self');
assert(html.includes('elonmusk') || html.includes('Elon Musk'), 'Must instantiate elon object');

// Vector diagram in Slide 27
assert(html.includes('Class Blueprint') && html.includes('Heap Instances'), 'Must include vector diagram for OOP blueprint vs heap instances in slide 27');

// Instance methods & composition
assert(html.includes('add_follower'), 'Must include add_follower method');
assert(html.includes('followers[0]') || html.includes('followers'), 'Must demonstrate object composition with followers list');
assert(html.includes('get_number_followers'), 'Must include get_number_followers computed method');

// State mutation & privacy
assert(html.includes('boo_mastodon') || html.includes('elon.handle ='), 'Must demonstrate modifying object properties');
assert(html.includes('_userid') || html.includes('_id'), 'Must demonstrate private attribute convention with underscore');

// Magic methods
assert(html.includes('__str__'), 'Must demonstrate __str__ magic method');
assert(html.includes('__repr__'), 'Must compare __str__ with __repr__');

console.log('✓ Task 3 Verification Passed for Presentation 05!');
