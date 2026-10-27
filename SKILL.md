---
name: quote-card-designer
description: "Crea quote card artistiche da una frase, un testo o un articolo, preservando la citazione e usando uno stile visivo disponibile."
metadata:
  version: "0.4.0"
---

# Quote Card Designer

Trasforma una frase o una citazione verificata in una quote card. Segui le
istruzioni dell'utente quando sono più specifiche di questo flusso o del profilo.
Se la skill viene invocata senza contenuto, chiedi di fornire una frase, un testo
da cui estrarre una citazione oppure il link a una fonte.

Per vedere gli esempi, offri il [catalogo visivo V1](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site).
L'utente può copiare il nome di uno stile e scriverlo nella conversazione.
La pagina non comunica automaticamente la selezione alla chat. Leggi i profili
inclusi nella skill: la consultazione del sito non è necessaria per generare.

## Definisci contenuto e stile

- Con una frase fornita, conserva parole, maiuscole, accenti e punteggiatura.
  Puoi scegliere gli a capo senza cambiare il testo.
- Per un URL, leggi [il processo editoriale](references/processo-editoriale.md).
  Verifica la citazione nel corpo della fonte e proponila insieme all'attribuzione
  che la fonte consente di verificare. Prima di generare, raccogli la scelta del
  testo e dello stile; salta questa attesa solo se l'utente delega esplicitamente
  la selezione e la creazione.
- Per un testo lungo fornito, applica lo stesso processo editoriale e proponi
  un passaggio letterale prima di creare, salvo delega esplicita.
- Se l'utente indica uno stile, risolvi il nome o l'alias nel
  [catalogo V1](references/catalogo-v1.yaml). Carica l'intero YAML del solo
  profilo scelto. Il catalogo distribuito comprende 50 stili. Il catalogo visivo V1
  può mostrare una selezione precedente; per la disponibilità fa fede il catalogo incluso nella
  skill. Il collegamento da offrire all'utente è il catalogo visivo V1;
  la gallery di sviluppo è riservata al lavoro del proprietario.
- Se indica un descrittore generico, mappalo a uno stile disponibile e spiega
  brevemente la corrispondenza. Se la richiesta può indicare due stili diversi,
  proponi quelle due alternative. Se non indica uno stile, proponi 2–3 opzioni
  pertinenti con un collegamento al catalogo e attendi la scelta.
- Se l'utente delega la scelta, seleziona uno stile adatto e procedi. Per uno
  stile non disponibile, spiega il limite e proponi le alternative più vicine.
- Quando chiedi lo stile, offri nello stesso messaggio la personalizzazione
  facoltativa: «Vuoi indicare dei colori e aggiungere il tuo nome come firma?
  Puoi anche lasciare a me i colori e creare la card senza firma».
  Se l'utente chiede una palette personale o una firma ma non fornisce i dati,
  chiedi insieme i soli dati mancanti prima di creare. Accetta nomi dei colori
  o codici HEX; non richiedere codici o ruoli tecnici. Non aggiungere un passaggio
  obbligatorio quando testo e stile sono completi e l'utente non ha richiesto
  una personalizzazione.
- Se manca il testo, chiedilo prima di generare. Non trasformare una sintesi in
  una citazione letterale e non inventare un autore o un'attribuzione.

Riassumi brevemente il testo, l'attribuzione e lo stile scelti. Quando i dati
sono completi, questo riepilogo non richiede un'ulteriore conferma: procedi alla
generazione. Per le citazioni proposte da un URL, attendi invece che l'utente
scelga il testo e, se non è già definito o delegato, lo stile.
Usa una o due frasi comprensibili, senza campi tecnici, nomi interni dei profili
o spiegazioni del metodo di rendering. Spiega dubbi di attribuzione quando
esistono; non aggiungere avvertenze di verifica per ogni nome fornito.

## Progetta, genera, controlla

- L'attribuzione è facoltativa. Se è presente, riportala esattamente in un
  registro leggibile ma visivamente subordinato alla citazione, sempre allineato
  a destra sul margine o su un asse destro chiaro della composizione. Può stare
  sotto la frase o in un altro spazio coerente con lo stile, ma il nome deve
  terminare sull'asse destro. Se manca, ometti l'attribuzione e lo spazio
  riservato.
  Un nome fornito dall'utente non equivale a un'attribuzione verificata.
- La firma personale è distinta dall'autore della citazione. Usa solo il nome
  richiesto esplicitamente, senza ricavarlo dal profilo dell'utente. Se manca
  un'attribuzione, colloca la firma nel registro grafico a essa destinato,
  più piccolo e leggero del testo, senza introdurla come autore della frase.
  Se è già presente un autore, conservalo e aggiungi una firma separata solo
  quando richiesta; non sostituire né unire i due nomi.
- Il default è una sola card verticale 4:5, con una palette variabile scelta
  perché adatta al contenuto e allo stile attivo. Applica le preferenze esplicite
  su formato, palette, font e numero di varianti.
- Leggi [stile e composizione](references/composizione.md). Il profilo definisce
  il linguaggio; scegli la struttura della card in base a frase, formato e
  nomi presenti. Se il documento dichiara `Composition Library`, carica solo
  quella libreria e usa una famiglia pertinente, adattandola alla richiesta.
  Nei profili senza libreria ricava una struttura dalle regole di `Layout`.
  La scelta è interna e non richiede un nuovo passaggio all'utente. Per nuove
  varianti differenzia la relazione fra testo e visual; per revisioni mirate
  conserva invece la composizione accettata.
- Leggi [i metodi di produzione](references/metodi-produzione.md) quando il
  profilo dichiara `Production`. Per ogni nuova composizione usa
  ImageGen per generare la composizione visiva della card, anche se il profilo
  suggerisce `typeset` o `hybrid`. Un'immagine generata come solo elemento da
  inserire in una card progettata interamente con uno script non basta. Puoi
  rifinire il risultato con font reali o altri strumenti per correggere testo e
  geometrie, conservando la direzione visiva generata. Non consegnare una card
  realizzata soltanto con impaginazione deterministica. Usa solo strumenti e
  metodi effettivamente disponibili; non dichiarare capacità, font o dimensioni
  non verificati.
  Su una base generata e approvata, una richiesta esplicita di lavoro ibrido
  permette di separare sfondo e testo e riutilizzare lo stesso sfondo per le
  revisioni tipografiche. Conserva originale, asset pulito e scena del testo;
  una nuova direzione visiva richiede nuovamente ImageGen.
- Leggi [costruzione del prompt](references/costruzione-prompt.md) e
  [fondamenti tipografici e compositivi](references/fondamenti-quote-card.md).
  Porta nel prompt le relazioni e i materiali pertinenti del profilo e scegli
  una direzione visiva legata a quella frase.
  Gli esempi chiariscono il linguaggio, ma non impongono citazioni, soggetti o
  palette. Non passarli automaticamente al generatore; usa invece eventuali
  reference operative approvate e dichiarate nel profilo scelto, rispettandone
  le indicazioni. Mantieni proporzioni
  naturali dei glifi, kerning e spazi fra parole; risolvi la capienza con corpo,
  a capo e composizione, senza tracking arbitrario per riempire le righe.
- Usa ImageGen integrato per la generazione. Non attivare servizi esterni a
  pagamento o percorsi API senza richiesta. Se ImageGen non è disponibile,
  segnala che non puoi produrre la card secondo questa skill; non sostituirlo
  silenziosamente con un renderer. Un prompt scritto non è un'immagine generata.
  Non aggiungere testi di riempimento.
- Per revisioni successive, intervieni sul difetto o sulla modifica richiesta
  e conserva le altre scelte già definite.
- Controlla testo, accenti, punteggiatura, attribuzione, leggibilità e rapporto
  fra lettering e immagine. Distingui ciò che hai verificato dai limiti del
  risultato; correggi in modo mirato se serve e ricontrolla. Se il difetto
  permane, indica il limite senza ripetere tentativi indefiniti.
- Se l'utente chiede solo analisi, un prompt o manutenzione della libreria, non
  avviare la generazione. Per modificare uno stile leggi
  [lo schema stile](references/schema-stile.md).

Consegna l'immagine e, quando disponibile, il file. Per una citazione estratta,
accompagna il risultato con il collegamento alla fonte consultata.
Non sovrascrivere risultati precedenti e non mostrare prompt o resoconti tecnici
se non richiesti.
