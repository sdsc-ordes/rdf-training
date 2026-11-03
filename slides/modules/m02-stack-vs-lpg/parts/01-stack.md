---
minutes: 5
---

# The same fact, twice

````md magic-move
```turtle
recipe:rosti rec:hasIngredient food:potato .
```
```turtle
@prefix rec:    <https://sdsc-ordes.github.io/rdf-training/vocab/recipes#> .
@prefix recipe: <https://sdsc-ordes.github.io/rdf-training/id/recipe/> .
@prefix food:   <https://sdsc-ordes.github.io/rdf-training/id/food/> .

recipe:rosti rec:hasIngredient food:potato .
```
````
