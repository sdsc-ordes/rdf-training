# Course design brief

Audience: mixed (incl. non-coders). Domain: food/recipes. Hands-on: browser first, notebooks optional.
Formats: 6 h day, 2×3 h afternoons, 2 h workshop — all built from the same modules.

## Principles

- One running example (the recipe KG); each hands-on starts from a known-good checkpoint.
- Every task has a *minimum* step (copy/edit) and a *stretch* step (from scratch / Python).
- Predict, then reveal: audience guesses before every query, validation or demo run.
- Slides are `core` (also in 2 h) or `ext`; one idea per slide, ≤5 bullets, one takeaway per module.

## Running example

- Classes: `schema:Recipe`, `rec:Food` + taxonomy (`rec:HardCheese ⊑ rec:Cheese ⊑ rec:DairyProduct ⊑ rec:AnimalProduct`, `rec:MeatOrFish`)
- Properties: `rec:hasIngredient`, `rec:containsIngredient`, `rec:hasAllergen`, `rec:grownIn`, `rec:cuisine`, `schema:totalTime`, `schema:suitableForDiet`, `skos:exactMatch`
- SKOS schemes: 14 EU allergens, cuisines, courses
- Traps: Worcestershire→anchovy, soy sauce→wheat→gluten, fish sauce, pesto→Parmesan→rennet, Fuji apples grown in Spain/France
- Competency questions:
  1. Recipes under 30 minutes?
  2. Recipes for a vegetarian, gluten-free guest?
  3. Recipes using ingredients grown in Spain?
  4. Which ingredients hide allergens?
  5. Which cuisine has the most vegan recipes?

## Modules

Minutes = core / full.

### M01 KG building blocks (15 / 20)
- Core: what a KG is; the triple; IRIs vs literals; prefixes; warm-up (apples sentences → triples); Turtle reveal; "where KGs run today" teaser
- Ext: history (corrected); Linked Data principles + live Wikidata dereference; blank nodes; datatypes and language tags; merging graphs
- Interaction: pairs write triples on sticky notes; "same sentence, different triples?"
- Takeaway: *A KG is a set of simple statements with global identifiers — that's what makes data mergeable.*

### M02 W3C stack vs property graphs (10 / 25)
- Core: one redrawn stack (model / syntax / semantics / validation / query); same fact in Turtle and Cypher; 5-row trade-off table; scenario vote
- Ext: timeline (RDF 1999 → 1.1 2014 → 1.2 CR 2026; RDFS 2004; OWL 2004/2009; SPARQL 2008/2013/1.2 WD; SKOS 2009; SHACL 2017/1.2 WD; JSON-LD 1.1 2020); RDF 1.2 triple terms + annotation syntax; named graphs; RDFS entailment; GQL (ISO/IEC 39075:2024), Cypher 25; ecosystem (Kuzu archived 2025, Memgraph, FalkorDB, Spanner Graph); RDF↔LPG bridges
- Example: "Alice rated Rösti 5 stars (source, confidence)" as Cypher edge property, RDF 1.2 annotation, RDF 1.1 n-ary
- Vote: supplier allergen merge → RDF; in-app recommendations → LPG; open nutrition data → RDF/JSON-LD
- Takeaway: *RDF is built for shared meaning across organisations, property graphs for traversal inside one app — the gap is narrowing.*

### M03 Modelling and reuse (5 / 25)
- Core: CQs → nouns/verbs → classes/properties; class/property/individual/literal; reuse first (schema.org, Wikidata, QUDT, SKOS); schema vs instance layer; steps 0–4 (step 0: write CQs)
- Ext: taxonomy vs meronomy; enumerations (RestrictedDiet, SKOS, `sh:in`); strings → things (`schema:recipeIngredient` is text); n-ary `rec:IngredientUsage`; blank vs named nodes; IRI strategy; language tags; domain/range infer, they don't constrain; synonyms (rocket/arugula); class or individual (Fuji); when OWL pays off
- Interaction: sort Fuji, apple, vegan, "30 minutes", Spain, contains, Rösti, gluten, Robin, grams into class/property/individual/literal
- Takeaway: *Start from your questions, reuse before you invent, turn queryable strings into things.*

### H1 Model the recipe domain (15 / 35)
- Core: pairs add 2 classes + 3 properties to a starter canvas for CQ2/CQ3; reveal reference model
- Full: underline nouns/verbs (5) → group canvas + schema.org lookup (15) → optional LLM class table, compare (bridge to M05) → reveal + discuss (10)
- Checkpoint: everyone continues with the reference vocabulary + shapes
- Takeaway: *There's no single right model, but there is one that answers your questions.*

### M04 Validation with SHACL (10 / 25)
- Core: why validate; OWA vs CWA (once); 5-line RecipeShape; report anatomy (focusNode, resultPath, value, message); spot-the-violation quiz
- Ext: node vs property shapes, targets; key constraint components + `sh:in`, `sh:node`, `sh:closed`; exact datatype matching (`450` ≠ `xsd:decimal`); severities + `sh:message` written for humans and LLMs; vegan rule (SHACL Core and SHACL-SPARQL); SHACL in CI; engines; SHACL 1.2 WDs; shapes as LLM schema docs; stretch: Bedretto bugs
- Micro-exercise: predict → validate in Zazuko → fix one → revalidate
- Takeaway: *Ontologies say what may be true; shapes say what your data must contain.*

### M05 LLMs for KG design and population (5 / 25)
- Core: loop diagram, top failure modes, H2 prompt walkthrough
- Interaction: vote which of 6 LLM triples are wrong
- Takeaway: *LLMs draft, SHACL checks, humans decide.*

| # | Layout | Slide |
|---|---|---|
| 1 | section | LLMs for KG design and population |
| 2 | features (4) | Where LLMs help: design, population, linking, quality |
| 3 | content | Drafting from CQs: role, CQs, reuse list, table first then Turtle, one CQ at a time |
| 4 | two-cols | LLM draft vs H1 reference: domain/range misuse, duplicate classes, no n-ary, no language tags |
| 5 | quote | Evidence: Lippolis et al. ESWC 2025; OntoChat; LLMs4KGOE 2026 |
| 6 | two-cols | Extraction (faithful, cite the span) vs synthetic generation (plausible, label it synthetic) |
| 7 | code | JSON Schema/LinkML → LLM JSON → JSON-LD context → RDF (SPIRES/OntoGPT, shown on recipes) |
| 8 (C) | content + takeaway | Generate → parse → SHACL → repair (N=3) → human queue |
| 9 | code | SHACL report fed back; `sh:message` an LLM can act on |
| 10 | two-cols | Wikidata linking: candidates → LLM picks → confirm; never trust Q-ids from memory (Fuji, rocket) |
| 11 (C) | features (4) | Identifier failures: invented terms, undeclared prefixes, http/https, IRI drift (`food:tomato`/`food:Tomatoes`) |
| 12 | features (4) | Literal/fact failures: decimal/double/integer, "30 min", missing language tags, plausible-but-wrong (Bedretto coordinates) |
| 13 | content | Review + provenance: named graph per batch, `prov:wasGeneratedBy`, privacy |
| 14 | content | Tools: any chat LLM, OntoGPT, LinkML, OpenRefine, pySHACL, Zazuko; Text2KGBench |

### H2 Generate → validate → repair → populate (20 / 40)
1. Paste prompt pack (vocabulary + shapes + allowed food IRIs + assigned cuisine) into own LLM → 5 recipes in Turtle (8)
2. Validate in Zazuko (8)
3. Paste report back, "fix only the violations", max 3 rounds; log error types on shared board (10)
4. Submit to shared pad; instructor merges the class graph; IRI clashes become visible (6)
5. Debrief: failure-mode taxonomy, "would you load this?" (8)
- Core: steps 1–3, one repair round, 5 min debrief. Fallback: buggy files for anyone without an LLM.
- Takeaway: *Validation turns plausible LLM output into loadable data.*

### M06 SPARQL (5 / 20)
- Core: a query is a Turtle-like pattern with variables; SELECT anatomy on CQ1; where to run it
- Ext: fixed Alice/Bob/Charlie (predict the rows); syntax cheat sheet; OPTIONAL, FILTER/NOT EXISTS, property paths, GROUP BY/HAVING, VALUES/BIND/COALESCE; SERVICE to Wikidata via QLever; CONSTRUCT/ASK/DESCRIBE/Update; endpoints; SPARQL 1.2 (Working Draft); check LLM-written queries
- Takeaway: *A query is a graph pattern with holes; you get every way it fits the data.*

### H3 Ask the recipe graph (10 / 30)
- L1 list recipes · L2 under 30 min sorted (CQ1) · L3 ingredients grown in Spain (CQ3) · L4 vegetarian + gluten-free via NOT EXISTS + path (CQ2, exposes Worcestershire/soy) · L5 vegan count per cuisine (CQ5) · L6 bonus federation
- Core: run L2 + L4, change one filter
- Takeaway: *Model for your questions and the queries almost write themselves.*

### M07 Architectures (0 / 20)
- One diagram built in 5 steps: sources → mapping/ETL (RML/YARRRML, R2RML/Ontop virtual KGs, JSON-LD, LLM extraction) → quality gate (SHACL in CI, named graphs, PROV-O) → storage (GraphDB 11, Fuseki, Oxigraph, QLever, Virtuoso, Stardog, Neptune, RDFox) → access (SPARQL, federation, REST/GraphQL, MCP) → apps (search, dashboards, graph RAG, agents)
- Table: materialised vs virtual vs federated (freshness, speed, control, complexity)
- Example: canteen allergen KG from supplier CSV, recipe-site JSON-LD, PDFs, Wikidata
- Interaction: "view source" on a recipe site to find `"@type": "Recipe"`; pairs place 8 component cards on layers
- Takeaway: *A KG is a pipeline, not a database; graph RAG is one more consumer.*

### M08 Use cases and tooling (0 / 15)
- 8 case cards, dot-vote, zoom into top 2; one-page tooling map by stage (model, map, validate, store, query, LLM), marked no-code or code
- Takeaway: *Successful KGs reuse the same building blocks; governance and scale are what differ.*

Card template: problem · what the KG holds · stack · access · what worked / trade-off · 2026 LLM angle · try-it link · module link

1. **SIB (UniProt, Bgee, Rhea) + SPHN**: federation works when vocabularies are shared; SPHN versioned schema + SHACL QA; federated text-to-SPARQL (chat.expasy.org)
2. **Wikidata**: qualifiers vs RDF 1.2; query service moving Blazegraph → QLever; LLMs invent Q-ids
3. **LINDAS + DCAT-AP CH**: cubes → visualize.admin.ch; governance harder than tech; LINDAS MCP
4. **Europeana / Linked Art**: expressive ontologies need usable profiles; multilingual labels
5. **Brick / 223P / RealEstateCore**: shared building ontology + SHACL; property paths ("sensors downstream of AHU-1")
6. **FIBO + GLEIF LEI**: heavyweight OWL, teams adopt slices; ontology as grounding glossary
7. **schema.org Recipe**: most-deployed RDF, JSON-LD in pages; loose semantics; read by AI search
8. **Bedretto / SDSC**: start small; units and coordinates are where errors hide

### M09 Graph RAG (15 / 35)
- Storyline: fluent ≠ grounded → vector RAG retrieves similar text → some questions need joins, counts, constraints, global views, fact checks → three graph families → demo → evidence and costs → decision guide
- Takeaway: *Use the graph for what text retrieval can't do — joins, counts, constraints, fact-checks — and vectors for the rest.*

| # | Layout | Slide |
|---|---|---|
| 1 | section | Graph RAG: grounding LLMs in KGs |
| 2 (C) | content + takeaway | Hook: "Can I serve this Caesar salad to my vegetarian friend?" — LLM says yes |
| 3 | content | Why ground: hallucination, stale/private knowledge, no provenance, can't count |
| 4 | two-cols | Vector RAG in one picture / what it's good at |
| 5 (C) | features (4) | Where vector RAG breaks: multi-hop, aggregation, hard constraints, global questions |
| 6 (C) | features (3) | A: LLM-built graph · B: curated KG as source of truth · C: hybrid |
| 7 | content | Family A: Microsoft GraphRAG (communities, local/global search), LightRAG, HippoRAG 2 |
| 8 | code | Family B: text-to-SPARQL (schema card from SHACL + prefixes + examples → query → run → cite IRIs; repair on error) |
| 9 | two-cols | KG as agent tool: MCP SPARQL servers (GraphDB 11, LINDAS MCP, SHACL-described servers) / shapes as tool docs |
| 10 | content | Demo setup: same LLM, same corpus, fair baseline |
| 11 (C) | two-cols | Q1 control + Q2 multi-hop: vector vs KG answer with "why excluded" path |
| 12 | key numbers | Q3 aggregation: true count vs vector count, tokens |
| 13 | two-cols | Q4 global themes: vector vs community summaries |
| 14 (C) | code | Q5 fact-check: claim → ASK → supported / contradicted / unknown |
| 15 | quote | Evidence: Han et al. 2502.11371; GraphRAG-Bench (ICLR 2026) |
| 16 | key numbers | Cost: indexing tokens, latency, LLM calls per answer |
| 17 | content | Limits: indexing cost, garbage in, fragile text-to-SPARQL, latency, open-world "unknown", prompt injection |
| 18 (C) | content + takeaway | Decision guide |

Demo questions (same corpus, same LLM, cached):
- **Q1 control**: "How long should the focaccia dough rise?" — both right, vector cheaper
- **Q2**: "Recipes under 30 min for a vegetarian, gluten-free guest?" — vector misses Worcestershire/soy; KG uses NOT EXISTS + `rec:hasIngredient/rec:containsIngredient*`
- **Q3**: "How many recipes use an ingredient grown in Spain, and which cuisine most?" — vector undercounts; GROUP BY exact
- **Q4**: "Main themes of this cookbook?" — community summaries win (optional, precomputed)
- **Q5**: "Pad Thai is vegan, gluten-free and Vietnamese" — claims → ASK: contradicted ×3; one "unknown" (open world)

Decision guide: single-hop doc lookups → vector RAG · joins/counts/constraints → curated KG + text-to-SPARQL/MCP · corpus-wide themes → GraphRAG/LightRAG · auditable answers → KG + provenance · in practice: hybrid.

## Errata to fix when porting

**Deck 1**
- History: RDF first draft 1997, roadmap 1998, SciAm 2001, Linked Data note 2006
- LD principles: say IRIs/HTTPS; credit TBL 2006
- LPG slide: "labels" are node/relationship types, not edge properties; schema claim is one-sided; reification point outdated by RDF 1.2
- Stack slide: only RDF is mandatory, not SPARQL; redraw the image
- "Big trois": RDF Rec 1999 (not 1996); RDFS Rec 2004; "Web Ontology Language"; RDFS is more than taxonomy
- Vocabularies: separate modelling languages (RDFS, OWL, SHACL, XSD) from domain vocabularies; SKOS maps concept schemes
- Enumeration example (Lausanne) isn't one; "it's" → "its"
- Thesaurus ≠ glossary; remove personal birth data
- `qudt:Meter` → `unit:M` with `unit:` = `http://qudt.org/vocab/unit/`
- OWA/CWA: not "informal/formal"; unique-name assumption is separate from CWA; caption doesn't fit the example; implicit class targets need `rdfs:Class` or `sh:targetClass`; mixed `:`/`ex:`
- Put the Polikoff quote attribution on the slide
- GraphDB 10 link → GraphDB 11 (Graphwise)
- Remove tracking URL and colleague in-jokes

**Deck 2**
- Friends example: add DISTINCT (Bob appears twice); add `PREFIX rdf` or use `a`
- Friend-age query filters the person, not the friend; ask "older than 30", answer Bob
- SPARQL queries aren't valid Turtle (only triple patterns borrow the syntax)
- `SELECT (?x)` is expression syntax; FROM is optional
- "Federative" → federated; results can be graphs or booleans; GraphDB → Graphwise; rdfLib → RDFLib

**Deck 3**
- SHACL AF note → SHACL 1.2 Working Drafts (Rules, Node Expressions)
- Property shapes constrain values reached via paths, not "edges"
- Adults example: adult is ≥18; `ex:person1` ≠ `ex:Person1`; Alice (15) and Bob (17) violate; SHACL reports, it doesn't filter
- Engines: TopBraid Composer discontinued (verify); pySHACL is its own package; org is `sdsc-ordes`; add Zazuko; drop shacl.org
- `sh:resultMessage` is optional unless `sh:message` is set; severity defaults to Violation; prefixes are case-sensitive
- `sh:TripleRule` casing; pin the Imaging Plaza link to a commit; recreate the Figma diagram in the repo

**Repo data**: see `legacy/README.md`; warm-up date becomes `"2025-03-12"^^xsd:date`.

## Risks

| Risk | Mitigation |
|---|---|
| Unequal LLM access | Mixed pairs; prompt pack < 2k tokens, tested on common assistants; buggy fallback files; toy data only |
| Tool outage | Primary + fallback per step; one worksheet page with all links; offline Oxigraph |
| Demo failure | Record/replay LLM cache; local embeddings; static export; screenshots for federation |
| Time overrun | Timers; minimum vs stretch steps; checkpoints; breaks after H3 |
| Pace gap | Fill-in vs from-scratch tasks; notebooks; glossary; parking lot |
| Standards drift | "Status as of" box; pre-course checklist |

Cut order when late (ext only): M08 → M07 detail → M02 timeline/OWL/GQL → M03 deep-dives → H3 L5/L6 → M09 Q4 + evidence/cost.
Never cut: H2 validation loop, M09 Q2/Q5, H1 core.

## Re-verify before each delivery

RDF 1.2 (CR) / SPARQL 1.2 (WD) / SHACL 1.2 (WD) status · WDQS → QLever cutover · TopBraid Composer status · GraphDB 11 MCP · UniProt/Wikidata sizes · exact titles of 2026 agentic GraphRAG survey, SEMANTiCS 2026 SPARQL-MCP, WU "Agentic SPARQL"

## Sources

- Lewis et al. 2020, RAG — arXiv 2005.11401
- Edge et al. 2024, GraphRAG — arXiv 2404.16130; LazyGraphRAG (Microsoft Research blog, 2024)
- Guo et al. 2024, LightRAG — arXiv 2410.05779
- Gutiérrez et al., HippoRAG — arXiv 2405.14831; HippoRAG 2 — arXiv 2502.14802
- Peng et al. 2024, Graph RAG survey — arXiv 2408.08921
- Han et al., RAG vs GraphRAG — arXiv 2502.11371
- Xiang et al., GraphRAG-Bench — arXiv 2506.05690 (ICLR 2026)
- Pan et al. 2024, Unifying LLMs and KGs — arXiv 2306.08302
- Sun et al., Think-on-Graph — arXiv 2307.07697
- Emonet et al., SIB federated text-to-SPARQL — arXiv 2410.06062
- Lippolis et al., Ontology generation with LLMs — arXiv 2503.05388
- Caufield et al., SPIRES / OntoGPT
- W3C: RDF 1.2 Concepts CR (2026-04-07); SHACL 1.2 WDs (2026)
- ISO/IEC 39075:2024 (GQL)
