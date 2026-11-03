# /// script
# requires-python = ">=3.11"
# dependencies = ["segno"]
# ///
"""Write QR codes for the course site pages to slides/public/qr/."""

from pathlib import Path

import segno

SITE = "https://sdsc-ordes.github.io/rdf-training/"
PAGES = {
    "site": "",
    "h1": "hands-on/h1-model.html",
    "h2": "hands-on/h2-validate.html",
    "h3": "hands-on/h3-query.html",
}
OUT = Path(__file__).resolve().parent.parent / "slides" / "public" / "qr"

OUT.mkdir(parents=True, exist_ok=True)
for name, page in PAGES.items():
    segno.make(SITE + page, error="m").save(OUT / f"{name}.svg", scale=8, border=1, dark="#26235C")
    print("wrote", OUT / f"{name}.svg")
