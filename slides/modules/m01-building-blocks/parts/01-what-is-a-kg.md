---
layout: two-cols-header
minutes: 2
---

# What is a knowledge graph?

::left::

- **Nodes** are things: a recipe, an apple, a country
- **Edges** are named relations between them
- Every node and edge has a **global identifier**

<div class="sdsc-takeaway">Facts become data you can merge, check and query.</div>

::right::

```mermaid
graph LR
  T([Apple tart]) -- has ingredient --> A([Fuji apple])
  A -- grown in --> S([Spain])
  A -- grown in --> F([France])
  T -- cuisine --> C([Swiss])
```

<!--
Poll: who has met "knowledge graph" at work? Web search, Wikidata, enterprise data catalogues.
Everything today uses one example: a recipe knowledge graph.
-->
