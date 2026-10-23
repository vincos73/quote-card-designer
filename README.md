# Quote Card Designer

Questo repository contiene lo skill `quote-card-designer` e la sorgente della [galleria completa degli stili](https://quote-card-designer-style-gallery.vincos.chatgpt.site/).

- `SKILL.md` e `references/catalogo-v1.yaml` definiscono il flusso e gli stili della release V1.
- `references/catalogo-stili.yaml` e `references/styles/` contengono la libreria estesa, inclusi gli stili sperimentali.
- [`gallery/README.md`](gallery/README.md) spiega come rigenerare la galleria e pubblicarla sul Sites esistente da Codex Cloud con il plugin Sites abilitato.

Per rigenerare la galleria dalla radice del repository: `python3 -m pip install -r gallery/requirements.txt` e `python3 gallery/build.py`.
