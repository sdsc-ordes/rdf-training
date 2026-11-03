---
layout: two-cols-header
minutes: 3
---

# Kind of, or part of?

::left::

## Taxonomy: *is a kind of*

```mermaid {scale: 0.8}
graph BT
  H[rec:HardCheese] --> C[rec:Cheese]
  C --> D[rec:DairyProduct]
  D --> A[rec:AnimalProduct]
```

`rdfs:subClassOf`

::right::

## Meronomy: *is part of*

```mermaid {scale: 0.8}
graph LR
  P([pesto]) --> B([basil])
  P --> N([pine nut])
  P --> M([Parmesan])
  P --> O([olive oil])
```

`rec:containsIngredient`

<!--
Taxonomies support inference ("Parmesan is an animal product").
Meronomies support "what is inside": the vegan check follows both, recipe → pesto → Parmesan → AnimalProduct.
-->
