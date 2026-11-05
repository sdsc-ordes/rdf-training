"""Code shown on slides and worksheets parses; deck imports, timings and bibliographies add up."""

import re
from pathlib import Path

import pytest
from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

from kgcourse import rdf, refs

SLIDES = rdf.ROOT / "slides"
SITE = rdf.ROOT / "site"
DOCS = sorted([*SLIDES.rglob("*.md"), *SITE.glob("**/*.md")])
PREFIXES = rdf.PREFIXES.read_text()
NAMESPACES = dict(Graph().parse(rdf.PREFIXES).namespaces())
AGENDA_MINUTES = {"workshop-2h.md": 120, "full-day.md": 360}


def code_blocks(path: Path):
    """Yield (lang, code, line) for ```turtle / ```sparql fences, also nested ones."""
    lines = path.read_text().splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^\s*(`{3,})(\w+)", lines[i])
        if m and m.group(2) in ("turtle", "sparql"):
            fence, start = m.group(1), i
            skip = i > 0 and "check: skip" in lines[i - 1]
            i += 1
            body = []
            while lines[i].strip() != fence:
                body.append(lines[i])
                i += 1
            if not skip:
                yield m.group(2), "\n".join(body), start + 1
        i += 1


BLOCKS = [(p, *b) for p in DOCS for b in code_blocks(p)]


@pytest.mark.parametrize(
    "path,lang,code,line", BLOCKS, ids=[f"{p.relative_to(rdf.ROOT)}:{line}" for p, _, _, line in BLOCKS]
)
def test_code_block_parses(path, lang, code, line):
    if lang == "turtle":
        Graph().parse(data=PREFIXES + code, format="turtle")
    else:
        prepareQuery(code, initNs=NAMESPACES)


@pytest.mark.parametrize("path", DOCS, ids=lambda p: str(p.relative_to(rdf.ROOT)))
def test_fences_and_includes(path):
    text = path.read_text()
    assert not re.search(r"^\s*`{3,}(ttl|rq|shacl)\b", text, re.MULTILINE), "use ```turtle or ```sparql"
    root = SLIDES if SLIDES in path.parents else SITE
    for m in re.finditer(r"^<<< @/(\S+?)(?:#([\w-]+))?(?=[\s{]|$)(.*)$", text, re.MULTILINE):
        target = root / m.group(1)
        assert target.exists(), target
        if m.group(2):
            assert f"#region {m.group(2)}" in target.read_text(), f"region {m.group(2)} in {target}"
        if target.suffix in (".ttl", ".rq"):
            assert re.search(r"\b(turtle|sparql)\b", m.group(3)), "name the language for .ttl/.rq includes"


def slides(path: Path) -> list[dict]:
    """Split a Slidev file into slides; return each slide's top-level frontmatter."""
    blocks, block, fence = [], [], None
    for line in path.read_text().splitlines():
        m = re.match(r"^\s*(`{3,})", line)
        if fence is None and m:
            fence = m.group(1)
        elif fence and line.strip() == fence:
            fence = None
        elif fence is None and line.strip() == "---":
            blocks.append(block)
            block = []
            continue
        block.append(line)
    blocks.append(block)

    def frontmatter(lines):
        text = [l for l in lines if l.strip()]
        if text and all(re.match(r"^([A-Za-z][\w-]*:(\s|$)|\s+\S)", l) for l in text):
            return dict(re.match(r"^([\w-]+):\s*(.*)$", l).groups() for l in text if not l[0].isspace())

    result, pending = [], None
    for b in blocks:
        fm = frontmatter(b)
        if fm is not None and pending is None:
            pending = fm
        elif any(l.strip() for l in b) or pending is not None:
            result.append(pending or {})
            pending = None
    if pending is not None:
        result.append(pending)
    return result


def expand(path: Path) -> list[tuple[Path, dict]]:
    out = []
    for fm in slides(path):
        if "src" in fm:
            assert set(fm) <= {"src", "hide"}, f"import block in {path} may only set src/hide"
            target = (path.parent / fm["src"]).resolve()
            assert target.exists(), target
            out += expand(target)
        else:
            out.append((path, fm))
    return out


DECKS = sorted(SLIDES.glob("*.md"))
MODULES = sorted(p for p in (SLIDES / "modules").iterdir() if p.is_dir())


@pytest.mark.parametrize("deck", DECKS, ids=lambda p: p.name)
def test_deck_expands(deck):
    assert expand(deck)


@pytest.mark.parametrize("deck", [d for d in DECKS if d.name in AGENDA_MINUTES], ids=lambda p: p.name)
def test_deck_minutes_match_agenda(deck):
    total = sum(int(fm.get("minutes", 0)) for _, fm in expand(deck))
    assert total == AGENDA_MINUTES[deck.name]


@pytest.mark.parametrize("module", MODULES, ids=lambda p: p.name)
def test_module_parts_are_all_used(module):
    core = {p for p, _ in expand(module / "core.md")} if (module / "core.md").exists() else set()
    full = {p for p, _ in expand(module / "full.md")}
    if not module.name.startswith("h"):  # hands-on modules have a short 2 h brief of their own
        assert core <= full
    assert {p.resolve() for p in (module / "parts").glob("*.md")} == core | full


def test_workshop_uses_core_modules_only():
    for fm in slides(SLIDES / "workshop-2h.md"):
        if fm.get("src", "").startswith("./modules/"):
            assert fm["src"].endswith("/core.md"), fm["src"]


@pytest.mark.parametrize("deck", DECKS, ids=lambda p: p.name)
def test_bibliography_is_current(deck):
    assert (refs.OUT / deck.name).read_text() == refs.render(deck), "run: uv run python -m kgcourse.refs"


def test_source_links_are_current():
    assert refs.URLS.read_text() == refs.urls(), "run: uv run python -m kgcourse.refs"


def test_every_reference_is_cited():
    labels = {label for path in SLIDES.rglob("*.md") for label in refs.cited(path)}
    assert set(refs.references()) <= labels


def test_slide_prefixes_match_data_prefixes():
    ts = (SLIDES / "setup" / "prefixes.ts").read_text()
    assert dict(re.findall(r"^\s*(\w+): '([^']+)',", ts, re.MULTILINE)) == dict(
        re.findall(r"@prefix (\w+):\s*<([^>]+)>", PREFIXES)
    )
