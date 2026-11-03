---
minutes: 4
---

# A knowledge graph is a pipeline

```mermaid {scale: 0.66}
graph LR
  S[Sources<br/>CSV · databases<br/>JSON · PDFs] --> M[Map and extract<br/>RML · Ontop<br/>JSON-LD · LLMs]
  M --> Q{Quality gate<br/>SHACL}
  Q --> T[(Triplestore)]
  T --> A[Access<br/>SPARQL · APIs · MCP]
  A --> U[Apps<br/>search · dashboards<br/>graph RAG]
  W[(Wikidata,<br/>other endpoints)] -. federation .-> A
```

<div class="sdsc-takeaway">Map, validate, store, serve. Graph RAG is just one more consumer.</div>

<!--
Example: a canteen allergen graph built from supplier CSV files (RML), recipe pages (JSON-LD),
recipe PDFs (LLM extraction) and Wikidata (federation), checked with SHACL, served to a menu app and a chatbot.
-->
