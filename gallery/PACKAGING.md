# Risorse della skill distribuita

`package_skill.py` costruisce un nuovo ZIP senza modificare i sorgenti,
l'installazione globale, una release esistente o un sito.

Il catalogo selezionato determina i profili e le librerie compositive. I
riferimenti Markdown del nucleo, le note nominate dai profili e i documenti
collegati vengono inclusi. Le altre risorse hanno un ruolo esplicito in
`package-resources.yaml`:

- `runtime_assets`: immagini operative approvate, eventuali font e licenze,
  o altre risorse necessarie al funzionamento. Sono incluse quando un documento
  le richiama. Gli `Approved Image Inputs` devono appartenere a questo gruppo.
- `archive_assets`: studi, esempi di calibrazione non necessari come input,
  proposte e backup storici. Restano nel repository; nello ZIP i percorsi
  dichiarati nei profili e i collegamenti Markdown diventano URL dell'archivio.

I link d'archivio usano il commit completo `archive_revision`, non `main`.
Prima di creare ciascun link, il generatore confronta i byte locali con
`git show <commit>:<percorso>`. Se non coincidono, si ferma: non può descrivere
una nuova risorsa locale come già disponibile a quella revisione. Quando si
aggiorna il riferimento d'archivio, verificare che il commit sia disponibile
nel repository indicato e raggiungibile dal remoto. Il solo confronto locale
non prova l'accessibilità via rete.

Il confezionamento richiede quindi il clone Git e il commit indicato, oltre
alle dipendenze Python. L'uso ordinario della skill estratta non richiede Git
né la consultazione online degli studi per generare una card.

I documenti esportati spiegano quando una risorsa è esterna; i sorgenti e gli
originali non vengono riscritti, compressi o eliminati. La trasformazione dei
profili riguarda soltanto i percorsi d'archivio dichiarati, non le regole visive.
Un nuovo asset non classificato o un collegamento locale mancante blocca la
build. I link Markdown inline, alle immagini e con definizione separata sono
controllati anche rispetto all'elenco effettivo dei file confezionati. I nomi
storici citati nel testo libero non sono automaticamente dipendenze operative.

Verifica con una destinazione ZIP temporanea nuova:

```sh
python3 -m unittest discover -s gallery/tests -v
python3 gallery/package_skill.py --output /percorso/temporaneo/nuovo.zip
```

L'archivio di verifica può mantenere la versione dei sorgenti in sviluppo:
non costituisce da solo una nuova release pubblicata. Prima di distribuire
una futura release, aggiornare e verificare la versione nell'ambito di quella
specifica operazione.
