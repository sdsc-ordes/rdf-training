# Knowledge graphs course

Slides, hands-on material and checks for an introductory course on RDF knowledge graphs:
triples, SHACL, SPARQL, LLM-assisted KG building and graph RAG, using a recipe knowledge graph.

Formats: 2 h workshop · 2×3 h afternoons · 6 h day — assembled from the same slide modules.

## Quickstart

```sh
direnv allow         # or: just shell  (nix dev shell: Node 24, uv, just, Chromium)
just setup           # uv sync + npm ci
just dev             # live slides (or: just dev src/slides/full-day.md)
just build           # site + decks → _site/
just export          # PDFs → _site/pdf/
just refs            # after editing src/slides/references.toml or Sources lines
just check           # everything CI runs; `just` lists the recipes
```

## Layout

| Path | Contents |
|---|---|
| `src/slides/` | Slidev decks (one `.md` per format) and `modules/` |
| `src/site/` | VitePress course hub with the hands-on worksheets |
| `src/hands-on/` | exercise files: starter model, buggy data, queries |
| `src/data/` | recipe knowledge graph, vocabulary and shapes |
| `src/kgcourse/` | Python helpers behind the tests and generators |
| `tests/` | checks for data, shapes, queries, slide code and bibliographies |
| `docs/` | `course-design/` (curriculum, agendas, errata), `legacy/` (previous material) |
| `external/sdsc-slides/` | SDSC slide kit (update: `uv run tools/scripts/update-sdsc-kit.py`) |
| `tools/` | `nix/` dev shell, `scripts/` build, export and slide checks |
