# Neon Sign

Proposta del 28 ottobre 2026. Richiesta: progettare lo YAML di un nuovo stile
con il massimo realismo, analizzando tre reference allegate. Nessuna card
richiesta o generata in questa fase.

Reference analizzate visivamente dagli allegati:

- `ee46d38715eae2e1d67497f139a2f66a.jpg`: contrasto fra tubi accesi e spenti,
  supporti, terminali, ombre e cablaggio su parete blu. Il guasto apparente è
  una possibilità espressiva, subordinata alla leggibilità.
- `e17ea363d84dd310f2bdf8217509b8ea (1).jpg`: tubi chiari con emissione ciano,
  segmentazione delle lettere, interruzioni, profondità e cavi discendenti.
- `b37fd7470ddfcfa3491d05aedc990493.jpg`: colonna asimmetrica, spazio scuro,
  traverse di sostegno e cavi lunghi. Testo, date, loghi e crediti non si
  trasferiscono nel nuovo stile.

Le immagini mostrano proprietà visive, non dimostrano l'autenticità fisica
degli oggetti raffigurati. Il vetro luminoso è una scelta progettuale esplicita.
La richiesta è interpretata come creazione di un profilo sperimentale locale,
senza inserimento nei cataloghi, selezione V1, installazione o pubblicazione.
La directory separa il profilo dalle tre strutture compositive; `neon-sign.yaml`
è l'esportazione autosufficiente dei due documenti.

La sintassi e il collegamento alla libreria sono verificabili con il loader
del progetto. Nella fase iniziale non erano state eseguite prove ImageGen.
Per adottare reference permanenti eseguire il confronto controllato previsto
dallo schema stile.

## Due esempi richiesti successivamente

Generati con ImageGen integrato il 28 ottobre 2026, senza immagini in input:
le reference hanno informato il profilo scritto. Non si tratta di un
confronto controllato con e senza reference.

| Esempio | Testo originale dimostrativo, senza autore | Composizione | Palette |
| --- | --- | --- | --- |
| `esempio-1.png` | Le idee brillano quando trovano spazio. | Insegna compatta su cinque righe | Rosa su blu scuro |
| `esempio-2.png` | Il futuro si accende un passo alla volta. | Colonna asimmetrica su quattro righe, cavi discendenti | Ciano su petrolio |

Prompt effettivi: `prompt-esempio-1.txt` e `prompt-esempio-2.txt`. Entrambe le
card sono state generate integralmente, compreso il lettering; nessun testo
è stato sovrapposto con uno script. Originali copiati senza modifiche nel
progetto. Dimensioni native: 1122 × 1402 pixel, quasi 4:5.

Controllo visivo eseguito su output nativi e copie di sola ispezione a
320 × 400 pixel: frasi corrette, cassa e punti finali presenti, percorso di
lettura chiaro, parole distinguibili, aloni compatibili con la lettura.
Vetro, terminali, supporti e cavi rendono la costruzione percepibile. Le
immagini non certificano una costruzione elettrica effettivamente realizzabile
né una simulazione fisica della luce.

Restano da valutare con l'utente la qualità estetica e il livello di realismo;
non sono provati testo spento, attribuzione o altri formati. Nessun catalogo
o sito è stato aggiornato. Profilo ed esportazione sono stati aggiornati
per descrivere le prove effettivamente svolte.

## Candidatura alla library

Il 28 ottobre 2026 l'utente ha chiesto di aggiungere Neon Sign alla library
come candidato. Stato richiesto: `release_candidate: false` e
`v1_shortlisted: true`. I due esempi, il profilo, le composizioni e i prompt
sono conservati insieme nella directory dello stile. La selezione della
release distribuita resta separata dalla candidatura.
