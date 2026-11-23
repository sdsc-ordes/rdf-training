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
