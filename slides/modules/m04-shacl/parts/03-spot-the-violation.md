---
layout: two-cols-header
class: code-small
minutes: 3
---

# Spot the violations

An LLM wrote this recipe. What will the validator say?

::left::

<<< @/../hands-on/h2-validate/buggy/b11-llm-first-attempt.ttl#pizza turtle

::right::

<v-clicks>

- Name has no language tag
- `"25 min"` is text, not a duration
- `food:mozzarella` is not a known food

</v-clicks>

<!--
Give the room a minute. Then reveal one by one. These are the exact results from the real validator.
-->
