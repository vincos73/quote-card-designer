"""Build the Sites gallery from the skill and its gallery-only image sources."""
from pathlib import Path
import html
import re
import subprocess
import yaml
from style_resources import load_style_document

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT
GALLERY = ROOT / 'gallery'
SOURCE_ASSETS = GALLERY / 'source-assets'
DESTINATION = GALLERY / 'dist/index.html'
PREVIEWS = DESTINATION.parent / 'assets'
EXAMPLES = [
    {'suffix': '', 'label': 'La domanda', 'text': '«Una buona domanda sposta il confine.»'},
    {'suffix': '-2', 'label': 'Le idee', 'text': '«Le idee crescono quando cambiano prospettiva.»'},
]
MODE_LABELS = {'typeset': 'Impaginazione', 'hybrid': 'Ibrida', 'generative': 'Generativa'}

CSS = r'''
:root{color-scheme:light;--paper:#f6f5f1;--ink:#222320;--muted:#62635d;--line:#d5d5cd;--focus:#155944}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;-webkit-font-smoothing:antialiased}::selection{background:#cce0d5;color:#112f23}button,input,summary{font:inherit}button,a,summary{touch-action:manipulation}a{color:inherit;text-underline-offset:4px}button{color:inherit}button,summary{cursor:pointer}:focus-visible{outline:3px solid var(--focus);outline-offset:5px}button:disabled{cursor:default}button,input{border-radius:0}button{background:none}input{caret-color:var(--focus)}[hidden]{display:none!important}
.skip{position:absolute;left:20px;top:-100px;padding:10px;background:#fff;z-index:5}.skip:focus{top:12px}.wrap{max-width:1344px;margin:0 auto;padding:0 48px}.masthead{display:flex;justify-content:space-between;align-items:center;gap:20px;padding:28px 0;border-bottom:1px solid var(--ink);font-size:14px}.wordmark{font-weight:700;letter-spacing:-.02em}.edition{color:var(--muted)}.intro{padding:48px 0 28px;display:grid;grid-template-columns:1.35fr 1fr;gap:40px;align-items:end}h1{font-size:clamp(36px,4vw,58px);font-weight:600;line-height:1.05;letter-spacing:-.04em;margin:0 0 18px;text-wrap:balance}.intro p{max-width:60ch;margin:0;color:var(--muted);font-size:17px}.shared-quote{padding:0 0 3px;margin:0}.shared-quote p{font-size:23px;color:var(--ink);line-height:1.35;letter-spacing:-.025em}.shared-quote figcaption{font-size:13px;color:var(--muted);margin-top:10px}.toolbar{display:flex;justify-content:space-between;align-items:end;gap:24px;border-top:1px solid var(--line);padding:24px 0 32px}.searchbox{display:block;max-width:420px;flex:1}.searchbox>span:first-child{font-size:13px;font-weight:600;display:block;margin-bottom:8px}.input-wrap{display:flex;align-items:center;gap:10px;background:#fff;border:1px solid #b5b6ae;padding:11px 14px}.input-wrap svg{width:19px;height:19px;flex:none;color:var(--muted)}input{background:transparent;border:0;outline:0;width:100%;min-width:0;color:var(--ink);font-size:15px}input::placeholder{color:#696a63}.input-wrap:focus-within{outline:2px solid var(--focus);outline-offset:2px}input:focus-visible{outline:0}.toolbar-right{display:flex;align-items:center;gap:22px}.count{font-size:13px;color:var(--muted);white-space:nowrap}.text-button{border:0;padding:8px 0;font-size:14px;text-decoration:underline;text-underline-offset:5px}.text-button:hover{color:var(--focus)}
.gallery{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:44px 28px;align-items:start;padding-bottom:56px}.style{min-width:0}.preview{padding:0;border:0;display:block;width:100%;position:relative;overflow:hidden;aspect-ratio:4/5;background:#e6e5df}.preview img{display:block;width:100%;height:100%;object-fit:contain}.preview-hint{position:absolute;bottom:12px;right:12px;background:#fff;color:#222;padding:6px 10px;font-size:12px;display:flex;align-items:center;gap:7px;opacity:0;transition:opacity .16s ease}.preview:hover .preview-hint,.preview:focus-visible .preview-hint{opacity:1}.preview-hint svg{width:14px;height:14px}.style-header{margin-top:18px;display:flex;gap:12px;justify-content:space-between;align-items:start}.style h2{margin:0;font-size:22px;line-height:1.2;font-weight:600;letter-spacing:-.025em;text-wrap:balance}.swatches{display:flex;gap:4px;margin:6px 0 0;flex-shrink:0}.swatch{display:block;width:13px;height:13px;border:1px solid #0002;border-radius:50%}.description{font-size:14px;color:var(--muted);margin:12px 0 18px;line-height:1.6;min-height:4.8em}.profile{border-top:1px solid var(--line);border-bottom:1px solid var(--line)}summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:14px;font-weight:600;padding:13px 0}summary::-webkit-details-marker{display:none}summary::after{content:'+';font-size:22px;font-weight:400;line-height:1}.profile[open]>summary::after{content:'−'}.profile-content{padding:0 0 20px}.profile-note{font-size:13px;line-height:1.6;color:var(--muted);margin:0 0 16px}.profile-actions{display:flex;align-items:center;gap:20px;margin-bottom:16px}.copy{font-size:13px;border:1px solid #a3a49b;padding:7px 12px;background:transparent}.copy:hover{background:#e7e8e0}.copy[disabled]{opacity:.65}.yaml{white-space:pre-wrap;overflow-wrap:anywhere;word-break:normal;max-height:520px;overflow:auto;scrollbar-width:thin;scrollbar-color:#999b90 #eeeee7;margin:0;padding:16px;background:#eeeee7;font:12px/1.65 ui-monospace,SFMono-Regular,Consolas,monospace;tab-size:2}.empty{padding:56px 0 90px;max-width:60ch}.empty p{color:var(--muted)}.footer{border-top:1px solid var(--ink);padding:22px 0 40px;display:flex;justify-content:space-between;gap:32px;color:var(--muted);font-size:12px}.footer p{margin:0;max-width:74ch}.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#222320;color:#fff;padding:12px 20px;max-width:calc(100% - 32px);font-size:14px;z-index:10}
dialog{padding:0;border:0;background:var(--paper);color:var(--ink);max-width:min(920px,calc(100vw - 32px));max-height:calc(100dvh - 32px);width:max-content}dialog::backdrop{background:#12130fe0}.dialog-bar{display:flex;justify-content:space-between;align-items:center;gap:30px;padding:14px 20px;border-bottom:1px solid var(--line)}.dialog-title{font-size:15px;font-weight:600;margin:0}.close{padding:6px 0;border:0;display:flex;align-items:center;gap:8px;font-size:14px}.close svg{width:18px;height:18px}.large-image{display:block;width:auto;height:auto;max-height:calc(100dvh - 116px);max-width:100%;margin:auto}body:has(dialog[open]){overflow:hidden}
@media(min-width:1000px){.style:has(.profile[open]){grid-column:1/-1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:28px;align-items:start}.style:has(.profile[open]) .style-info{min-width:0}.style:has(.profile[open]) .style-header{margin-top:0}.style:has(.profile[open]) .description{min-height:0;max-width:70ch}.style:has(.profile[open]) .yaml{max-height:440px}}
@media(max-width:999px){.wrap{padding:0 28px}.intro{gap:28px;grid-template-columns:1.25fr 1fr}.shared-quote p{font-size:20px}.gallery{grid-template-columns:repeat(2,minmax(0,1fr));gap:36px 24px}.toolbar-right{gap:14px}.style h2{font-size:21px}}
@media(max-width:600px){.wrap{padding:0 20px}.masthead{padding:20px 0;font-size:12px}.intro{display:block;padding:34px 0 24px}h1{font-size:39px;max-width:10ch;margin-bottom:16px}.intro p{font-size:16px}.shared-quote{margin-top:26px;padding:0 0 0 16px;border-left:1px solid var(--line)}.shared-quote p{font-size:20px;max-width:25ch}.shared-quote figcaption{font-size:12px;margin-top:6px}.toolbar{display:block;padding:20px 0 26px}.searchbox{max-width:none}.toolbar-right{justify-content:space-between;margin-top:12px}.gallery{grid-template-columns:minmax(0,1fr);gap:36px;padding-bottom:36px}.style-header{margin-top:16px}.style h2{font-size:24px}.description{font-size:15px;min-height:0;margin-bottom:16px}.preview-hint{opacity:1}.footer{display:block;padding-bottom:28px}.footer p+p{margin-top:12px}.yaml{font-size:12px;padding:12px;max-height:430px}dialog{max-width:calc(100vw - 20px);max-height:calc(100dvh - 20px)}.dialog-bar{padding:12px}.large-image{max-height:calc(100dvh - 100px)}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
@media print{.toolbar,.preview-hint,.skip,dialog,.toast,.profile-actions{display:none!important}.wrap{padding:0}.intro{padding:20px 0}.gallery{grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.style{break-inside:avoid}.style:has(.profile[open]){display:block;grid-column:auto}.yaml{max-height:none;overflow:visible}.footer{padding-bottom:0}}
.palette-note{font-size:11px;line-height:1.4;color:var(--muted);margin-top:4px;flex-shrink:0}.example-picker{display:flex;gap:8px;margin-top:10px}.example-picker button{flex:1;min-width:0;border:1px solid var(--line);padding:10px 6px;min-height:44px;font-size:13px;line-height:1.4}.example-picker button[aria-pressed="true"]{border-color:var(--ink);background:var(--ink);color:#fff}.example-picker button:hover:not([aria-pressed="true"]){background:#e7e8e0}.example-count{font-size:12px;color:var(--muted);margin:8px 0 0}.quote-list{list-style:none;margin:0;padding:0}.quote-list li+li{margin-top:12px}.shared-quote .quote-list p{font-size:18px}.examples{min-width:0}@media print{.example-picker,.example-count{display:none}.example-panel[hidden]{display:block!important}.example-panel+.example-panel{margin-top:12px}}
'''

CSS += r'''
.intro{grid-template-columns:minmax(0,1fr)}
.release-filters{border:0;margin:0 0 24px;padding:0;min-width:0}.release-filters legend{font-size:13px;font-weight:600;margin-bottom:10px;padding:0}.release-options{display:flex;flex-wrap:wrap;gap:10px 22px}.release-filter{display:flex;align-items:center;gap:9px;max-width:100%;cursor:pointer;font-size:14px}.release-filter input{width:18px;height:18px;min-width:18px;accent-color:var(--focus);margin:0}.release-filter input:focus-visible{outline:3px solid var(--focus);outline-offset:4px}.release-meta{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;margin-top:10px;font-size:12px;color:var(--muted)}.release-badge{background:#244932;color:#fff;padding:4px 8px}.pilot-badge{border:1px solid #35567c;color:#244866;padding:3px 8px}.release-note{font-size:13px;color:var(--muted);max-width:75ch;margin:0 0 24px}@media print{.release-filters,.release-note{display:none}}
.toolbar{flex-wrap:wrap;padding-bottom:18px}.toolbar-right{flex-wrap:wrap;column-gap:20px;row-gap:4px}.searchbox{min-width:0}.family-filters{border:0;margin:0 0 30px;padding:0;min-width:0}.family-filters legend{font-size:13px;font-weight:600;margin-bottom:10px;padding:0}.family-options{display:flex;flex-wrap:wrap;gap:8px}.family-option{display:inline-flex;align-items:center;justify-content:space-between;gap:12px;max-width:100%;min-height:44px;border:1px solid var(--line);padding:8px 12px;text-align:left;font-size:13px;line-height:1.4}.family-option[aria-pressed="true"]{border-color:var(--ink);background:var(--ink);color:#fff}.family-option:hover:not([aria-pressed="true"]),.family-tag:hover{border-color:var(--focus);background:#e7e8e0}.family-number{font-variant-numeric:tabular-nums;flex-shrink:0}.family-tag{display:inline-block;max-width:100%;margin-top:12px;border:1px solid var(--line);padding:5px 9px;font-size:12px;line-height:1.4;text-align:left;min-height:32px}.family-tag[aria-pressed="true"]{border-color:var(--focus);color:var(--focus)}.text-button:disabled{opacity:.55;text-decoration:none}.filter-note{font-size:13px;color:var(--muted);margin:10px 0 0}
@media(max-width:600px){.toolbar{padding-bottom:16px}.toolbar-right{gap:6px 18px}.family-filters{margin-bottom:24px}.family-options{gap:7px}.family-option{padding:8px 10px}.family-tag{min-height:40px}}
@media print{.family-filters,.reset-filters{display:none!important}.family-tag{border:0;padding:0;min-height:0}}
'''

CSS += r'''
.shortlist-badge{border:1px solid #8a5a17;background:#fff4df;color:#68410b;padding:3px 8px}
'''

JS = r'''
const search = document.getElementById('search');
const styles = [...document.querySelectorAll('.style')];
const count = document.getElementById('result-count');
const empty = document.getElementById('empty');
const expand = document.getElementById('expand-all');
const resetFilters = document.getElementById('reset-filters');
const releaseFilters = [...document.querySelectorAll('input[name="release-status"]')];
const familyOptions = [...document.querySelectorAll('.family-option')];
const familyTags = [...document.querySelectorAll('.family-tag')];
let selectedFamily = '';
const normalise = text => text.toLocaleLowerCase('it').normalize('NFD').replace(/[\u0300-\u036f]/g,'');
const visibleStyles = () => styles.filter(style => !style.hidden);
function updateExpand(){
  const visible = visibleStyles();
  const allOpen = visible.length && visible.every(style => style.querySelector('details').open);
  expand.textContent = allOpen ? 'Chiudi tutte le descrizioni' : 'Apri tutte le descrizioni';
  expand.disabled = !visible.length;
  expand.setAttribute('aria-expanded',String(Boolean(allOpen)));
}
function applyFilters(){
  const terms = normalise(search.value.trim()).split(/\s+/).filter(Boolean);
  const releaseStatus = releaseFilters.find(input => input.checked).value;
  styles.forEach(style => {
    const familyMatches = !selectedFamily || style.dataset.family === selectedFamily;
    const searchMatches = terms.every(term => normalise(style.dataset.search).includes(term));
    const releaseMatches = releaseStatus === 'all'
      || (releaseStatus === 'selected' && style.dataset.releaseCandidate === 'true')
      || (releaseStatus === 'shortlisted' && style.dataset.v1Shortlisted === 'true')
      || (releaseStatus === 'unreleased' && style.dataset.releaseCandidate === 'false');
    style.hidden = !(familyMatches && searchMatches && releaseMatches);
  });
  familyOptions.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.familyFilter === selectedFamily)));
  familyTags.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.familyFilter === selectedFamily)));
  const n = visibleStyles().length;
  count.textContent = n === styles.length ? `${n} stili` : `${n} di ${styles.length} stili`;
  empty.hidden = n !== 0;
  resetFilters.disabled = !selectedFamily && !search.value && releaseStatus === 'all';
  updateExpand();
}
search.addEventListener('input',applyFilters);
releaseFilters.forEach(input => input.addEventListener('change',applyFilters));
document.querySelectorAll('[data-family-filter]').forEach(button => button.addEventListener('click',()=>{
  selectedFamily = button.dataset.familyFilter;
  applyFilters();
}));
function clearFilters(){
  search.value = ''; selectedFamily = ''; releaseFilters[0].checked = true; applyFilters(); search.focus();
}
resetFilters.addEventListener('click',clearFilters);
document.getElementById('reset-search').addEventListener('click',clearFilters);
expand.addEventListener('click',()=>{
  const visible = visibleStyles();
  const target = !visible.every(style => style.querySelector('details').open);
  visible.forEach(style=>style.querySelector('details').open=target);
  updateExpand();
});
document.querySelectorAll('details').forEach(item=>item.addEventListener('toggle',updateExpand));
document.querySelectorAll('[data-example-target]').forEach(button=>button.addEventListener('click',()=>{
  const group=button.closest('.examples');
  group.querySelectorAll('.example-panel').forEach(panel=>panel.hidden=panel.id!==button.dataset.exampleTarget);
  group.querySelectorAll('[data-example-target]').forEach(option=>option.setAttribute('aria-pressed',String(option===button)));
  group.querySelector('.example-count').textContent=`Esempio ${button.dataset.exampleNumber} di ${group.querySelectorAll('.example-panel').length}`;
}));
let toastTimer;
function notify(text){
  const toast = document.getElementById('toast');
  toast.textContent=text;toast.hidden=false;
  clearTimeout(toastTimer);toastTimer=setTimeout(()=>{toast.hidden=true},3200);
}
async function copyText(text){
  if(navigator.clipboard && window.isSecureContext){
    try{await navigator.clipboard.writeText(text);return true;}catch{}
  }
  const field=document.createElement('textarea');
  field.value=text;field.style.cssText='position:fixed;top:0;left:0;opacity:0;';
  document.body.append(field);field.select();
  let copied=false;
  try{copied=document.execCommand('copy');}catch{}
  field.remove();return copied;
}
document.querySelectorAll('[data-copy]').forEach(button=>button.addEventListener('click',async()=>{
  const text=document.getElementById(button.dataset.copy).textContent;
  const copied=await copyText(text);button.focus({preventScroll:true});
  notify(copied ? 'Profilo completo copiato.' : 'Copia non disponibile: seleziona il testo del profilo e copialo manualmente.');
}));
const dialog=document.getElementById('image-dialog');
let trigger;
document.querySelectorAll('.preview').forEach(button=>button.addEventListener('click',()=>{
  trigger=button;
  const image=button.querySelector('img');
  const large=document.createElement('img');large.className='large-image';large.src=image.src;large.alt=image.alt;document.getElementById('image-slot').replaceChildren(large);
  document.getElementById('dialog-title').textContent=`${button.dataset.name} · Esempio ${button.dataset.example}`;
  dialog.showModal();
}));
document.getElementById('close-dialog').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close();});
dialog.addEventListener('close',()=>trigger?.focus({preventScroll:true}));
'''

ICONS = {
    'search': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/></svg>',
    'zoom': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5"/></svg>',
    'close': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>',
}

def escape(value):
    return html.escape(str(value), quote=True)

def palette(profile):
    colours = []
    def collect(value):
        if isinstance(value, dict):
            for child in value.values(): collect(child)
        elif isinstance(value, str) and re.fullmatch(r'#[0-9A-Fa-f]{6}', value):
            if value.upper() not in colours: colours.append(value.upper())
    collect(profile.get('Color Palette', {}))
    return colours[:5]

def image_uri(style, number, example):
    name = f'{style["id"]}{example["suffix"]}'
    image = SOURCE_ASSETS / f'{name}.png'
    if not image.is_file():
        key = 'example' if number == 1 else f'example_{number}'
        reference = style.get(key)
        if not reference:
            raise FileNotFoundError(f'Manca l’immagine sorgente per {style["id"]}, esempio {number}')
        image = SKILL / reference
    if not image.is_file():
        raise FileNotFoundError(f'Manca l’esempio grafico: {image}')
    preview = PREVIEWS / f'{name}.jpg'
    if not preview.exists() or image.stat().st_mtime > preview.stat().st_mtime:
        try:
            from PIL import Image
        except ImportError:
            if not subprocess.run(['which', 'sips'], capture_output=True).returncode == 0:
                raise RuntimeError('Installa Pillow: python3 -m pip install -r gallery/requirements.txt')
            subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '82',
                            '-Z', '1000', str(image), '--out', str(preview)],
                           check=True, capture_output=True)
        else:
            with Image.open(image) as source:
                source.thumbnail((1000, 1000))
                if source.mode != 'RGB':
                    source = source.convert('RGB')
                source.save(preview, 'JPEG', quality=82, optimize=True)
    return f'assets/{preview.name}'

def examples_for_style(style):
    examples = []
    count = style.get('example_count', len(EXAMPLES))
    if not isinstance(count, int) or count < 1:
        raise ValueError(f"example_count non valido per {style.get('id')}: {count}")
    for number in range(1, count + 1):
        default = EXAMPLES[number - 1] if number <= len(EXAMPLES) else {
            'suffix': f'-{number}', 'label': f'Esempio {number}', 'text': ''
        }
        prefix = 'example' if number == 1 else f'example_{number}'
        example = dict(default)
        for key in ('text', 'label'):
            example[key] = style.get(f'{prefix}_{key}', example[key])
        example['suffix'] = style.get(f'{prefix}_asset_suffix', example['suffix'])
        if not isinstance(example['suffix'], str) or not re.fullmatch(r'(?:|-\d+)', example['suffix']):
            raise ValueError(f"Suffix dell'esempio {number} non valido per {style.get('id')}")
        if not example['text']:
            raise ValueError(f"Manca il testo dell'esempio {number} per {style.get('id')}")
        examples.append(example)
    return examples

def build():
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    for stale_preview in PREVIEWS.glob('*.jpg'):
        stale_preview.unlink()
    catalog = yaml.safe_load((SKILL/'references/catalogo-stili.yaml').read_text())
    release_count = sum(bool(style.get('release_candidate')) for style in catalog['styles'])
    shortlist_count = sum(bool(style.get('v1_shortlisted')) for style in catalog['styles'])
    unreleased_count = len(catalog['styles']) - release_count
    families = catalog['families']
    family_by_id = {family['id']: family['name'] for family in families}
    if not families or len(family_by_id) != len(families):
        raise ValueError('Le famiglie devono avere ID unici e non essere vuote')
    family_counts = {family['id']: 0 for family in families}
    for style in catalog['styles']:
        if style.get('family') not in family_by_id:
            raise ValueError(f"Famiglia assente o sconosciuta per {style['id']}")
        family_counts[style['family']] += 1
    cards = []
    for style in catalog['styles']:
        identifier = style['id']
        family_id = style['family']
        family_name = family_by_id[family_id]
        is_candidate = bool(style.get('release_candidate'))
        is_shortlisted = bool(style.get('v1_shortlisted'))
        if is_candidate and is_shortlisted:
            raise ValueError(f'Stato V1 ambiguo per {identifier}: selezionato e candidate')
        method = MODE_LABELS.get(style.get('production_mode'), '')
        if (is_candidate or is_shortlisted) and not method:
            raise ValueError(f"Metodo di produzione assente o sconosciuto per {identifier}")
        pilot_tag = '<span class="pilot-badge">Test pilota</span>' if style.get('pilot_selected') else ''
        release_meta = f'<div class="release-meta"><span class="release-badge">Selezionata V1</span>{pilot_tag}<span>Metodo consigliato: {method}</span></div>' if is_candidate else ''
        if is_shortlisted:
            release_meta = '<div class="release-meta"><span class="shortlist-badge">V1 candidate</span></div>'
        profile_path = SKILL/style['profile']
        original = profile_path.read_text()
        document, resources = load_style_document(profile_path)
        if resources:
            original = yaml.safe_dump(document, allow_unicode=True, sort_keys=False, width=100)
        profile = {key: value for key, value in document.items() if key != 'Design Style'}
        profile.update(document['Design Style'])
        examples = examples_for_style(style)
        featured = style.get('featured_example', 1)
        if not isinstance(featured, int) or not 1 <= featured <= len(examples):
            raise ValueError(f'featured_example non valido per {identifier}: {featured}')
        panels, choices = [], []
        for number, example in enumerate(examples, 1):
            uri = image_uri(style, number, example)
            panel_id = f'{identifier}-example-{number}'
            hidden = ' hidden' if number != featured else ''
            panels.append(f'''<div class="example-panel" id="{panel_id}"{hidden}>
<button class="preview" data-name="{escape(style['name'])}" data-example="{number}" aria-label="Ingrandisci l’esempio {number} di {escape(style['name'])}">
<img src="{uri}" width="1122" height="1402" alt="{escape(style['name'])}, esempio {number}: {escape(example['text'])}" decoding="async">
<span class="preview-hint">{ICONS['zoom']} Ingrandisci</span></button></div>''')
            pressed = 'true' if number == featured else 'false'
            choices.append(f'<button data-example-target="{panel_id}" data-example-number="{number}" aria-controls="{panel_id}" aria-pressed="{pressed}">{number} · {escape(example["label"])}</button>')
        colours = palette(profile)
        swatches = ''.join(f'<span class="swatch" style="background:{c}" title="{c}"></span>' for c in colours)
        if colours:
            palette_info = f'<div class="swatches" role="img" aria-label="Alcuni colori del profilo: {", ".join(colours)}">{swatches}</div>'
        else:
            variable_palette = profile.get('Color Palette', {}).get('Fixed Colors') is False or 'ColorSystem' in profile
            label = 'Palette variabile' if variable_palette else 'Colori nel profilo'
            palette_info = f'<span class="palette-note">{label}</span>'
        search = ' '.join([style['name'], style['summary'], family_name, method, *style['tags'], *style['aliases'], *profile.get('Mood',[])])
        cards.append(f'''<article class="style" id="{identifier}" data-family="{escape(family_id)}" data-release-candidate="{str(is_candidate).lower()}" data-v1-shortlisted="{str(is_shortlisted).lower()}" data-production-mode="{escape(style.get('production_mode', ''))}" data-search="{escape(search)}">
<div class="examples">{''.join(panels)}<div class="example-picker" role="group" aria-label="Scegli un esempio di {escape(style['name'])}">{''.join(choices)}</div><p class="example-count" aria-live="polite">Esempio {featured} di {len(examples)}</p></div>
<div class="style-info"><div class="style-header"><h2>{escape(style['name'])}</h2>{palette_info}</div>
<button class="family-tag" data-family-filter="{escape(family_id)}" aria-controls="catalogo" aria-pressed="false" aria-label="Filtra per famiglia: {escape(family_name)}">{escape(family_name)}</button>
{release_meta}
<p class="description">{escape(style['summary'])}</p>
<details class="profile"><summary>Descrizione estesa</summary><div class="profile-content">
<p class="profile-note">Profilo integrale usato per guidare la generazione, con l’eventuale libreria di composizioni inclusa. Il soggetto e la composizione vengono scelti ogni volta in funzione della frase.</p>
<div class="profile-actions"><button class="copy" data-copy="profile-{identifier}">Copia il profilo</button></div>
<pre class="yaml" id="profile-{identifier}" lang="en" tabindex="0">{escape(original)}</pre>
</div></details></div></article>''')
    count=len(cards)
    family_filters = ''.join(
        f'<button class="family-option" data-family-filter="{escape(family["id"])}" aria-controls="catalogo" aria-pressed="false"><span>{escape(family["name"])}</span><span class="family-number">{family_counts[family["id"]]}</span></button>'
        for family in families
    )
    example_total=sum(len(examples_for_style(style)) for style in catalog['styles'])
    comparison_link = '<p style="margin-top:18px"><a href="confronto-test.html">Apri i confronti degli stili</a></p>' if (ROOT/'confronto-test.html').is_file() else ''
    page=f'''<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Il catalogo visivo degli stili di Quote Card Designer: esempi grafici, descrizioni e profili completi di generazione.">
<title>Catalogo degli stili · Quote Card Designer</title><style>{CSS}</style></head>
<body><a class="skip" href="#catalogo">Vai agli stili</a><div class="wrap">
<header class="masthead"><span class="wordmark">Quote Card Designer</span><span class="edition">{count} stili · {example_total} immagini</span></header>
<main><div class="intro"><div><h1>Catalogo degli stili</h1><p>Esplora gli esempi disponibili per ogni linguaggio visivo ed espandi la scheda per consultare il profilo completo.</p>{comparison_link}</div></div>
<section aria-label="Strumenti del catalogo" class="toolbar">
<label class="searchbox" for="search"><span>Cerca uno stile</span><span class="input-wrap">{ICONS['search']}<input id="search" type="search" placeholder="Nome, famiglia, atmosfera o tecnica" autocomplete="off" aria-controls="catalogo"></span></label>
<div class="toolbar-right"><span class="count" id="result-count" role="status" aria-live="polite">{count} stili</span><button class="text-button reset-filters" id="reset-filters" disabled>Azzera filtri</button><button class="text-button" id="expand-all" aria-controls="catalogo" aria-expanded="false">Apri tutte le descrizioni</button></div></section>
<fieldset class="family-filters"><legend>Filtra per famiglia</legend><div class="family-options"><button class="family-option" data-family-filter="" aria-controls="catalogo" aria-pressed="true"><span>Tutte le famiglie</span><span class="family-number">{count}</span></button>{family_filters}</div><p class="filter-note">I numeri indicano gli stili di ogni famiglia. Puoi combinare una famiglia con la ricerca.</p></fieldset>
<fieldset class="release-filters"><legend>Stato release</legend><div class="release-options">
<label class="release-filter"><input name="release-status" type="radio" value="all" aria-controls="catalogo" checked><span>Tutti ({count})</span></label>
<label class="release-filter"><input name="release-status" type="radio" value="selected" aria-controls="catalogo"><span>Selezionati V1 ({release_count})</span></label>
<label class="release-filter"><input name="release-status" type="radio" value="shortlisted" aria-controls="catalogo"><span>Candidates ({shortlist_count})</span></label>
<label class="release-filter"><input name="release-status" type="radio" value="unreleased" aria-controls="catalogo"><span>Non ancora nella release ({unreleased_count})</span></label>
</div></fieldset>
<p class="release-note">I metodi indicati sono consigli progettuali da verificare. Gli esempi possono precedere le ultime modifiche a font e palette.</p>
<section class="gallery" id="catalogo" aria-label="Stili disponibili">{''.join(cards)}</section>
<div id="empty" class="empty" hidden><h2>Nessuno stile trovato</h2><p>Prova un'altra ricerca o famiglia, oppure azzera i filtri per tornare al catalogo completo.</p><button class="copy" id="reset-search">Azzera i filtri</button></div></main>
<footer class="footer"><p>Il numero di esempi varia per stile. Soggetti, palette e composizioni possono variare; ogni immagine conserva il proprio testo di prova. Formato di riferimento verticale 4:5.</p><p>Catalogo degli stili · Quote Card Designer</p></footer></div>
<dialog id="image-dialog" aria-labelledby="dialog-title"><div class="dialog-bar"><h2 id="dialog-title" class="dialog-title"></h2><button id="close-dialog" class="close" autofocus>{ICONS['close']} Chiudi</button></div><div id="image-slot"></div></dialog>
<div class="toast" id="toast" role="status" aria-live="polite" hidden></div><script>{JS}</script></body></html>'''
    DESTINATION.write_text(page,encoding='utf-8')
    print(f'Catalogo creato: {DESTINATION} ({DESTINATION.stat().st_size/1024/1024:.2f} MB, {count} stili, {example_total} immagini)')

if __name__ == '__main__':
    build()
