import re

from rdflib import RDF, Graph, Namespace

from kgcourse import rdf, shacl

PROMPT = (rdf.HANDS_ON / "h2-validate" / "prompt-generate.md").read_text()
EXAMPLE = PROMPT.split("exactly these prefixes:")[1].split("Rules:")[0].replace("Follow this example exactly:", "")
SCHEMA = Namespace("https://schema.org/")


def test_prompt_example_is_valid():
    g = rdf.kg()
    g.parse(data=EXAMPLE, format="turtle")
    _, results = shacl.validate(g)
    assert results == set()


def test_prompt_example_is_not_in_the_graph():
    # An LLM copies the example; if its IRI were taken, its triples would merge into that recipe.
    example = set(Graph().parse(data=EXAMPLE, format="turtle").subjects(RDF.type, SCHEMA.Recipe))
    assert example and not example & set(rdf.kg().subjects(RDF.type, SCHEMA.Recipe))


def test_prompt_placeholders_are_filled_by_the_site():
    loader = (rdf.SITE / "hands-on" / "h2.data.ts").read_text()
    for name in set(re.findall(r"\{\{(\w+)\}\}", PROMPT)):
        assert f".replace('{{{{{name}}}}}'" in loader, name
