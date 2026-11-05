---
minutes: 2
---

# Where the terms fit

<div class="terms">
<div>
  <p class="terms-head">Where it lives <span>· kinds of</span></p>
  <div class="tbox tbox-1">
    <b>Graph database</b>
    <div v-click="1" class="tbox tbox-2"><b>Triplestore</b><small>RDF, queried with SPARQL</small></div>
    <div v-click="1" class="tbox tbox-2"><b>Property graph database</b><small>queried with Cypher or GQL</small></div>
  </div>
</div>
<div v-click="2" class="terms-arrow">stores</div>
<div v-click="2">
  <p class="terms-head">What it contains <span>· parts of</span></p>
  <div class="tbox tbox-1">
    <b>Knowledge graph</b>
    <div class="terms-row">
      <div v-click="3" class="tbox tbox-2"><b>Instance data</b><small>recipe:rosti, food:fuji-apple</small></div>
      <div v-click="3" class="tbox tbox-2"><b>Schema</b>
        <div v-click="4" class="tbox tbox-3"><b>Ontology</b>, also called vocabulary<small>classes and properties (RDFS, OWL)</small>
          <div class="tbox tbox-4"><b>Taxonomy</b><small>the <code>rdfs:subClassOf</code> hierarchy</small></div>
        </div>
        <div v-click="4" class="tbox tbox-3"><b>Shapes</b><small>what valid data looks like (SHACL)</small></div>
      </div>
    </div>
  </div>
  <p v-click="5" class="terms-note">In RDF the schema is a graph too: its triples can sit in the same store as the data and be queried together.</p>
</div>
</div>

<p class="fine">Sources: Hogan et al. 2021 · W3C RDF Schema 1.1 · W3C SHACL</p>

<!--
People use these words interchangeably; the boxes separate them. On the left, a box inside a box is a kind of it. On the right, it is a part of it. The arrow is the only "stores".
A knowledge graph does not need a triplestore: it can also be Turtle files, or a virtual graph over a SQL database (Ontop, R2RML; the benchmark on slide 4).
"Vocabulary" and "ontology" are used for the same thing; schema.org calls itself a vocabulary. Fixed lists such as cuisines and allergens (SKOS) are also part of the schema.
Meronomy (part-of, slide 29) is not in the schema: "pesto contains basil" is instance data. Only the property rec:containsIngredient is defined in the ontology.
Because the schema is triples, one SPARQL query can ask about data and schema at once, e.g. ?food a/rdfs:subClassOf* rec:AnimalProduct.
-->
