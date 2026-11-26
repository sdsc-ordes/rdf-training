# Knowledge graphs course

Slides, hands-on material and checks for an introductory course on RDF knowledge graphs:
triples, SHACL, SPARQL, LLM-assisted KG building and graph RAG, using a recipe knowledge graph.

Formats: 2 h workshop · 2×3 h afternoons · 6 h day — assembled from the same slide modules.

## Course contents

- **Building blocks:** triples, IRIs, Turtle, Linked Data
- **RDF and property graphs:** the W3C stack (RDFS, OWL, SKOS, SHACL, SPARQL) and when a property graph fits better
- **Modelling:** competency questions, classes and properties, SKOS value lists, reuse of vocabularies
- **Validation:** SHACL shapes and validation reports
- **LLMs build graphs:** drafting, extraction, the generate–validate–repair loop
- **Querying:** SPARQL patterns, property paths, aggregates, federation
- **Architectures** (full day): mapping, storage, serving the graph
- **Graph RAG:** LLM-built graphs, text-to-SPARQL, hybrid vector and graph retrieval
- **Use cases and tools** (full day): industry, health and public-sector examples

Hands-on, in the browser: model the recipe domain · generate, validate and repair data with an LLM · query the recipe graph.

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
| `src/data/` | `ontology/` (classes and properties, SKOS value lists, SHACL shapes), `golden/` instance data, `advanced/` SHACL-SPARQL and rules |
| `src/kgcourse/` | Python helpers behind the tests and generators |
| `tests/` | checks for data, shapes, queries, slide code and bibliographies |
| `src/rete/` | RETE lab: script that builds the `.rete` file and the self-contained query page |
| `docs/` | published RETE lab: `index.html` (exercises), `lab.html`, `data/recipes.rete` |
| `docs/course-design/` | course design brief: modules, minutes per format, errata |
| `external/sdsc-slides/` | SDSC slide kit (update: `uv run tools/scripts/update-sdsc-kit.py`) |
| `tools/` | `nix/` dev shell, `scripts/` build, export and slide checks |
