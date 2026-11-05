---
minutes: 3
---

# Feeding the report back

```text
A SHACL validator found the problems below in your Turtle. Fix only these
problems and return the complete corrected Turtle, nothing else.

- recipe:pizza-margherita schema:totalTime: Use exactly one totalTime of type
  xsd:dayTimeDuration, e.g. "PT30M"^^xsd:dayTimeDuration.
- recipe:gazpacho schema:suitableForDiet: Diets must be schema.org
  RestrictedDiet values, e.g. schema:VeganDiet.
```

- Messages written as instructions get fixed faster
- Cap the rounds (we use 3), then hand over to a person
- Watch for "fixes" that delete the problem instead of solving it

<!--
These are real messages from our shapes, for the buggy file b11 in hands-on 2.
-->
