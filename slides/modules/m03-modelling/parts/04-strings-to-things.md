---
layout: two-cols-header
class: code-small
minutes: 3
---

# From strings to things

::left::

## A string (schema.org)

```turtle
recipe:rosti schema:recipeIngredient
    "800 g potatoes, grated" .
```

Fine for display and search engines. You can't ask "which recipes use potatoes?"

::right::

## Things

<<< @/../data/golden/recipes.ttl#rostiUsage turtle

Food, amount and unit are each queryable and checkable.

<!--
Lesson from SPHN: objectification pays off for anything you want to query or reuse (units, codes),
but it costs triples and query complexity. Turn strings into things where your questions need it.
-->
