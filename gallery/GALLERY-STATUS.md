# Gallery di sviluppo · stato del 27 ottobre 2026

La [gallery di sviluppo](https://quote-card-designer-style-gallery.vincos.chatgpt.site/) è pubblicata alla versione Sites **41** con l'interfaccia Indice svizzero. Contiene **78 stili**, **167 immagini**, **50 inclusi nella skill 0.4.0**, **3 candidati** e 28 stili fuori release, candidati inclusi.

I candidati sono **Photo Marker**, **Décollage** e **Typewritten Marginalia**. Le prime due candidature sono state aggiunte il 27 ottobre; Typewritten Marginalia era già candidata nella versione 40. Nessuno dei tre è incluso nel pacchetto distribuito 0.4.0. Il [catalogo pubblico V1](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site/) mantiene i suoi 50 stili.

La versione 41 conserva tutte le 78 schede e le 167 immagini della versione 40. I soli cambi di contenuto delle schede sono i badge e gli attributi di candidatura di Photo Marker e Décollage; ricerca, filtri, esempi, profili, copia e ingrandimento conservano il comportamento esistente. Gli accessi della gallery sono rimasti invariati: condivisione con gli invitati già autorizzati. Ricevuta: [pubblicazione-v41.json](pubblicazione-v41.json).

`gallery/build.py` applica `swiss_gallery.py` e `swiss-gallery.css` alla gallery prodotta dai sorgenti. La build locale può contenere studi non presenti online, inclusi quattro studi Neo Swiss. Non sincronizzare l'intera build sul sito senza confrontare le differenze e verificare che tutti gli studi siano pronti per la pubblicazione.

## Aggiornamento successivo in parallelo

La versione Sites **42**, pubblicata successivamente da un altro lavoro, aggiunge Filament Collage con due immagini e conserva integralmente le 78 schede e il layout della versione 41: **79 stili, 169 immagini e 3 candidati**. I sorgenti di Filament sono oggetto di lavoro locale separato e non fanno parte del commit di questo intervento; lo snapshot della libreria versionato qui riproduce la selezione di 78 stili della versione 41. Verificare e integrare il lavoro separato prima di rigenerare la versione 42 dal repository.
