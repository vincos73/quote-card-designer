# Halftone e Duotone — ricerca e scelte di stile

Fonti consultate sul web il 24 ottobre 2026. La distinzione riguarda due
proprietà diverse della riproduzione fotografica; i termini non sono opposti.

## Caratteristiche verificate

**Halftone (retino).** I toni continui della foto vengono simulati tramite
punti: area, densità o distribuzione dei segni cambiano la quantità apparente
d'inchiostro. Nel retino AM il passo è regolare e varia la dimensione del
punto; altri retini variano la distribuzione. Il procedimento funziona con
un solo inchiostro, ma si applica anche a separazioni multiple, incluso CMYK.
Non significa quindi necessariamente bianco e nero.

**Duotone (bicromia fotografica).** La stessa immagine in scala di grigi è
riprodotta con due inchiostri, ciascuno con una propria risposta ai toni.
Un caso tradizionale usa nero per le ombre e un secondo colore per arricchire
mezzitoni e luci. Sovrapposizione degli inchiostri e carta producono toni
intermedi: non sono soltanto due campiture piatte o due colori RGB totali.
Una foto tinta con un solo inchiostro colorato è invece un monotone.

Un duotone stampato può impiegare retini. Gli allegati colorati dell'utente
mostrano proprio proprietà sovrapposte: retino visibile e resa cromatica
ridotta. Il colore da solo non basta per classificare una foto come duotone.

## Decisioni per i due profili

| Aspetto | Halftone Editorial B/W | Duotone Halftone |
| --- | --- | --- |
| Firma visiva | Punti tondi ordinati che ricostruiscono la foto | Lo stesso linguaggio fotografico retinato in bicromia |
| Default cromatico | Nero neutro e bianco puro | Due colori dominanti a contrasto, per esempio blu e giallo |
| Toni | Rapporto tra punti neri e intervalli bianchi | Rapporto tra punti, intervalli e masse dei due colori |
| Superficie | Stampa ruvida con usura contenuta e punto leggibile | Stampa ruvida con punto leggibile e contrasto cromatico |
| Retino evidente | Obbligatorio | Obbligatorio |
| Testo | Grande sovraimpressione nera o bianca | Grande sovraimpressione con uno dei due colori |

La precedente proposta di Duotone a toni continui è stata superata dalla
direzione esplicita dell'utente: per questa libreria si vuole un **Duotone
Halftone**, con retino sempre visibile e due colori a contrasto. La ricerca
tecnica resta il contesto; non sostituisce il linguaggio grafico richiesto
negli allegati.

In entrambi i profili la fotografia dipende dal significato della frase;
ritratti, porte o scale non sono soggetti obbligatori. Il nuovo test B/W
usa una persona con lente d'ingrandimento per «Cambiare sguardo cambia tutto».
Prima è stato mostrato il risultato guidato dai riferimenti, poi è stata
prodotta una baseline con richiesta breve senza immagini.

I PNG sono simulazioni visive RGB: non certificano separazioni fisiche a uno
o due inchiostri, curve di stampa o una frequenza LPI. Non viene dichiarata
una resa perfetta o ripetibile sulla base di un solo test per profilo.

## Fonti lette

1. [PrintWiki — Halftone](https://printwiki.org/Halftone): riproduzione fotografica tramite punti, dimensione e densità del retino.
2. [Adobe — Convert an image to Bitmap mode](https://helpx.adobe.com/photoshop/desktop/adjust-color/color-modes/convert-an-image-to-bitmap-mode.html): distingue soglia, dithering e Halftone Screen; documenta frequenza, angolo e forma del punto.
3. [Adobe — Duotones in Photoshop](https://helpx.adobe.com/photoshop/desktop/adjust-color/color-effects-techniques/duotones-in-photoshop.html): numero d'inchiostri, monotone/duotone, curve per ciascun inchiostro e colori risultanti dalle sovrapposizioni.
4. [Adobe — Create and edit duotone images](https://helpx.adobe.com/photoshop/desktop/adjust-color/color-effects-techniques/create-and-edit-duotone-images.html): immagine in scala di grigi, scelta degli inchiostri e distribuzione attraverso curve distinte.
5. [PrintWiki — Duotone](https://printwiki.org/Duotone): due retini della medesima foto, ruoli tonali e distinzione dal cosiddetto fake duotone.
6. [Wikipedia — Halftone](https://en.wikipedia.org/wiki/Halftone): consultata come fonte secondaria per retini a colori, separazioni e distinzione AM/FM.

I precedenti URL brevi Adobe reindirizzano a pagine nuove; qui sono riportati
gli indirizzi canonici effettivamente letti. Le copie HTML di ricerca sono
conservate nell'area di lavoro, non sono dipendenze del pacchetto di stile.
