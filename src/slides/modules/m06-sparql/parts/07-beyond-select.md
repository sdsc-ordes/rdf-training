---
minutes: 2
---

# Beyond SELECT

<table class="compact">
  <thead><tr><th>Form</th><th>Returns</th><th>Example use</th></tr></thead>
  <tbody>
    <tr><td><code>SELECT</code></td><td>a table</td><td>lists, counts</td></tr>
    <tr><td><code>ASK</code></td><td>yes or no</td><td>does Pad Thai contain peanuts? (q10)</td></tr>
    <tr><td><code>CONSTRUCT</code></td><td>a new graph</td><td>a shopping list, a subgraph to export</td></tr>
    <tr><td><code>DESCRIBE</code></td><td>a graph about a resource</td><td>"tell me about food:pesto"</td></tr>
    <tr><td><code>INSERT</code>, <code>DELETE</code></td><td>changes the data</td><td>SPARQL Update</td></tr>
  </tbody>
</table>

- Endpoints speak the SPARQL protocol over HTTP; results come as JSON, XML, CSV or TSV
- LLMs write plausible SPARQL: run it, check the result, read the query

<p class="fine">Sources: W3C SPARQL 1.1 · W3C SPARQL 1.2</p>

<!--
SPARQL 1.2 is a W3C Working Draft (2026); 1.1 (2013) is the current Recommendation.
-->
