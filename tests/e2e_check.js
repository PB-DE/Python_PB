const fs = require('fs');
const path = require('path');
const assert = require('assert');

const filePath = path.join(__dirname, '..', 'python_presentation.html');

console.log('Running End-to-End Presentation Verification...');

const html = fs.readFileSync(filePath, 'utf8');

// 1. File size check (< 250KB)
const stats = fs.statSync(filePath);
const sizeKb = Math.round(stats.size / 1024);
console.log(`- File Size: ${sizeKb} KB (Target: < 250 KB)`);
assert(sizeKb < 250, `File size should be lightweight, currently ${sizeKb} KB`);

// 2. Well-formed HTML structure
assert(html.startsWith('<!DOCTYPE html>'), 'Must start with <!DOCTYPE html>');
assert(html.includes('</html>'), 'Must close </html>');
assert(html.includes('</head>') && html.includes('<body>'), 'Must have standard HTML sections');

// 3. Slide IDs and count
const slideIdMatches = html.match(/id="slide-\d+"/g) || [];
console.log(`- Detected ${slideIdMatches.length} slides with distinct IDs`);
assert(slideIdMatches.length === 35, `Expected exactly 35 slides, found ${slideIdMatches.length}`);

// Check uniqueness
const idSet = new Set(slideIdMatches);
assert(idSet.size === 35, 'All slide IDs must be unique');

// Check consecutive 1 to 35
for (let i = 1; i <= 35; i++) {
  assert(html.includes(`id="slide-${i}"`), `Missing slide-${i}`);
}

// 4. Zero broken images
const imgMatches = html.match(/<img[^>]+>/g) || [];
assert(imgMatches.length === 0, `All graphics should be inline vector SVGs, found ${imgMatches.length} <img> tags`);

// 5. Verification of 3 inline vector diagrams
assert(html.includes('CENTRAL PROCESSING UNIT') && html.includes('Arithmetic Logic Unit (ALU)'), 'Computer Architecture SVG complete');
assert(html.includes('Address: 0x7f8a') && html.includes('3.14156'), 'Shallow vs Deep Copy SVG complete');
assert(html.includes('Transistors') && html.includes('Time (Years)'), 'Moore Law Curve SVG complete');

// 6. Zero external network resources
assert(!html.includes('http://') && !html.includes('https://'), 'Must be 100% self-contained offline with zero external CDNs');

console.log('✓ End-to-End Automated Verification Passed Perfectly!');
