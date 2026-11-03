"""Run the hands-on SPARQL queries against the recipe KG; snapshot results as TSV.

    uv run python -m kgcourse.queries --update   # rewrite expected/*.tsv
"""

from __future__ import annotations

import sys
from functools import cache
from pathlib import Path

from pyoxigraph import QueryBoolean, QueryResultsFormat, RdfFormat, Store

from . import rdf

QUERIES = rdf.ROOT / "hands-on" / "h3-query" / "queries"
EXPECTED = rdf.ROOT / "hands-on" / "h3-query" / "expected"


@cache
def store() -> Store:
    s = Store()
    for path in (*rdf.CONTEXT, rdf.RECIPES):
        s.load(path=path, format=RdfFormat.TURTLE)
    return s


def is_online(query: Path) -> bool:
    return "# online: true" in query.read_text()


def run(query: Path) -> str:
    result = store().query(query.read_text())
    if isinstance(result, QueryBoolean):
        return f"{bool(result)}\n".lower()
    return result.serialize(format=QueryResultsFormat.TSV).decode()


def expected_path(query: Path) -> Path:
    return EXPECTED / f"{query.stem}.tsv"


def main() -> None:
    if "--update" not in sys.argv:
        sys.exit(__doc__)
    EXPECTED.mkdir(exist_ok=True)
    for query in sorted(QUERIES.glob("*.rq")):
        if not is_online(query):
            expected_path(query).write_text(run(query))
            print("wrote", expected_path(query).relative_to(rdf.ROOT))


if __name__ == "__main__":
    main()
