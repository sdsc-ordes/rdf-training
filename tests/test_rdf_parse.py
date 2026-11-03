import pytest
from rdflib import Graph

from kgcourse.rdf import ROOT

TTL = sorted(p for d in ("data", "hands-on", "legacy") for p in (ROOT / d).rglob("*.ttl"))


@pytest.mark.parametrize("path", TTL, ids=lambda p: str(p.relative_to(ROOT)))
def test_turtle_parses(path):
    if path.name.startswith("llm-raw"):  # deliberately broken LLM output
        with pytest.raises(Exception):
            Graph().parse(path)
    else:
        Graph().parse(path)
