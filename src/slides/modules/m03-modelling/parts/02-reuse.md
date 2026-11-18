---
minutes: 2
---

# Reusing vocabularies

<table class="compact">
  <thead><tr><th>Need</th><th>Reused</th></tr></thead>
  <tbody>
    <tr><td>Recipes, names, authors, times, diets</td><td>schema.org</td></tr>
    <tr><td>Allergens, cuisines, courses</td><td>SKOS concept schemes</td></tr>
    <tr><td>Units (grams, teaspoons)</td><td><a href="https://nssdc.gsfc.nasa.gov/planetary/text/mco_pr_19991110.txt" target="_blank" rel="noopener">QUDT</a></td></tr>
    <tr><td>Countries</td><td>Wikidata</td></tr>
    <tr><td>Ingredients as things, products, "grown in"</td><td><b>our own</b> <code>rec:</code> terms</td></tr>
  </tbody>
</table>

<p class="fine">Sources: schema.org Recipe · W3C SKOS · QUDT · Vrandečić & Krötzsch 2014</p>

<!--
Why our own rec:hasIngredient? schema:recipeIngredient is plain text ("400 g Gruyère, grated"):
fine for search engines, useless for "which recipes contain cheese?".
The QUDT link opens NASA's 1999 press release on the Mars Climate Orbiter, lost because ground software used pound-force seconds where newton-seconds were expected.
QUDT started in NASA's NExIOM project at Ames; no source says the crash triggered it.
-->
