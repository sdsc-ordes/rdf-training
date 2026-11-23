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
    <p>An LLM extracts entities from text, then summarises communities of related entities. Microsoft GraphRAG, LightRAG.</p>
    <div class="flow">
      <span class="fn">Text chunks</span><span class="fa"></span>
      <span class="fn fn-llm bb">LLM extracts entities and relations</span><span class="fa"></span>
      <span class="fn fn-graph">Graph</span><span class="fa"></span>
      <span class="fn fn-graph">Communities</span><span class="fa"></span>
      <span class="fn fn-llm bb">LLM summarises each community</span><span class="fa"></span>
      <span class="fn fn-llm">LLM answers: local or global search</span>
    </div>
  </div>
  <div class="sdsc-feature">
    <h3>B · Curated KG</h3>
    <p>The LLM writes SPARQL or calls graph tools (MCP); the KG is the source of truth.</p>
    <div class="flow">
      <span class="fn">Question</span><span class="fa"></span>
      <span class="fn fn-llm">LLM writes SPARQL from shapes and example queries</span><span class="fa"></span>
      <span class="fn fn-graph">Run the query; retry if it fails or returns nothing</span><span class="fa"></span>
      <span class="fn fn-llm">LLM answers, citing IRIs</span>
    </div>
  </div>
  <div class="sdsc-feature">
    <h3>C · Hybrid</h3>
    <p>Vector search finds the entities or passages the question is about. The graph then follows their links to related facts.</p>
    <div class="flow">
      <span class="fn">Question</span><span class="fa"></span>
      <span class="fn fn-vec bb">Vector search finds matching entities or text passages</span><span class="fa"></span>
      <span class="fn fn-graph">Graph follows their links to related nodes and edges</span><span class="fa"></span>
      <span class="fn fn-llm">LLM answers from the vector matches plus the nodes and edges found</span>
    </div>
  </div>
</div>

<div class="legend">
  <span class="lg lg-step-graph">graph step</span>
  <span class="lg lg-step-vec">vector step</span>
  <span class="lg lg-step-llm">LLM step</span>
  <span class="lg lg-bb">black box: output varies or cannot be traced</span>
</div>

<p class="fine">Sources: Edge et al. 2024 · Guo et al. 2024 · Pan et al. 2024</p>

<!--
A suits large unstructured corpora and "global" questions, at a high indexing cost.
B suits structured, governed data: answers can cite IRIs. Shapes (SHACL) describe the schema to the LLM.
C is what most production systems end up with.
Steps are coloured by what does the work: graph, vectors or the LLM. Red dashed outline = black box: in A the graph and summaries depend on the LLM run; in C the matches come from a similarity score, not a rule you can check, and shift when the embedding model or index changes.
The final answer is LLM-written in all three, B included, so it is not marked. B's SPARQL is LLM-written too, but you can read it and it runs the same way every time. All three end with the LLM answering; what differs is where its context comes from.
A answers in two ways: local search around one entity, or global search over the community summaries.
C: the papers call the vector matches entry points. Vector search runs over entity labels and descriptions, or over text chunks linked to entities. The graph then expands from those nodes along their edges, with a hop limit or a query. The prompt gets the question, the matched text and the nodes and edges found, usually written out as triples.
B gives the LLM the shapes, classes, properties and example queries, and retries when a query fails or returns nothing. Variant: an agent calls graph tools over MCP.
-->
