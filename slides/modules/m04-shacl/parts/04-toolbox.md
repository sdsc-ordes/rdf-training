---
minutes: 3
---

# The shape toolbox

<table class="compact">
  <thead><tr><th>Question</th><th>Constraints</th></tr></thead>
  <tbody>
    <tr><td>Which things?</td><td><code>sh:targetClass</code>, <code>sh:targetNode</code>, <code>sh:targetSubjectsOf</code>, <code>sh:targetObjectsOf</code></td></tr>
    <tr><td>How many values?</td><td><code>sh:minCount</code>, <code>sh:maxCount</code></td></tr>
    <tr><td>What kind of value?</td><td><code>sh:datatype</code>, <code>sh:class</code>, <code>sh:nodeKind</code></td></tr>
    <tr><td>Which values?</td><td><code>sh:in</code>, <code>sh:hasValue</code>, <code>sh:minInclusive</code>, <code>sh:maxExclusive</code></td></tr>
    <tr><td>What text?</td><td><code>sh:pattern</code>, <code>sh:languageIn</code>, <code>sh:uniqueLang</code>, <code>sh:maxLength</code></td></tr>
    <tr><td>Combine shapes</td><td><code>sh:node</code>, <code>sh:and</code>, <code>sh:or</code>, <code>sh:not</code>, <code>sh:xone</code></td></tr>
    <tr><td>Nothing else allowed</td><td><code>sh:closed</code></td></tr>
  </tbody>
</table>

<!--
Property shapes constrain the values reached through a path from each focus node.
Paths can be sequences, inverses or repeats, as in the vegan rule.
-->
