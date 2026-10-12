const fs = require('fs');
const path = require('path');
const assert = require('assert');

const filePath = path.join(__dirname, '..', 'python_presentation_04.html');

console.log('Running Task 4: End-to-End Verification for python_presentation_04.html...');

assert(fs.existsSync(filePath), 'Target file must exist');
const html = fs.readFileSync(filePath, 'utf8');

// 1. File size check (lightweight requirement: < 250 KB)
const stats = fs.statSync(filePath);
const fileSizeKB = stats.size / 1024;
console.log(`File size: ${fileSizeKB.toFixed(2)} KB (Target: < 250 KB)`);
assert(fileSizeKB < 250, `File size should be < 250 KB, currently ${fileSizeKB.toFixed(2)} KB`);

// 2. Zero external dependencies
assert(!html.includes('http://') && !html.includes('https://'), 'Must not contain external HTTP/HTTPS CDN references');

// 3. Exactly 36 unique slide IDs (slide-1 to slide-36)
const slideMatches = html.match(/class="slide[^"]*" id="([^"]+)"/g) || [];
console.log(`Total slides found: ${slideMatches.length}`);
assert.strictEqual(slideMatches.length, 36, `Expected exactly 36 slides, found ${slideMatches.length}`);

for (let i = 1; i <= 36; i++) {
  assert(html.includes(`id="slide-${i}"`), `Slide with id="slide-${i}" must exist`);
}

// 4. Balanced tags check
const openSections = (html.match(/<section/g) || []).length;
const closeSections = (html.match(/<\/section>/g) || []).length;
assert.strictEqual(openSections, closeSections, `Unbalanced <section> tags: ${openSections} opened, ${closeSections} closed`);
assert.strictEqual(openSections, 36, `Expected exactly 36 <section> tags, found ${openSections}`);

// 5. Check no image tags pointing to non-existent local paths
const imgMatches = html.match(/<img[^>]+src="([^">]+)"/g) || [];
imgMatches.forEach(imgTag => {
  const src = imgTag.match(/src="([^">]+)"/)[1];
  const fullPath = path.resolve(path.dirname(filePath), src);
  assert(fs.existsSync(fullPath), `Image source ${src} must exist locally`);
});

// 6. SVG validation
const openSvgs = (html.match(/<svg/g) || []).length;
const closeSvgs = (html.match(/<\/svg>/g) || []).length;
assert.strictEqual(openSvgs, closeSvgs, `Unbalanced <svg> tags: ${openSvgs} opened, ${closeSvgs} closed`);
assert(openSvgs >= 2, `Must contain at least 2 inline SVGs (Memory Diagram & Tokenization Pipeline), found ${openSvgs}`);

// Diagram specific checks
assert(html.includes('Python List') && html.includes('NumPy ndarray'), 'Memory Diagram must contain comparison labels');
assert(html.includes('Tokenization &amp; Joining Pipeline') || html.includes('Tokenization'), 'Pipeline Diagram must contain pipeline labels');

// 7. Clean Branding & Footer
assert(html.includes('Civil Aviation Training Center (CATC)'), 'Footer must contain CATC branding');
assert(!html.includes('Computer Science'), 'Presentation must NOT contain "Computer Science"');

console.log('✓ All End-to-End checks passed successfully for Presentation 04!');
