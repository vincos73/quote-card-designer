# Quote Card Designer

**Quote Card Designer aiuta a creare quote card con uno stile visivo distintivo**, a partire da una frase, un testo o un articolo. La skill combina la citazione con un linguaggio grafico riconoscibile: per esempio un poster Neo Swiss, una pagina a inchiostro o una composizione fotografica con lettere monumentali.

Non si limita a cambiare colori o caratteri. Per ogni stile usa indicazioni su tipografia, materiali, immagini e rapporto tra testo e composizione; adatta il risultato alla frase e alle preferenze dell'utente. La citazione viene preservata e il risultato va controllato, in particolare per accenti, punteggiatura e attribuzione.

## Come funziona

1. Fornisci una frase, un testo più lungo o il link a un articolo. Per un articolo la skill propone una citazione verificabile e la sua attribuzione.
2. Scegli uno stile dal [catalogo visivo](https://quote-card-designer-catalogo-v1.vincos.chatgpt.site) oppure chiedi un suggerimento. Puoi indicare colori, formato e un'eventuale firma.
3. La skill progetta la composizione e usa **ImageGen integrato** per generare la card completa. Controlla poi il testo e la leggibilità e, se necessario, interviene sul risultato.

La versione **0.4.0** comprende **50 stili**. Il formato predefinito è una card verticale 4:5; una richiesta esplicita può cambiarlo. ImageGen deve essere disponibile nell'ambiente usato: un prompt scritto da solo non è una card generata.

## Un esempio: prompt breve e direzione della skill

Due prove reali con la stessa frase, formato 4:5 e ruoli cromatici. A sinistra il generatore riceve una richiesta breve; a destra il prompt traduce le indicazioni del profilo **Neo Swiss** della skill, inclusi gerarchia, spazi e forma grafica.

| Senza indicazioni della skill | Con la direzione della skill |
| :---: | :---: |
| <img src="docs/confronto-neo-swiss/senza-skill.png" width="360" alt="Quote card ottenuta con prompt breve, testo blu su fondo avorio con forma arancione"> | <img src="docs/confronto-neo-swiss/con-direzione-skill.png" width="360" alt="Quote card ottenuta con indicazioni Neo Swiss della skill, testo blu su fondo avorio con forma arancione"> |

Nel primo risultato la frase usa un registro uniforme; nel secondo il contrasto tipografico mette in evidenza «cambiano». Entrambi riportano la frase completa. Sono **due output singoli**, non una misura generale dell'efficacia della skill: i prompt differiscono anche per livello di dettaglio e le prove non dimostrano ripetibilità. [Leggi condizioni, prompt e limiti](docs/confronto-neo-swiss/note-originali.md).

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

- [`SKILL.md`](SKILL.md) e [`references/catalogo-v1.yaml`](references/catalogo-v1.yaml) definiscono il flusso e i 50 stili distribuiti.
- La [gallery di sviluppo](https://quote-card-designer-style-gallery.vincos.chatgpt.site/) è riservata al proprietario e agli ospiti autorizzati. Contiene anche stili candidati e sperimentali: la presenza in gallery non implica l'inclusione nella release.
- [`gallery/catalogo-v1/`](gallery/catalogo-v1/README.md) contiene i sorgenti riproducibili del catalogo pubblico. [Stato della gallery di sviluppo](gallery/GALLERY-STATUS.md): versione pubblicata, candidati e differenze con la build locale.
- [Note della release 0.4.0](releases/0.4.0.md): selezione, verifiche e limiti.

Per rigenerare la gallery: installa le dipendenze con `python3 -m pip install -r gallery/requirements.txt`, poi esegui `python3 gallery/build.py`. Per creare uno ZIP della skill: `python3 gallery/package_skill.py`. La build locale può contenere studi non ancora pubblicati; confronta le differenze prima di aggiornare il sito.
