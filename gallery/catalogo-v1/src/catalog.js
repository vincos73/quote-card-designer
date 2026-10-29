(() => {
  const data = JSON.parse(document.getElementById('style-data').textContent);
  const grid = document.getElementById('style-grid');
  const search = document.getElementById('search-input');
  const filter = document.getElementById('family-filter');
  const nav = document.getElementById('family-nav');
  const count = document.getElementById('result-count');
  const empty = document.getElementById('empty-state');
  const reset = document.getElementById('reset-filters');
  const status = document.getElementById('copy-status');
  const dialog = document.getElementById('zoom-dialog');
  let category = '';
  let lastTrigger = null;
  let statusTimer;
  const normalize = text => text.toLocaleLowerCase('it').normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  const categories = [{id: '', name: 'Tutti gli stili'}, ...data.families];
  for (const family of categories) {
    const button = document.createElement('button');
    button.type = 'button'; button.className = 'family-button'; button.dataset.category = family.id;
    button.setAttribute('aria-pressed', String(!family.id));
    const label = document.createElement('span'); label.textContent = family.name;
    const amount = document.createElement('span'); amount.className = 'family-count';
    amount.textContent = family.id ? data.items.filter(item => item.family === family.id).length : data.items.length;
    button.append(label, amount);
    button.addEventListener('click', () => { category = family.id; filter.value = category; render(); });
    nav.append(button);
    if (family.id) { const option = document.createElement('option'); option.value = family.id; option.textContent = family.name; filter.append(option); }
  }
  function render() {
    const query = normalize(search.value.trim());
    const visible = data.items.filter(style => (!category || style.family === category) && (!query || normalize([style.name, style.summary, style.familyName, style.exampleLabel, ...(style.aliases || [])].join(' ')).includes(query)));
    grid.replaceChildren(...visible.map(createCard));
    count.textContent = `${visible.length} ${visible.length === 1 ? 'stile' : 'stili'}${category || query ? ` di ${data.items.length}` : ''}`;
    empty.hidden = visible.length !== 0;
    reset.hidden = !(category || query);
    nav.querySelectorAll('.family-button').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.category === category)));
  }
  function createCard(style) {
    const card = document.createElement('article'); card.className = 'style-card'; card.dataset.styleId = style.id;
    const sample = document.createElement('button'); sample.type = 'button'; sample.className = 'sample-button'; sample.setAttribute('aria-label', `Ingrandisci esempio di ${style.name}`);
    const image = document.createElement('img'); image.src = style.asset; image.alt = `Esempio visivo dello stile ${style.name}`; image.width = style.width; image.height = style.height; image.loading = 'lazy'; image.decoding = 'async';
    const hint = document.createElement('span'); hint.className = 'zoom-hint'; hint.setAttribute('aria-hidden', 'true'); hint.innerHTML = "<svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M8 4H4v4m12-4h4v4M4 16v4h4m12-4v4h-4\"/></svg>"; sample.append(image, hint);
    sample.addEventListener('click', () => {
      lastTrigger = sample; document.getElementById('dialog-title').textContent = style.name;
      const image = document.getElementById('dialog-image'); image.src = style.asset; image.alt = `Esempio visivo ingrandito dello stile ${style.name}`; image.width = style.width; image.height = style.height;
      document.getElementById('dialog-caption').textContent = `${style.exampleLabel || 'Esempio'} · ${style.familyName}`; dialog.showModal();
    });
    const row = document.createElement('div'); row.className = 'card-row';
    const heading = document.createElement('h2'); heading.className = 'card-title';
    const number = document.createElement('span'); number.className = 'card-number'; number.textContent = String(style.index).padStart(2, '0'); heading.append(number, document.createTextNode(style.name));
    const copy = document.createElement('button'); copy.type = 'button'; copy.className = 'copy-button'; copy.innerHTML = "<svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><rect x=\"8\" y=\"8\" width=\"12\" height=\"12\" rx=\"1\"/><path d=\"M16 8V4H4v12h4\"/></svg><span>Copia nome</span>"; copy.setAttribute('aria-label', `Copia nome ${style.name}`); copy.addEventListener('click', () => copyName(style.name));
    row.append(heading, copy);
    const meta = document.createElement('p'); meta.className = 'card-meta'; meta.textContent = 'Incluso nella 0.4.0';
    const details = document.createElement('details'); details.className = 'card-details';
    const summary = document.createElement('summary'); summary.textContent = 'Dettagli';
    const description = document.createElement('p'); description.textContent = style.summary;
    const family = document.createElement('p'); family.className = 'card-family'; family.textContent = style.familyName;
    details.append(summary, description, family); card.append(sample, row, meta, details); return card;
  }
  async function copyName(name) {
    clearTimeout(statusTimer);
    let copied = false;
    try { await navigator.clipboard.writeText(name); copied = true; } catch {
      const helper = document.createElement('textarea'); helper.value = name; helper.readOnly = true; helper.className = 'clipboard-helper'; document.body.append(helper); helper.select();
      try { copied = document.execCommand('copy'); } catch { copied = false; } helper.remove();
    }
    status.textContent = copied ? `Nome copiato: ${name}` : `Copia non disponibile. Seleziona e copia questo nome: ${name}`;
    statusTimer = setTimeout(() => { status.textContent = ''; }, 5000);
  }
  function clearFilters() { category = ''; filter.value = ''; search.value = ''; render(); search.focus(); }
  reset.addEventListener('click', clearFilters); document.getElementById('reset-empty').addEventListener('click', clearFilters);
  filter.addEventListener('change', () => { category = filter.value; render(); }); search.addEventListener('input', render);
  document.getElementById('dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => { if (lastTrigger && document.contains(lastTrigger)) lastTrigger.focus(); });
  document.addEventListener('keydown', event => { if (event.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName) && !dialog.open) { event.preventDefault(); search.focus(); } });
  render();
})();
