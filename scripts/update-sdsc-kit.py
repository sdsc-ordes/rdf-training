# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Refresh the vendored SDSC slide kit and re-theme slides/ from its tokens.

    uv run scripts/update-sdsc-kit.py            # download, replace vendor/, install theme
    uv run scripts/update-sdsc-kit.py --no-fetch # only re-install theme from vendor/
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from datetime import date
from pathlib import Path

URL = "https://swissdatasciencecenter.github.io/sdsc-design-guidelines/agent-skills/sdsc-slides.zip"
ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "vendor" / "sdsc-slides"
SLIDES = ROOT / "slides"
LOGOS = ["SDSC_Logo_RGB.png", "SDSC_Logo_White.png", "SDSC_logo_horizontal_rgb_white.png"]


def fetch() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        zpath = Path(tmp) / "kit.zip"
        with urllib.request.urlopen(URL) as resp:
            zpath.write_bytes(resp.read())
            modified = resp.headers.get("Last-Modified", "unknown")
        names = zipfile.ZipFile(zpath).namelist()
        if not all(n.startswith("sdsc-slides/") and ".." not in n for n in names):
            sys.exit("unexpected paths in kit zip")
        provenance = (KIT / "PROVENANCE.md").read_text()
        shutil.rmtree(KIT)
        zipfile.ZipFile(zpath).extractall(KIT.parent)
        sha = hashlib.sha256(zpath.read_bytes()).hexdigest()
    lines = [
        f"- Last-Modified: {modified} · sha256 `{sha}`" if l.startswith("- Last-Modified")
        else f"- Retrieved: {date.today()}" if l.startswith("- Retrieved")
        else l
        for l in provenance.splitlines()
    ]
    (KIT / "PROVENANCE.md").write_text("\n".join(lines) + "\n")


def install() -> None:
    py = sys.executable
    subprocess.run([py, KIT / "scripts/build_slidev_theme.py", "-o", SLIDES / "style.css"], check=True)
    shutil.copy(KIT / "assets/slidev/global-bottom.vue", SLIDES / "global-bottom.vue")
    public = SLIDES / "public"
    (public / "partners").mkdir(parents=True, exist_ok=True)
    for name in LOGOS:
        shutil.copy(KIT / "assets/logos" / name, public / name)
    for logo in (KIT / "assets/logos/partners").glob("*_white.png"):
        shutil.copy(logo, public / "partners" / logo.name)
    subprocess.run([py, KIT / "scripts/verify_tokens.py"], check=True, stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-fetch", action="store_true", help="skip download, re-install from vendor/")
    if not ap.parse_args().no_fetch:
        fetch()
    install()
    print("SDSC theme installed in slides/")
