// Test script to verify index.html links, JupyterLab integration, and lab sheet links
const fs = require('fs');
const path = require('path');

const indexPath = path.resolve(__dirname, '../index.html');
if (!fs.existsSync(indexPath)) {
  console.error('FAIL: index.html does not exist');
  process.exit(1);
}

const html = fs.readFileSync(indexPath, 'utf-8');

let failed = 0;

function assert(condition, message) {
  if (!condition) {
    console.error(`FAIL: ${message}`);
    failed++;
  } else {
    console.log(`PASS: ${message}`);
  }
}

// 1. Verify JupyterLab link presence
const jupyterUrl = 'https://jupyter.org/try-jupyter/lab/';
assert(html.includes(jupyterUrl), `index.html contains ${jupyterUrl}`);

// 2. Count JupyterLab links in DOM
const jupyterLinks = html.match(/href="https:\/\/jupyter\.org\/try-jupyter\/lab\/"[^>]*>/g) || [];
assert(jupyterLinks.length >= 4, `Found ${jupyterLinks.length} JupyterLab links in HTML (expected at least 4: nav, core, shortcuts, footer)`);

// 3. Verify security attributes on all JupyterLab links
jupyterLinks.forEach((linkTag, idx) => {
  assert(linkTag.includes('target="_blank"'), `JupyterLab link #${idx + 1} has target="_blank"`);
  assert(linkTag.includes('rel="noopener'), `JupyterLab link #${idx + 1} has rel="noopener"`);
});

// 4. Verify all 5 deck links
for (let i = 1; i <= 5; i++) {
  const deckNo = String(i).padStart(2, '0');
  const deckFile = `python_presentation_${deckNo}.html`;
  assert(html.includes(`href="${deckFile}"`), `Contains link to deck ${deckFile}`);
}

// 5. Verify all 5 interactive HTML lab sheets
for (let i = 1; i <= 5; i++) {
  const labRegex = new RegExp(`Lab_0${i}_Exercise_[^"']+\\.html`);
  assert(labRegex.test(html), `Contains link to HTML lab sheet 0${i}`);
  const mdRegex = new RegExp(`Lab_0${i}_Exercise_[^"']+\\.md`);
  assert(mdRegex.test(html), `Contains link to raw Markdown source 0${i}`);
}

// 6. Verify shortcut key 'J' handler
assert(html.includes("e.key === 'j'") || html.includes("e.key === 'J'"), "Keyboard shortcut handler supports key 'j'");

if (failed > 0) {
  console.error(`\n${failed} assertions failed.`);
  process.exit(1);
} else {
  console.log('\nAll index.html verification checks passed successfully!');
}

