// Verification test for Back-to-Portal button and keyboard navigation in all 5 slide decks
const fs = require('fs');
const path = require('path');

const decks = [
  'python_presentation_01.html',
  'python_presentation_02.html',
  'python_presentation_03.html',
  'python_presentation_04.html',
  'python_presentation_05.html'
];

let failed = 0;

function assert(condition, message) {
  if (!condition) {
    console.error(`FAIL: ${message}`);
    failed++;
  } else {
    console.log(`PASS: ${message}`);
  }
}

console.log('Testing Back to Portal navigation across all presentation decks...');

decks.forEach((deckFile) => {
  const filePath = path.resolve(__dirname, '..', deckFile);
  if (!fs.existsSync(filePath)) {
    assert(false, `${deckFile} exists`);
    return;
  }

  const html = fs.readFileSync(filePath, 'utf-8');

  // 1. Back button element presence
  const hasButton = html.includes('class="portal-back-btn"') || html.includes('portal-back-btn');
  assert(hasButton, `${deckFile} contains .portal-back-btn element`);

  // 2. Links to index.html
  const hasPortalLink = /<a[^>]*href=["']index\.html["'][^>]*class=["'][^"']*portal-back-btn[^"']*["']/.test(html) ||
                        /<a[^>]*class=["'][^"']*portal-back-btn[^"']*["'][^>]*href=["']index\.html["']/.test(html);
  assert(hasPortalLink, `${deckFile} portal button links directly to index.html`);

  // 3. CSS styling
  const hasCss = html.includes('.portal-back-btn') && html.includes('position: fixed');
  assert(hasCss, `${deckFile} contains fixed CSS styling for .portal-back-btn`);

  // 4. Keyboard shortcuts (KeyH / KeyP / Escape returning to index.html)
  const hasKeyH = html.includes("'KeyH'") || html.includes('"KeyH"');
  const hasEscape = html.includes("'Escape'") || html.includes('"Escape"');
  assert(hasKeyH, `${deckFile} handles KeyH shortcut for returning to portal`);
  assert(hasEscape, `${deckFile} handles Escape shortcut for returning to portal`);
});

if (failed > 0) {
  console.error(`\nTest suite finished with ${failed} failures.`);
  process.exit(1);
} else {
  console.log('\nAll Back to Portal checks passed successfully across all 5 slide decks!');
}
