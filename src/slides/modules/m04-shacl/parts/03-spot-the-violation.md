---
class: code-small no-prefixes
minutes: 3
---

# Spot the violations

An LLM wrote this recipe. What will the validator say?

````md magic-move {at: 2}
```turtle
recipe:pizza-margherita a schema:Recipe ;
    schema:name "Pizza Margherita" ;
    schema:description "Classic Neapolitan pizza with tomato, mozzarella and basil."@en ;
    schema:author person:luca-bernasconi ;
    schema:totalTime "25 min" ;
    rec:course course:main ;
    schema:suitableForDiet schema:VegetarianDiet ;
    rec:hasIngredient food:wheat-flour, food:tomato, food:mozzarella, food:basil, food:olive-oil .
```
```turtle {2}
recipe:pizza-margherita a schema:Recipe ;
    schema:name "Pizza Margherita"@en ;
    schema:description "Classic Neapolitan pizza with tomato, mozzarella and basil."@en ;
    schema:author person:luca-bernasconi ;
    schema:totalTime "25 min" ;
    rec:course course:main ;
    schema:suitableForDiet schema:VegetarianDiet ;
    rec:hasIngredient food:wheat-flour, food:tomato, food:mozzarella, food:basil, food:olive-oil .
```
```turtle {5}
recipe:pizza-margherita a schema:Recipe ;
    schema:name "Pizza Margherita"@en ;
    schema:description "Classic Neapolitan pizza with tomato, mozzarella and basil."@en ;
    schema:author person:luca-bernasconi ;
    schema:totalTime "PT25M"^^xsd:dayTimeDuration ;
    rec:course course:main ;
    schema:suitableForDiet schema:VegetarianDiet ;
    rec:hasIngredient food:wheat-flour, food:tomato, food:mozzarella, food:basil, food:olive-oil .
```
```turtle {6}
recipe:pizza-margherita a schema:Recipe ;
    schema:name "Pizza Margherita"@en ;
    schema:description "Classic Neapolitan pizza with tomato, mozzarella and basil."@en ;
    schema:author person:luca-bernasconi ;
    schema:totalTime "PT25M"^^xsd:dayTimeDuration ;
    rec:cuisine cuisine:italian ;
    rec:course course:main ;
    schema:suitableForDiet schema:VegetarianDiet ;
    rec:hasIngredient food:wheat-flour, food:tomato, food:mozzarella, food:basil, food:olive-oil .
```
````

<div class="compare">
<div v-click="1">

<p class="code-label">Shapes, one constraint each (from recipes.shapes.ttl)</p>

```turtle
recsh:Recipe-name sh:path schema:name ;
    sh:datatype rdf:langString .
recsh:Recipe-totalTime sh:path schema:totalTime ;
    sh:datatype xsd:dayTimeDuration .
recsh:Recipe-cuisine sh:path rec:cuisine ;
    sh:minCount 1 .
```

</div>
<div class="swap">
<div v-click="[2, 3]">

<p class="result-label">① The name has no language tag</p>

```turtle
[] sh:focusNode recipe:pizza-margherita ;
   sh:resultPath schema:name ;
   sh:value "Pizza Margherita" ;
   sh:sourceShape recsh:Recipe-name ;
   sh:sourceConstraintComponent sh:DatatypeConstraintComponent .
```

</div>
<div v-click="[3, 4]">

<p class="result-label">② <code>"25 min"</code> is text, not a duration</p>

```turtle
[] sh:focusNode recipe:pizza-margherita ;
   sh:resultPath schema:totalTime ;
   sh:value "25 min" ;
   sh:sourceShape recsh:Recipe-totalTime ;
   sh:sourceConstraintComponent sh:DatatypeConstraintComponent .
```

</div>
<div v-click="4">

<p class="result-label">③ There is no <code>rec:cuisine</code></p>

```turtle
[] sh:focusNode recipe:pizza-margherita ;
   sh:resultPath rec:cuisine ;
   sh:sourceShape recsh:Recipe-cuisine ;
   sh:sourceConstraintComponent sh:MinCountConstraintComponent .
```

</div>
</div>
</div>

<!--
Click 1: the property shapes behind the three results, cut down to the constraint that fails. Let the room compare each line with the data.
Clicks 2 to 4: one result each. Its validation report entry appears on the right and the data is fixed in place (highlighted line).
The name also gets a second entry, sh:LanguageInConstraintComponent: the shape allows only en, de, fr and it.
After the three fixes the recipe passes. The full shapes also set counts, allowed languages and messages (src/data/shapes/recipes.shapes.ttl).
Prefix lines are hidden on this slide so the listings fit. These are the exact results from the real validator.
-->
