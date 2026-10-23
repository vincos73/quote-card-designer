# Stile e composizione

Lo stile definisce il linguaggio: materiali, trattamento delle immagini,
registri tipografici, gerarchia, ruoli cromatici e relazioni che lo rendono
riconoscibile. La composizione decide come distribuire quel linguaggio nella
card specifica: forma e posizione della frase, direzione dei segni, densità,
ritaglio, margini, spazio libero e ancoraggi.

Le relazioni essenziali restano nel profilo. Per esempio, in Pixel Field il
retino deve reagire al blocco di testo; questo non impone una diagonale. In
Medieval Folio scrittura e miniatura appartengono allo stesso foglio; questo
non impone un bordo floreale completo. Una ripetizione del testo esplicitamente
prevista dal profilo resta un vincolo anche cambiando impaginato.

## Carica soltanto la libreria dello stile scelto

Il documento YAML mantiene la radice `Design Style`. Può avere una seconda
chiave alla radice:

```yaml
Composition Library: composizioni.yaml
```

Il percorso è relativo alla directory del profilo. Leggi il documento collegato,
la cui radice `Composition Library` contiene `Style Name`, `Selection` e
`Families`. Il catalogo può esportare la stessa libreria incorporata come
mappa sotto `Composition Library`: in quel caso è già disponibile nel testo
copiato. Non cercare un altro file.

Le famiglie descrivono strutture possibili, condizioni d'uso, adattamento della
frase e del formato. Sono un repertorio aperto; non sono modelli a coordinate
fisse e non devono essere sommati tutti nella stessa card.

Nei profili senza libreria, usa `Layout` e le regole esistenti per distinguere
relazioni essenziali e scelte variabili. Progetta una composizione pertinente
senza inventare file mancanti, caricare altre librerie o modificare il profilo.

## Scegli la struttura per la richiesta

1. Fissa il testo letterale e identifica formato, eventuale attribuzione o
   firma e preferenze esplicite. Una composizione richiesta dall'utente ha
   precedenza sulle proposte della libreria, se compatibile con il contenuto.
2. Valuta l'ingombro reale previsto della frase: parole lunghe, gruppi di senso,
   accenti, numero di righe e presenza del nome. La lunghezza non si riduce a
   una soglia universale di caratteri.
3. Confronta internamente le famiglie pertinenti e scegline una come struttura
   principale. Motiva la scelta con significato, leggibilità, formato e spazio
   necessario. Se nessuna è adatta, costruiscine una coerente con lo stile.
4. Progetta insieme area della citazione, densità del visual e ancoraggi. Per
   una frase lunga apri più spazio e riduci l'invasione ornamentale prima di
   ridurre il carattere. Ricomponi per un nuovo rapporto, evitando di ritagliare
   semplicemente la stessa card.
5. Se attribuzione o firma mancano, recupera lo spazio. Se presenti, mantienile
   esatte, leggibili, subordinate e sull'asse destro previsto dal flusso.

La scelta è ordinariamente interna: frase e stile restano sufficienti per
procedere. Chiedi una decisione solo quando un conflitto sostanziale richiede
di cambiare un requisito dell'utente.

## Varia senza perdere identità

Per nuove card varia struttura quando il testo lo giustifica, direzione,
densità, ritaglio, proporzioni e soggetto. La palette è una variabile ulteriore;
da sola non crea una nuova composizione. Usa solo risultati visibili nella
conversazione per evitare ripetizioni; non presumere una memoria tra sessioni.

Per varianti richieste insieme, differenzia almeno la relazione fra citazione
e visual, conservando il testo. Per una revisione mirata conserva invece la
composizione accettata, salvo richiesta contraria o necessità di risolvere il
difetto. Non forzare casualità o rotazioni a scapito della leggibilità.

## Porta una scelta nel prompt e controllala

Trasmetti al generatore il linguaggio effettivo dello stile e la sola struttura
scelta, con gli adattamenti della richiesta. Non incollare tutte le famiglie
come istruzioni simultanee. Descrivi relazioni concrete; un identificatore
come `broken-diagonal` da solo non dirige il modello.

Quando il progetto conserva note di produzione, annota famiglia scelta,
adattamenti e motivo. Questo è un resoconto di progettazione, non una misura
automatica del risultato.

Dopo la generazione verifica sia l'identità dello stile sia la composizione:
testo preminente, ordine di lettura, integrazione del visual, spazi liberi e
adattamento alla frase. Una libreria ben strutturata non dimostra da sola
varietà o miglioramento estetico; servono confronti su immagini nuove.
