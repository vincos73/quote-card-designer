# Quote Card Designer

**Quote Card Designer aiuta a creare quote card con uno stile visivo distintivo**, a partire da una frase, un testo o un articolo. La skill combina la citazione con un linguaggio grafico riconoscibile: per esempio un poster Neo Swiss, una pagina a inchiostro o una composizione fotografica con lettere monumentali.

Non si limita a cambiare colori o caratteri. Per ogni stile usa indicazioni su tipografia, materiali, immagini e rapporto tra testo e composizione; adatta il risultato alla frase e alle preferenze dell'utente. La citazione viene preservata e il risultato va controllato, in particolare per accenti, punteggiatura e attribuzione.

## Come funziona

1. Fornisci una frase, un testo più lungo o il link a un articolo. Per un articolo la skill propone una citazione verificabile e la sua attribuzione.
2. Scegli uno stile dal [catalogo visivo](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site) oppure chiedi un suggerimento. Puoi indicare colori, formato e un'eventuale firma.
3. La skill progetta la composizione e usa **ImageGen integrato** per generare la card completa. Controlla poi il testo e la leggibilità e, se necessario, interviene sul risultato.

La versione **0.4.0** comprende **50 stili**. Il formato predefinito è una card verticale 4:5; una richiesta esplicita può cambiarlo. ImageGen deve essere disponibile nell'ambiente usato: un prompt scritto da solo non è una card generata.

## Un esempio: Editorial Interlock

Due prove reali con ImageGen, la stessa frase e il formato verticale 4:5. A sinistra una richiesta breve con il solo nome dello stile; a destra un prompt che traduce le indicazioni del profilo **Editorial Interlock** della skill, registrato nella prova come versione 0.3.3.

| Prompt breve, senza profilo | Indicazioni del profilo della skill |
| :---: | :---: |
| <img src="docs/confronto-editorial-interlock/prompt-breve.png" width="360" alt="Quote card con testo su un paesaggio architettonico, generata con prompt breve"> | <img src="docs/confronto-editorial-interlock/direzione-skill.png" width="360" alt="Quote card con un prisma centrale di vetro e carta intrecciato alla tipografia"> |

Nel primo risultato la frase occupa un paesaggio architettonico; nel secondo un soggetto centrale attraversa la composizione tipografica. Alcune lettere del secondo si sovrappongono al prisma e richiedono più attenzione nella lettura.

È un **confronto illustrativo fra due prompt**, non una dimostrazione isolata dell'effetto della skill: il secondo è più dettagliato e specifica anche il soggetto. Le immagini sono singoli risultati, senza prova di ripetibilità; il prompt guidato non documenta l'esecuzione dell'intero flusso della skill. [Condizioni, prompt integrali e limiti](docs/confronto-editorial-interlock/README.md).

## Installa la skill

Scarica lo [ZIP della versione 0.4.0](https://github.com/vincos73/quote-card-designer/releases/tag/v0.4.0): contiene la cartella `quote-card-designer/` con `SKILL.md` e tutti i riferimenti necessari. Nella release trovi anche il checksum SHA-256.

### Codex

1. Scarica ed estrai lo ZIP.
2. Copia l'intera cartella `quote-card-designer` in `~/.agents/skills/` per renderla disponibile nei tuoi progetti, oppure in `.agents/skills/` nel repository in cui vuoi usarla. Se esiste già una cartella con lo stesso nome, conserva prima una copia della versione precedente.
3. Apri una nuova chat Codex e chiedi, per esempio: «Usa `$quote-card-designer` per creare una card Neo Swiss con questa frase: …». Se la skill non appare, riavvia Codex.

La [documentazione ufficiale sulle skill](https://learn.chatgpt.com/docs/customization/overview#skills) descrive le cartelle globali e di progetto e il loro utilizzo.

### ChatGPT

In **ChatGPT Work**, se il tuo account offre gli agenti con skill personalizzate, apri l'agente, scegli **Add skill** e carica la skill seguendo le opzioni disponibili nell'interfaccia. Usa la cartella completa estratta dallo ZIP, o lo ZIP se l'interfaccia lo accetta. La disponibilità dipende dal prodotto e dai permessi del workspace. [Guida ufficiale agli agenti con skill](https://developers.openai.com/cookbook/articles/chatgpt-agents-sales-meeting-prep).

L'installazione locale in Codex non installa automaticamente la skill in ogni esperienza di ChatGPT. Per distribuirla come plugin installabile occorre un pacchetto e un percorso di pubblicazione dedicati; questo repository distribuisce attualmente lo **ZIP della skill**, non un plugin pubblico. [Documentazione sui plugin](https://developers.openai.com/plugins/concepts/plugins).

## Repository e gallery di sviluppo

- La **libreria di sviluppo condivisa** contiene **127 stili**: 50 nella release
  0.4.0, 34 candidati e 43 sperimentali. Profili e materiali disponibili sono
  versionati nel repository, anche quando lo stile non è distribuito. Per lavorare
  da portatile e iMac: [flusso di sviluppo e sincronizzazione](docs/SVILUPPO-STILI.md).
- [`SKILL.md`](SKILL.md) e [`references/catalogo-v1.yaml`](references/catalogo-v1.yaml) definiscono il flusso e i 50 stili distribuiti.
- La [gallery di sviluppo](https://quote-card-designer-style-gallery.vincos.chatgpt.site/) è riservata al proprietario e agli ospiti autorizzati. Contiene anche stili candidati e sperimentali: la presenza in gallery non implica l'inclusione nella release.
- [`gallery/catalogo-v1/`](gallery/catalogo-v1/README.md) contiene i sorgenti riproducibili del catalogo pubblico. [Stato della gallery di sviluppo](gallery/GALLERY-STATUS.md): versione pubblicata, candidati e differenze con la build locale.
- [Note della release 0.4.0](releases/0.4.0.md): selezione, verifiche e limiti.

Per rigenerare la gallery: installa le dipendenze con `python3 -m pip install -r gallery/requirements.txt`, poi esegui `python3 gallery/build.py`. Per creare uno ZIP della skill: `python3 gallery/package_skill.py`. La build locale può contenere studi non ancora pubblicati; confronta le differenze prima di aggiornare il sito.
