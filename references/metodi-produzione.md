# Scegliere come realizzare la card

Leggi `Production` nel profilo attivo. Le preferenze dell'utente prevalgono.
`Preferred Mode` orienta la rifinitura, non sostituisce la generazione: ogni
nuova composizione richiede ImageGen per la composizione visiva
dell'intera card. Una generazione scartata, o il solo inserimento di una foto
generata in una card progettata da uno script, non soddisfa questo requisito.
Verifica che gli strumenti e le risorse siano disponibili prima di promettere
il risultato.

- **`typeset`, rifinitura tipografica:** genera con ImageGen la card completa,
  comprese gerarchia, relazioni e lettering. Se serve, correggi la citazione e
  le geometrie con un motore di rendering e font reali, mantenendo la
  composizione generata come base visiva effettiva del risultato. Il profilo
  artistico non è già un template esecutivo.
- **`hybrid`, ibrida:** genera con ImageGen la composizione della card,
  progettando insieme visual e zone del testo. Puoi poi sostituire o comporre
  il testo con font reali e applicare livelli, maschere o materiali coerenti.
  Conserva l'immagine generata e la scena di rifinitura per le revisioni.
  Quando l'utente richiede esplicitamente il lavoro a livelli su una base
  approvata, conserva lo sfondo pulito come asset e riusalo per le varianti
  tipografiche. La ricostruzione generativa di uno sfondo può cambiare grana
  e colore locale: verifica il risultato prima di considerarlo la base fissa.
- **`generative`, generativa completa:** genera immagine e lettering insieme
  con ImageGen, soprattutto quando il tratto manuale o il materiale delle
  lettere fa parte dello stile. Controlla visivamente l'intera citazione; il
  nome di un font nel prompt non ne garantisce l'uso esatto.

La scelta ordinaria per l'utente è frase e stile. Gestisci il metodo senza
chiedergli dettagli tecnici; rendili espliciti quando cambiano un vincolo o la
resa richiesta. Se occorre un'alternativa, conserva i requisiti sostanziali e
dichiara il limite concreto. Non sostituire in silenzio un font esatto richiesto
con una somiglianza generata.

Carica i file font inclusi o effettivamente recuperabili nell'ambiente, con
licenza e provenienza. Un URL è una risorsa da risolvere, non prova del suo uso.
Mantieni spaziatura naturale e proporzioni dei glifi: risolvi la capienza con
a capo, composizione e corpi adatti, senza tracking arbitrario per riempire righe.
Se la correzione del testo richiederebbe di ricostruire da zero la card con uno
script, prova una revisione mirata con ImageGen. Se il difetto persiste, dichiara
il limite invece di consegnare un risultato solo tipografico.

In tutti i metodi verifica testo, attribuzione, dimensioni effettive, contrasto,
gerarchia e rapporto con il visual. Distingui tempo di esecuzione, preparazione
e revisione quando li confronti. Conserva il risultato accettato senza avviare
varianti o correzioni per il solo fatto che sono possibili.
