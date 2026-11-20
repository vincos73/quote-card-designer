// Serve the catalog build on localhost, then run with Node, Playwright and Chromium:
// node gallery/catalogo-v1/tests/browser.cjs http://127.0.0.1:8000
// Set BROWSER_CHANNEL=chrome to use an installed Chrome instead of bundled Chromium.
const assert = require('node:assert/strict');
const { test } = require('node:test');
const { chromium } = require('playwright');

test('confronto delle proposte e ricerca per tecnica', async t => {
  const base = new URL(process.argv[2]);
  const browser = await chromium.launch({channel: process.env.BROWSER_CHANNEL});
  t.after(() => browser.close());
  const page = await browser.newPage({permissions: ['clipboard-read', 'clipboard-write']});
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const cards = page.locator('article[data-style-id]');
  const visibleIds = () => cards.evaluateAll(nodes => nodes.map(node => node.dataset.styleId));
  const ids = ['linocut', 'cyanotype', 'notebook-sketch'];
  const comparison = new URL(base);
  comparison.searchParams.set('confronta', ids.join(','));

  for (const width of [1440, 768, 390, 320]) {
    await page.setViewportSize({width, height: 900});
    await page.goto(comparison.href);
    await cards.first().waitFor();
    assert.deepEqual(await visibleIds(), ids);
    await cards.locator('img').evaluateAll(images => Promise.all(images.map(image => image.decode())));
    const boxes = await cards.evaluateAll(nodes => nodes.map(node => node.getBoundingClientRect().toJSON()));
    assert.ok(boxes.every(box => box.top === boxes[0].top && box.right <= width));
    assert.ok(boxes[1].left >= boxes[0].right && boxes[2].left >= boxes[1].right);
  }

  await page.getByRole('button', {name: 'Ingrandisci esempio di Cyanotype'}).click();
  assert.equal(await page.getByRole('dialog').getByRole('heading').innerText(), 'Cyanotype');
  await page.keyboard.press('Escape');
  await page.getByRole('button', {name: 'Copia nome Cyanotype'}).click();
  assert.equal(await page.evaluate(() => navigator.clipboard.readText()), 'Cyanotype');
  await page.getByRole('link', {name: 'Tutti gli stili'}).click();
  const total = await cards.count();
  assert.ok(total > 3);
  const search = page.getByRole('searchbox');
  const searches = [
    ['stampa a secco', ['embossed-paper', 'embossed-paper-raised']],
    ['cianotipia', ['cyanotype']], ['linoleografia', ['linocut']],
    ['pittura a spatola', ['palette-knife-painting']], ['Liberty', ['art-nouveau']],
    ['costruttivismo', ['constructivist']],
  ];
  for (const [query, expected] of searches) {
    await search.fill(query);
    assert.deepEqual(await visibleIds(), expected, query);
  }
  await search.fill('zzzz');
  assert.equal(await cards.count(), 0);
  await page.getByRole('button', {name: 'Azzera i filtri', exact: true}).click();
  assert.equal(await cards.count(), total);

  for (const query of ['linocut,cyanotype', 'linocut,linocut,cyanotype', 'linocut,cyanotype,inesistente']) {
    comparison.searchParams.set('confronta', query);
    await page.goto(comparison.href);
    await search.waitFor();
    assert.equal(await cards.count(), total);
  }
  assert.deepEqual(errors, []);
});
