---
layout: two-cols-header
minutes: 2
---

# A query is a pattern with holes

::left::

## Data

```turtle
recipe:caesar-salad schema:totalTime
    "PT20M"^^xsd:dayTimeDuration .
```

::right::

## Pattern

````md magic-move {at: 1}
```sparql
SELECT ?recipe ?time WHERE {
  ?recipe schema:totalTime ?time .
}
```
```sparql
SELECT ?zorg ?plimf WHERE {
  ?zorg schema:totalTime ?plimf .
}
```
````

The engine returns every way the pattern fits the data.

<p v-click="1">With these names the query returns the same results.</p>

::bottom::

<p class="fine">Sources: W3C SPARQL 1.1</p>

<!--
Variables start with ?. The WHERE block uses the same triple syntax as Turtle.
Click: the variables get meaningless names. The engine matches by position in the pattern, so ?zorg still binds the recipe and ?plimf the time.
-->

---
minutes: 3
---

# Recipes under 30 minutes

<<< @/../hands-on/h3-query/queries/q04-quick.rq sparql {5|6-8|9|10|12|all}

<!--
Step through: pattern, language filter, time filter, sort. Typed literals make the comparison work.
This is query q04 from hands-on 3; it answers competency question 1 from the modelling module.
-->
