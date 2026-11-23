---
minutes: 2
---

# Which of our dishes can a vegetarian, gluten-free guest eat?

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>General knowledge</h3>
    <p>The LLM learned this in training: Worcestershire sauce usually contains anchovy, and soy sauce usually contains wheat. Some brands contain neither.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Your own data</h3>
    <p>Your menu, the brands you buy and their labels are not in its training data, so it cannot check them.</p>
  </div>
</div>

<!--
Ask a chatbot live: it will say Worcestershire sauce usually contains anchovy. That is right in general,
but it cannot tell whether the bottle you buy does, or which of your dishes use it.
The answer needs every dish on the menu, each checked against the labels of the products you actually buy.
Retrieval brings your data into the prompt; a graph also follows the links from dish to product to ingredient.
-->
