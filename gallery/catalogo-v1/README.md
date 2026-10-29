# Catalogo visivo V1

Sorgenti del catalogo pubblico: interfaccia Indice svizzero, dati e anteprime approvate della skill 0.5.0. Il catalogo mostra tutti i 103 stili della release in 11 categorie; la gallery completa di sviluppo è un progetto distinto.

Esegui `python3 gallery/catalogo-v1/build.py` dalla radice del repository. La build predefinita va in `build/catalogo-v1-dist/`; con `--output <percorso>` si può scegliere un'altra directory. Le immagini sono verificate rispetto a `asset-manifest.json` prima di essere copiate.

La selezione coincide con `references/catalogo-v1.yaml`. Le 50 schede precedenti e le loro anteprime sono conservate; per i 53 stili aggiunti viene usato l'esempio principale indicato da `featured_example` nel catalogo di sviluppo. Il manifesto registra immagini e provenienza senza presentare le anteprime recuperate dalla gallery come originali nativi. Logo, font Archivo, licenza e interazioni riprendono la versione Sites 5 già pubblicata e sono inclusi nei sorgenti riproducibili.

Il progetto Sites mantiene il proprio checkout e il proprio `.openai/hosting.json`. La pubblicazione richiede di allineare le modifiche nel checkout Sites, conservare il manifest e l'accesso pubblico esistente, quindi usare il flusso Sites. Non sostituire il catalogo pubblico con la gallery di sviluppo.

Pubblicazione del 27 ottobre 2026: Sites versione **4**, sorgente `c17d842fff2d81d922fb93bd23e15a485d7d6575`, accesso pubblico invariato. Ricevuta: `pubblicazione-v4.json`.

Pubblicazione del 29 ottobre 2026: Sites versione **6**, sorgente `ae03980657478212b35aee021191aca7d28a1584`, skill **0.5.0**, **103 stili**. Accesso pubblico e revisione 2 della politica di accesso invariati. Stato di pubblicazione confermato da Sites e pagina online verificata nel browser. Ricevuta: [pubblicazione-v6.json](pubblicazione-v6.json). Controlli su selezione, immagini, conservazione e interazioni: [qa-0.5.0.json](qa-0.5.0.json).
