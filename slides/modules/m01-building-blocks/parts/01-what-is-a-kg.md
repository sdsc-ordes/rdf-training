---
layout: two-cols-header
minutes: 2
---

# What is a knowledge graph?

::left::

- **Nodes** are things: a recipe, an apple, a country
- **Edges** are named relations between them
- Every node and edge has a **global identifier**

::right::

```mermaid
graph LR
  T([Apple tart]) -- has ingredient --> A([Fuji apple])
  A -- grown in --> S([Spain])
  A -- grown in --> F([France])
  T -- cuisine --> C([Swiss])
```

::bottom::

<p class="fine">Sources: Hogan et al. 2021</p>

<!--
Poll: who has met "knowledge graph" at work? Web search, Wikidata, enterprise data catalogues.
Everything today uses one example: a recipe knowledge graph.
-->
