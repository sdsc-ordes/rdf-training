---
layout: two-cols-header
minutes: 2
---

# Start from the questions

::left::

1. Which recipes take less than 30 minutes?
2. What can I cook for a vegetarian, gluten-free guest?
3. Which recipes use ingredients grown in Spain?
4. Which ingredients hide allergens?
5. Which cuisine has the most vegan recipes?

::right::

**Nouns → classes**
recipe, ingredient, allergen, country, cuisine, diet

**Verbs → properties**
takes (time), contains, grown in, has allergen, suits (diet)

<!--
These are competency questions: the graph is done when it can answer them.
They also become the SPARQL queries in hands-on 3.
-->

---
minutes: 1
---

# Four kinds of things

<table class="compact">
  <thead><tr><th>Kind</th><th>Example</th><th>In Turtle</th></tr></thead>
  <tbody>
    <tr><td><b>Class</b></td><td>Recipe, Food</td><td><code>schema:Recipe</code></td></tr>
    <tr><td><b>Individual</b></td><td>Rösti, Fuji apple</td><td><code>recipe:rosti</code></td></tr>
    <tr><td><b>Property</b></td><td>has ingredient, grown in</td><td><code>rec:hasIngredient</code></td></tr>
    <tr><td><b>Literal</b></td><td>40 minutes, "Rösti" in German</td><td><code>"Rösti"@de</code></td></tr>
  </tbody>
</table>

<!--
Quick check: is "vegan" a class, an individual or a literal? (Here: an individual, schema:VeganDiet.)
-->
