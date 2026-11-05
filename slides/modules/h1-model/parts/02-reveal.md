---
minutes: 3
---

# One model that could work

```mermaid {scale: 0.75}
graph LR
  R["Recipe<br/>schema:Recipe"]:::reused -- rec:hasIngredient --> F["Food<br/>rec:Food"]:::ours
  F -- rec:containsIngredient --> F
  F -. subclasses .-> T["Food types<br/>rec:DairyProduct …"]:::ours
  F -- rec:hasAllergen --> A(["Allergens<br/>allergen:gluten …"]):::lists
  F -- rec:grownIn --> C["Countries<br/>wd:Q29 …"]:::external
  R -- rec:cuisine --> K(["Cuisines<br/>cuisine:swiss …"]):::lists
  R -- schema:suitableForDiet --> D(["Diets<br/>schema:VeganDiet …"]):::reused
  %% colours mirror vendor/sdsc-slides/references/tokens.toml
  classDef ours fill:#26235C,stroke:#26235C,color:#FFFFFF
  classDef reused fill:#DDDEEC,stroke:#5561A6,color:#26235C
  classDef lists fill:#FFFFFF,stroke:#5561A6,color:#26235C
  %% external is a rect rounded with rx/ry (half its height): a stadium's outline is drawn in short pieces, which breaks the dashes
  classDef external fill:#FFFFFF,stroke:#5561A6,stroke-dasharray:4 3,color:#26235C,rx:36px,ry:36px
```

<div class="legend">
  <span class="lg lg-ours">our own terms (<code>rec:</code>)</span>
  <span class="lg lg-reused">reused from schema.org</span>
  <span class="lg lg-lists">our own lists, written with SKOS</span>
  <span class="lg lg-external">external data: Wikidata</span>
</div>

<!--
Other models can work too; check yours against the five competency questions.
Boxes are classes; rounded nodes are fixed lists of values, shown with an example IRI.
SKOS is not a source but a vocabulary for writing such lists (concepts, labels, broader/narrower).
Point out containsIngredient: products like Worcestershire sauce have ingredients of their own.
That is where hidden anchovies and gluten live. Full model: data/vocab/recipes.ttl.
-->
