# Seconda card ricreata con un impaginatore

La card usa realmente **Archivo Bold 700**, larghezza nativa 100%, e **Libre Caslon Text Regular 400** per i testi piccoli. I font provengono dal repository ufficiale Google Fonts; i binari e le rispettive licenze sono conservati in `fonts/`. Famiglie, versioni, assi e SHA-256 sono nel YAML.

Il renderer legge `card.yaml`, eredita contenuto, palette e geometria dalla seconda prova e usa CoreText per la composizione e CoreGraphics per gli export. La verifica rifiuta un font diverso da quello previsto e controlla glifi mancanti, tagli e collisioni tra righe.

## File

- `card-archivo-700.png`: card 1440 × 1800 px.
- `card-archivo-700.svg`: versione vettoriale a tracciati, indipendente dalla disponibilità dei font sul computer che la apre.
- `card-archivo-700.pdf`: export PDF vettoriale.
- `confronto-generatore-impaginatore.png`: confronto a pari altezza con la versione generativa.
- `card.yaml`: configurazione del renderer e riferimenti ai font reali.
- `render.py`, `render.swift`: ingresso dal YAML e impaginatore.
- `verifica-impaginazione.json`: font effettivi, metriche, controlli e campioni del fondo.
- `verifica-riproducibilita.json`: controllo di una seconda esecuzione e corrispondenza degli output.

## Rigenerazione

Su macOS, con Swift e Python 3 più PyYAML già disponibili:

```sh
python3 render.py
```

Il processo non richiede accesso alla rete dopo il download iniziale. Modificare i testi o i parametri nel YAML e ricreare gli export. Non alterare i file dei font mantenendo le vecchie impronte: il renderer blocca il lavoro quando il binario non corrisponde al font fissato.

## Scelte e risultato

Si conservano frase, estratto, a capo e palette della seconda prova. I corpi richiesti dal YAML vengono ridotti uniformemente per blocco, senza comprimere i caratteri: 155,3442 px per la frase, 236,4919 px per l'estratto e 23,6033 px per i microtesti. Il rapporto tra i due registri principali è circa 1,522. Gli assi effettivi sono verificati, senza font sostitutivi.

La versione impaginata ha lettere meno serrate e un peso più controllato di quella generativa. Il fondo usa il colore esatto `#18212E`, senza grana o variazioni di superficie. La geometria segue il YAML: il generatore aveva interpretato alcune posizioni, tra cui quella del secondo blocco del footer, collocato nella terza colonna anziché nella seconda. Il confronto mostra quindi la risposta dei due metodi allo stesso progetto, con una scelta di font ora esplicita; non isola sperimentalmente una sola variabile.

Archivo è una scelta progettuale adatta al linguaggio. Non è un'identificazione del font dei riferimenti originali, la cui famiglia resta incerta. La rasterizzazione può cambiare con un'altra versione del sistema o un altro motore; l'SVG a tracciati conserva le forme e le posizioni senza dipendere dal caricamento dei font.

Fonti: [Archivo di Omnibus-Type](https://www.omnibus-type.com/fonts/archivo/), [Archivo in Google Fonts](https://github.com/google/fonts/tree/main/ofl/archivo), [Libre Caslon Text in Google Fonts](https://github.com/google/fonts/tree/main/ofl/librecaslontext).
