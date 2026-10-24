# Studio Risograph e overprint

Fonti web e tutti i nove allegati dell'utente consultati il 24 ottobre 2026.

## Indicazione di progetto

La scelta dell'utente è mantenere **un solo stile Risograph, sempre con
overprint e mescolanza visibile**. Si regola l'estensione dell'effetto,
non la sua presenza. Non viene creato uno stile Overprint separato per
questa direzione e la variante knockout non è offerta nel catalogo.

La distinzione tecnica resta valida: il materiale Riso può esistere anche
senza un collage trasparente e l'overprint può essere usato in altri
processi. Unirli sempre è la scelta estetica del nostro profilo, non una
caratteristica universale della risografia.

Nel repository esisteva una bozza chiamata Neo Risograph, concentrata su
ritagli d'archivio e piccoli scarti di colore. Questa viene aggiornata allo
studio fotografico richiesto, mantenendo l'ID `neo-risograph` e il vecchio
nome come alias. Il profilo e gli esempi precedenti sono conservati; la
struttura del nuovo YAML raccoglie tutte le regole sotto `Design Style`.

## Caratteristiche sostenute dalle fonti

- **Passaggi a colori spot.** SVA RisoLAB descrive stencil avvolti su tamburi d'inchiostro, con il disegno separato in strati di colore. RISO documenta duplicatori a uno e a due colori: il materiale non richiede sempre una composizione a più immagini sovrapposte.
- **Carta non patinata e deposito tattile.** RISOTTO spiega l'assorbimento su carte non patinate e il possibile trasferimento dell'inchiostro ancora fresco. La grana non è una patina da stendere uniformemente sopra ogni immagine.
- **Dithering o retino.** La FAQ di RISOTTO distingue una modalità Grain dall'aspetto più fine e sparso e diverse modalità Screen. Riso non equivale necessariamente ai grandi punti tondi del profilo Halftone.
- **Copertura irregolare e piccoli scarti.** Campiture molto dense possono risultare disomogenee; passaggi ripetuti possono produrre segni di trascinamento e disallineamento. Sono possibilità materiali da dosare, non difetti obbligatori da applicare ovunque.
- **Traslucenza degli inchiostri.** La FAQ conferma la natura generalmente traslucida degli inchiostri, indicando il metallico oro come eccezione più opaca. Nei nostri test si simulano normali inchiostri colorati, non quelli metallici.
- **Toni fotografici e gradienti sono possibili.** La guida avanzata tratta densità, fotografia e gradazioni: il vecchio divieto assoluto di gradienti non descriveva bene il processo. La proposta conserva toni costruiti dall'inchiostro, evitando sfumature digitali lucide.

Il conteggio dei passaggi, le formulazioni e le impostazioni dipendono da
macchina, inchiostro e stampatore. Le indicazioni numeriche delle guide
non diventano controlli certificati di ImageGen.

## Che cosa aggiunge overprint

Adobe distingue il knockout, nel quale il colore superiore riserva lo
spazio sottostante, dalla sovrastampa che lascia interagire gli inchiostri.
Nella nostra simulazione, una forma rossa sopra una blu mantiene entrambe
le componenti e genera una zona mista più scura. Questo effetto non è una
terza sagoma opaca aggiunta all'incrocio.

Le due modalità attive del profilo sono quindi:

| Modo | Scelta grafica |
| --- | --- |
| Selettivo | Una o poche intersezioni significative mostrano il colore misto |
| Dominante | Il collage è costruito soprattutto dalle immagini che si attraversano |

La modalità senza mescolanza è stata provata per confronto e non scelta.
L'overprint non impone più grana o disallineamento: questi aspetti possono
essere dosati senza eliminare la mescolanza. I modi Hard Light e Color Burn mostrati nella JPG
didattica sono metodi digitali per ottenere un aspetto, non formule
universali del comportamento degli inchiostri in stampa.

## Lettura degli allegati

I tre JPG mostrano un ritratto con vegetazione in due colori, esempi
fotografici risoprint con sovrapposizioni e una tavola di metodi di fusione.
I sei AVIF sono stati scaricati e convertiti in copie PNG per osservarli;
gli originali sono conservati.

- `presentation-9-o.avif`: frammento di busto e rosa su passaggi distinti, con intersezioni più scure.
- `presentation-10-o.avif`: busto e segnale sovrapposti, con i dettagli di entrambi percepibili.
- `presentation-8-o.avif`: figura e cornice attraversate da aree cromatiche; l'impaginato non è un requisito dello stile.
- `presentation-4-o.avif`: dettaglio ravvicinato della grana fine e irregolare, utile a distinguere questo materiale dai grossi punti Halftone.
- `presentation-7-o.avif`: soggetti fotografici ripetuti su più passaggi, con incroci e una componente nera aggiuntiva.
- `presentation-2-o.avif`: teschio e vegetazione stampati su passaggi che si incontrano.

Nomi, etichette promozionali, corpi, animali, armi o fiori degli esempi non
sono contenuti da copiare automaticamente. In una quote card i soggetti
devono essere pertinenti alla frase.

## Prova visuale

La frase dimostrativa è «Le idee crescono quando si incontrano».
Una mano fotografica blu e un ramo corallo esprimono incontro e crescita.
La prima prova usa overprint selettivo. Una revisione della stessa card
usa knockout nelle intersezioni, conservando geometria, palette e grana
quanto consentito dall'editing generativo.

Solo le copie di `presentation-9-o.avif` e `presentation-4-o.avif` sono
input della prima generazione; la seconda riceve soltanto la prima card.
Le reference esterne non vengono rese dipendenze automatiche del profilo.
Il test non confronta con/senza reference né dimostra ripetibilità.

Nel pacchetto sono inclusi il [resoconto del confronto](confronto.md) e
l'[esempio scelto con overprint](esempio-overprint.png). Il controllo
knockout resta nel repository di sviluppo e non è incluso. Nel test la
grana rimaneva visibile in entrambi; cambiava il colore degli incroci.
L'esempio con mescolanza è quello scelto. Il knockout resta un controllo
storico, non una seconda variante nel catalogo. Il default selettivo
regola quanto estendere l'overprint: la sua presenza è sempre richiesta
dal profilo. Non è un vincolo universale del processo di stampa.

I PNG sono simulazioni RGB: non certificano colori fluorescenti reali,
separazioni spot o un risultato identico su una macchina Riso fisica.

## Fonti lette

1. [SVA RisoLAB — What is a Risograph?](https://risolab.sva.edu/): stencil, tamburi, colori spot e utilizzo artistico.
2. [RISO — The Art of RISO](https://us.riso.com/industries/art-communities/): processo e applicazione nella comunità artistica, incluso SVA RisoLAB.
3. [RISO — Digital Duplicators](https://us.riso.com/products/digital-duplicators/): famiglie di macchine a uno e a due colori.
4. [RISOTTO — What is risograph printing?](https://risottostudio.com/pages/what-is-risograph-printing): stencil e passaggi, inchiostri, carta e caratteristiche materiali.
5. [RISOTTO — Printing FAQ](https://risottostudio.com/pages/printing-faq): traslucenza, modalità Grain/Screen e comportamento delle fotografie.
6. [RISOTTO — Advanced print setup](https://risottostudio.com/pages/advanced-print-setup): densità, campiture, trascinamenti, gradazioni e registro.
7. [RISOTTO — Basic print setup](https://risottostudio.com/pages/basic-print-setup): separazione dei passaggi, imperfezioni e preparazione del lavoro.
8. [Adobe Illustrator — Overprint](https://helpx.adobe.com/illustrator/using/overprinting.html): differenza tra knockout e sovrastampa, interazione dei colori e anteprima.

Le copie HTML di ricerca e gli allegati originali sono conservati
nell'area di sviluppo, non in questo pacchetto. Gli URL inizialmente
tentati e risultati inesistenti non sono citati come fonti.
