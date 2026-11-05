import pytest
from rdflib import Graph
from rdflib.plugins.parsers.notation3 import BadSyntax

from kgcourse.rdf import DATA, HANDS_ON, ROOT

TTL = sorted(p for d in (DATA, HANDS_ON, ROOT / "docs" / "legacy") for p in d.rglob("*.ttl"))


@pytest.mark.parametrize("path", TTL, ids=lambda p: str(p.relative_to(ROOT)))
def test_turtle_parses(path):
    if path.name.startswith("llm-raw"):  # deliberately broken LLM output
        with pytest.raises(BadSyntax):
            Graph().parse(path)
    else:
        Graph().parse(path)
