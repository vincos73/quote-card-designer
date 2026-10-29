# Editor Canvas — nodi in modifica

Data: 29 ottobre 2026. EC2 ha ricevuto un riscontro positivo («bello») e la
richiesta di una nuova prova con un altro testo. Dopo EC3, l'utente ha
richiesto la candidatura online, pubblicata nella gallery versione 65.

La richiesta è rendere Editor Canvas più d'impatto, realistico e poco scontato.
Il confronto mantiene la frase dell'esempio storico: «Ogni scelta dà forma al
futuro.». Nessuna attribuzione o firma aggiunta.

## Direzione proposta

Un ritaglio ravvicinato di un editor moderno mostra la frase mentre viene
lavorata. La parola «forma» aumenta di scala e diventa blu cobalto; il contorno
della «o» mostra nodi di modifica. L'area di lavoro grafite, i righelli senza
numeri e i piccoli strumenti contestuali rendono leggibile il contesto.
L'avorio dell'artboard e il nero della frase preservano il contrasto.

Da trasferire: un'operazione specifica legata al testo, grande differenza di
scala tra frase e strumenti, oggetto attivo riconoscibile, controlli coerenti,
ritaglio dell'interfaccia, spazi tra parole visibili. La frase, la «o», il blu,
i quattro a capo e le posizioni dei pannelli appartengono a questa prova.
Non impongono soggetti, palette o distribuzioni alle card successive.

## Generazioni e scelta

1. `prova-1.png`, con `prompt-prova-1.md`: composizione completa da testo,
   senza reference. Frase corretta ma spazi troppo stretti; le maniglie
   diagonali della «o» non rappresentano una tangente credibile.
2. `prova-2-spaziatura.png`, con `prompt-prova-2-correzione.md`: modifica della
   prima prova. Migliora gli spazi e rimuove il riquadro della parola, ma il
   segmento orizzontale resta staccato dal nodo; non è un esempio affidabile
   di trascinamento Bézier.
3. `prova-3-nodi.png`, con `prompt-prova-3-nodi.md`: modifica della seconda.
   Elimina il segmento, mantiene quattro nodi sul contorno e il cursore
   vicino al nodo superiore. È la prova proposta EC2: uno stato di modifica
   del tracciato prima di selezionare una maniglia. Il cursore non dimostra
   un trascinamento in corso.

La terza generazione semplifica un dettaglio non riuscito; non è un altro
tentativo di ricostruire la stessa maniglia. Tutte le immagini intermedie
sono conservate. Il prompt della terza è una modifica e va letto con il
relativo bersaglio e con il prompt iniziale per ricostruire la composizione.

## Verifica e limiti

Controllati visivamente frase, accento grave in «dà», punto finale, ordine
di lettura, spazi tra parole, contrasto e assenza di attribuzioni inventate.
La composizione richiama un editor ma non è lo screenshot di un software
esistente né prova di funzionalità. I contorni sono raster generati, non
curve vettoriali misurate; il font esatto non è certificato.

La richiesta al generatore era 4:5; i PNG restituiti misurano 1122×1402,
molto vicini ma non esattamente equivalenti a quel rapporto. Non sono stati
stirati o ritagliati. Il seguito EC3 prova una frase più lunga, un accento
arancio e la selezione di un oggetto ruotato; è documentato in
[note-prospettiva.md](note-prospettiva.md). Restano da testare un testo lungo,
un cambiamento cromatico più ampio e l'attribuzione facoltativa. Due esempi
non dimostrano ripetibilità. Le verifiche della build sono in `verifica.json`.

Il profilo di sviluppo passa a 0.2.0 e documenta i limiti. Nella prima fase
locale EC1 restava l'anteprima principale. Dopo la richiesta esplicita
dell'utente, EC3 diventa l'anteprima e lo stile è candidato nella gallery
online versione 65. Tutti e tre gli esempi restano consultabili.
La pubblicazione comprende un commit/push nella sorgente Sites; non è stato
eseguito un commit/push del repository GitHub. Nessuna installazione globale
o promozione della release. Ricevuta: `gallery/pubblicazione-v65.json`.
