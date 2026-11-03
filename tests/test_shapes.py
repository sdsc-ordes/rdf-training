import pytest

from kgcourse import rdf, shacl


@pytest.mark.parametrize("inference", ["none", "rdfs"])
def test_golden_data_has_no_results(inference):
    _, results = shacl.validate(rdf.kg(), inference=inference)
    assert results == set()


def test_golden_data_passes_sparql_shapes():
    shapes = rdf.load(rdf.DATA / "shapes" / "recipes.shapes-sparql.ttl")
    conforms, results = shacl.validate(rdf.kg(), shapes=shapes, advanced=True)
    assert conforms, results


def test_usages_match_ingredients():
    ask = """ASK { ?r rec:hasIngredientUsage/rec:food ?f .
                   FILTER NOT EXISTS { ?r rec:hasIngredient ?f } }"""
    assert not rdf.kg().query(ask).askAnswer
