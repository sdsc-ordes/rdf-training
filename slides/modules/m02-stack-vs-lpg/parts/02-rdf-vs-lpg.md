---
layout: two-cols-header
minutes: 2
---

# One fact, two graph models

"Alice rated Rösti 5 stars, with 80 % confidence."

::left::

## RDF 1.2

<!-- check: skip (RDF 1.2 annotation syntax) -->
```turtle
person:alice ex:rated recipe:rosti
    {| ex:stars 5 ; ex:confidence 0.8 |} .
```

Statements about statements are new in RDF 1.2.

::right::

## Property graph (Cypher)

```cypher
(:Person {name: "Alice"})
  -[:RATED {stars: 5, confidence: 0.8}]->
(:Recipe {name: "Rösti"})
```

Properties on edges are built in.

<!--
Before RDF 1.2 you needed reification or an extra node for the rating.
Labels in a property graph are node or relationship types (Person, RATED), not edge properties.
-->

---
minutes: 2
---

# Trade-offs

<table class="compact">
  <thead><tr><th></th><th>RDF knowledge graph</th><th>Labelled property graph</th></tr></thead>
  <tbody>
    <tr><td><b>Identity</b></td><td>Global IRIs, merge across sources</td><td>IDs local to one database</td></tr>
    <tr><td><b>Schema</b></td><td>Shared vocabularies, SHACL</td><td>Constraints per database</td></tr>
    <tr><td><b>Edge details</b></td><td>RDF 1.2 triple terms</td><td>Edge properties, built in</td></tr>
    <tr><td><b>Query</b></td><td>SPARQL (W3C), federated</td><td>Cypher, GQL (ISO, 2024)</td></tr>
    <tr><td><b>Sweet spot</b></td><td>Data shared between organisations</td><td>Fast traversal inside one app</td></tr>
  </tbody>
</table>

<div class="sdsc-takeaway">RDF is built for shared meaning, property graphs for traversal inside one application. The gap is narrowing.</div>

<!--
GQL = ISO/IEC 39075:2024. Neo4j's Cypher 25 is converging on it.
Bridges exist both ways: Neo4j's neosemantics plugin, Amazon Neptune serves both models.
-->
