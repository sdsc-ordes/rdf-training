---
minutes: 2
---

# DemocraSci, a property graph of the Swiss Parliament

<div class="dsci">
  <img src="/img/democrasci-schema-plain.png" alt="DemocraSci schema: bills, debates, speeches, votes, persons, parties and cantons, linked by relationships such as proposes, sponsors, voted and member of" />
  <div class="dsci-text">
    <h3>Data</h3>
    <p>Structured information from Swiss Parliament proceedings, more than 35,000 documents</p>
    <h3>Graph</h3>
    <p>A schema for the policy-making process, stored in Neo4j. Timestamps on relationships record how a law changes over time.</p>
    <h3>Project</h3>
    <p>Long-running SDSC project with political scientists from UZH and ETH Zurich, who set the research questions</p>
  </div>
</div>

<p class="fine">Sources: DemocraSci 2024</p>

<!--
The public release is a Neo4j dump on Zenodo (CC BY 4.0) covering legislative periods 48 to 51, 2007 to 2023.
The timestamps on relationships are the edge properties from the trade-offs slide.
Ask the room: the data is published openly as a Neo4j dump. Given the vote slide, would RDF have suited publication better?
-->

---
minutes: 1
---

# How DemocraSci is used

<div class="dsci">
  <div class="dsci-figure">
    <img src="/img/democrasci-schema-plain.png" alt="DemocraSci schema" />
    <img v-click class="dsci-overlay" src="/img/democrasci-schema-subgraphs.png" alt="The same schema with four subgraphs circled: policy topics, debates in a chamber, speeches and proposals, and persons with their party, canton and location" />
  </div>
  <div class="dsci-text">
    <p>Topic modelling, stance detection and embeddings enrich and expand the graph</p>
    <div v-after>
      <p>Subgraphs centred on a person or a bill are used to study polarisation, variation in discourse and how parliament has changed</p>
      <div class="dsci-charts">
        <img src="/img/democrasci-polarisation-agriculture.png" alt="Line chart: polarisation of agriculture per legislative period against the mean, rising above it in recent periods" />
        <img src="/img/democrasci-polarisation-social-welfare.png" alt="Line chart: polarisation of social welfare per legislative period, close to the mean throughout" />
      </div>
      <p class="dsci-caption">From a study of the most and least polarising topics</p>
    </div>
  </div>
</div>

<p class="fine">Sources: DemocraSci 2024</p>

<!--
Enrichment adds new nodes and properties on top of the parsed proceedings.
Circled subgraphs: policy topics, debates in a chamber, speeches and proposals, persons with party, canton and location.
Charts: polarisation per legislative period for agriculture and for social welfare, each against the overall mean.
-->
