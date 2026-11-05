"""SHACL validation with results reduced to comparable tuples."""

from __future__ import annotations

from typing import NamedTuple

from pyshacl import shacl_rules
from pyshacl import validate as pyshacl_validate
from rdflib import BNode, Graph
from rdflib.namespace import SH

from . import rdf


class Result(NamedTuple):
    focus: str
    path: str | None
    shape: str
    component: str
    severity: str


def _name(g: Graph, node) -> str | None:
    if node is None:
        return None
    if isinstance(node, BNode):
        return "_"
    return node.n3(g.namespace_manager)


def validate(data: Graph, shapes: Graph | None = None, inference: str = "none",
             advanced: bool = False) -> tuple[bool, set[Result]]:
    """Validate `data`; conforms means no sh:Violation (warnings and info are allowed)."""
    shapes = shapes if shapes is not None else rdf.load(rdf.SHAPES)
    _, report, _ = pyshacl_validate(data, shacl_graph=shapes, inference=inference,
                                    advanced=advanced)
    report.namespace_manager = data.namespace_manager
    results = {
        Result(
            focus=_name(report, report.value(r, SH.focusNode)),
            path=_name(report, report.value(r, SH.resultPath)),
            shape=_name(report, report.value(r, SH.sourceShape)),
            component=_name(report, report.value(r, SH.sourceConstraintComponent)),
            severity=_name(report, report.value(r, SH.resultSeverity)),
        )
        for r in report.objects(None, SH.result)  # top-level results, not sh:detail
    }
    return not any(r.severity == "sh:Violation" for r in results), results


def infer(data: Graph, rules: Graph) -> Graph:
    """Apply the SHACL rules in `rules` to `data` until nothing new is inferred; return the result."""
    return shacl_rules(data, shacl_graph=rules, advanced=True, iterate_rules=True)
