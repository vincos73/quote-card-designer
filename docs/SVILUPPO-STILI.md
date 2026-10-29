# Libreria condivisa fra portatile e iMac

## Catalogo pubblico e installazione · 29 ottobre 2026

Il catalogo pubblico collegato dalla skill è allineato alla **0.5.0**:
**103 stili in 11 categorie**, Sites versione **6**. Sono conservati accesso
pubblico, logo, font e interazioni della versione 5, oltre alle 50 schede
precedenti. La gallery di sviluppo resta alla versione 68.
[Ricevuta](../gallery/catalogo-v1/pubblicazione-v6.json) e
[verifiche](../gallery/catalogo-v1/qa-0.5.0.json).

L'installazione locale di questa sessione è stata aggiornata dallo ZIP 0.5.0,
con copia di ripristino e identità verificata dei 273 file. L'aggiornamento
locale non si propaga agli altri computer: usare lo stesso ZIP della release.

## Release 0.5.0 · 29 ottobre 2026

La release GitHub **0.5.0** comprende **103 stili**: i 50 già distribuiti più
**tutti i 53 candidati** presenti nel catalogo prima di questa pubblicazione.
La libreria di sviluppo mantiene 130 stili, con 27 sperimentali fuori release.
I candidati promossi non sono più marcati `v1_shortlisted`; la selezione e il
catalogo incluso coincidono. La release incorpora anche la nuova guida alla
scelta dello stile e le correzioni del flusso di creazione e modifica.

Il pacchetto contiene 75 librerie compositive e 273 file. Le regole visive dei
nuovi profili sono conservate; cambia lo stato di disponibilità. Per i dettagli
consultare [note](../releases/0.5.0.md) e [manifesto](../releases/0.5.0-manifest.json).

La pubblicazione della release non aggiorna l'installazione locale o i Sites.
La gallery Sites resta alla versione 68 annotata nello sviluppo locale e il catalogo pubblico
può mostrare una selezione precedente. Un successivo allineamento dovrà
conservare accessi, materiali online e distinzione fra gallery e catalogo.

## Stato precedente · 29 ottobre 2026

Dopo le dodici candidature richieste dall'utente, la libreria comprende
**127 stili: 50 nella release 0.4.0, 46 candidati e 31 sperimentali**.
Nomi correnti: **Chalkboard**, **Cartographic**, **Civic**, **Food** e
**Sport**; gli identificatori delle cartelle e i nomi precedenti come alias
sono conservati. La gallery Sites versione **61** mantiene la sua selezione
di 122 stili e 262 immagini, con 46 candidati. Non aggiunge i cinque studi
presenti soltanto nella build locale e non cambia la release o l'installazione.

[Ricevuta della pubblicazione](../gallery/pubblicazione-v61.json).

## Riconciliazione iniziale

Il repository conserva la libreria di sviluppo; le release distribuiscono una
selezione approvata. Il 29 ottobre 2026 la riconciliazione della sorgente Sites
versione 60 con la libreria locale ha raccolto **127 stili**: **50 nella release
0.4.0, 34 candidati e 43 sperimentali**. La gallery pubblicata ne contiene 122;
cinque studi sono soltanto locali. Salvare uno stile su GitHub non lo promuove
alla release e non pubblica una nuova versione del sito.

## Dove lavorare

- `references/catalogo-stili.yaml`: indice di tutti i 130 stili. Per ogni voce,
  seguire il campo `profile`, che può indicare una variante specifica.
- `references/styles/<id>/`: profili, composizioni, esempi, prompt, ricerche e
  note disponibili. I materiali storici sono conservati accanto alle revisioni.
- `references/catalogo-v1.yaml`: indice dei 103 stili distribuiti nella 0.5.0.
  La versione installata della skill legge questo catalogo, non tutta la libreria.
- `gallery/source-profiles/sites-v60/`: YAML esatti estratti dalle 122 schede
  della gallery, comprese le composizioni incorporate.
- `gallery/reconciliation/2026-10-29.json`: provenienza, hash degli esempi,
  differenze fra profili, risorse recuperate e riferimenti ancora mancanti.

I campi storici hanno questi significati:

| Stato | `release_candidate` | `v1_shortlisted` |
| --- | --- | --- |
| Incluso nella release | `true` | `false` o assente |
| Candidato alla prossima selezione | `false` | `true` |
| Sperimentale | `false` | `false` o assente |

Non attivare entrambi i campi. Il nome storico `release_candidate` indica
l'inclusione nella release, non il badge Candidates della gallery.

## Passare da un computer all'altro

Usare su entrambe le macchine un clone di `vincos73/quote-card-designer`, con il
branch `main` come base condivisa. All'inizio di una sessione:

```sh
git status --short
git pull --ff-only
```

Se ci sono modifiche locali, conservarle e riconciliarle prima di aggiornare;
non usare reset, checkout forzati o copie dell'intera cartella per sovrascriverle.
Se `--ff-only` segnala una divergenza, confrontare i commit dei due computer.

Durante il lavoro, aggiungere lo stile in `references/styles/<id>/` e aggiornare
la sua voce nel catalogo esteso. Conservare i PNG nativi e i prompt quando
disponibili; indicare i limiti delle prove. Prima di cambiare macchina:

```sh
git diff --check
python3 gallery/build.py
git add references/styles/<id> references/catalogo-stili.yaml
git commit -m "Update <id> development style"
git push origin main
```

Includere nel commit anche gli eventuali script o documenti effettivamente
modificati. Se due sessioni lavorano contemporaneamente sugli stessi file,
usare branch distinti e confrontare le modifiche prima di unirle a `main`.

## Verifiche e release

```sh
python3 -m pip install -r gallery/requirements.txt
python3 gallery/build.py
python3 gallery/validate.py
python3 gallery/package_skill.py --output /tmp/quote-card-designer-verifica.zip
```

Usare una destinazione ZIP nuova a ogni esecuzione. Il generatore della release
verifica la selezione separata e include soltanto i suoi profili e dipendenze.
La riconciliazione del 29 ottobre conserva identici i 150 file della release
0.4.0. Non crea una release di sviluppo né cambia la skill globale installata.

## Limiti del recupero dalla gallery

Gli esempi nelle directory `gallery-v60/` sono i file serviti dal sito: alcuni
sono JPEG compressi, altri PNG. Non sono tutti originali nativi. Le risorse
supplementari disponibili nella sorgente Sites sono conservate in
`risorse-sites-v60/`; i file citati nei profili ma non recuperabili sono elencati
nel registro e nei documenti `PROVENIENZA.md` dei rispettivi stili. Recuperarli
dall'altro computer quando disponibili, senza inventare prompt o note mancanti.

Cinque stili avevano profili diversi fra libreria locale e gallery. Per i quattro
fuori release il catalogo punta alla variante `profilo-gallery-v60.yaml`,
conservando il profilo locale precedente. Futurismo Italiano conserva il profilo
distribuito: nella gallery differisce il nome. Tutti gli YAML pubblicati sono
comunque archiviati integralmente.

La build riunisce anche i cinque studi assenti dalla gallery: Cosmic Wireframe
Grid, Ethereal Editorial, Faceted Ink, Halftone Editorial sperimentale e Literary
Editorial. Non pubblicare la build completa su Sites senza una richiesta che
comprenda anche questi studi. GitHub può contenere tutti gli esperimenti anche
quando il sito mantiene una selezione diversa.
