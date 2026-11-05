---
minutes: 2
---

# Try it: view source on a recipe page

Open any big recipe website, view the page source and search for `"@type": "Recipe"`.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Rösti",
  "totalTime": "PT40M",
  "recipeIngredient": ["800 g potatoes, grated", "40 g butter", "1 tsp salt"],
  "suitableForDiet": "https://schema.org/VegetarianDiet"
}
</script>
```

<p class="fine">Sources: schema.org Recipe · W3C JSON-LD 1.1</p>

<!--
Most people have been publishing RDF without knowing it: this is JSON-LD with schema.org.
Note recipeIngredient is plain text here, which is why our graph models ingredients as things.
-->
