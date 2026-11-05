---
minutes: 4
---

# Materialised, virtual or federated

<table class="compact">
  <thead><tr><th></th><th>Materialised</th><th>Virtual</th><th>Federated</th></tr></thead>
  <tbody>
    <tr><td><b>How</b></td><td>Convert and load into a triplestore</td><td>Map sources, query them live (Ontop)</td><td>Query other endpoints with <code>SERVICE</code></td></tr>
    <tr><td><b>Freshness</b></td><td>As fresh as the last load</td><td>Live</td><td>Live</td></tr>
    <tr><td><b>Speed</b></td><td>Fast</td><td>Depends on the sources</td><td>Depends on others</td></tr>
    <tr><td><b>Control</b></td><td>Full</td><td>Shared with source owners</td><td>Little</td></tr>
  </tbody>
</table>

<p class="fine">Sources: Calvanese et al. 2017 · W3C SPARQL 1.1</p>

<!--
Most systems mix the three: materialise your core data, federate for reference data like Wikidata.
-->
