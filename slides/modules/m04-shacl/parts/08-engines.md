---
minutes: 2
---

# Where to run SHACL

<table class="compact">
  <thead><tr><th>Where</th><th>Tools</th></tr></thead>
  <tbody>
    <tr><td>Browser</td><td>Zazuko SHACL Playground (data stays local), SHACL Play!, EU ITB validator</td></tr>
    <tr><td>Code</td><td>pySHACL (Python), Apache Jena SHACL, RDF4J, TopBraid SHACL API, rdf-validate-shacl (JavaScript)</td></tr>
    <tr><td>Triplestores</td><td>GraphDB, Stardog: validate on write</td></tr>
    <tr><td>CI</td><td>Validate on every change, like this course's repository does</td></tr>
  </tbody>
</table>

<p class="fine">SHACL 1.2 (Working Drafts, 2026) adds node expressions and a separate rules specification.</p>

<p class="fine">Sources: W3C SHACL 1.2 · pySHACL</p>

<!--
Engines differ on SHACL-SPARQL support and on edge cases; our repo cross-checks pySHACL against the
engine behind the Zazuko playground so the hands-on gives the same answers as the tests.
-->
