---
class: code-small
minutes: 3
---

# Node shapes and property shapes

<<< @/../data/shapes/recipes.shapes.ttl#recipeShapes turtle {2|3-5|6-7|10|11-13|14-15|all}

- **Node shape:** which things get checked · **Property shape:** what one property must look like

<!--
Node shape: sh:targetClass = which things get checked; sh:property = which property shapes apply;
sh:closed = no properties beyond the listed ones, which catches typos like rec:hasIngrediant.
Property shape: path = which property; minCount/maxCount = how many; datatype = what kind of value.
These are the real shapes the hands-on uses (data/shapes/recipes.shapes.ttl).
-->

---
minutes: 1
---

# Reading a validation report

<table class="compact">
  <thead><tr><th>Field</th><th>Answers</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td><code>sh:focusNode</code></td><td>Which thing?</td><td><code>recipe:pizza-margherita</code></td></tr>
    <tr><td><code>sh:resultPath</code></td><td>Which property?</td><td><code>schema:totalTime</code></td></tr>
    <tr><td><code>sh:value</code></td><td>Which value?</td><td><code>"25 min"</code></td></tr>
    <tr><td><code>sh:resultMessage</code></td><td>What to fix?</td><td>Use exactly one totalTime of type xsd:dayTimeDuration…</td></tr>
    <tr><td><code>sh:resultSeverity</code></td><td>How bad?</td><td><code>sh:Violation</code>, <code>sh:Warning</code>, <code>sh:Info</code></td></tr>
  </tbody>
</table>

<p class="fine">Sources: W3C SHACL</p>

<!--
The report is RDF as well: you can store and query it. Severity defaults to sh:Violation.
-->
