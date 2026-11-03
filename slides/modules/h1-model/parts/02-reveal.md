---
minutes: 3
---

# One model that works

```mermaid
graph LR
  R[schema:Recipe] -- rec:hasIngredient --> F[rec:Food]
  F -- rec:containsIngredient --> F
  F -- rec:hasAllergen --> A[Allergen · SKOS]
  F -- rec:grownIn --> C[Country · Wikidata]
  R -- rec:cuisine --> K[Cuisine · SKOS]
  R -- schema:suitableForDiet --> D[Diet · schema.org]
  F -. subclasses .-> AP[rec:AnimalProduct · rec:PlantFood · …]
```

<div class="sdsc-takeaway">There's no single right model, but there is one that answers your questions.</div>

<!--
Point out containsIngredient: products like Worcestershire sauce have ingredients of their own.
That is where hidden anchovies and gluten live. Full model: data/vocab/recipes.ttl.
-->
