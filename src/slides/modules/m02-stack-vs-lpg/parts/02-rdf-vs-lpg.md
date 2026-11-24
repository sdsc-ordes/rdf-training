---
layout: two-cols-header
minutes: 2
---

# The same fact in two graph models

"Alice rated Rösti 5 stars, with 80 % confidence."

::left::

## RDF 1.2

<!-- check: skip (RDF 1.2 annotation syntax) -->
```turtle
person:alice ex:rated recipe:rosti
    {| ex:stars 5 ; ex:confidence 0.8 |} .
```

Statements about statements are new in RDF 1.2.

<p class="fine">Few triplestores and tools support RDF 1.2 yet.</p>

::right::

## Property graph (Cypher)

```cypher
(:Person {name: "Alice"})
  -[:RATED {stars: 5, confidence: 0.8}]->
(:Recipe {name: "Rösti"})
```

Properties on edges are built in.

::bottom::

<p class="fine">Sources: W3C RDF 1.2 · Neo4j Cypher 25</p>

<!--
Before RDF 1.2 you needed reification or an extra node for the rating.
RDF 1.2 is still a Candidate Recommendation: check your triplestore's support before relying on it.
Labels in a property graph are node or relationship types (Person, RATED), not edge properties.
-->
