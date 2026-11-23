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
    <div class="flow">
      <span class="fn fn-text">Documents</span>
      <span class="fe">LLM extracts entities and relations</span>
      <span class="fn fn-graph">Entity graph</span>
      <span class="fe">clusters, summarised by an LLM</span>
      <span class="fn fn-text">Cluster summaries</span>
      <span class="fe">retrieved for the question</span>
      <span class="fn fn-llm">LLM answers</span>
    </div>
  </div>
  <div class="sdsc-feature">
    <h3>B · Curated KG</h3>
    <p>The LLM writes SPARQL or calls graph tools (MCP); the KG is the source of truth.</p>
    <div class="flow">
      <span class="fn fn-text">Question</span>
      <span class="fe">LLM writes SPARQL or calls a tool</span>
      <span class="fn fn-graph">Curated KG</span>
      <span class="fe">result rows, with IRIs</span>
      <span class="fn fn-llm">LLM answers</span>
    </div>
  </div>
  <div class="sdsc-feature">
    <h3>C · Hybrid</h3>
    <p>Vectors find the entry points, the graph expands and checks them.</p>
    <div class="flow">
      <span class="fn fn-text">Question</span>
      <span class="fe">similarity search</span>
      <span class="fn fn-vec">Vector index</span>
      <span class="fe">nearest entities</span>
      <span class="fn fn-graph">Curated KG</span>
      <span class="fe">neighbours, checked against the graph</span>
      <span class="fn fn-llm">LLM answers</span>
    </div>
  </div>
</div>

<p class="fine">Sources: Edge et al. 2024 · Guo et al. 2024 · Pan et al. 2024</p>

<!--
A suits large unstructured corpora and "global" questions, at a high indexing cost.
B suits structured, governed data: answers can cite IRIs. Shapes (SHACL) describe the schema to the LLM.
C is what most production systems end up with.
The flows use one style per kind of thing: dashed boxes are text, navy is a graph, light blue is a vector index. All three end with the LLM writing the answer; what differs is where its context comes from.
-->
