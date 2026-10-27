# Categorie della gallery

Categorie riviste il 25 ottobre 2026. Catalogo aggiornato il 26 ottobre 2026: 69 stili pubblicati, 144 immagini e 11 categorie principali.

## Criterio

La categoria indica il linguaggio visivo che distingue lo stile. Non è una tassonomia di storia dell’arte: i repertori possono avere affinità trasversali, recuperabili con ricerca, tag e alias. Tecniche, soggetti e palette restano adattabili alla frase. Ogni stile compare una volta nei filtri principali.

## Cambiamenti principali

- Separati tipografia e geometrie; Neo Industrial entra nel disegno tecnico.
- Separati collage e fotomontaggi dai retini e dai processi di stampa.
- Distinte le immagini fotografiche da luce, superfici e materiali.
- Distinti gli strumenti di disegno e lettering dall’illustrazione e dalla decorazione.
- Sostituita l’etichetta generica «Repertori storici» con «Classici e incisioni». Psychedelic Art, Lowbrow e Vintage Horror passano all’illustrazione.
- Organic e Folk Art sono in illustrazione e decorazione; Handwritten in fotografia; Retro-futurism Art in collage; Digital Textile in luce e materiali.

## Assegnazioni pubblicate

| Categoria | Stili | Contenuto |
| --- | ---: | --- |
| Tipografia e impaginazione | 9 | Neo Swiss, Chromatic Type, Modern Minimalism, Condensed Editorial, Type Overprint, Dirty Brutalism, Neo Brutalism, ASCII Editorial, Literary Editorial |
| Geometrie e pattern | 7 | Optical, Analog Geometry, Interlocking Pop Geometry, Symbol Loom, Glyph Terrain, Neo Mondrian, Symbolic Modernism |
| Disegno tecnico e wireframe | 5 | Neo Industrial Editorial, Digital Blueprint, Signal Atlas, Cosmic Wireframe Grid, Architectural Isometric |
| Collage e fotomontaggio | 4 | Dada, Digital Collage, Vintage Collage, Retro-futurism Art |
| Retini e stampa | 7 | Halftone Editorial, Pixel Field, Threshold Mosaic, Newspaper, Risograph, Duotone Halftone, Halftone B/W |
| Fotografia e atmosfere | 7 | Surreal Editorial, Ethereal Editorial, Editorial Interlock, Oneiric Glow, Cinema Editorial, Handwritten, Blue Note |
| Luce e materiali | 4 | Digital Textile, Dynamic Gradient, Prismatic Flutes, Chromatic Liquid Metal |
| Disegno e lettering | 7 | Graffiti, Ink, Pencil, Calligraphic Brush, Faceted Ink, Watercolor, Ballpen |
| Illustrazione e decorazione | 8 | Child Design, Underground Comic, Organic, Folk Art, Psychedelic Art, Lowbrow, Vintage Horror, Futurismo Italiano |
| Classici e incisioni | 6 | Vintage Scientific Illustration, Classical Roman, Medieval Folio, Chinese Illustration, Ukiyo-e Editorial, Occult Editorial |
| Interfacce e cultura digitale | 5 | Cyberpunk Editorial, Glitch Editorial, Retro UI, Y2K, Editor Canvas |

## Sorgenti e verifica

Le definizioni e tutte le 69 assegnazioni sono in `references/catalogo-stili.yaml`. Handwritten, Psychedelic Art, Lowbrow e Vintage Horror sono stati recuperati dalla sorgente Sites e riallineati nella libreria locale insieme a Optical; la provenienza dei rispettivi profili e JPEG è documentata nelle cartelle degli stili.

La modifica riguarda categorie, filtri, spiegazioni, etichette e parole indicizzate della ricerca. Profili degli stili, immagini, testi delle card e stati di release sono conservati. La release V1 distribuita resta uno snapshot separato.

La validazione controlla copertura delle categorie, conteggi, coerenza delle etichette con la categoria della scheda, struttura della griglia e asset. Sintassi JavaScript verificata.

Verifica interattiva della revisione delle categorie del 25 ottobre:

- Tutti gli 11 filtri mostrano il numero atteso di schede e la propria descrizione.
- La combinazione Collage + Candidates restituisce Dada e Retro-futurism Art.
- Aggiungendo la ricerca «retro» rimane una sola scheda.
- Ricerca senza corrispondenze, stato vuoto e azzeramento verificati.
- Le etichette sulle schede attivano il filtro corretto; il reset ripristina 65 stili.

## Pubblicazione verificata

Pubblicata la versione Sites **21** il 25 ottobre 2026, sorgente
`befacf657019fb3be5c110d7fd0f50b79089269d`. La lettura della pagina online
conferma 65 stili, 136 immagini e tutti gli 11 filtri con i conteggi riportati.

[Apri la gallery](https://quote-card-designer-style-gallery.vincos.chatgpt.site/).

## Aggiornamenti del 26 ottobre 2026

La versione **22**, sorgente `2fb61d3930cb4dca98bbb89eb2c8f781880f1b2f`,
pubblica le revisioni approvate di Y2K cromo/olografico e Retro UI bitmap.
Ogni scheda offre due frasi diverse e il profilo con tre famiglie compositive.
Sono state conservate integralmente le altre 63 schede e tutti gli asset
precedenti. Ricerca, selettori, caricamento delle quattro immagini e
ingrandimento verificati nella sorgente destinata alla pubblicazione.

La versione **23**, sorgente `bb6358c372ea774bb122ac41095546f1e714233f`,
aggiunge **Futurismo Italiano** come **V1 candidate**, con due immagini.
La categoria è Illustrazione e decorazione; la selezione V1 resta di 20
stili e i candidates diventano 28. Le 65 schede precedenti e i loro asset
sono conservati integralmente.

Entrambi i deploy Sites sono riusciti. La pagina online della versione 23
conferma 66 stili, 138 immagini e il nuovo badge; il filtro Candidates e
il selettore dei due esempi sono verificati nella sorgente pubblicata.
La griglia e tutti i conteggi sono validi. I profili YAML esportati per i
tre stili contengono la rispettiva libreria di composizioni completa.
Accesso riservato e ospiti autorizzati conservati.

La skill sorgente è aggiornata nel repository del progetto. Non risulta
una copia separata di Quote Card Designer installata nelle directory locali
delle skill; Quote Card Builder è un progetto distinto e non è stato modificato.

## Sincronizzazione integrale · versione 24

Su richiesta dell'utente tutti gli stili, profili ed esempi attivi della gallery
locale sono ora anche online. La versione Sites **24**, sorgente
`2b5d69ef5777da4a8039b5a1d7a067011cd8032a`, è stata pubblicata con esito
**succeeded** il 26 ottobre 2026. Comprende **67 stili, 140 immagini,
20 selezionati V1 e 29 candidate**. Blue Note entra come candidate con il
mosaico fotografico approvato. La sincronizzazione include anche la terza
prova Neo Swiss presente nella gallery locale.

Verificata l'identità SHA-256 di tutti i 141 file di `dist` fra build locale
e sorgente Sites prima del confezionamento. L'archivio salvato corrisponde
al commit pubblicato. Struttura delle schede, categorie e asset validati;
conteggi e scheda Blue Note controllati nel browser online. Politica di
accesso custom e ospite autorizzato conservati senza variazioni.

Il dettaglio della pubblicazione è in `gallery/pubblicazione-v24.json`.
Il catalogo distribuito V1 conserva i 20 stili della selezione attuale;
questa pubblicazione non esegue la migrazione delle candidate nella release.

## Literary Editorial in esplorazione · versione 25

La versione Sites **25**, sorgente `9601bf185d9ce4991c787d1d1bcd13716c9f2e2a`,
pubblica **Literary Editorial** con due prove, su richiesta dell'utente,
**senza candidatura V1**. Entrambi i flag di selezione sono falsi; la seconda
prova è inizialmente in evidenza. Il catalogo online e locale conta ora
**68 stili e 142 immagini**, con **20 selezionati V1 e 29 candidate**.

Le 67 schede precedenti e i loro 140 file immagine sono invariati. Validati
griglia, asset, categorie e parità di tutti i 143 file di `dist` fra build
locale e sorgente Sites. Verificati il selettore delle due prove e l'assenza
dello stile dal filtro Candidates. La pagina online mostra la nuova scheda
senza badge candidate. Deploy riuscito; accesso custom e ospite autorizzato
conservati. Dettaglio in `gallery/pubblicazione-v25.json`.

## Symbolic Modernism · versione 26

La versione Sites **26**, sorgente `a174b4de4ccf3c0e3bb7663091b1818a4f9bfa65`,
pubblica **Symbolic Modernism** nella categoria Geometrie e pattern, con il
passaggio geometrico della prima prova e la clessidra flat della terza.
Quest'ultima è inizialmente in evidenza. Lo studio a curve resta materiale
di sviluppo e non entra nei due esempi attivi.

La gallery online e locale conta **69 stili e 144 immagini**. I selezionati
V1 restano 20 e le candidate 29; questa richiesta di gallery non modifica
la selezione. Le 68 schede precedenti e i loro 142 file immagine sono
invariati. Verificati griglia, categorie, asset e parità SHA-256 di tutti
i 145 file di `dist` fra build locale e sorgente Sites.

Il selettore dei due esempi è stato controllato nella preview, e la nuova
scheda è stata verificata anche nel browser online. Deploy **succeeded**;
accesso custom e ospite autorizzato conservati. Provenienza e risultato
sono in `gallery/pubblicazione-v26.json`.

## Integrazione delle candidate nella V1 · 26 ottobre 2026

Su richiesta dell'utente, le 29 candidate entrano nella selezione V1 insieme
ai 20 stili precedenti. Il catalogo distribuito e la selezione della libreria
comprendono **49 stili**, versione skill **0.3.0**, con le stesse 11 categorie
della galleria estesa. I 20 studi rimanenti restano fuori release.

La build locale comprende 69 stili e 144 immagini; il pacchetto della skill
include 49 profili e 31 librerie di composizioni, più le risorse locali
dichiarate. Sono conservati i limiti delle prove documentati nei profili.
La versione Sites **27**, sorgente
`8aafc8a2210da7c7fd63f5671608cf41103a9f54`, pubblica le etichette aggiornate:
**49 selezionati V1, 0 candidate e 20 fuori release**. Deploy riuscito e
filtro V1 verificato nel browser online. Le 144 immagini sono identiche alla
versione 26; pubblico custom e ospite autorizzato conservati. Provenienza e
risultato sono in `gallery/pubblicazione-v27.json`. Le versioni precedenti
riportate sopra descrivono lo stato al momento del rispettivo deploy.


## Symbolic Modernism nella V1 · versione 28

Su richiesta esplicita dell'utente, Symbolic Modernism entra nella V1.
La skill **0.3.1** comprende **50 stili e 32 librerie di composizioni**.
La versione Sites **28**, sorgente
`49f1976d0cd82848725101c39bc08cb31adf52e5`, aggiorna il badge della scheda
e i conteggi: 50 selezionati V1, 0 candidate e 19 fuori release.
Le altre 68 schede e tutte le 144 immagini sono invariate rispetto alla
versione 27. Deploy riuscito; badge e filtro V1 verificati online; accessi
conservati. Provenienza e risultato sono in `gallery/pubblicazione-v28.json`.
