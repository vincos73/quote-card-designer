# Dirty Brutalism, confronto con e senza reference

La coppia confronta [la prova con reference](esempio.png) e [la prova senza reference](esempio-2.png). In entrambe: testo «Ogni scelta dà forma al futuro.», nessuna attribuzione, tre righe identiche, formato verticale richiesto 4:5, palette obiettivo avorio/nero/arancio e famiglia `material-threshold` con una scala in cemento riprodotta in xerografia. I prompt sono identici dopo il solo preambolo di trasferimento della reference. Entrambi gli output nativi misurano 1122 × 1402 px, circa 4:5.

| Aspetto | Con reference | Senza reference |
| --- | --- | --- |
| Gerarchia e leggibilità | Citazione molto dominante sul campo avorio, disgiunta dalla fotografia densa. | Citazione altrettanto dominante, con un campo chiaro più aperto. |
| Correttezza letterale | Frase completa una volta, sentence case, accento grave e punto presenti; nessun testo aggiuntivo. | Stesso esito letterale; nessun testo aggiuntivo. |
| Materiali | Forte grana xerografica e tagli netti, neri chiusi, arancio granuloso al margine inferiore sinistro. | Lo stesso linguaggio di riproduzione resta riconoscibile senza immagini ricevute. |
| Composizione | Scala e taglio verticale racchiudono il campo del testo; accento cromatico più largo sulla soglia. | Scala più continua lungo la diagonale, testo leggermente più slanciato; il taglio verticale è meno determinante. |
| Rischio di copia | Si trasferisce il linguaggio del montage; non sono riprodotte le sue scritte, i suoi simboli o un suo intero impaginato. Resta una vicinanza al repertorio architettonico. | La relazione con il repertorio viene dal prompt scritto; nessuna immagine ricevuta è stata fornita al generatore. |

La prova senza reference conserva gli elementi distintivi dello stile. In questa coppia non emerge un vantaggio indispensabile dell'allegato visivo: il profilo può restare utilizzabile attraverso le sole istruzioni YAML. Questo non dimostra equivalenza generale dei due metodi né una preferenza dell'utente; le reference restano facoltative, senza diventare dipendenze del pacchetto.

È una singola coppia e il prompt comune descrive intenzionalmente la stessa composizione. Non valuta la varietà fra famiglie, la robustezza su frasi diverse, la modifica di palette/font/formato o l'uso su un dispositivo fisico. Non è stato eseguito un test con una seconda frase o con una preferenza modificata. I valori cromatici e la famiglia del font non sono misure certificate dell'output generato.
