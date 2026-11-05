---
layout: two-cols-header
class: code-small
minutes: 2
---

# Merging two graphs

::left::

## Grocer

```turtle
food:fuji-apple rec:grownIn wd:Q29 .
```

## Recipe site

```turtle
recipe:apple-tart rec:hasIngredient food:fuji-apple .
```

::right::

## Both, merged

```turtle
recipe:apple-tart rec:hasIngredient food:fuji-apple .
food:fuji-apple rec:grownIn wd:Q29 .
```

A new answer appears: the apple tart uses an ingredient grown in Spain.

<!--
Merging RDF graphs is a set union: no join keys, no schema migration. Same IRI, same thing.
The hard part moves to agreeing on IRIs and vocabularies.
-->
