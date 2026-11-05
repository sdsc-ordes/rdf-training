from kgcourse import rdf, shacl

PROMPT = (rdf.HANDS_ON / "h2-validate" / "prompt-generate.md").read_text()


def test_prompt_example_is_valid():
    turtle = PROMPT.split("exactly these prefixes:")[1].split("Rules:")[0]
    turtle = turtle.replace("Follow this example exactly:", "")
    g = rdf.context()
    g.parse(data=turtle, format="turtle")
    _, results = shacl.validate(g)
    assert results == set()
