# Quote Card Designer

Skill per creare quote card artistiche da frasi, testi e articoli. La versione **0.4.0** comprende **50 stili**: i 41 della versione 0.3.6 e i nove candidati della gallery verificata il 27 ottobre 2026.

Nuovi stili inclusi: **Neo Swiss, Ink, Pencil, Ballpen, Photo Type Split, Photo Type Monument, Ink Drip, Type Blur e Graphite Negative**. Pencil usa la direzione lettering in costruzione; Ballpen quella con testo protagonista e caos equilibrato. I profili conservano le preferenze e i limiti delle prove documentate nella gallery.

- [Scarica lo ZIP 0.4.0 e il checksum](https://github.com/vincos73/quote-card-designer/releases/tag/v0.4.0).
- [Note della versione e verifiche](releases/0.4.0.md).
- `SKILL.md` e `references/catalogo-v1.yaml` definiscono il flusso e i 50 stili disponibili. Il nome del file del catalogo è mantenuto per compatibilità.
- Il [catalogo visivo V1](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site) è il collegamento per chi usa la skill ed è aggiornato ai 50 stili della 0.4.0. Per la disponibilità fa fede il catalogo incluso nel pacchetto.
- La [gallery completa](https://quote-card-designer-style-gallery.vincos.chatgpt.site/) è lo spazio di sviluppo del proprietario. `references/catalogo-stili.yaml` e i suoi file collegati conservano i 77 stili della libreria estesa; solo 50 entrano nel pacchetto.

La skill, i sorgenti e lo ZIP sono pubblicati su GitHub. Il 27 ottobre 2026 sono stati allineati anche i Sites: **gallery versione 39**, con 77 stili, 165 immagini, 50 inclusi e zero candidati; **catalogo V1 versione 3**, con i 50 stili della release. Accessi conservati: gallery condivisa con gli invitati esistenti, catalogo pubblico. Ricevute in `gallery/pubblicazione-v39.json` e `gallery/pubblicazione-catalogo-v1-v3.json`.

## Build e distribuzione

Installa le dipendenze in un ambiente Python: `python3 -m pip install -r gallery/requirements.txt`.

- `python3 gallery/build.py` rigenera la gallery locale e ne controlla struttura e risorse.
- `python3 gallery/package_skill.py` verifica selezione, versioni, nomi, profili e dipendenze, poi crea `build/quote-card-designer-0.4.0.zip`. Non sovrascrive un archivio esistente.

Lo ZIP contiene una sola directory `quote-card-designer/`, con istruzioni, catalogo, profili, composizioni e risorse collegate. Esclude la gallery completa, gli stili fuori release e gli studi di sviluppo non richiesti dai profili. Per l'installazione locale, sostituisci la directory della skill con quella estratta, conservando prima una copia della versione precedente.

Il [flusso della gallery](gallery/README.md) descrive build e pubblicazione sul Sites esistente. La build locale comprende studi non presenti online: non sostituire il sito con l'intera build senza esaminare le differenze.
