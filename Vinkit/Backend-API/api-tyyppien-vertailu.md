<!-- tags: vinkit, backend-api -->

# API-tyyppien vertailu (REST, GraphQL, SOAP, WebSocket ym.)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Valitse oikea API-tyyppi sovelluksellesi.

## 1. REST API (Representational State Transfer)

**Ominaisuudet:**
- Käyttää HTTP-metodeja (GET, POST, PUT, DELETE)
- Tilaton kommunikointi (stateless)
- JSON-dataformaatti

**Esimerkki:**

```
GET     /api/users
POST    /api/users
PUT     /api/users/1
DELETE  /api/users/1
```

**Käyttötapaukset:** verkkosovellukset, mobiilisovellukset, CRUD-operaatiot, verkkokaupat, sosiaalisen median alustat.

**Esimerkkejä:** GitHub API, Twitter API, Stripe API.

## 2. GraphQL API

**Ominaisuudet:**
- Yksi endpoint
- Client pyytää vain tarvitsemaansa dataa
- Joustavat kyselyt (flexible queries)

**Esimerkki:**

```graphql
{
  user(id: 1) {
    name
    email
  }
}
```

**Käyttötapaukset:** monimutkaiset frontend-sovellukset, React/Angular/Vue-sovellukset, sosiaalisen median alustat, useat client-laitteet.

**Esimerkkejä:** GitHub GraphQL API, Shopify API.

## 3. SOAP API (Simple Object Access Protocol)

**Ominaisuudet:**
- XML-pohjainen
- Erittäin turvallinen
- Tiukat standardit

**Esimerkki:**

```xml
<soap:Envelope>
  <soap:Body>
    <GetUser>
      <id>1</id>
    </GetUser>
  </soap:Body>
</soap:Envelope>
```

**Käyttötapaukset:** pankkijärjestelmät, terveydenhuollon sovellukset, yritysohjelmistot, valtion järjestelmät.

**Esimerkkejä:** maksuportit (payment gateways), ERP-järjestelmät.

## 4. WebSocket API

**Ominaisuudet:**
- Reaaliaikainen kommunikointi
- Kaksisuuntainen yhteys (full-duplex)
- Pysyvä yhteys (persistent connection)

**Esimerkki:**

```javascript
const socket =
  new WebSocket("ws://example.com");
```

**Käyttötapaukset:** chat-sovellukset, live-ilmoitukset, online-pelaaminen, osakemarkkinasovellukset, videoneuvottelut.

**Esimerkkejä:** WhatsApp Web, Slack, Discord.

## 5. gRPC API

**Ominaisuudet:**
- Korkea suorituskyky
- Käyttää Protocol Buffersia
- Tukee streamingiä

**Esimerkki:**

```protobuf
service UserService {
  rpc GetUser(UserRequest)
    returns (UserResponse);
}
```

**Käyttötapaukset:** mikropalveluarkkitehtuuri, sisäisten palveluiden kommunikointi, nopeat sovellukset, pilvipohjaiset järjestelmät.

**Esimerkkejä:** Google Cloud Services.

## 6. OpenAPI (Swagger)

**Ominaisuudet:**
- API-dokumentaatiostandardi
- Generoi API-dokumentaation automaattisesti

**Käyttötapaukset:** API-dokumentaatio, tiimien yhteistyö, API-testaus.

**Esimerkkityökaluja:** Swagger UI, Swagger Editor.

## 7. RPC API (Remote Procedure Call)

**Ominaisuudet:**
- Suorittaa funktioita etäpalvelimilla
- Proseduuriorientoitunut (procedure-oriented)

**Esimerkki:**

```json
{
  "method": "getUser",
  "params": [1]
}
```

**Käyttötapaukset:** sisäiset palvelut, hajautetut järjestelmät, legacy-sovellukset.

**Esimerkkejä:** Thrift, JSON-RPC.

## 8. Streaming API

**Ominaisuudet:**
- Jatkuva datan siirto
- Reaaliaikaiset päivitykset

**Käyttötapaukset:** live-urheilutulokset, IoT-laitteet, osakekaupankäyntialustat, analytiikkadashboardit.

**Esimerkkejä:** Server-Sent Events (SSE), Apache Kafka, AWS Kinesis.

## Pikavertailu

| API-tyyppi | Paras käyttöön | Dataformaatti | Reaaliaikainen |
|---|---|---|---|
| REST | Web- ja mobiilisovellukset | JSON | Ei |
| GraphQL | Joustava datan haku | JSON | Ei |
| SOAP | Yritystason tietoturva | XML | Ei |
| WebSocket | Chat ja pelit | JSON/Binary | Kyllä |
| gRPC | Mikropalvelut | Protocol Buffers | Kyllä |
| RPC | Etäfunktiokutsut | JSON/XML | Ei |
| Streaming | Live-data | Vaihtelee | Kyllä |

## Minkä API:n pitäisi valita?

| Käyttötapaus | Suositeltu API |
|---|---|
| Verkkokauppasivusto | REST |
| Sosiaalisen median sovellus | GraphQL |
| Pankkisovellus | SOAP |
| Chat-sovellus | WebSocket |
| Mikropalvelut | gRPC |
| IoT-järjestelmä | Streaming API |
| Sisäinen yritysjärjestelmä | RPC / gRPC |

## Haastattelukysymys

**K: Mikä API sopii parhaiten reaaliaikaisiin chat-sovelluksiin?**

**V:** WebSocket API, koska se tarjoaa pysyvän yhteyden ja kaksisuuntaisen (bidirectional) kommunikoinnin.

## Keskeinen johtopäätös

Eri API-tyyppien ymmärtäminen auttaa rakentamaan skaalautuvia, turvallisia ja korkean suorituskyvyn sovelluksia. Oikea API, parempi suorituskyky, tyytyväiset käyttäjät.

### Yhteenveto valintaperusteista

- REST → CRUD-sovellukset
- GraphQL → joustava datan haku
- WebSocket → reaaliaikaiset sovellukset
- gRPC → korkean suorituskyvyn mikropalvelut
- SOAP → yritystason tietoturva
