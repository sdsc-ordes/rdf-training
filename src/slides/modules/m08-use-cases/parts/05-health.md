---
minutes: 2
---

# BenevolentAI: a COVID-19 drug candidate

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>Problem</h3>
    <p>January 2020: find an approved drug that might work against the new coronavirus.</p>
  </div>
  <div class="sdsc-feature">
    <h3>The graph</h3>
    <p>Dozens of biomedical databases (ChEMBL, Gene Ontology, Reactome and others) plus relations text-mined from about 30 million papers.</p>
  </div>
  <div class="sdsc-feature">
    <h3>How it was used</h3>
    <p>Queries found 378 inhibitors of AAK1, a protein involved in virus entry; 47 were approved drugs. Experts ruled out cancer drugs and chose baricitinib, which also reduces inflammation.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Result</h3>
    <p>FDA emergency use (2020), WHO recommendation (2022), FDA approval (2022). In the RECOVERY trial (8,156 patients), baricitinib reduced deaths by 13%.</p>
  </div>
</div>

<p class="fine">Sources: Richardson et al. 2020 · Smith et al. 2021 · WHO 2022 · Lilly 2022 · RECOVERY 2022</p>

<!--
The graph produced the shortlist (within about 48 hours, according to the company); experts chose, trials decided.
The measured benefit shrank as trials grew: 38% fewer deaths in COV-BARRIER (2021), 13% in RECOVERY (2022).
The papers are by BenevolentAI staff. How the graph is stored has not been published.
-->

---
minutes: 2
---

# Genomics England: rare-disease diagnosis

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>Problem</h3>
    <p>Find the one variant that causes a patient's rare disease among millions of variants in their genome.</p>
  </div>
  <div class="sdsc-feature">
    <h3>The ontology</h3>
    <p>The Human Phenotype Ontology (HPO) arranges symptoms in a hierarchy and links them to more than 8,100 rare diseases. It is published in OWL.</p>
  </div>
  <div class="sdsc-feature">
    <h3>How it is used</h3>
    <p>Clinicians record symptoms as HPO terms. Exomiser compares them with diseases and animal models, counting related symptoms through the hierarchy, and ranks candidate genes.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Result</h3>
    <p>100,000 Genomes pilot: a diagnosis for 25% of 2,183 patients; a quarter of those diagnoses changed clinical decisions. In 4,877 solved cases, Exomiser ranked the right gene first 82.6% of the time.</p>
  </div>
</div>

<p class="fine">Sources: Gargano et al. 2024 · Smedley et al. 2021 · Jacobsen et al. 2022 · Genomics England 2024</p>

<!--
The 25% diagnostic yield comes from the whole pipeline (gene panels, Exomiser, clinical scientists), not Exomiser alone.
The 82.6% is a retrospective test on cases that were already solved.
Every rare-disease case in Genomics England's pipeline now runs through Exomiser.
-->

---
minutes: 2
---

# DeepRare: an LLM agent for rare diseases

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>What it is</h3>
    <p>An LLM system with more than 40 tools. It extracts HPO terms from clinical notes, maps diseases to Orphanet and OMIM identifiers, and runs Exomiser.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Accuracy</h3>
    <p>Correct first diagnosis in 64.4% of 163 cases, against 54.6% for five experienced physicians. With genetic data (168 cases): 69.1%, against 55.9% for Exomiser alone.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Evidence</h3>
    <p>Each diagnosis cites its evidence. Experts agreed with it in 95.4% of reviews, but also found invented reference links.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Limits</h3>
    <p>A retrospective study (Nature, 2026). The system has not been tested in clinical practice.</p>
  </div>
</div>

<p class="fine">Sources: Zhao et al. 2026</p>

<!--
The physicians could use search engines but no AI tools.
The standard identifiers (HPO, Orphanet, OMIM) are what make its evidence checkable: compare with module 9.
A graph RAG example from the same field: KG-RAG over the SPOKE biomedical graph (Soman et al., Bioinformatics 2024)
raised Llama-2-13B's accuracy on multiple-choice questions from 0.31 to 0.53.
-->
