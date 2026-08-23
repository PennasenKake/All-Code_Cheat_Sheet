<!-- tags: vinkit, ai-ml -->

# Miten rakennat AI-agentin

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Infografiikka kuvaa AI-agentin rakentamisen kahdeksan vaihetta sekä vertailee suosituimpia agenttityökaluja ja -alustoja.

## 1. Määrittele tarkoitus ja laajuus (Define Purpose & Scope)

- Käyttötapaus (use case)
- Käyttäjien tarpeet (user needs)
- Onnistumisen mittarit (success criteria)
- Rajoitteet (constraints)

## 2. Systeemipromptin suunnittelu (System Prompt Design)

- Tavoitteet (goals)
- Rooli/persoona (role/persona)
- Ohjeet (instructions)
- Suojakaiteet (guardrails)

## 3. Valitse kielimalli (Choose LLM)

- Peruspalvelu (base model)
- Parametrit (temperature, top-p)
- Kontekstin koko (context window)
- Kustannus/viive (cost/latency)

## 4. Työkalut ja integraatiot (Tools & Integrations)

- Yksinkertaiset (paikalliset) työkalut
- API:t (web, sovellukset, data)
- MCP-palvelin
- AI-agentti työkaluna
- Räätälöidyt funktiot (custom functions)

## 5. Muistijärjestelmät (Memory Systems)

- Episodinen muisti (keskusteluhistoria)
- Työmuisti (working memory)
- Vektoritietokanta
- SQL/strukturoitu tietokanta
- Tiedostovarasto

## 6. Orkestrointi (Orchestration)

- Reitit/työnkulut (routes/workflows)
- Triggerit
- Parametrit
- Viestijonot (message queues)
- Agentti-agentille-kommunikointi (Agent2Agent)
- Virheenkäsittely

## 7. Käyttöliittymä (User Interface)

- Chat-käyttöliittymä
- Web-sovellus
- API-rajapinta
- Slack/Discord-botti

## 8. Testaus ja arviointi (Testing & Evals)

- Yksikkötestit
- Viivetestaus (latency testing)
- Laatumittarit
- Iterointi ja parannus

## Työkaluvertailu

### Kuluttaja-AI-agentit

| Tuote | LLM | Käyttöönotto | Ominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| ChatGPT (OpenAI) | GPT-5 | Pilvi | Mukautetut GPT:t, ääni, näkö, muisti, DALL-E-integraatio | Yleiskäyttöinen assistentti, luova työ |
| Claude (Anthropic) | Claude 4.5 | Pilvi | Projektit, artifactit, analyysi, 200K konteksti | Tutkimus, kirjoittaminen, koodaus |
| Perplexity | Useita | Pilvi | Haku edellä, lähdeviittaukset, Pro-haku | Tutkimusassistentti, faktantarkistus |

### Agenttiset koodaustyökalut

| Tuote | LLM | Käyttöönotto | Ominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| Cursor | Claude, GPT | Paikallinen + pilvi | Täysi IDE, composer-tila, monitiedostomuokkaus | Ammattikehittäjät, monimutkaiset projektit |
| Windsurf (Codeium) | Cascade | Paikallinen + pilvi | Flow't, agenttinen muokkaus, koodikannan tuntemus | Tiimikehitys, suuret koodikannat |
| Claude Code (Anthropic) | Claude 4.5 | Paikallinen | Terminaalinatiivi, git-integraatio, autonominen koodaus | CLI-työnkulut, automaatioskriptit |

### No-code-työkalut

| Tuote | LLM | Käyttöönotto | Ominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| Lindy | GPT-5 | Pilvi | 3000+ integraatiota, luonnollisen kielen työnkulut | Liiketoiminta-automaatio, ei-tekniset tiimit |
| Relay.app | GPT-5 | Pilvi | Ihminen mukana silmukassa, natiivi Gmail/Slack-tuki | Tiimityönkulut, hyväksynnät |
| n8n | Useita | Paikallinen/pilvi | 400+ integraatiota, itse isännöitävä, avoin lähdekoodi | Tekniset tiimit, tietosuojatarpeet |

### Kehitysframeworkit

| Tuote | LLM | Käyttöönotto | Ominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| LangGraph | Mikä tahansa | Paikallinen/pilvi | Graafipohjaiset vuot, tilanhallinta, syklit | Monimutkaiset työnkulut, tuotantosovellukset |
| CrewAI | Mikä tahansa | Paikallinen/pilvi | Roolipohjainen, 40+ integraatiota, tehtävien delegointi | Moniagenttitiimit, autonomiset järjestelmät |
| LlamaIndex | Mikä tahansa | Paikallinen/pilvi | RAG-ensin, dataliittimet, kyselymoottorit | Tietointensiiviset sovellukset, dokumentti-Q&A |
