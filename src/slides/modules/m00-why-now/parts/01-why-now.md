---
minutes: 2
---

# Why this course now?

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>LLMs need grounding</h3>
    <p>Fluent answers without sources. Graph RAG brings facts you can check and cite.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Agents need tools</h3>
    <p>Protocols like MCP let AI agents query your graph; its schema tells them what exists.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Graphs got cheaper to build</h3>
    <p>LLMs draft models and extract facts; validation catches their errors.</p>
  </div>
  <div class="sdsc-feature">
    <h3>New standard versions</h3>
    <p>RDF 1.2 nears completion, SHACL and SPARQL 1.2 are in draft, GQL became an ISO standard.</p>
  </div>
</div>

<p class="fine">Sources: Sequeda et al. 2023 · Anthropic 2024 · Lippolis et al. 2025 · W3C RDF 1.2 · W3C SHACL 1.2 · W3C SPARQL 1.2 · ISO GQL 2024</p>

<!--
Grounding: in the data.world benchmark (Sequeda et al.), GPT-4 answered 16% of 43 insurance questions correctly with SQL on the database, and 54% with SPARQL on an OWL ontology mapped to the same database (R2RML).
Graph RAG went mainstream after Microsoft GraphRAG (2024), which builds its graph from text with an LLM; graph databases and triplestores now ship LLM integrations.
MCP (Model Context Protocol, open standard since November 2024); triplestore vendors (e.g. GraphDB 11) offer MCP servers.
RDF 1.2 Concepts: Candidate Recommendation Snapshot (7 April 2026). SHACL 1.2 Core and SPARQL 1.2 Query: Working Drafts (2 and 1 November 2026). GQL: ISO/IEC 39075:2024.
Scale: Wikidata's query service is moving to QLever. Swiss examples later today: SPHN, LINDAS.
-->
