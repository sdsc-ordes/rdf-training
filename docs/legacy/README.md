# Legacy material

Superseded by `src/slides/`. Kept for reference.

## Old decks (2023–24, PowerPoint, not in git)

| Deck | Slides | Topics |
|---|---|---|
| Session 1 – Introduction to RDF | 28 | history, triples, Linked Data principles, RDF vs property graphs, RDF/RDFS/OWL, vocabularies, taxonomy/meronomy, classes/properties/individuals, modelling steps, blank nodes, URI strategy, open vs closed world, SPHN lessons |
| Session 2 – Introduction to SPARQL | 13 | SELECT/WHERE, keywords, friends example, syntax cheat sheet, endpoints, CONSTRUCT/INSERT/DELETE/ASK, GraphDB demo |
| Session 3 – Introduction to SHACL | 23 | SHACL Core/SPARQL, open vs closed world, node/property shapes, adults example, constraint components, engines, validation report |

Errata found when porting are listed in `docs/course-design/curriculum.md`.

## Files

- `triples.txt`: warm-up exercise (sentences → triples)
- `sparql-queries.txt`: playground links and a borehole query
- `bedretto/`: borehole schema, shapes and instances from the Bedretto Underground Lab project

## Known issues in `bedretto/` (left as-is, used as a "spot the bugs" exercise)

- `ui:elevation` shape: malformed `sh:node`, and the `CentiM` unit uses https instead of the http QUDT namespace
- `ui:type`: `sh:datatype xsd:string` plus `sh:class ui:BoreholeType` can never both hold, and `ui:BoreholeType` is undefined
- `simple-taxonomy.ttl`: `rdfs:domain` makes anything with a `ui:name` a `ui:Borehole` under inference
- `instances.ttl`: bare decimals (`30.5`) are not `xsd:double`; coordinates point to San Francisco and Vancouver; "Vailais" should be Valais; boreholes aren't linked to arrays
