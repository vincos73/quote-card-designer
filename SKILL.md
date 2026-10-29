---
name: quote-card-designer
description: "Crea o modifica quote card artistiche da frasi, testi o articoli, preservando la citazione. Aiuta a esplorare e scegliere gli stili disponibili."
metadata:
  version: "0.5.0"
---

# Quote Card Designer

Trasforma una frase o una citazione verificata in una quote card. Segui le
istruzioni dell'utente quando sono più specifiche di questo flusso o del profilo.
Parti dalla richiesta corrente e dalle informazioni già disponibili:

- Per esplorare o confrontare gli stili, mostra le possibilità pertinenti e
  descrivi le differenze utili alla scelta. Non richiedere una citazione né
  avviare una generazione per la sola consultazione.
- Per modificare una card, individua il risultato indicato nella conversazione
  o allegato, ispezionalo e passalo realmente al flusso di editing. Riusa testo
  e scelte già definite; chiedi soltanto una base non disponibile o un dettaglio
  necessario alla modifica. Non riaprire la scelta dello stile. Se ci sono più
  risultati e non è chiaro quale modificare, chiedi quale usare.
- Per creare una nuova card, chiedi una frase, un testo da cui estrarla o una
  fonte solo se il contenuto manca anche nella conversazione. Se l'intento di
  creazione è chiaro, prosegui con le sole scelte ancora necessarie.
- Per sola analisi, un prompt o manutenzione della libreria, non avviare la
  generazione. Per aggiungere o modificare uno stile leggi
  [lo schema stile](references/schema-stile.md).

Se la skill è invocata senza una richiesta riconoscibile, chiedi se l'utente
vuole creare una card, esplorare gli stili o modificare un risultato.

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
  profilo scelto. Il catalogo distribuito comprende 103 stili. Il catalogo visivo V1
  può mostrare una selezione precedente; per la disponibilità fa fede il catalogo incluso nella
  skill. Il collegamento da offrire all'utente è il catalogo visivo V1;
  la gallery di sviluppo è riservata al lavoro del proprietario.
- Quando devi consigliare o scegliere uno stile, anche su delega, leggi
  [come scegliere lo stile](references/scelta-stile.md). Parti da intento,
  caratteristiche del testo e vincoli già disponibili; usa il catalogo per
  individuare i candidati e leggi i profili di tutti quelli che proporrai.
  Un descrittore generico va interpretato attraverso queste informazioni.
  Se la scelta non è delegata, indica una proposta motivata e aggiungi solo
  alternative compatibili che cambiano un effetto utile: al massimo tre stili
  in tutto, anche meno quando bastano. Collega il catalogo e offri «scegli tu».
  Non chiedere un brief aggiuntivo per una richiesta già sufficiente.
- Se l'utente delega la scelta, anche in risposta alle opzioni, scegli con gli
  stessi criteri e procedi appena il contenuto è definito o la sua selezione è
  delegata. Non imporre un altro menu o una conferma. Conserva uno stile già
  scelto e le sue personalizzazioni esplicite. Per uno stile non disponibile,
  spiega il limite e proponi alternative presenti nel catalogo attivo.
- Quando attendi la scelta dello stile, offri nello stesso messaggio colori
  e firma come aggiunta facoltativa, se non sono già definiti: «Se vuoi, puoi
  indicare colori o firma». Non rendere la risposta a questa aggiunta necessaria.
  Se l'utente chiede una palette personale o una firma ma non fornisce i dati,
  chiedi insieme i soli dati mancanti prima di creare. Accetta nomi dei colori
  o codici HEX; non richiedere codici o ruoli tecnici. Non aggiungere un passaggio
  obbligatorio quando testo e stile sono completi e l'utente non ha richiesto
  una personalizzazione.
- Per una citazione da selezionare, proponi nello stesso messaggio testo,
  attribuzione sostenuta dalla fonte e stile consigliato, quando anche lo stile
  è ancora da scegliere. Raccogli insieme le sole decisioni mancanti.
- Non trasformare una sintesi in una citazione letterale e non inventare un
  autore o un'attribuzione.

Riassumi brevemente il testo, l'attribuzione e lo stile scelti. Quando i dati
sono completi, questo riepilogo non richiede un'ulteriore conferma: procedi alla
generazione. Per una citazione proposta da un URL o da un testo lungo, attendi
le sole scelte non ancora definite o delegate dall'utente.
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
- Per revisioni successive, usa la base individuata e intervieni sul difetto o
  sulla modifica richiesta, conservando le altre scelte già definite. Verifica
  il risultato prima di dichiararle preservate; l'editing generativo non
  garantisce da solo che ogni altro dettaglio rimanga identico.
- Controlla testo, accenti, punteggiatura, attribuzione, leggibilità e rapporto
  fra lettering e immagine. Distingui ciò che hai verificato dai limiti del
  risultato; correggi in modo mirato se serve e ricontrolla. Se il difetto
  permane, indica il limite senza ripetere tentativi indefiniti.

Consegna l'immagine e, quando disponibile, il file. Per una citazione estratta,
accompagna il risultato con il collegamento alla fonte consultata.
Non sovrascrivere risultati precedenti e non mostrare prompt o resoconti tecnici
se non richiesti.
