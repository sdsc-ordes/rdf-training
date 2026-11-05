import csv

import pytest
from pyshacl.entrypoints import meta_validate
from rdflib import RDF, Namespace

from kgcourse import rdf, shacl

H2 = rdf.HANDS_ON / "h2-validate"
EXPECTED: dict[str, set[shacl.Result]] = {}
with open(H2 / "expected.tsv", newline="") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        EXPECTED.setdefault(row["file"], set()).add(
            shacl.Result(row["focus"], row["path"] or None, row["shape"], row["component"], row["severity"])
        )


@pytest.mark.parametrize("inference", ["none", "rdfs"])
def test_golden_data_has_no_results(inference):
    _, results = shacl.validate(rdf.kg(), inference=inference)
    assert results == set()


def test_golden_data_passes_sparql_shapes():
    shapes = rdf.load(rdf.DATA / "shapes" / "recipes.shapes-sparql.ttl")
    conforms, results = shacl.validate(rdf.kg(), shapes=shapes, advanced=True)
    assert conforms, results


def test_cheese_dish_rule_matches_query():
    rec = Namespace("https://sdsc-ordes.github.io/rdf-training/vocab/recipes#")
    out = shacl.infer(rdf.kg(), rdf.load(rdf.DATA / "shapes" / "recipes.rules.ttl"))
    query = "SELECT ?r WHERE { ?r a schema:Recipe ; rec:hasIngredient/a/rdfs:subClassOf* rec:Cheese }"
    expected = {row.r for row in rdf.kg().query(query)}
    assert len(expected) == 2 and set(out.subjects(RDF.type, rec.CheeseDish)) == expected


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


@pytest.mark.parametrize("path", sorted((rdf.DATA / "shapes").glob("*.ttl")), ids=lambda p: p.name)
def test_shapes_pass_shacl_shacl(path):
    conforms, _, text = meta_validate(rdf.load(path))
    assert conforms, text
