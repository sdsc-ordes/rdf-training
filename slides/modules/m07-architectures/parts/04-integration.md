---
minutes: 4
---

# Copy, map or ask?

<table class="compact">
  <thead><tr><th></th><th>Materialised</th><th>Virtual</th><th>Federated</th></tr></thead>
  <tbody>
    <tr><td><b>How</b></td><td>Convert and load into a triplestore</td><td>Map sources, query them live (Ontop)</td><td>Query other endpoints with <code>SERVICE</code></td></tr>
    <tr><td><b>Freshness</b></td><td>As fresh as the last load</td><td>Live</td><td>Live</td></tr>
    <tr><td><b>Speed</b></td><td>Fast</td><td>Depends on the sources</td><td>Depends on others</td></tr>
    <tr><td><b>Control</b></td><td>Full</td><td>Shared with source owners</td><td>Little</td></tr>
  </tbody>
</table>

<div class="sdsc-takeaway">Federation is a blessing and a curse: no copies, but someone else's outage is your outage.</div>

<!--
Most systems mix the three: materialise your core data, federate for reference data like Wikidata.
-->
