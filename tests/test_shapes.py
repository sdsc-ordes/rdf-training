import csv

import pytest

from kgcourse import rdf, shacl

H2 = rdf.ROOT / "hands-on" / "h2-validate"
EXPECTED: dict[str, set[shacl.Result]] = {}
with open(H2 / "expected.tsv", newline="") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        EXPECTED.setdefault(row["file"], set()).add(shacl.Result(
            row["focus"], row["path"] or None, row["shape"], row["component"], row["severity"]))


@pytest.mark.parametrize("inference", ["none", "rdfs"])
def test_golden_data_has_no_results(inference):
    _, results = shacl.validate(rdf.kg(), inference=inference)
    assert results == set()


def test_golden_data_passes_sparql_shapes():
    shapes = rdf.load(rdf.DATA / "shapes" / "recipes.shapes-sparql.ttl")
    conforms, results = shacl.validate(rdf.kg(), shapes=shapes, advanced=True)
    assert conforms, results


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_buggy_file_gives_expected_results(name):
    g = rdf.context()
    g.parse(H2 / "buggy" / name)
    conforms, results = shacl.validate(g)
    assert not conforms
    assert results == EXPECTED[name]


def test_every_buggy_file_has_expectations():
    assert {p.name for p in (H2 / "buggy").glob("*.ttl")} == set(EXPECTED)


def test_usages_match_ingredients():
    ask = """ASK { ?r rec:hasIngredientUsage/rec:food ?f .
                   FILTER NOT EXISTS { ?r rec:hasIngredient ?f } }"""
    assert not rdf.kg().query(ask).askAnswer
