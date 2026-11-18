---
minutes: 2
---

# Which would you pick?

1. Merge allergen data from five food suppliers <span v-click>→ **RDF**: shared IRIs and vocabularies</span>
2. Real-time recommendations inside one shop app <span v-click>→ **Property graph**: fast local traversal</span>
3. Publish open nutrition data for anyone to reuse <span v-click>→ **RDF / JSON-LD**: open standards, linkable</span>

<div v-click>
<div class="sdsc-features pick">
  <div class="sdsc-feature">
    <h3>RDF fits best when</h3>
    <ol>
      <li>Data from several sources is merged</li>
      <li>Others will reuse or link to the data</li>
      <li>Several tools check the same schema</li>
    </ol>
  </div>
  <div class="sdsc-feature">
    <h3>A property graph fits best when</h3>
    <ol>
      <li>One application owns the data</li>
      <li>Queries filter on edge values over many hops</li>
      <li>You run weighted graph algorithms</li>
    </ol>
  </div>
</div>

<div class="sdsc-takeaway">Ask whether people outside your application will use the data.</div>
</div>

<p class="fine">Sources: W3C RDF 1.1 Concepts · W3C JSON-LD 1.1 · W3C SHACL · Neo4j Cypher 25 · Neo4j GDS</p>

<!--
Show of hands before each reveal. There are no wrong answers if people can give a reason.
The fourth click shows the summary cards.
RDF: shared IRIs mean no key mapping when merging; W3C standards and JSON-LD for reuse; SHACL shapes run on any SHACL engine.
Property graph: the app team defines labels and constraints; edge filters over many hops suit fraud rings and recommendations;
algorithm libraries (shortest path, PageRank, community detection) ship with Neo4j GDS and Memgraph MAGE, rarely with triplestores.
Mixed setups exist: keep the shared model in RDF and load a copy into Neo4j with neosemantics for app queries.
-->
