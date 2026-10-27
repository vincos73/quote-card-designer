# Neo Swiss · confronto pratico con prompt semplice

Richiesta del 26 ottobre 2026: confrontare la nuova prova senza griglia con
una generazione basata su un prompt semplice senza skill.

## Materiali e produzione

- **A, direzione sviluppata con la skill:** [prova 8](esempio-8.png), risultato
  della sequenza progettuale della conversazione e della rimozione delle
  griglie dalla prova 7. Dispone di indicazioni dettagliate e revisioni.
- **B, prompt semplice:** [immagine](confronto-semplice-1.png) da una sola
  chiamata nuova a ImageGen integrato con il
  [prompt breve integrale](prompt-confronto-semplice-1.md). Nessun profilo,
  libreria compositiva, immagine di riferimento o esempio A è stato passato
  come input alla chiamata. Nessuna correzione del risultato B.

Prompt B, congelato prima della generazione:

> Crea una quote card verticale 4:5 in stile Neo Swiss, con fondo giallo e testo nero, senza griglie. Testo esatto: «Le idee crescono quando cambiano prospettiva.» Non aggiungere altro testo.

Entrambe le immagini native misurano 1122 × 1402 px, prossime a 4:5. Sono
stati fissati la stessa frase richiesta, la direzione giallo/nero e l'assenza
di griglia. Non sono misurati HEX identici, font reali o rapporti di contrasto.

## Risultati osservabili

Controllo a dimensione nativa e in copie larghe 320 px:

| Criterio | A, con direzione sviluppata | B, prompt semplice |
| --- | --- | --- |
| Parole e punto | Corretti | Corretti |
| Caporali richieste | Presenti | Entrambe omesse |
| Griglia e banda | Assenti | Assenti |
| Lettura | Due gruppi con enfasi sul verbo | Un blocco a bandiera sinistra |
| Pesi e scala | Regular/bold con verbo più grande | Tutto pesante, scala pressoché uniforme |
| Leggibilità a 320 px | Frase leggibile | Frase leggibile |
| Rapporto con lo spazio | Asimmetria fra due assi e vuoto intermedio | Blocco compatto con margine sinistro unico |

B raggiunge già una composizione leggibile e riconoscibile con una richiesta
molto breve. A offre più controllo dell'enfasi e dei rapporti spaziali e conserva
la punteggiatura completa, ma non emerge una superiorità estetica oggettiva:
la scelta visiva resta dell'utente.

## Limiti

È un confronto pratico fra questi due output, non una valutazione isolata
dell'effetto della skill. La sessione aveva già letto la skill e visto le
prove; l'isolamento riguarda gli input espliciti passati alla chiamata B,
non la storia dell'agente che la esegue. A ha ricevuto molte più indicazioni
e revisioni, B un solo tentativo; mancano parità di budget, ripetizioni,
seed controllati e valutazione indipendente. Non sono usati subagenti.
Il risultato non autorizza conclusioni generali sull'utilità della skill.
