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



<p class="fine">Sources: W3C RDF 1.2 · W3C SPARQL 1.1 · ISO GQL 2024</p>

<!--
GQL = ISO/IEC 39075:2024. Neo4j's Cypher 25 is converging on it.
Bridges exist both ways: Neo4j's neosemantics plugin, Amazon Neptune serves both models.
-->
