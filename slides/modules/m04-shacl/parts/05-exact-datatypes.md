---
minutes: 2
---

# Datatypes are exact

<table class="compact">
  <thead><tr><th>You write</th><th>Turtle reads it as</th><th>Passes <code>sh:datatype</code> …</th></tr></thead>
  <tbody>
    <tr><td><code>450</code></td><td><code>xsd:integer</code></td><td>not <code>xsd:decimal</code></td></tr>
    <tr><td><code>30.5</code></td><td><code>xsd:decimal</code></td><td>not <code>xsd:double</code></td></tr>
    <tr><td><code>3.05e1</code></td><td><code>xsd:double</code></td><td><code>xsd:double</code></td></tr>
    <tr><td><code>"30 min"</code></td><td><code>xsd:string</code></td><td>not <code>xsd:dayTimeDuration</code></td></tr>
  </tbody>
</table>

<div class="sdsc-takeaway">Our old borehole data wrote coordinates like <code>-122.4194</code> but its shapes required <code>xsd:double</code>: every coordinate would fail.</div>

<!--
SHACL compares the datatype IRI exactly; xsd:integer being "derived from" xsd:decimal does not count.
Pick datatypes that match how people and LLMs will actually write the values.
-->
