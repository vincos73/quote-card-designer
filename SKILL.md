---
name: quote-card-designer
description: "Crea o modifica quote card artistiche da frasi, testi o articoli, preservando la citazione. Aiuta a esplorare e scegliere gli stili disponibili."
metadata:
  version: "0.5.5"
---

# Quote Card Designer

Trasforma una frase o una citazione verificata in una quote card. Segui le
istruzioni dell'utente quando sono più specifiche di questo flusso o del profilo.
Parti dalla richiesta corrente e dalle informazioni già disponibili:

- Per esplorare o confrontare gli stili, usa la scelta iniziale descritta
  sotto. La sola consultazione non richiede una citazione né la generazione.
- Per modificare una card, individua il risultato indicato nella conversazione
  o allegato, ispezionalo e passalo realmente al flusso di editing. Riusa testo
  e scelte già definite; chiedi soltanto una base non disponibile o un dettaglio
  necessario alla modifica. Non riaprire la scelta dello stile. Se ci sono più
  risultati e non è chiaro quale modificare, chiedi quale usare.
- Per creare una nuova card, chiedi una frase, un testo da cui estrarla o una
  fonte solo se il contenuto manca anche nella conversazione. Fai questa
  richiesta nello stesso messaggio delle tre proposte iniziali.
- Per sola analisi, un prompt o manutenzione della libreria, non avviare la
  generazione. Per aggiungere o modificare uno stile leggi
  [lo schema stile](references/schema-stile.md).

## Mostra subito tre stili e il confronto visivo

Nella prima risposta utile per una nuova card, un'estrazione di citazione o
un'esplorazione di stili, mostra sempre **tre stili distinti**, ciascuno con
una breve ragione. Subito sotto aggiungi i link **Confronta questi tre stili**
e [Catalogo completo](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site).
Il primo apre gli esempi nello stesso ordine della risposta. Costruiscilo con
gli ID delle tre proposte come indicato in [come scegliere lo stile](references/scelta-stile.md).
Se manca il testo o la fonte non è accessibile,
proponi tre punti di partenza con le informazioni disponibili, nello stesso
messaggio in cui chiedi ciò che manca. Vale anche per un'invocazione senza
una richiesta riconoscibile, in cui inviti l'utente a indicare cosa vuole fare.

Per un articolo o un testo lungo, mostra i tre stili e i due link nella stessa
risposta che propone citazione e attribuzione. Vale anche per «estrai una
frase». In quel caso presenta gli stili per un'eventuale card e fermati alla
proposta. Se l'utente ha già scelto uno stile, mettilo per primo e presenta
gli altri due come alternative facoltative. Su delega, indica quale dei tre
usi e procedi quando anche il testo è definito o delegato.

Invita a rispondere con il nome di uno stile oppure «scegli tu» quando la
scelta è aperta. La pagina del catalogo non comunica la selezione alla chat.
Prima di generare una nuova card, verifica che le tre proposte e i due link
siano già comparsi per questa card. Se mancano, mostrali ora. «Ok» alla
citazione o «crea card» senza un nome di stile o una delega esplicita non
risolvono la scelta. In quel caso chiedi solo lo stile. Riusa le opzioni già
presentate quando la conversazione continua.

## Definisci contenuto e stile

- Con una frase fornita, conserva parole, maiuscole, accenti e punteggiatura.
  Puoi scegliere gli a capo senza cambiare il testo.
- Mostra virgolette esterne alla frase, caporali o segni di citazione decorativi
  solo se l'utente chiede esplicitamente di mostrarli. Altrimenti omettili,
  anche quando delimitano la frase nel messaggio, nella fonte o nel prompt:
  quei delimitatori non sono automaticamente testo da stampare. Conserva invece
  le virgolette interne che appartengono al contenuto. Questa scelta prevale
  sugli esempi e sulle indicazioni dei profili.
- Per un URL, leggi [il processo editoriale](references/processo-editoriale.md).
  Verifica la citazione nel corpo della fonte e proponila insieme all'attribuzione
  che la fonte consente di verificare. Prima di generare, raccogli la scelta del
  testo e dello stile; salta questa attesa solo se l'utente delega esplicitamente
  la selezione e la creazione.
- Per un testo lungo fornito, applica lo stesso processo editoriale e proponi
  un passaggio letterale prima di creare, salvo delega esplicita.
- Risolvi nomi e alias nel [catalogo V1 incluso](references/catalogo-v1.yaml),
  che fa fede per i 103 stili disponibili. Leggi il profilo YAML completo di
  ciascuno stile proposto e usa quello scelto per la generazione. Conserva le
  personalizzazioni esplicite. Se lo stile richiesto non è disponibile,
  spiega il limite e presenta le tre proposte dal catalogo attivo.
- Quando attendi la scelta dello stile, offri nello stesso messaggio colori
  e firma come aggiunta facoltativa, se non sono già definiti: «Se vuoi, puoi
  indicare colori o firma». Non rendere la risposta a questa aggiunta necessaria.
  Se l'utente chiede una palette personale o una firma ma non fornisce i dati,
  chiedi insieme i soli dati mancanti prima di creare. Accetta nomi dei colori
  o codici HEX; non richiedere codici o ruoli tecnici. Non aggiungere un passaggio
  obbligatorio quando testo e stile sono completi e l'utente non ha richiesto
  una personalizzazione.
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
- Quando l'utente chiede un logo, usa il file fornito, distinto da firma e
  attribuzione. Se offre più varianti, scegli quella leggibile sul fondo locale
  (per esempio bianca su scuro, scura su chiaro), rispettando una variante
  esplicitamente richiesta. Conserva simbolo, lettering, proporzioni e colori;
  non reinterpretare il marchio nello stile della card né aggiungere fondini
  quando la variante scelta è già leggibile.
  Collocalo sempre in uno spazio libero nelle zone periferiche del quadro:
  lungo un bordo o in un angolo, con respiro dal margine e dimensione leggibile
  ma subordinata alla frase. Scegli la zona disponibile senza imporre un angolo
  fisso; evita il campo centrale anche quando è libero. Non coprire citazione,
  attribuzione, firma o elementi essenziali del visual. Se non c'è una soluzione
  periferica leggibile con i file disponibili, chiedi soltanto la variante o
  l'adattamento necessario, senza ricolorare il logo o aggiungere un fondino
  autonomamente. Se l'utente chiede soltanto di aggiungere il logo a una
  card approvata, applica il file originale come livello sulla base e salva una
  nuova PNG. Mantieni i pixel della card fuori dall’impronta del logo.
  Per gli strumenti, il controllo del risultato e le nuove composizioni,
  segui la [guida al logo](references/costruzione-prompt.md#applica-il-logo-su-una-card-approvata).
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
  segnala il limite per le nuove composizioni e per gli editing generativi; non sostituirlo
  silenziosamente con un renderer. Un prompt scritto non è un'immagine generata.
  Non aggiungere testi di riempimento.
- Per revisioni successive, usa la base individuata e intervieni sul difetto o
  sulla modifica richiesta, conservando le altre scelte già definite. Verifica
  il risultato prima di dichiararle preservate; l'editing generativo non
  garantisce da solo che ogni altro dettaglio rimanga identico.
- Controlla testo, accenti, punteggiatura, attribuzione, leggibilità e rapporto
  fra lettering e immagine. Verifica le virgolette rispetto alla richiesta
  dell'utente, non ai delimitatori usati per scrivere il prompt.
  Se c'è un logo, controlla variante, fedeltà al file, leggibilità e posizione
  periferica, oltre alle modifiche collaterali della card.
  Distingui ciò che hai verificato dai limiti del
  risultato; correggi in modo mirato se serve e ricontrolla. Se il difetto
  permane, indica il limite senza ripetere tentativi indefiniti.

Consegna l'immagine e, quando disponibile, il file. Per una citazione estratta,
accompagna il risultato con il collegamento alla fonte consultata.
Non sovrascrivere risultati precedenti e non mostrare prompt o resoconti tecnici
se non richiesti.
