---
minutes: 5
---

# Four kinds of LLM errors

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>Syntax</h3>
    <p>The file doesn't parse. Caught before validation.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Vocabulary</h3>
    <p>Invented properties, diets or foods. Caught by closed shapes and allowed lists.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Values</h3>
    <p>Wrong datatypes or language tags. Caught by datatype rules.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Facts</h3>
    <p>Valid but false: a wrong cooking time. Not caught by SHACL.</p>
  </div>
</div>

<div class="sdsc-takeaway">Validation turns plausible LLM output into loadable data, but valid is not the same as true.</div>

<!--
Map the board tally onto these four. Facts need sources, review or cross-checks against other data.
-->
