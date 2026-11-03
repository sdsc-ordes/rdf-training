---
minutes: 2
---

# Where text retrieval breaks

Vector RAG finds passages that *look like* the question. Some questions need more.

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>Multi-hop</h3>
    <p>Vegetarian? Recipe → sauce → anchovy.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Counting</h3>
    <p>How many recipes use Spanish ingredients?</p>
  </div>
  <div class="sdsc-feature">
    <h3>Hard constraints</h3>
    <p>No gluten at all, not "probably none".</p>
  </div>
  <div class="sdsc-feature">
    <h3>Whole corpus</h3>
    <p>What are the main themes of this cookbook?</p>
  </div>
</div>

<!--
Vector RAG: chunk documents, embed them, retrieve the top-k most similar chunks, paste them into the prompt.
It is good at single-hop lookups in text and remains the right tool for those.
-->

---
minutes: 2
---

# Three ways to bring in a graph

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>A · LLM-built graph</h3>
    <p>An LLM extracts entities from text, then summarises clusters. Microsoft GraphRAG, LightRAG.</p>
  </div>
  <div class="sdsc-feature">
    <h3>B · Curated KG</h3>
    <p>The LLM writes SPARQL or calls graph tools (MCP); the KG is the source of truth.</p>
  </div>
  <div class="sdsc-feature">
    <h3>C · Hybrid</h3>
    <p>Vectors find the entry points, the graph expands and checks them.</p>
  </div>
</div>

<!--
A suits large unstructured corpora and "global" questions, at a high indexing cost.
B suits structured, governed data: answers can cite IRIs. Shapes (SHACL) describe the schema to the LLM.
C is what most production systems end up with.
-->
