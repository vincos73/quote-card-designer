# Editorial Interlock · confronto fra due prompt

Prova del 26 ottobre 2026: due immagini ImageGen integrate, formato verticale 4:5, con la stessa frase «Le idee crescono quando cambiano prospettiva.».

## A · Prompt breve senza profilo passato al generatore

> Crea una quote card verticale 4:5 con la frase «Le idee crescono quando cambiano prospettiva.» nello stile Editorial Interlock.

[Immagine A](prompt-breve.png) · SHA-256 `42ff354bbaa42f51eba945487a2dae6d481150011a11ce1acc5cec81a3eb334c`

## B · Indicazioni derivate dal profilo della skill

> Card editoriale completa 4:5 con un forte soggetto materiale centrale intrecciato alla tipografia come copertina di rivista sperimentale. Frase esatta «Le idee crescono quando cambiano prospettiva.» una volta come composizione principale, distribuita in gruppi di parole di scale diverse ma con ordine di lettura naturale; il soggetto centrale (un prisma di vetro e carta che cambia asse prospettico) attraversa selettivamente spazi e alcuni contorni, passando davanti/dietro in pochi punti precisi senza coprire lettere. Colore tipografico armonizzato al soggetto, contrasto verificato, carta opaca, intervalli calmi; niente titoli o testi ulteriori.

[Immagine B](direzione-skill.png) · SHA-256 `688a30faa9e8630f7881694b96f04e079d9f43da4eec47e4d89e4d33fc3cb0b8`

Il prompt B traduce il profilo Editorial Interlock registrato come versione 0.3.3. Specifica anche il soggetto: un prisma di vetro e carta. Non documenta un'esecuzione dell'intero flusso della skill.

## Cosa si osserva

A propone un ambiente architettonico con la frase come blocco tipografico. B intreccia un oggetto centrale e la frase, con variazioni di scala e parole distribuite intorno al soggetto. Entrambe le immagini riportano la frase e il punto finale; nel risultato B alcuni tratti delle lettere si fondono con i bordi del prisma e la lettura richiede più attenzione.

## Limiti

Sono due singoli risultati, non un test controllato dell'effetto isolato della skill. Per B non è registrata una revisione successiva. I prompt differiscono per lunghezza, livello di dettaglio e scelta del soggetto. I prompt A sono stati congelati prima della lettura dei profili per la serie B, ma le prove sono state condotte in un contesto sequenziale condiviso; la registrazione non dimostra un isolamento completo dell'agente. Modello raster, seed e impostazioni non sono esposti; non ci sono ripetizioni o valutazioni indipendenti. La preferenza estetica rimane soggettiva.

I prompt e le impronte dei file sono conservati anche in [evidenze.json](evidenze.json).
