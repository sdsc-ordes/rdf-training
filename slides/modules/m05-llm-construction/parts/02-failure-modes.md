---
minutes: 2
---

# How LLMs get RDF wrong

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>Invented terms</h3>
    <p><code>schema:PescatarianDiet</code> sounds right but does not exist.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Broken syntax</h3>
    <p>Undeclared prefixes and unescaped quotes: the file does not even parse.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Wrong datatypes</h3>
    <p><code>"25 min"</code> instead of a duration; <code>30.5</code> is a decimal, not a double.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Plausible but false</h3>
    <p>Coordinates for a site in Switzerland that point to San Francisco. Only checks that know the domain catch this.</p>
  </div>
</div>

<p class="fine">Sources: schema.org</p>

<!--
Never trust Wikidata IDs an LLM writes from memory: look them up.
-->
