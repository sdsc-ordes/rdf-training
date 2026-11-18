# /// script
# requires-python = ">=3.11"
# dependencies = ["segno"]
# ///
"""Write QR codes for the repository and worksheets on GitHub to src/slides/public/qr/.

They point to the Markdown worksheets on main until the course site is published.
"""

from pathlib import Path

import segno

REPO = "https://github.com/sdsc-ordes/rdf-training"
WORKSHEETS = f"{REPO}/blob/main/src/site/hands-on/"
PAGES = {
    "site": REPO,
    "h1": WORKSHEETS + "h1-model.md",
    "h2": WORKSHEETS + "h2-validate.md",
    "h3": WORKSHEETS + "h3-query.md",
}
OUT = Path(__file__).resolve().parents[2] / "src" / "slides" / "public" / "qr"

OUT.mkdir(parents=True, exist_ok=True)
for name, url in PAGES.items():
    segno.make(url, error="m").save(OUT / f"{name}.svg", scale=8, border=1, dark="#26235C")
    print("wrote", OUT / f"{name}.svg")
