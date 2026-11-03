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

```sparql
SELECT ?recipe ?time WHERE {
  ?recipe schema:totalTime ?time .
}
```

The engine returns every way the pattern fits the data.

<!--
Variables start with ?. The WHERE block uses the same triple syntax as Turtle.
-->

---
minutes: 3
---

# Recipes under 30 minutes

<<< @/../hands-on/h3-query/queries/q04-quick.rq sparql {5|6-8|9|10|12|all}

<div class="sdsc-takeaway">Model for your questions and the queries almost write themselves.</div>

<!--
Step through: pattern, language filter, time filter, sort. Typed literals make the comparison work.
This is query q04 from hands-on 3.
-->
