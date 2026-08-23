<!-- tags: vinkit, ai-ml -->

# How to Build AI Agents from Scratch (10 vaihetta)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä. Alkuperäinen lähde: Dr. Maryam Miradi.

Infografiikka esittää käytännönläheisen 10-vaiheisen prosessin AI-agentin rakentamiseen tyhjästä.

## Vaihe 1 – Määrittele agentin rooli ja tavoite

- Mitä agentti tekee?
- Ketä se auttaa?
- Millaista tulostetta se tuottaa?
- Esimerkki: lääketieteellinen assistenttiagentti, joka lukee röntgenkuvia, tiivistää löydökset ja puhuu tulokset ääneen.

## Vaihe 2 – Suunnittele strukturoitu syöte ja tuloste

- Käytä Pydantic AI:ta tai JSON-skeemoja määrittelemään, mitä agentti vastaanottaa ja palauttaa.
- Vältä sotkuista vapaata tekstiä — ajattele kuin API:a suunnittelisit.
- Työkalut: Pydantic AI, LangChain Output Parsers

## Vaihe 3 – Prompt ja agentin käytöksen viritys

- Aloita roolipohjaisilla systeemipromptelilla.
- Käytä prompt tuningia tai prefix tuningia johdonmukaisen persoonan ja tehtäväkäytöksen saavuttamiseksi.
- Työkalut: GPT-4, Claude, Prefix Tuning, Prompt Tuning

## Vaihe 4 – Lisää päättely ja työkalujen käyttö

- Varusta agentti päättelykehyksillä: ReAct (Reasoning + Action), Chain-of-Thought.
- Anna pääsy työkaluihin, kuten verkkohakuun, koodin tulkkeihin tai dokumenttien noutajiin.
- Työkalut: LangChain, OpenAI Tools, ReAct Framework

## Vaihe 5 – Rakenna moniagenttilogiikka (tarvittaessa)

- Käytä orkestrointikehyksiä agenttien roolien ja koordinoinnin määrittelyyn.
- Luo esimerkiksi Planner-, Researcher- ja Reporter-agentit, joilla kullakin on oma syöte-/tulosteskeemansa.
- Työkalut: CrewAI, LangGraph, OpenAI Swarm

## Vaihe 6 – Lisää muisti ja pitkän aikavälin konteksti (RAG)

- Tarvitseeko agentin muistaa mitä on tapahtunut aiemmin?
- Käytä keskustelumuistia, yhteenvetomuistia tai vektoripohjaista muistia.
- Työkalut: Zep, LangChain Memory, ChromaDB, FAISS

## Vaihe 7 – Lisää ääni- tai näköominaisuudet (valinnainen)

- Tekstistä puheeksi: Coqui tai ElevenLabs.
- Kuvan ymmärtäminen: GPT-4o tai LLaMA 3.2 Vision.
- Näiden avulla agentti voi "nähdä" ja "puhua".

## Vaihe 8 – Toimita tuloste

- Muotoile tulosteet esim. Markdowniksi, PDF:ksi tai JSON:ksi.
- Tulosteen tulee olla luettavaa ja jäsenneltävää (parsable).
- Työkalut: Pydantic AI, LangChain Parsers

## Vaihe 9 – Kääri käyttöliittymään

- Luo front-end, esimerkiksi Gradio, Streamlit tai FastAPI.
- Tämä on se vaihe, joka muuttaa agentin oikeaksi tuotteeksi.

## Vaihe 10 – Arvioi ja monitoroi

- Aja testipromptteja ja työkaluketjuja luotettavuuden tarkistamiseksi.
- Käytä lokeja, benchmarkkeja ja palautetta jatkuvaan parantamiseen.
- Työkalut: MCP Logs, OpenAI Evaluation API, mukautetut mittaristot (Custom Metrics Dashboards)
