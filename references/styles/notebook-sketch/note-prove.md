# Notebook Sketch — prove del 29 ottobre 2026

Richiesta iniziale: uno stile da notebook, come appunti presi a un convegno,
con un disegno e molte note confusionarie.

## Scelta dell'utente

L'utente ha scelto **A · Biro da platea**, con il testo più in evidenza, e ha
chiesto la candidatura nella gallery online. Il profilo operativo descrive
ora la penna a sfera, la frase grande e protagonista, lo schizzo e le note
subordinate. Il catalogo propone soltanto A; B, C e D restano studi archiviati.
Il profilo, le composizioni e la voce di catalogo iniziali sono conservati in
file con suffisso `-studio-iniziale.yaml`.

La pagina di confronto locale è stata rimossa su indicazione dell'utente.
La candidatura non include lo stile nella release 0.4.0 e non modifica la
skill globale. La pubblicazione richiesta viene registrata separatamente
nella [ricevuta della versione 66](../../../gallery/pubblicazione-v66.json):
pubblicazione riuscita, 29 ottobre 2026.

## Contenuti

Frasi e annotazioni sono testi dimostrativi scritti per questa esplorazione.
Non provengono da una conferenza reale, non sono estratti da una fonte e non
sono attribuiti al relatore disegnato. I prompt conservano gli elenchi esatti
delle note richieste. Nessun autore o firma personale.

- A, B, D: **Le idee prendono forma mentre ascolti.**
- C: **Una buona domanda cambia il percorso.**

## Quattro prove

| Prova | Direzione | Relazione compositiva | Osservazione |
| --- | --- | --- | --- |
| A · Biro da platea | Biro blu e richiami rossi, carta a quadretti | Frase sopra la scena, relatore al leggio e pubblico | Il contesto del convegno è immediato; il titolo grande e le note isolate restano relativamente ordinati. |
| B · Grafite ed evidenziatore | Grafite, carta libera, accenti gialli | Ritratto di ascoltatrice a sinistra, conclusione in basso a destra | La materia e i contorni cercati danno una pagina di disegno; le note sono meno fitte e il ritratto domina. |
| C · Appunti in piena corsa | Inchiostro nero, petrolio e arancio, puntinato | Mano disegnata e percorsi fra le note | Più energia e connessioni; la frase mantiene una presenza da poster. Non compare la nota secondaria richiesta «meno risposte». |
| D · Pagina fitta | Revisione ImageGen di A, stesso foglio e strumenti | Frase ridotta, note più numerose intorno alla scena | Più vicina alla densità richiesta: otto appunti aggiuntivi, molte frecce e una frase meno monumentale. Resta una simulazione illustrata e la scrittura è ancora piuttosto regolare. |

La D era la proposta suggerita durante l'esplorazione; la scelta successiva
dell'utente è A. Le quattro immagini restano conservate per confronto storico.

## Verifica visiva

Controllate tutte le frasi principali sui quattro output: parole, iniziali,
ordine di lettura e punto finale corrispondono al testo del prompt. Spaziatura
naturale e nessuna parola schiacciata per aggirare il visual. Le prove non
contengono attribuzione: l'allineamento dell'autore non è stato collaudato.

Le note sono leggibili come brevi annotazioni e rimangono subordinate. Il
controllo è visivo, non una certificazione OCR: la punteggiatura minuta,
soprattutto i puntini di sospensione, non è uniforme in tutte le prove.
In C manca «meno risposte»; la prova è conservata come studio, senza dichiarare
esatto l'intero apparato secondario. In D le otto note aggiunte sono presenti.

I quattro PNG nativi misurano **1122 × 1402 px**, rapporto circa 4:5; non sono
stati ritagliati né modificati dopo la generazione. A, B e C sono nuove
generazioni, senza immagini di riferimento. D è un editing di A: la reference
è stata fornita realmente a ImageGen dopo averla vista, non soltanto citata.

Queste prove verificano due frasi e variazioni di palette, strumento e
composizione. Non dimostrano la ripetibilità dello stile, la resa di una
citazione lunga o l'esattezza di decine di note obbligatorie. Se in un lavoro
reale tutte le note devono essere letterali, controllarle e correggerle prima
di considerare la card finale.

## Materiali conservati

- `profilo.yaml`: linguaggio proposto dello stile, senza fissare il soggetto.
- `composizioni.yaml`: tre relazioni compositive adattabili.
- `prova-*.png`: quattro output originali di ImageGen.
- `prompt-prova-*.md`: i quattro prompt effettivamente inviati.
- `*-studio-iniziale.yaml`: profilo, composizioni e catalogazione precedenti alla scelta.
- `PROVENIENZA.md` e `generazioni.json`: origine, relazione fra prove e hash.

Le modifiche locali riguardano la nuova cartella e la sua voce candidata nel
catalogo esteso. Le lavorazioni concorrenti nel repository sono conservate.
Per le verifiche tecniche vedere `verifica-studio-iniziale.json` per la prima
esplorazione e la successiva verifica di candidatura della gallery.
