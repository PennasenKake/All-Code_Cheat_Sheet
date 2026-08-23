<!-- tags: vinkit, ai-ml -->

# Miten rakennetaan AI-agentti (arkkitehtuurikaavio)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

"Building AI Agents is no longer optional." Kahdeksanvaiheinen prosessi AI-agentin rakentamiseen, sekä vertailutaulukko suosituista työkaluista ja alustoista.

## Rakennusvaiheet

1. **Define Purpose & Scope** (määrittele tarkoitus ja laajuus) – käyttötapaus (use case), käyttäjätarpeet, onnistumiskriteerit, rajoitteet.
2. **System Prompt Design** (järjestelmäpromptin suunnittelu) – tavoitteet, rooli/persoona, ohjeet, suojakaiteet (guardrails).
3. **Choose LLM** (valitse kielimalli) – peruskielimalli, parametrit (lämpötila, top-p), kontekstin koko (context window), kustannus/viive.
4. **Tools & Integrations** (työkalut ja integraatiot) – API:t (web, data), tietokannat ja tallennus, tekoälytyökalut ja -palvelut, funktiot (functions).
5. **Memory Systems** (muistijärjestelmät) – episodinen muisti, semanttinen muisti, vektoritallennus, SQL/strukturoitu data, tiedostotallennus.
6. **Orchestration** (orkestrointi) – työnkulut/virrat (workflows/flows), liipaisimet (triggers), parametrit, viestijonot (message queues), agentin reititys (agent routing), virheenkäsittely.
7. **User Interface** (käyttöliittymä) – chat-käyttöliittymä, web-sovellus, API-päätepiste, Slack-/Discord-botti.
8. **Testing & Evals** (testaus ja arviointi) – yksikkötestit, viiveen testaus, laatumittarit, iterointi ja parantaminen.

Vaiheet 1–3 etenevät järjestyksessä, minkä jälkeen työkalut ja integraatiot (4) syöttävät muistijärjestelmiä (5), jotka puolestaan syöttävät orkestrointia (6). Orkestroinnista edetään käyttöliittymään (7) ja lopuksi testaukseen ja arviointiin (8).

## Työkalu- ja alustavertailu

### Consumer AI Agents

| Tuote | LLM | Käyttöönotto | Avainominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| ChatGPT (OpenAI) | GPT-4o | Pilvi | Mukautetut GPT:t, ääni, näkö, muisti, DALL·E-integraatio | Yleiskäyttöinen avustaja, luova työ |
| Claude (Anthropic) | Claude 3.5 | Pilvi | Projects, artifacts, analyysi, 200K konteksti | Tutkimus, kirjoittaminen, koodaus |
| Perplexity | Useita | Pilvi | Haku ensin, lähdeviitteet, Pro search | Tutkimusavustaja, faktantarkistus |

### Agentic Coding Tools

| Tuote | LLM | Käyttöönotto | Avainominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| Cursor | Claude, GPT-4o | Paikallinen + pilvi | Täysi IDE, composer-tila, monitiedostomuokkaus | Ammattikehittäjät, monimutkaiset projektit |
| Windsurf (Codeium) | Cascade | Paikallinen + pilvi | Virrat, agenttinen muokkaus, koodikannan tuntemus | Tiimikehitys, isot koodikannat |
| Claude Code (Anthropic) | Claude 3.5 | Paikallinen | Terminaalinatiivi, git-integraatio, autonomiset koodausskriptit | CLI-työnkulut, automaatioskriptit |

### No-Code Builders

| Tuote | LLM | Käyttöönotto | Avainominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| Lindy | GPT-4o | Pilvi | 3000+ integraatiota, luonnollisen kielen työnkulut | Liiketoiminnan automaatio, ei-tekniset tiimit |
| Relay.app | GPT-4o | Pilvi | Human-in-loop, Gmail/Slack-natiivi | Tiimien työnkulut, hyväksynnät |
| n8n | Useita | Paikallinen + pilvi | 400+ integraatiota, itsehostattava, avoin lähdekoodi | Tekniset tiimit, tietosuojatarpeet |

### Development Frameworks

| Tuote | LLM | Käyttöönotto | Avainominaisuudet | Sopii parhaiten |
|---|---|---|---|---|
| LangGraph | Mikä tahansa | Paikallinen/pilvi | Graafipohjaiset virrat, tilanhallinta, syklit | Monimutkaiset työnkulut, tuotantosovellukset |
| CrewAI | Mikä tahansa | Paikallinen/pilvi | Roolipohjainen, 40+ integraatiota, tehtävien delegointi | Moniagenttitiimit, autonomiset järjestelmät |
| LlamaIndex | Mikä tahansa | Paikallinen/pilvi | RAG-ensin, dataliittimet, kyselymoottorit | Tietointensiiviset sovellukset, dokumentti-Q&A |
