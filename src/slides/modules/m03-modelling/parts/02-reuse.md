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

<div v-click="[1, 2]" class="quote-overlay">
  <blockquote>
    <p>“The ‘root cause’ of the loss of the spacecraft was the failed translation of English units into metric units in a segment of ground-based, navigation-related mission software, as NASA has previously announced,” said Arthur Stephenson, chairman of the Mars Climate Orbiter Mission Failure Investigation Board. “The failure review board has identified other significant factors that allowed this error to be born, and then let it linger and propagate to the point where it resulted in a major error in our understanding of the spacecraft’s path as it approached Mars.”</p>
  </blockquote>
  <p class="fine">Sources: NASA 1999</p>
</div>

<!--
Why our own rec:hasIngredient? schema:recipeIngredient is plain text ("400 g Gruyère, grated"):
fine for search engines, useless for "which recipes contain cheese?".
Click once to show the quote from NASA's 1999 press release on the Mars Climate Orbiter, lost because ground software used pound-force seconds where newton-seconds were expected. Click again to hide it.
QUDT started in NASA's NExIOM project at Ames; no source says the crash triggered it.
-->
