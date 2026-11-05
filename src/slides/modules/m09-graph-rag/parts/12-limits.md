---
minutes: 2
---

# Limits and risks

- **Data errors:** wrong facts in the graph come back as confident answers
- **Unknown is not false:** the graph only knows what is in it
- **Prompt injection through data:** text in your graph can carry instructions
- **Evaluation is hard:** LLM judges are biased, benchmarks rarely match your questions

<p class="fine">Sources: Greshake et al. 2023 · Zheng et al. 2023</p>

<!--
Mitigations: read-only access, timeouts, provenance, and tests with your own questions.
Open world again: the fact-check demo's "spicy" claim was unknown, not false.
-->
