---
minutes: 2
---

# Vector RAG in one picture

```mermaid {scale: 0.68}
graph LR
  D[Documents] --> C[Chunks] --> E[Embeddings]
  Q[Question] --> QE[Embedding]
  E --> S{Most similar<br/>chunks}
  QE --> S
  S --> P[Prompt:<br/>question + chunks] --> A[Answer]
```

- Good at: "what does the text say about X?"
- Blind to: facts spread over several documents, totals, strict rules

<!--
Chunk, embed, retrieve the top-k most similar chunks, paste them into the prompt.
It stays the right tool for single-hop lookups in text, and it is cheap to set up.
-->
