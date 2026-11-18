---
minutes: 2
---

# Where the terms fit

<div class="terms">
<div>
  <p class="terms-head">Where it's stored</p>
  <div class="tbox tbox-1">
    <b>Graph database</b>
    <div v-click="1" class="tbox tbox-2"><b>Triplestore</b><small>RDF, queried with SPARQL</small>
      <div class="tbox-logos">
        <span class="tlogo"><img src="/logos/apache-jena.svg" alt="Apache Jena" /><i class="lic lic-foss">FOSS</i></span>
        <span class="tlogo"><img src="/logos/graphdb.png" alt="Graphwise GraphDB" /><i class="lic lic-closed">not FOSS</i></span>
        <span class="tlogo"><img src="/logos/amazon-neptune.svg" alt="Amazon Neptune" /><i class="lic lic-closed">not FOSS</i></span>
        <span class="tlogo"><img src="/logos/virtuoso.png" alt="Virtuoso" /><i class="lic lic-foss">FOSS</i></span>
        <span class="tlogo"><img src="/logos/oxigraph.svg" alt="Oxigraph" /><i class="lic lic-foss">FOSS</i></span>
      </div>
    </div>
    <div v-click="1" class="tbox tbox-2"><b>Property graph database</b><small>queried with Cypher or GQL</small>
      <div class="tbox-logos">
        <span class="tlogo"><img src="/logos/neo4j.png" alt="Neo4j" /><i class="lic lic-foss">FOSS</i></span>
        <span class="tlogo"><img src="/logos/memgraph.png" alt="Memgraph" /><i class="lic lic-closed">not FOSS</i></span>
        <span class="tlogo"><img src="/logos/amazon-neptune.svg" alt="Amazon Neptune" /><i class="lic lic-closed">not FOSS</i></span>
        <span class="tlogo"><img src="/logos/janusgraph.png" alt="JanusGraph" /><i class="lic lic-foss">FOSS</i></span>      </div>
    </div>
  </div>
</div>
<div v-click="2" class="terms-arrow">stores</div>
<div v-click="2">
  <p class="terms-head">What it contains</p>
  <div class="tbox tbox-1">
    <b>Knowledge graph</b>
    <div class="terms-row">
      <div v-click="3" class="tbox tbox-2"><b>Instance data</b><small>recipe:rosti, food:fuji-apple</small></div>
      <div v-click="3" class="tbox tbox-2"><b>Schema</b>
        <div v-click="4" class="tbox tbox-3"><b>Ontology</b>
          <div class="tbox tbox-4"><b>Vocabulary</b><small>classes and properties (RDFS, OWL)</small></div>
          <div class="tbox tbox-4"><b>Taxonomy</b><small>the <code>rdfs:subClassOf</code> hierarchy</small></div>
        </div>
        <div v-click="4" class="tbox tbox-3"><b>Shapes</b><small>what valid data looks like (SHACL)</small></div>
      </div>
    </div>
  </div>
  <p v-click="5" class="terms-note">In RDF the schema is a graph too, so one SPARQL query can cover both.</p>
</div>
</div>

<p class="fine">Sources: Hogan et al. 2021 · W3C RDF Schema 1.1 · W3C SHACL · Jena licence · Oxigraph licence · Virtuoso licence · Neo4j licence · Memgraph licence · JanusGraph licence · GraphDB · Neptune</p>

<!--
Logos are trademarks of their owners, shown as examples only. FOSS = free and open-source software licence.
Logos, left to right: Apache Jena, Graphwise GraphDB, Amazon Neptune, Virtuoso, Oxigraph (triplestores); Neo4j, Memgraph, Amazon Neptune, JanusGraph (property graph databases). Neptune serves both models, so it appears in both boxes. FOSS badges: Jena, Virtuoso, Oxigraph, JanusGraph are open source; Neo4j is open source only in its Community edition; GraphDB, Neptune and Memgraph are not (Memgraph's BSL is source-available).
People use these words interchangeably; the boxes separate them. On the left, a box inside a box is a kind of it. On the right, it is a part of it. The arrow is the only "stores".
A knowledge graph does not need a triplestore: it can also be Turtle files, or a virtual graph over a SQL database (Ontop, R2RML; the benchmark on slide 4).
The vocabulary names the terms (classes, properties); the taxonomy defines the hierarchy between them; the ontology holds both. Some people call a whole ontology a vocabulary: schema.org calls itself one. Fixed lists such as cuisines and allergens (SKOS) are also part of the schema.
Meronomy (part-of, slide 29) is not in the schema: "pesto contains basil" is instance data. Only the property rec:containsIngredient is defined in the ontology.
Because the schema is triples, one SPARQL query can ask about data and schema at once, e.g. ?food a/rdfs:subClassOf* rec:AnimalProduct.
-->
