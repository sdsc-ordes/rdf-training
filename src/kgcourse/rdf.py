"""Paths and graph loading for the course data."""

from __future__ import annotations

from pathlib import Path

from rdflib import Graph

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
PREFIXES = DATA / "prefixes.ttl"
SHAPES = DATA / "shapes" / "recipes.shapes.ttl"

# What attendees paste next to their own recipes: vocabulary, concepts, foods, people.
CONTEXT = [
    *sorted((DATA / "vocab").glob("*.ttl")),
    *sorted((DATA / "concepts").glob("*.ttl")),
    DATA / "golden" / "foods.ttl",
    DATA / "golden" / "people.ttl",
]
RECIPES = DATA / "golden" / "recipes.ttl"


def load(*paths: Path | str) -> Graph:
    """Parse Turtle files into one graph with the course prefixes bound."""
    g = Graph()
    for prefix, ns in Graph().parse(PREFIXES).namespaces():
        g.bind(prefix, ns, replace=True)
    for path in paths:
        g.parse(path)
    return g


def context() -> Graph:
    """Load the vocabulary and reference data the recipes depend on."""
    return load(*CONTEXT)


def kg() -> Graph:
    """Load the full recipe knowledge graph."""
    return load(*CONTEXT, RECIPES)
