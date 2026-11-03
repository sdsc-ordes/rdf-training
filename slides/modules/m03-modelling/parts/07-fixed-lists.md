---
minutes: 2
---

# Fixed lists of values

<table class="compact">
  <thead><tr><th>Option</th><th>Use it when</th><th>In this course</th></tr></thead>
  <tbody>
    <tr><td>Reuse an existing list</td><td>Someone already defined it</td><td>Diets: <code>schema:VeganDiet</code></td></tr>
    <tr><td>SKOS concept scheme</td><td>You need labels, translations, broader and narrower terms</td><td>Allergens, cuisines</td></tr>
    <tr><td><code>sh:in</code> in a shape</td><td>You only need to check allowed values</td><td>Units</td></tr>
  </tbody>
</table>

<!--
The 14 EU allergens are a SKOS scheme with labels in en, de, fr and it.
Cuisines use skos:broader: Swiss is narrower than European.
-->
