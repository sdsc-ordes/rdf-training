---
minutes: 2
---

# Reusing vocabularies

<table class="compact">
  <thead><tr><th>Need</th><th>Reused</th></tr></thead>
  <tbody>
    <tr><td>Recipes, names, authors, times, diets</td><td>schema.org</td></tr>
    <tr><td>Allergens, cuisines, courses</td><td>SKOS concept schemes</td></tr>
    <tr><td>Units (grams, teaspoons)</td><td>QUDT</td></tr>
    <tr><td>Countries</td><td>Wikidata</td></tr>
    <tr><td>Ingredients as things, products, "grown in"</td><td><b>our own</b> <code>rec:</code> terms</td></tr>
  </tbody>
</table>

<p class="fine">Sources: schema.org Recipe · W3C SKOS · QUDT · Vrandečić & Krötzsch 2014</p>

<!--
Why our own rec:hasIngredient? schema:recipeIngredient is plain text ("400 g Gruyère, grated"):
fine for search engines, useless for "which recipes contain cheese?".
-->
