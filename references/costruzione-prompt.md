# Dal profilo alla card

## Forma il brief della richiesta

Fissa il testo esatto, l'eventuale attribuzione e la firma personale distinta,
poi identifica stile, formato, palette e direzione tipografica richiesti.
Usa i default del catalogo e del
profilo per i dati non specificati.

Una frase più lunga richiede una nuova gerarchia e una diversa distribuzione
della densità. Non applicare semplicemente lo stesso impaginato rimpicciolito.
Se un vincolo impedisce una lettura ragionevole, spiega il conflitto e chiedi
quale vincolo modificare; non abbreviare una citazione in silenzio.

## Risolvi le priorità

Le scelte esplicite dell'utente prevalgono sui default del profilo.
Prepara una versione effettiva del profilo nel prompt che risolva i conflitti:
con una palette sostitutiva, sostituisci anche le regole che impongono i colori
precedenti. Non limitarti ad aggiungere due istruzioni incompatibili.

Mantieni i ruoli compositivi di fondo, testo e accenti quando possibile.
Con un font richiesto, conserva il carattere dello stile attraverso scala,
spaziatura e materiali compatibili, senza ripristinare di nascosto il default.
Non certificare l'uso esatto di una famiglia partendo da un'immagine generata.
Una richiesta di corrispondenza tipografica esatta va distinta da una direzione
visiva approssimabile dal tool.

L'attribuzione fornita dall'utente è ammessa come dato fornito; non inventarla
per soddisfare un apparato del profilo. L'assenza di un autore non richiede una
domanda quando la card può essere realizzata senza firma.
Se è presente, prepara un registro distinto: nome esatto, corpo inferiore alla
citazione e peso visivo più quieto, con contrasto leggibile. Allinea il nome a
destra, ancorando il suo margine finale al bordo destro utile o a un asse destro
chiaro della composizione. Scegli la posizione verticale secondo il profilo,
senza farlo competere con la frase o con l'eventuale estratto ingrandito. Non
aggiungere cariche, titoli o prefissi non forniti e non presentare come verificata
un'attribuzione soltanto indicata.

Se l'utente vuole personalizzare i colori ma non li indica, chiedili prima di
generare; bastano nomi comuni o codici HEX. Applica la palette ai ruoli dello
stile mantenendo contrasto e leggibilità. Colori delegati non richiedono una
domanda. Se un vincolo cromatico rende il testo illeggibile, spiega il conflitto
e proponi l'aggiustamento necessario.

Registra la firma personale separatamente dall'attribuzione. Se l'autore manca,
usa per la firma lo stesso registro grafico subordinato, senza attribuire la
citazione al firmatario. Mantieni l'autore se presente; una firma aggiuntiva
esplicitamente richiesta resta distinta. Non inventare un nome personale.

## Scegli la direzione della singola card

Applica [stile e composizione](composizione.md). Distingui il linguaggio del
profilo dalle possibili distribuzioni degli elementi. Leggi l'eventuale
`Composition Library`, scegli una struttura principale e adattala all'ingombro
della frase, al formato e alla presenza di attribuzione o firma. Porta nel
prompt la sola struttura scelta. I profili senza libreria restano utilizzabili
attraverso le loro regole di `Layout`.

Individua una relazione visiva pertinente al testo: una giustapposizione, un
ritmo, una tensione tipografica o un principio di costruzione.
Una metafora letterale non è obbligatoria per ogni frase.

Decidi tu i soggetti in ragione del contenuto, del contesto e del tono della
richiesta. Gli elenchi dei profili offrono possibilità, senza limitare la scelta
a quei soggetti. Non imporre un personaggio ricorrente e non chiedere una scelta
all'utente come passaggio ordinario. Una preferenza esplicita sul soggetto va
rispettata.

Seleziona dal repertorio pochi elementi compatibili; il numero dipende dalla
composizione. Descrivi come interagiscono, quali masse contano e dove serve
respiro. Materiali, gerarchie e rapporti di scala devono rendere riconoscibile
lo stile.
Trasmetti nel prompt le relazioni strutturali del profilo, distinguendole dagli
elementi facoltativi. Non sostituirle con il solo nome dello stile o con generici
inviti a usare tipografia pulita e spazio vuoto.

Applica i [fondamenti comuni](fondamenti-quote-card.md): definisci ordine di
lettura, registri tipografici, margini e ancoraggi adatti a quella composizione.
Progetta a capo per gruppi di senso, interlinea e contrasto locale insieme al
visual. La griglia può restare invisibile e ammettere scarti intenzionali.
Mantieni un ritmo ottico coerente negli spazi, senza imporre identico kerning
a tutte le coppie né identico tracking a registri diversi. Nei collage e nel
lettering conserva le irregolarità espressive che lasciano chiara la frase.

Non cambiare famiglia, corpo o proporzioni di una singola parola o riga solo
per evitare un'immagine. A parità di registro tipografico conserva il disegno
dei caratteri, senza compressioni o deformazioni locali. Risolvi le collisioni
spostando o ridimensionando il visual, cambiando gli a capo o, se serve,
ridimensionando uniformemente l'intero blocco. Una variazione tipografica deve
avere una ragione espressiva esplicita, non nascondere un problema di spazio.

Gli esempi sono calibrazione, non soggetti da riprodurre a ogni richiesta.
Se la loro immagine viene passata al tool, dichiarane il ruolo: materiali,
trattamento o relazioni. Il tool deve poter riceverla realmente; una semplice
menzione del percorso non prova che sia stata fornita al generatore.
Scegli la palette come decisione separata. Non trasferire automaticamente i
colori delle immagini di riferimento: usali solo se richiesti dall'utente o
scelti esplicitamente per quella card. Nel prompt distingui le proprietà
visive da trasferire da colori, testo, soggetti e impaginato da reinventare.

## Costruisci il prompt di generazione

Chiedi a ImageGen la composizione della card completa, non soltanto un'immagine
da inserire successivamente in un layout progettato separatamente.
Su una base già generata e approvata, se l'utente richiede il lavoro ibrido,
segui il [riuso di sfondo e testo](metodi-produzione.md): le revisioni solo
tipografiche possono riutilizzare l'asset pulito senza rigenerare il visual.

Usa una struttura leggibile, in italiano o inglese secondo l'ambiente:

1. Tipo di asset, destinazione, rapporto e output singolo o varianti richieste.
2. Linguaggio effettivo: concept, mood, palette con ruoli, tipografia,
   relazioni essenziali, repertorio pertinente, materiali, effetti e regole.
3. Composizione scelta per la card: distribuzione delle masse, area del testo,
   ordine di lettura, densità, enfasi e ancoraggi, adattati alla frase e al
   formato. Non trasferire le altre famiglie come alternative simultanee.
4. Citazione delimitata, integralmente letterale, ed eventuale attribuzione e/o
   firma, ciascuna con testo esatto, ruolo, posizione e gerarchia subordinata.
   Spiega al generatore che una firma personale non è l'autore della citazione.
5. Vincoli di leggibilità e divieto di testi inventati.

Mantieni i dati visivi concreti. Non ridurre una scheda a «bello, artistico,
nello stile indicato». Evita anche di appesantire il prompt con altri stili,
cataloghi, log di lavoro o tutti gli elementi disponibili.
Seleziona dalla guida comune le indicazioni utili alla card; non copiarla
integralmente. Specifica come ottenere l'effetto, senza trattare valori scritti
nel prompt come controlli tipografici deterministici.

Di default visualizza la citazione una volta. Se il profilo attivo prevede una
ripetizione strutturale, come frase completa ed estratto ingrandito, applica quel
contratto: conserva il testo integrale e ripeti soltanto l’estratto letterale
scelto, senza riscriverlo. Una richiesta esplicita dell’utente prevale; se entra
in conflitto con un elemento essenziale dello stile, rendi esplicito il conflitto.
Niente scritte fittizie per simulare etichette, giornali, dashboard o apparati tecnici.

## Usa e controlla il risultato

Applica il [metodo di produzione](metodi-produzione.md) del profilo con gli
strumenti disponibili. Usa il generatore integrato per le fasi generative.
Per modificare un'immagine fornita,
ispezionala e usa il flusso di editing supportato mantenendo gli elementi che
l'utente vuole conservare. Segui gli argomenti e i limiti del tool effettivo:
non simulare selettori di modello, file inviati o dimensioni non disponibili.

Controlla il risultato visibile rispetto al brief. Correggi il difetto osservato
con un intervento mirato che mantenga gli altri vincoli. Di norma fermati dopo
una correzione se il problema persiste e dichiaralo, salvo diversa richiesta.
Controlla anche che le righe vicine al visual non siano state compresse o
ridisegnate per farle entrare nello spazio residuo.
Usa la lista di controllo della guida comune anche per spazi, a capo, ancoraggi
e contrasto locale. Valuta la lettura alla scala d'uso quando puoi ispezionarla;
un file ad alta risoluzione non prova da solo la leggibilità nel feed.

L'immagine consegnata è l'output principale. Conserva il prompt effettivamente
usato quando il progetto o l'ambiente lo permette, senza imporre all'utente
finale una spiegazione tecnica a ogni richiesta.

