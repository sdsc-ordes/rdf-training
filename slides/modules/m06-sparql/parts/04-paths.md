---
class: code-small
minutes: 3
---

# Following paths

<<< @/../hands-on/h3-query/queries/q05-dairy.rq sparql {8|9|all}

- `/` follows one step after another, `*` repeats zero or more times
- The query follows products and the class hierarchy itself: no reasoner needed

<!--
Line 8: from a recipe through its ingredients into products (pesto → Parmesan).
Line 9: from a food's type up the hierarchy (HardCheese → Cheese → DairyProduct). This is query q05.
-->
