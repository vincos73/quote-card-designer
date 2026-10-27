# Catalogo visivo V1

Sorgenti del catalogo pubblico: interfaccia Indice svizzero, dati e anteprime approvate della skill 0.4.0. Il catalogo mostra 50 stili in 11 categorie; la gallery completa e i suoi candidati sono un progetto distinto.

Esegui `python3 gallery/catalogo-v1/build.py` dalla radice del repository. La build predefinita va in `build/catalogo-v1-dist/`; con `--output <percorso>` si può scegliere un'altra directory. Le immagini sono verificate rispetto a `asset-manifest.json` prima di essere copiate.

Il progetto Sites mantiene il proprio checkout e il proprio `.openai/hosting.json`. La pubblicazione richiede di allineare le modifiche nel checkout Sites, conservare il manifest e l'accesso pubblico esistente, quindi usare il flusso Sites. Non sostituire il catalogo pubblico con la gallery di sviluppo.

Pubblicazione del 27 ottobre 2026: Sites versione **4**, sorgente `c17d842fff2d81d922fb93bd23e15a485d7d6575`, accesso pubblico invariato. Ricevuta: `pubblicazione-v4.json`.
