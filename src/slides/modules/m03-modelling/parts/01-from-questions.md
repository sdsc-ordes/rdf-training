---
layout: two-cols-header
minutes: 2
---

# Start from the questions

::left::

1. Which <Term k="class">recipes</Term> <Term k="property">take</Term> less than <Term k="literal">30 minutes</Term>?
2. What can I cook for a <Term k="value">vegetarian</Term>, <Term k="value">gluten-free</Term> guest?
3. Which <Term k="class">recipes</Term> <Term k="property">use</Term> <Term k="class">ingredients</Term> <Term k="property">grown in</Term> <Term k="value">Spain</Term>?
4. Which <Term k="class">recipes</Term> <Term k="property">contain</Term> <Term k="value">fish</Term>?
5. Which <Term k="class">cuisine</Term> <Term k="property">has</Term> the most <Term k="value">vegan</Term> <Term k="class">recipes</Term>?

::right::

<div class="cq-legend">
<div v-click><span class="term term-class on">Nouns</span> → classes<p>recipe, ingredient, cuisine</p></div>
<div v-click><span class="term term-property on">Verbs</span> → properties<p>take (time), use, contain, grown in, has (cuisine)</p></div>
<div v-click><span class="term term-value on">Enum values</span> → fixed lists<p>vegetarian, gluten-free, vegan (diets) · Spain (countries) · fish (allergens)</p></div>
<div v-click><span class="term term-literal on">Amounts</span> → literals<p>30 minutes</p></div>
</div>

::bottom::

<p class="fine">Sources: Noy & McGuinness 2001</p>

<!--
These are competency questions: the graph is done when it can answer them.
Each click marks one kind of term. Not every word becomes a term: "What can I cook" means recipes, and "guest" needs no class.
Discuss: in our model, cuisines are a fixed list (SKOS) rather than a class; "fish" in question 4 is an allergen.
Question 4 also needs what products contain: Worcestershire sauce contains anchovies.
They also become the SPARQL queries in hands-on 3.
-->

---
minutes: 1
---

# Four kinds of things

<table class="compact">
  <thead><tr><th>Kind</th><th>Example</th><th>In Turtle</th></tr></thead>
  <tbody>
    <tr><td><b>Class</b></td><td>Recipe, Food</td><td><code>schema:Recipe</code>, <code>rec:Food</code></td></tr>
    <tr><td><b>Individual</b></td><td>Rösti, Fuji apple</td><td><code>recipe:rosti</code>, <code>food:fuji-apple</code></td></tr>
    <tr><td><b>Property</b></td><td>has ingredient, grown in</td><td><code>rec:hasIngredient</code>, <code>rec:grownIn</code></td></tr>
    <tr><td><b>Literal</b></td><td>40 minutes, "Rösti" in German</td><td><code>"PT40M"^^xsd:dayTimeDuration</code>, <code>"Rösti"@de</code></td></tr>
  </tbody>
</table>

<!--
Quick check: is "vegan" a class, an individual or a literal? (Here: an individual, schema:VeganDiet.)
-->
