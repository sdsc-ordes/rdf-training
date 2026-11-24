---
minutes: 3
---

# One model that could work

<div class="cq-strip">
  <span><b>2</b> What can I cook for a vegetarian, gluten-free guest?</span>
  <span><b>3</b> Which recipes use ingredients grown in Spain?</span>
</div>

```mermaid {scale: 0.6}
graph LR
  R["Recipe<br/>schema:Recipe"]:::reused -- rec:hasIngredient --> F["Food<br/>rec:Food"]:::ours
  R -- schema:recipeIngredient --> L["Ingredient lines<br/>#quot;40 g butter#quot;"]:::literal
  F -- rec:containsIngredient --> F
  F -. subclasses .-> T["Food types<br/>rec:DairyProduct …"]:::ours
  F -- rec:hasAllergen --> A(["Allergens<br/>allergen:gluten …"]):::lists
  F -- rec:grownIn --> C["Countries<br/>wd:Q29 …"]:::external
  R -- rec:cuisine --> K(["Cuisines<br/>cuisine:swiss …"]):::lists
  R -- schema:suitableForDiet --> D(["Diets<br/>schema:VeganDiet …"]):::reused
  %% colours mirror external/sdsc-slides/references/tokens.toml
  classDef ours fill:#26235C,stroke:#26235C,color:#FFFFFF
  classDef reused fill:#DDDEEC,stroke:#5561A6,color:#26235C
  classDef lists fill:#FFFFFF,stroke:#5561A6,color:#26235C
  classDef literal fill:#F4F3F8,stroke:#5561A6,stroke-dasharray:4 3,color:#26235C
  %% external is a rect rounded with rx/ry (half its height): a stadium's outline is drawn in short pieces, which breaks the dashes
  classDef external fill:#FFFFFF,stroke:#5561A6,stroke-dasharray:4 3,color:#26235C,rx:36px,ry:36px
```

<div class="legend">
  <span class="lg lg-ours">our own terms (<code>rec:</code>)</span>
  <span class="lg lg-reused">reused from schema.org</span>
  <span class="lg lg-lists">our own lists, written with SKOS</span>
  <span class="lg lg-external">external data: Wikidata</span>
  <span class="lg lg-literal">text value</span>
</div>

<!--
Other models can work too; check yours against the five competency questions.
Question 2: Recipe -> rec:hasIngredient -> Food (and rec:containsIngredient for products) -> rec:hasAllergen gluten; meat and fish are food types (subclasses). Hands-on 3 query q09.
Question 3: Recipe -> rec:hasIngredient -> Food -> rec:grownIn -> wd:Q29. Hands-on 3 query q06.
The same model also answers questions 4 (fish) and 5 (cuisines, diets); question 1 needs schema:totalTime, which the diagram leaves out.
Boxes are classes; rounded nodes are fixed lists of values, shown with an example IRI.
SKOS is not a source but a vocabulary for writing such lists (concepts, labels, broader/narrower).
Two ingredient edges: schema:recipeIngredient holds the recipe's text lines as written; schema.org expects plain text there, so links to Food things use our own rec:hasIngredient.
Point out containsIngredient: products like Worcestershire sauce have ingredients of their own.
That is where hidden anchovies and gluten live. Full model: src/data/vocab/recipes.ttl.
-->
