<!-- tags: vinkit, jarjestelmasuunnittelu -->

# Miten WebSocket toimii

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

WebSocket on protokolla, joka mahdollistaa täysduplex-viestinnän (full-duplex) asiakkaan ja palvelimen välillä yhden pitkäkestoisen TCP-yhteyden yli.

Muista: Full-Duplex, Real-time, Low Latency, Efficient, Persistent.

## 1. Mikä on WebSocket?

Kun yhteys on muodostettu, sekä asiakas että palvelin voivat lähettää viestejä toisilleen milloin tahansa (pysyvä/persistent yhteys clientin ja serverin välillä).

## 2. WebSocket vs. HTTP

| Ominaisuus | HTTP | WebSocket |
|---|---|---|
| Yhteys | Lyhytkestoinen | Pitkäkestoinen (persistent) |
| Kommunikointi | Pyyntö–vastaus | Täysduplex (kaksisuuntainen) |
| Ylikuormitus (overhead) | Korkea (otsikot joka pyynnössä) | Matala (minimaalinen overhead) |
| Reaaliaikaisuus | Rajallinen (polling / SSE) | Sisäänrakennettu reaaliaikaisuus |
| Käyttötapaus | Verkkosivut, API:t, CRUD-operaatiot | Live-chat, pelit, striimaus |

## 3. Miten yhteys käynnistyy (handshake)

1. Asiakas lähettää HTTP Upgrade -pyynnön.
2. Palvelin vastaa: `101 Switching Protocols`.
3. WebSocket-yhteys on muodostettu.

Kättelyn jälkeen HTTP:tä ei enää käytetä – yhteys on nyt WebSocket-yhteys.

## 4. Täysduplex-viestintä

Sekä asiakas että palvelin voivat lähettää viestejä toisistaan riippumatta, milloin tahansa: asiakkaalta palvelimelle ja palvelimelta asiakkaalle samanaikaisesti, useita viestejä peräkkäin kumpaankin suuntaan.

## 5. Viestin kulku

- **Tekstiviesti:** Client → `"Hello Server!"` → Server
- **Palvelimen vastaus:** Server → `"Hello Client!"` → Client
- **Binääriviesti:** Client → `1011010101...` → Server

Viestit voivat olla tekstiä tai binääridataa, ja kumpikin osapuoli voi lähettää milloin vain.

## 6. Yleisiä käyttötapauksia

- **Live Chat** – reaaliaikainen viestintä käyttäjien välillä.
- **Online Gaming** – reaaliaikaiset päivitykset ja pelaajien toiminnot.
- **Live Notifications** – push-tyyppiset reaaliaikaiset ilmoitukset.
- **Live Streaming** – reaaliaikainen data, kommentit, tilastot.
- **Collaborative Apps** – dokumentit, valkotaulut, koodieditorit.

## 7. Yhteyden tilat

`CONNECTING` (asiakas yrittää muodostaa yhteyden) → `OPEN` (yhteys muodostettu, data voi virrata molempiin suuntiin) → `CLOSING` (jompikumpi osapuoli aloittaa sulkemisen) → `CLOSED` (yhteys suljettu). Suljetusta tilasta voidaan palata takaisin `CONNECTING`-tilaan uudelleenyhdistämistä varten.

## 8. Yhteyden sulkeminen

1. Close frame lähetetään (esim. asiakkaalta).
2. Close frame lähetetään takaisin (palvelimelta).
3. Yhteys suljetaan (TCP-yhteys päätetään).

Kumpi tahansa osapuoli voi aloittaa sulkemisen, mutta molempien on vahvistettava se siistiä sulkemista varten.

## 9. WebSocket-kehyksen (frame) rakenne

| Kenttä | Koko | Selitys |
|---|---|---|
| FIN | 1 bitti | Viimeinen kehys viestissä (1 = kyllä) |
| RSV1–3 | 1 bitti kukin | Varattu laajennuksille |
| Opcode | 4 bittiä | Kehyksen tyyppi (teksti, binääri, close, ping, pong) |
| Mask | 1 bitti | Onko payload maskattu (1 = kyllä) |
| Payload Length | 7/16/64 bittiä | Datan pituus |
| Masking Key | 32 bittiä | Käytetään payloadin maskaukseen asiakkaalta |
| Payload Data | vaihteleva | Varsinainen viestidata |

Asiakkaiden **täytyy** maskata kehykset; palvelinten **ei saa** maskata kehyksiä.

## 10. Esimerkki: live-chat-virtaus

- Käyttäjä A (selain) lähettää "Hi!" WebSocket-palvelimelle.
- Palvelin välittää sen käyttäjälle B ("Forward: Hi!").
- Käyttäjä B vastaa "Hello!", palvelin lähettää sen takaisin ("Receive: Hello!") molemmille tai asianosaisille käyttäjille.

Viestit toimitetaan välittömästi kaikille yhdistetyille asiakkaille.

## 11. WebSocket vs. HTTP (tiivistetysti)

- **HTTP (Request-Response):** yksi pyyntö = yksi vastaus, yhteys suljetaan vastauksen jälkeen, ei ihanteellinen reaaliaikasovelluksille, korkeampi overhead.
- **WebSocket (Full-Duplex):** pysyvä yhteys, kaksisuuntainen kommunikointi, erinomainen reaaliaikasovelluksille, matalampi overhead ja viive.

## Vinkkejä (Pro Tip)

- Käytä sydämenlyöntejä (heartbeat, ping/pong) pitämään yhteys elossa.
- Käsittele uudelleenyhdistäminen eksponentiaalisella backoffilla.
- Käsittele virheet ja katkokset aina siististi.
- Käytä WebSocketeja vain silloin, kun reaaliaikaisuutta oikeasti tarvitaan.

WebSocketit mahdollistavat reaaliaikaiset kokemukset, joista käyttäjät pitävät.
