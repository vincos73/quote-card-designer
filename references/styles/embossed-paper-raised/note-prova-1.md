# Embossed Paper — prima prova, 29 ottobre 2026

L'utente ha richiesto la rinomina del precedente stile in Debossed Paper,
la creazione di un vero Embossed Paper e una prova con lettere sollevate
dalla carta. Nessuna candidatura o pubblicazione è stata richiesta.

## Produzione

Frase dimostrativa già presente nel progetto:
**Anche il silenzio ha una forma.** Nessuna attribuzione o firma.

Base effettivamente passata al tool come immagine da modificare:
`references/styles/debossed-paper/prova-1-avorio.png`, PNG nativo ImageGen
della precedente esplorazione. Si conserva la relazione fra frase serif
su quattro righe, conchiglia in basso a destra e carta avorio per isolare
visivamente la direzione del rilievo. Non è una reference adottata nel
profilo per tutte le future generazioni e non è un test A/B sull'utilità
di reference operative.

ImageGen integrato genera l'intera card modificata. Il primo prompt effettivo
è `prompt-prova-1.md`; output nativo `prova-1-prima.png`, 1122 × 1402 px RGB.
Le lettere sono chiaramente sollevate, ma altezza e bordi danno in parte
l'impressione di elementi applicati sul foglio.

Una sola correzione mirata con `prompt-prova-1-correzione.md`, usando quel PNG
come target: abbassare il rilievo e ammorbidire il raccordo alla carta,
conservando citazione, struttura, palette e luce. Output scelto `prova-1.png`,
1122 × 1402 px RGB, quasi 4:5, non ritagliato o ritoccato. La riduzione richiesta
nel prompt è una direzione visiva, non una misura verificata del risultato.
Anteprima per QA `anteprima-prova-1.png`, ridimensionata a 320 × 400 px con sips.

## Controllo visivo

Ispezionati risultato nativo e anteprima. Frase completa una sola volta,
maiuscola iniziale A, tutte le altre lettere minuscole, punto finale corretto.
Quattro righe nello stesso ordine, nessuna parola deformata per raggiungere
una larghezza comune. Frase dominante e conchiglia subordinata; nessuna
attribuzione o scritta aggiunta.

Facce delle lettere illuminate e rialzate rispetto al fondo; ombre corte
proiettate fuori dai bordi basso-destri, coerenti con la luce da alto-sinistra.
Anche i punti e la conchiglia sono positivi. Il rilievo resta riconoscibile
nell'anteprima, diversamente dalla base in incavo. Testo leggibile a quella
scala nella visualizzazione usata, senza certificazione su altri dispositivi.

La correzione rende le ombre più leggere e le spalle più morbide. Il rilievo
resta accentuato in alcuni tratti e il raccordo alla superficie conserva
un aspetto generativo; l'immagine non dimostra un risultato ottenibile con
una matrice reale. La texture e alcuni piccoli contorni differiscono dalla
base, quindi non si rivendica una conservazione identica di tutti i pixel.

## Limiti e conservazione

Una sola frase, palette, composizione e registro serif, con una correzione.
Non provati altri testi, sans, attribuzione, colori o produzione da zero
senza base. La richiesta corrente era una prova: non si avviano ulteriori
varianti per ampliare la validazione.

Il nuovo stile è sperimentale in `references/catalogo-stili.yaml`, id
`embossed-paper-raised`, nome **Embossed Paper**, entrambi gli stati release
e candidatura falsi. Il precedente stile mantiene id e risorse storici,
nome **Debossed Paper** e candidatura preesistente. Prompt, prima resa,
correzione e PNG nativo finale sono conservati.
