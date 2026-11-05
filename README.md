# Knowledge graphs course

Slides, hands-on material and checks for an introductory course on RDF knowledge graphs:
triples, SHACL, SPARQL, LLM-assisted KG building and graph RAG, using a recipe knowledge graph.

Formats: 2 h workshop · 2×3 h afternoons · 6 h day — assembled from the same slide modules.

## Quickstart

```sh
nix develop          # or: direnv allow  (Node 24, uv, Chromium)
npm ci
npm run dev -- slides/workshop-2h.md   # live slides (or slides/full-day.md)
npm run build                          # site + decks → _site/
npm run export                         # PDFs → _site/pdf/
uv run python -m kgcourse.refs         # after editing slides/references.toml or Sources lines
```

## Layout

| Path | Contents |
|---|---|
| `slides/` | Slidev decks (one `.md` per format) and `modules/` |
| `site/` | VitePress course hub |
| `vendor/sdsc-slides/` | SDSC slide kit (theme: `uv run scripts/update-sdsc-kit.py`) |
| `course-design/` | curriculum, agendas, errata |
| `legacy/` | previous material |
