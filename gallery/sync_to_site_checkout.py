"""Copy a built gallery into an already opened Sites source checkout."""
from pathlib import Path
import json
import shutil
import sys

GALLERY = Path(__file__).resolve().parent
PROJECT_ID = "appgprj_6adb7b4f342881918cd48a4c247a3092"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python3 gallery/sync_to_site_checkout.py <checkout_path>")
    checkout = Path(sys.argv[1]).expanduser().resolve()
    source_manifest = GALLERY / ".openai/hosting.json"
    destination_manifest = checkout / ".openai/hosting.json"
    if not (checkout / ".git").is_dir():
        raise SystemExit(f"Non è un checkout Git di Sites: {checkout}")
    if not destination_manifest.is_file():
        raise SystemExit(f"Manca il manifest Sites nel checkout: {destination_manifest}")
    source = json.loads(source_manifest.read_text())
    destination = json.loads(destination_manifest.read_text())
    if source.get("project_id") != PROJECT_ID or destination.get("project_id") != PROJECT_ID:
        raise SystemExit("Il project_id del checkout non coincide con la galleria")
    built = GALLERY / "dist"
    if not (built / "index.html").is_file():
        raise SystemExit("Manca la build. Esegui prima python3 gallery/build.py")
    target = checkout / "dist"
    if target.is_dir():
        shutil.rmtree(target)
    shutil.copytree(built, target)
    print(f"Galleria copiata in {checkout}. Usa il flusso Sites per push e deploy privato.")


if __name__ == "__main__":
    main()
