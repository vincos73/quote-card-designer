# Galleria degli stili

Questa directory contiene il sorgente della [galleria Sites](https://quote-card-designer-style-gallery.vincos.chatgpt.site/) e il generatore. Il catalogo è `references/catalogo-stili.yaml`; i profili e la maggior parte delle immagini sono in `references/styles/`. `source-assets/` contiene solo 16 immagini usate dalla galleria precedente che non coincidono con gli esempi correnti del profilo o non hanno un riferimento nel catalogo. Non sostituire il catalogo esteso con `references/catalogo-v1.yaml`.

## Aggiornare la galleria

1. Aggiungi o modifica il profilo, le immagini e la voce in `references/catalogo-stili.yaml`. Gli stili fuori release hanno `release_candidate: false`. Per un V1 candidate aggiungi anche `v1_shortlisted: true`: mostra il badge «V1 candidate» e il filtro «Candidates», senza inserirlo nei selezionati. I due stati non possono essere attivi insieme.
2. Installa le dipendenze: `python3 -m pip install -r gallery/requirements.txt`.
3. Dalla radice del repository esegui `python3 gallery/build.py`. La build genera `gallery/dist/index.html` e una JPEG per ogni esempio. `dist/` è ignorata da Git perché deriva dai sorgenti.
4. Controlla il risultato e committa i sorgenti su GitHub.

La build conserva ricerca, filtri per famiglia e release, profili YAML integrali e selettore degli esempi. Le immagini sono file separati: Sites rifiuta un singolo HTML oltre 25 MB.

La sincronizzazione controlla gli identificatori degli stili già presenti nel checkout Sites. Se il sito contiene stili assenti dalla build locale, si ferma prima di sostituire `dist/`: occorre allineare i sorgenti per conservare gli aggiornamenti pubblicati da altri ambienti.

## Pubblicare sul Sites esistente

La pubblicazione richiede il plugin **Sites** con accesso al progetto `appgprj_6adb7b4f342881918cd48a4c247a3092`. Il progetto è privato. Il manifest `gallery/.openai/hosting.json` conserva l'ID e la directory statica. Una credenziale Git di Sites è temporanea: non salvarla nel repository o nei segreti di GitHub.

Nel contesto Codex che dispone del plugin Sites:

1. Chiama `get_site` per confermare gli accessi correnti e `create_source_repository_write_credential` per ottenere la credenziale temporanea.
2. Apri la sorgente Sites con lo `site-workflow.mjs` del plugin in una directory vuota. Invia la credenziale al processo tramite stdin, come indicato dallo skill Sites. Conserva il `checkout_path` restituito.
3. Esegui `python3 gallery/sync_to_site_checkout.py <checkout_path>` dalla radice del repository GitHub.
4. Richiama `site-workflow.mjs` nello stesso checkout, passando la credenziale e un `archivePath` temporaneo. Il risultato deve contenere `commit_sha` e `archive` della sorgente caricata.
5. Conserva gli accessi restituiti da `get_site`. Se il sito è riservato al solo proprietario, usa `save_version_and_deploy_private` con quel `project_id`, `commit_sha` e `archive`. Se include altri visitatori, usa `save_site_version` e poi `deploy_site_version` con l'ID esatto della versione salvata. Se il risultato non è terminale, consulta `get_deployment_status`.

Se il plugin Sites non è disponibile in Codex Cloud, la build può essere preparata e committata da lì, ma la pubblicazione sul Sites esistente deve essere eseguita in una chat con il plugin abilitato. Il repository da solo non fornisce una credenziale di pubblicazione.
