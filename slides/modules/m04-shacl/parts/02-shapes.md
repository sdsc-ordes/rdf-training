---
class: code-small
minutes: 3
---

# A shape for recipe times

<<< @/../data/shapes/recipes.shapes.ttl#totalTime turtle {2|3-5|6|7|all}

- Targets every `schema:Recipe` (set on the recipe shape)
- The message is written for people, and for LLMs that repair data

<!--
Walk through: path = which property; minCount/maxCount = how many; datatype = what kind of value.
This is the real shape the hands-on uses (data/shapes/recipes.shapes.ttl).
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

<!--
The report is RDF as well: you can store and query it. Severity defaults to sh:Violation.
-->
