"""Build each deck's bibliography from the sources its slides cite.

Slides cite with one line, labels separated by " · ":
    <p class="fine">Sources: Berners-Lee 2006 · W3C RDF 1.2</p>
Full entries live in slides/references.toml, keyed by label.

    uv run python -m kgcourse.refs   # rewrite slides/references/<deck>.md and urls.json

setup/preparser.ts reads urls.json to link each label on the slides to its source.
"""

from __future__ import annotations

import html
import json
import re
import sys
import tomllib
from pathlib import Path

from . import rdf

SLIDES = rdf.ROOT / "slides"
REFERENCES = SLIDES / "references.toml"
OUT = SLIDES / "references"
URLS = OUT / "urls.json"
PER_SLIDE = 12

CITE = re.compile(r'<p class="fine">Sources?: (.+?)</p>')
SRC = re.compile(r"^src:\s*(\S+)\s*$", re.M)


def references() -> dict[str, dict]:
    return tomllib.loads(REFERENCES.read_text())


def files(deck: Path) -> list[Path]:
    """The deck and every file it imports with `src:`, in order (except the generated bibliography)."""
    out = [deck]
    for m in SRC.finditer(deck.read_text()):
        target = (deck.parent / m.group(1)).resolve()
        if target.parent != OUT:
            out += files(target)
    return out


def cited(path: Path) -> list[str]:
    return [label.strip() for m in CITE.finditer(path.read_text()) for label in m.group(1).split(" · ")]


def render(deck: Path) -> str:
    refs = references()
    labels = {label for f in files(deck) for label in cited(f)}
    if missing := labels - refs.keys():
        raise KeyError(f"{deck.name} cites labels missing from {REFERENCES.name}: {sorted(missing)}")
    labels = sorted(labels, key=str.casefold)
    pages = [labels[i:i + PER_SLIDE] for i in range(0, len(labels), PER_SLIDE)]
    slides = []
    for n, page in enumerate(pages, 1):
        title = "References" if len(pages) == 1 else f"References ({n}/{len(pages)})"
        items = []
        for label in page:
            ref = refs[label]
            url = html.escape(ref["url"])
            items.append(f'  <li><b>{html.escape(label)}</b> · {html.escape(ref["text"])} '
                         f'<a href="{url}">{url.removeprefix("https://").removeprefix("http://")}</a></li>')
        note = "\n\n<!--\nGenerated from slides/references.toml: uv run python -m kgcourse.refs\n-->" if n == 1 else ""
        slides.append(f"---\nclass: references\n---\n\n# {title}\n\n<ul class=\"refs\">\n"
                      + "\n".join(items) + f"\n</ul>{note}\n")
    return "\n".join(slides)


def urls() -> str:
    """Label -> URL, for the source links on the slides."""
    return json.dumps({label: ref["url"] for label, ref in references().items()}, indent=2, ensure_ascii=False) + "\n"


def decks() -> list[Path]:
    return sorted(SLIDES.glob("*.md"))


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for deck in decks():
        target = OUT / deck.name
        target.write_text(render(deck))
        print("wrote", target.relative_to(rdf.ROOT))
    URLS.write_text(urls())
    print("wrote", URLS.relative_to(rdf.ROOT))


if __name__ == "__main__":
    sys.exit(main())
