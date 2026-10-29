# Quote Card Designer: sviluppo condiviso

- Per creare o modificare stili di sviluppo, consultare
  `references/catalogo-stili.yaml` e seguire il campo `profile` della voce.
  Il catalogo esteso comprende anche stili non distribuiti dalla skill installata.
- Il flusso fra portatile e iMac è descritto in `docs/SVILUPPO-STILI.md`.
  Verificare lo stato Git e gli aggiornamenti remoti prima di modificare i file.
  Conservare e confrontare le modifiche presenti; evitare sovrascritture forzate.
- Tenere separati sviluppo, selezione della release, skill globale e pubblicazione
  Sites. Un aggiornamento di stile non autorizza a promuoverlo nella release o a
  pubblicarlo sul sito.
- Conservare profili, composizioni, prompt e immagini disponibili. Non descrivere
  anteprime recuperate dal sito come originali nativi. Non inventare materiali
  mancanti: consultare `PROVENIENZA.md` e il registro di riconciliazione.
- Per ogni card finale usare ImageGen per l'intera composizione; conservare la
  citazione, la spaziatura naturale e l'attribuzione allineata a destra se presente.
- Verificare la build della gallery dopo modifiche a catalogo o risorse. Se il
  cambiamento interessa la selezione o le dipendenze distribuite, verificare anche
  il pacchetto con `gallery/package_skill.py`.
