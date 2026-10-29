# Gallery di sviluppo · stato del 29 ottobre 2026

## Gallery versione 61 · candidature e nomi · 29 ottobre 2026

Su richiesta dell'utente diventano candidati: **Cut Paper, Chalkboard, Cartographic, Civic, Food, Sport, Finance, Economy, Science Book, Space Atlas, Tech Mechanism ed Eco Print**.

Nomi aggiornati: Chalkboard Design → Chalkboard; Geografica → Cartographic;
Carta Comune / Segni abitati → Civic; Impronta di gusto → Food;
Motion Proof → Sport. Identificatori e percorsi restano stabili; i vecchi
nomi sono conservati come alias.

Gallery online: **122 stili, 262 immagini, 50 inclusi nella 0.4.0,
46 candidati e 26 esclusi**. Le altre 110 schede e tutti i 514 file
preesistenti diversi dall'indice sono conservati identici, incluse le sezioni
di studio e i confronti. Gli YAML consultabili riportano nomi e candidatura.
Ricerca dei dodici stili e dei vecchi nomi verificata nel browser.
Accessi `custom` e revisione della policy 1 invariati.

La libreria locale conta **127 stili, 272 immagini, 46 candidati e
31 sperimentali**. La release 0.4.0 conserva identici tutti i suoi 150 file;
la skill globale installata non viene modificata.

[Ricevuta](pubblicazione-v61.json), [verifiche](qa/candidates-v61.json).

## Storico · 27 ottobre 2026

La [gallery di sviluppo](https://quote-card-designer-style-gallery.vincos.chatgpt.site/) è pubblicata alla versione Sites **41** con l'interfaccia Indice svizzero. Contiene **78 stili**, **167 immagini**, **50 inclusi nella skill 0.4.0**, **3 candidati** e 28 stili fuori release, candidati inclusi.

I candidati sono **Photo Marker**, **Décollage** e **Typewritten Marginalia**. Le prime due candidature sono state aggiunte il 27 ottobre; Typewritten Marginalia era già candidata nella versione 40. Nessuno dei tre è incluso nel pacchetto distribuito 0.4.0. Il [catalogo pubblico V1](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site/) mantiene i suoi 50 stili.

La versione 41 conserva tutte le 78 schede e le 167 immagini della versione 40. I soli cambi di contenuto delle schede sono i badge e gli attributi di candidatura di Photo Marker e Décollage; ricerca, filtri, esempi, profili, copia e ingrandimento conservano il comportamento esistente. Gli accessi della gallery sono rimasti invariati: condivisione con gli invitati già autorizzati. Ricevuta: [pubblicazione-v41.json](pubblicazione-v41.json).

`gallery/build.py` applica `swiss_gallery.py` e `swiss-gallery.css` alla gallery prodotta dai sorgenti. La build locale può contenere studi non presenti online, inclusi quattro studi Neo Swiss. Non sincronizzare l'intera build sul sito senza confrontare le differenze e verificare che tutti gli studi siano pronti per la pubblicazione.

## Aggiornamento successivo in parallelo

La versione Sites **42**, pubblicata successivamente da un altro lavoro, aggiunge Filament Collage con due immagini e conserva integralmente le 78 schede e il layout della versione 41: **79 stili, 169 immagini e 3 candidati**. I sorgenti di Filament sono oggetto di lavoro locale separato e non fanno parte del commit di questo intervento; lo snapshot della libreria versionato qui riproduce la selezione di 78 stili della versione 41. Verificare e integrare il lavoro separato prima di rigenerare la versione 42 dal repository.
