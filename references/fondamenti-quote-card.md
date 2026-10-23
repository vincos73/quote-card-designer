# Fondamenti per quote card e poster a prevalenza testuale

Riferimento comune per progettare il prompt e controllare l'immagine. Il profilo
selezionato definisce il linguaggio e le sue libertà espressive; le preferenze
esplicite dell'utente prevalgono sui valori predefiniti.

Questa è una sintesi operativa di principi tipografici e compositivi, con fonti
primarie e adattamenti per la generazione di immagini. Le indicazioni per la
lettura continuativa, le interfacce e i poster non si trasferiscono automaticamente
l'una nell'altra.

## 1. Gerarchia prima degli effetti

Stabilire che cosa si deve notare per primo e in quale ordine si deve leggere
la frase. Dimensione, peso, contrasto e raggruppamento concorrono alla gerarchia;
non basta ingrandire una parola. Evitare che elementi equivalenti per forza
visiva competano tutti per il primo posto.
Fondamento: [Nielsen Norman Group, Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/).

Per questa categoria di card la frase ha precedenza comunicativa. L'immagine
può occupare molta superficie e avere forte presenza, ma deve favorire o
arricchire la lettura. Non esiste una proporzione universale fra percentuale
di testo e percentuale di immagine.

Distinguere pochi ruoli: citazione, eventuale enfasi, eventuale attribuzione.
Ogni variazione dovrebbe corrispondere a uno di questi ruoli o a un'intenzione
espressiva leggibile. Il numero di ruoli non determina il numero di famiglie
tipografiche: un collage può impiegare più caratteri senza creare nuovi livelli.

L'attribuzione, quando fornita, è un registro secondario: il nome deve avere
corpo inferiore e peso visivo minore della citazione, con distanza sufficiente
per distinguerne il ruolo. Allineare il nome a destra sul margine utile o su un
asse destro chiaro. Può seguire la frase, occupare un modulo del footer o
un'altra posizione coerente con il profilo. Anche nel lettering manuale deve
restare chiaramente subordinata. Non ridurre contrasto o corpo fino a renderla
illeggibile nel feed. Il nome resta esatto; non aggiungere qualifiche o formule
non richieste. Se manca, eliminarne anche lo spazio riservato.

## 2. Kerning, tracking e spazio fra parole

| Termine | Cosa controlla |
| --- | --- |
| Kerning | La compensazione fra specifiche coppie di caratteri. |
| Tracking | La spaziatura aggiunta o sottratta a un insieme di caratteri. |
| Spaziatura fra parole | La separazione percepibile fra le unità lessicali. |

Il kerning non deve avere un valore uguale per tutte le coppie. La correzione
ottica tiene conto delle forme; le misure relative al corpo non equivalgono
a distanze costanti in pixel. Anche font o corpi diversi richiedono valutazioni
ottiche. Riferimento tecnico:
[Adobe, kerning e tracking](https://helpx.adobe.com/indesign/desktop/format-and-style-text/tabs-indents-and-spacing/about-kerning-and-tracking.html).

Mantenere un ritmo coerente entro ciascun registro, correggendo buchi e
addensamenti indesiderati. Una variazione di corpo non obbliga a conservare
identico tracking: le esigenze di spaziatura possono cambiare fra testo piccolo
e titolo. Butterick descrive anche aggiustamenti diversi per maiuscole e
minuscole e per differenti scale:
[Letterspacing](https://practicaltypography.com/letterspacing.html).

Formula da tradurre nel prompt:

> Mantieni coerenza ottica entro ogni registro tipografico. Cura le coppie di
> lettere e gli spazi fra parole. Evita variazioni accidentali usate soltanto
> per occupare lo spazio rimasto.

## 3. Disegno dei caratteri, pesi e dimensioni

Pesi e corpi diversi sono ammessi nella stessa frase quando rendono chiara
un'enfasi o una gerarchia. La differenza deve restare intenzionale lungo la
composizione.

Come criterio progettuale, preservare le proporzioni del carattere scelto.
Per un registro stretto usare un disegno condensato coerente; evitare una
singola parola schiacciata per aggirare un'immagine. Lo stesso vale per lettere
stirate, spessori localmente alterati e cambi di famiglia introdotti soltanto
per risolvere una collisione.

Quando il visual invade il testo, valutare prima posizione, scala e ritaglio
del visual; poi gli a capo e, se serve, la scala uniforme del blocco o del
registro interessato. Un cambiamento tipografico espressivo resta possibile,
ma va distinto da un adattamento opportunistico alla capienza.

Controllo: lettere dello stesso registro mantengono proporzioni e spessori
riconoscibili anche vicino al visual? Le differenze corrispondono alle enfasi
progettate?

## 4. A capo, interlinea e continuità

Per le citazioni:

- Preferire gruppi di senso e nessi sintattici comprensibili.
- Evitare parole funzionali isolate per mera capienza e letture che alterino
  il rapporto fra una negazione, una condizione e il resto della frase.
- Una parola isolata può essere un'enfasi intenzionale; non è sempre un errore.
- Non imporre che tutte le righe occupino la stessa larghezza.
- Non cambiare parole o punteggiatura per migliorare la sagoma del blocco.

Per l'interlinea controllare accenti, ascendenti, discendenti e separazione
delle righe alla scala d'uso. Le raccomandazioni per paragrafi di lettura
continuativa, come il 120–145% discusso da Butterick, non sono una prescrizione
automatica per titoli monumentali o collage:
[Line spacing](https://practicaltypography.com/line-spacing.html).

## 5. Griglia editoriale e allineamenti

Definire una struttura adatta al contenuto: margini, assi, colonne o moduli,
intervalli e relazioni fra testo e visual. La griglia fornisce riferimenti per
posizione, scala e ritmo; può rimanere invisibile.
Riferimento: [Figma, Layout Grids](https://www.figma.com/best-practices/everything-you-need-to-know-about-layout-grids/).

Per la card scegliere pochi ancoraggi chiari: un bordo del testo, un asse
condiviso, un intervallo ricorrente o un limite di campitura. Non serve adottare
sempre lo stesso numero di colonne né rendere visibile una scacchiera.

Una griglia di base tipografica coordina le linee di scrittura; è distinta da
una griglia generale di impaginazione. Il suo passo dipende dal sistema
tipografico, e può cambiare fra aree:
[Adobe, baseline grid](https://helpx.adobe.com/indesign/desktop/layout-and-grid-tools/grids/use-a-baseline-grid.html).

Testo principale e attribuzione possono appartenere a moduli diversi. Uno
scarto, una rotazione o un elemento fuori griglia devono avere una funzione
nel sistema. Non obbligare ogni ritaglio Dada alla medesima linea di base.

## 6. Relazione fra testo e immagini

Progettare testo e visual insieme. Nella comunicazione da poster, gerarchia e
leggibilità vanno valutate nel contesto e alla distanza di fruizione:
[Adobe, Poster layout and design](https://www.adobe.com/express/learn/blog/poster-layout-design).

Per questa skill:

- L'LLM sceglie soggetti e metafore dal contenuto e dal contesto, rispettando
  eventuali richieste specifiche. Nessun soggetto ricorrente obbligatorio.
- Il rapporto può essere letterale, metaforico, ironico o puramente formale.
- Il visual partecipa alla struttura attraverso bordi, ritagli, direzioni,
  campiture o spazi; la sua funzione non si esaurisce nel riempire un vuoto.
- Le sovrapposizioni possono essere forti, purché non rendano ambigue le lettere.
- Evitare contatti accidentali fra bordi, tratti e lettere che simulano altri
  caratteri o sembrano errori di ritaglio.
- Prevedere zone di respiro e distinguere la densità del collage dalla densità
  immediatamente dietro il testo.

La prominenza della frase si giudica dal percorso di lettura, non solo dalla
dimensione nominale delle lettere.

## 7. Contrasto e scala di fruizione

Verificare il contrasto dove il testo incontra davvero il fondo, anche sopra
texture e fotografie. Due tinte molto sature non garantiscono un buon contrasto
di luminanza.

Come riferimento quantitativo per il testo digitale, WCAG indica 4,5:1 per
testo ordinario e 3:1 per testo grande, con definizioni ed eccezioni proprie.
Il criterio include immagini di testo; la classificazione dipende dalla scala
di presentazione. Questi rapporti non certificano da soli una card social:
[W3C, Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

Valutare l'immagine alla dimensione prevista nel feed e poi in dettaglio.
Un file grande può contenere lettere poco leggibili una volta ridotto.
Controllare anche l'attribuzione, quando presente, senza trasformarla in
microtesto decorativo. Se la scala d'uso non è ispezionabile, segnalare il limite
senza dichiarare verificata quella leggibilità.

## 8. Regole comuni ed eccezioni di stile

| Livello | Criterio |
| --- | --- |
| Vincolo del contenuto | Citazione fedele, ordine e punteggiatura preservati, attribuzione corretta quando presente. |
| Criterio di lettura | Sequenza comprensibile, lettere riconoscibili, spazi e separazioni intenzionali. |
| Buona pratica | Gerarchie motivate, registri coerenti, ancoraggi, proporzioni dei caratteri e respiro. |
| Libertà espressiva | Rotazioni, ritagli, contrasti estremi, disallineamenti e più font, se sostengono lo stile e restano leggibili. |

Nel Dada le irregolarità possono appartenere ai ritagli. Nel Neon possono
essere protagonisti scala, etichette e interferenze. Nel neoindustriale contano
parentela delle geometrie e allineamenti. Sono applicazioni ai profili, non
norme universali della tipografia.

Un effetto previsto dal profilo non giustifica automaticamente un difetto
accidentale. Il controllo cerca la funzione della scelta, oltre alla sua presenza.

## 9. Controllo operativo

Prima di generare:

1. Qual è l'ordine di lettura?
2. Quali variazioni tipografiche hanno un ruolo?
3. Quali margini e ancoraggi tengono insieme testo e visual?
4. Dove sono previsti contrasto locale e respiro?
5. Se è presente un nome, ha un registro leggibile ma subordinato alla citazione?

Dopo la generazione:

1. Rileggere parole, segni e attribuzione rispetto al testo originale.
2. Controllare proporzioni dei caratteri, ritmo degli spazi e collisioni.
3. Valutare la frase alla scala d'uso e poi i dettagli.
4. Verificare che il visual sostenga il percorso di lettura.
5. Distinguere un difetto osservabile da una preferenza estetica.
6. Correggere il difetto individuato, mantenendo il resto del brief.

## 10. Dal riferimento al prompt

Usare questo modulo per la progettazione e il controllo. Il profilo selezionato
specifica materiali ed eccezioni; l'LLM decide soggetto e composizione per il
caso concreto.

Nel prompt vanno le poche indicazioni pertinenti alla card, senza copiare ogni
volta un trattato. Un generatore raster non offre necessariamente controlli
tipografici deterministici: un parametro scritto non prova il risultato.
Verificare visivamente e non dichiarare valori misurati senza una misura reale.
