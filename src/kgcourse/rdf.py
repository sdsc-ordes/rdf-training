"""Paths and graph loading for the course data."""

from __future__ import annotations

from pathlib import Path

from rdflib import Graph

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
DATA = SRC / "data"
HANDS_ON = SRC / "hands-on"
SLIDES = SRC / "slides"
SITE = SRC / "site"
PREFIXES = DATA / "prefixes.ttl"

# The ontology in three modules: classes and properties, SKOS value lists, SHACL Core shapes.
ONTOLOGY = DATA / "ontology" / "ontology.ttl"
ENUMERATIONS = DATA / "ontology" / "enumerations.ttl"
SHAPES = DATA / "ontology" / "shapes.ttl"
# Examples beyond SHACL Core (SHACL-SPARQL, SHACL rules).
SHACL_ADVANCED = DATA / "shacl-advanced.ttl"
# Countries, units, foods, people and recipes.
INSTANCES = DATA / "instances.ttl"
# The recipe knowledge graph: ontology, value lists and instance data.
KG = [ONTOLOGY, ENUMERATIONS, INSTANCES]


def load(*paths: Path | str) -> Graph:
    """Parse Turtle files into one graph with the course prefixes bound."""
    g = Graph()
    for prefix, ns in Graph().parse(PREFIXES).namespaces():
        g.bind(prefix, ns, replace=True)
    for path in paths:
        g.parse(path)
    return g


def kg() -> Graph:
    """Load the full recipe knowledge graph."""
    return load(*KG)
