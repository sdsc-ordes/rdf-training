import pytest

from kgcourse import queries

ALL = sorted(queries.QUERIES.glob("*.rq"))
OFFLINE = [q for q in ALL if not queries.is_online(q)]


@pytest.mark.parametrize("query", OFFLINE, ids=lambda q: q.stem)
def test_query_matches_snapshot(query):
    assert queries.run(query) == queries.expected_path(query).read_text()


def test_every_offline_query_has_a_snapshot():
    assert {q.stem for q in OFFLINE} == {p.stem for p in queries.EXPECTED.glob("*.tsv")}
