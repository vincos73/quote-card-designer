# Aggiungere uno stile

Usa questa guida per una richiesta esplicita di estensione o modifica della
libreria. Non serve leggerla per generare una card ordinaria.

## Scheda

Crea una directory con un identificatore breve in minuscolo e trattini.
Usa `profilo.yaml` con radice `Design Style`.

Mantieni queste famiglie di informazioni, con sottocampi adatti al linguaggio:

- `Name` e `Concept`.
- `Canvas`, con `Ratio` e tipo di output.
- `Mood`.
- `Color Palette`, con valori e ruoli.
- `Typography`, con registri e gerarchie.
- `Layout`, con relazioni compositive essenziali e vincoli di integrazione.
- `Elements`, oppure `Graphic Elements` e `Imagery`, per il repertorio.
- `Effects`.
- `Rules`, oppure `Visual Rules` con eventuali `Exclusions`.

Puoi aggiungere campi pertinenti come temperatura, allineamento o texture.
Non creare dati di riempimento per completare uno schema.

Prevedi l'attribuzione facoltativa fornita dall'utente o verificata nella fonte:
un registro più piccolo e visivamente più leggero della citazione, coerente con
il profilo e leggibile. Puoi rappresentarla in `Typography > Attribution` e in
`Content Contract > author`. Se manca, il layout si ricompone senza segnaposto.

Descrivi le regole del linguaggio separatamente da soggetti e impaginati di una
singola prova. Palette e font sono valori di partenza, sostituibili su richiesta.
Gli elenchi di soggetti sono repertori aperti: l'LLM sceglie di volta in volta
in base a citazione e contesto, rispettando un eventuale soggetto richiesto.
Chiarisci contraddizioni nel materiale fornito senza cambiare silenziosamente
una direzione già approvata.

## Composizioni separate

Per uno stile con più strutture compatibili, conserva nel profilo i principi
che devono reggere in tutte le card. Metti le distribuzioni alternative in
`composizioni.yaml`, nella stessa directory. Aggiungi al documento del profilo
la chiave alla radice `Composition Library: composizioni.yaml`.

La libreria ha radice `Composition Library`, `Style Name` uguale al nome del
profilo, una sezione `Selection` e una lista `Families`. Ogni famiglia contiene
`id`, `Name`, `Use When`, `Structure`, `Text Adaptation` e `Format Adaptation`;
può aggiungere assi di variazione e controlli pertinenti. Descrivi relazioni
adattabili, senza fissare una citazione, un soggetto, coordinate o una palette.
Non trasformare ogni elemento del repertorio in una famiglia obbligatoria.

Il flusso comune [stile e composizione](composizione.md) guida la scelta interna.
I profili precedenti senza libreria restano validi. La confezione V1 deve
includere i file collegati; l'esportazione da catalogo incorpora stile e
libreria in due sezioni YAML, così il testo copiato è autosufficiente.

## Catalogo e collegamenti

Aggiorna l'indice distribuito `catalogo-v1.yaml` con identificatore, nome, alias,
descrizione breve, tag e percorso del profilo relativo alla radice della skill.
Nella libreria di sviluppo, se presente, aggiorna anche `catalogo-stili.yaml`;
la selezione di release e il sito devono essere generati dalla stessa sorgente.
Per un nuovo esempio aggiungi immagine, note e prompt effettivo e collega i
percorsi nella stessa voce. Se l'esempio manca, ometti quei campi.

Il catalogo contiene indicazioni per scegliere e aprire file; non deve contenere
l'intero profilo. Se cresce molto, suddividilo per famiglie prima di aumentare
stabilmente il contesto di ogni richiesta.

## Esempi e controllo

Per un esempio generato, conserva testo, immagine nativa e prompt effettivo.
Nelle note indica cosa trasferire e cosa apparteneva alla singola composizione.
Una card riuscita è un esempio di calibrazione, non prova di ripetibilità.

Per uno stile sperimentale che potrebbe beneficiare di immagini di riferimento,
prima di renderle parte del flusso prepara sempre una coppia di prove: stessa
frase letterale, formato, palette, famiglia compositiva e prompt di base; in
una prova passa le immagini a ImageGen dichiarando quali proprietà trasferire,
nell'altra non passarle. La palette resta una scelta indipendente dalle
reference, salvo richiesta esplicita dell'utente. Confronta gerarchia e
leggibilità del testo, correttezza letterale, qualità dei materiali, varietà
compositiva e rischio di copiare i soggetti o l'impaginato degli esempi.
Mostra entrambe le prove e registra vantaggi, difetti e limiti del confronto.
La decisione se usare stabilmente le immagini si prende con l'utente dopo il
test; non dedurla dalla sola riuscita di una card e non aggiungere immagini
operative automaticamente al pacchetto.

Controlla che i percorsi siano relativi e risolvibili, che il file YAML sia
leggibile e che i contenuti siano trasferibili. Mantieni fuori dal pacchetto
identità personali, percorsi locali e note operative di progetto.

Prova il nuovo stile su frasi diverse e su almeno una preferenza modificata.
Se non è stato provato, dichiaralo nel resoconto di sviluppo.
L'aggiunta di un profilo compatibile richiede una voce di catalogo, non un nuovo
elenco nel nucleo. Cambia SKILL.md solo per un nuovo comportamento condiviso.

