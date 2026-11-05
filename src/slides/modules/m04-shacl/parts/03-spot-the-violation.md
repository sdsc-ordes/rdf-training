---
class: code-small
minutes: 3
---

# Spot the violations

An LLM wrote this recipe. What will the validator say?

<<< @/../hands-on/h2-validate/buggy/b11-llm-first-attempt.ttl#pizza turtle

<div class="flex gap-10 text-sm">
  <div v-click>① The name has no language tag</div>
  <div v-click>② <code>"25 min"</code> is text, not a duration</div>
  <div v-click>③ <code>food:mozzarella</code> is not a known food</div>
</div>

<!--
Give the room a minute. Then reveal one by one. These are the exact results from the real validator.
-->
