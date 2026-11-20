# Catalogo visivo V1

I sorgenti del catalogo pubblico includono l'interfaccia Indice svizzero, i dati della skill 0.5.5 e le anteprime approvate. Il catalogo mostra 103 stili in 11 categorie.

Installa le dipendenze con `python3 -m pip install -r gallery/requirements.txt` nel tuo ambiente virtuale. Esegui `python3 gallery/catalogo-v1/build.py` dalla radice del repository. La build predefinita va in `build/catalogo-v1-dist/`; con `--output <percorso>` si può scegliere un'altra directory. Le immagini sono verificate rispetto a `asset-manifest.json` prima di essere copiate.

La selezione coincide con `references/catalogo-v1.yaml`. Le 50 schede precedenti e le loro anteprime sono conservate; per i 53 stili aggiunti viene usato l'esempio principale indicato da `featured_example` nel catalogo di sviluppo. Il manifesto registra immagini e provenienza senza presentare le anteprime recuperate dalla gallery come originali nativi. Logo, font Archivo, licenza e interazioni riprendono la versione Sites 5 già pubblicata e sono inclusi nei sorgenti riproducibili.

Il progetto Sites mantiene il proprio checkout e il proprio `.openai/hosting.json`. La pubblicazione richiede di allineare le modifiche nel checkout Sites, conservare il manifest e l'accesso pubblico esistente, quindi usare il flusso Sites. Non sostituire il catalogo pubblico con la gallery di sviluppo.

Pubblicazione del 27 ottobre 2026: Sites versione **4**, sorgente `c17d842fff2d81d922fb93bd23e15a485d7d6575`, accesso pubblico invariato. Ricevuta: `pubblicazione-v4.json`.

Pubblicazione del 29 ottobre 2026: Sites versione **6**, sorgente `ae03980657478212b35aee021191aca7d28a1584`, skill **0.5.0**, **103 stili**. Accesso pubblico e revisione 2 della politica di accesso invariati. Stato di pubblicazione confermato da Sites e pagina online verificata nel browser. Ricevuta: [pubblicazione-v6.json](pubblicazione-v6.json). Controlli su selezione, immagini, conservazione e interazioni: [qa-0.5.0.json](qa-0.5.0.json).

## Sorgenti 0.5.1 · 1 novembre 2026

La selezione dei 103 stili e tutte le anteprime sono invariate. La versione dei dati locali è 0.5.1 e i badge leggono quella versione, senza una stringa fissa nel JavaScript. Questa preparazione non pubblica Sites: la pagina online resta alla versione 6, riferita alla skill 0.5.0.

## Sorgenti 0.5.2 · 2 novembre 2026

Dati locali allineati alla build 0.5.2, con selezione e anteprime invariate. Le nuove istruzioni riguardano i loghi nelle card generate, non il logo del sito. La release GitHub 0.5.2 distribuisce la nuova regola. La pubblicazione GitHub non aggiorna Sites né le copie locali della skill.

## Confronto e ricerca · 0.5.4

Il parametro `confronta` accetta tre ID distinti del catalogo V1, separati da virgole. La pagina mostra le anteprime approvate nello stesso ordine del link. «Tutti gli stili» riapre la ricerca. Un collegamento incompleto, duplicato o sconosciuto apre il catalogo con un avviso. [Confronta questi tre stili](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site/?confronta=linocut,cyanotype,notebook-sketch)

La build prende alias e tag da `references/catalogo-v1.yaml`. Per esempio, «stampa a secco» restituisce carta in incavo e carta in rilievo. Il test [browser.cjs](tests/browser.cjs) verifica il confronto e la ricerca sulla build servita in locale.

Il 20 novembre 2026 Sites ha pubblicato la versione 7 del catalogo pubblico. [Ricevuta della pubblicazione](pubblicazione-v7.json)

## Glitch Editorial · 0.5.5

Il 20 novembre 2026 Sites ha pubblicato la versione 8. La scheda di Glitch Editorial descrive gli strappi orizzontali, il rumore e i canali di colore disallineati. Il catalogo comprende 103 stili in 11 categorie. [Ricevuta della pubblicazione](pubblicazione-v8.json)
