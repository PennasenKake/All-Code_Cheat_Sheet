<!-- tags: vinkit, backend-api -->

# Cookies vs JWT -vertailu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Mikä on Cookie?

Cookie on pieni tietopalanen, joka tallennetaan selaimeen.

**Autentikaatiokulku:**
1. Käyttäjä kirjautuu sisään.
2. Palvelin luo session.
3. Palvelin lähettää Session ID:n cookiessa.
4. Selain tallentaa cookien.
5. Selain lähettää cookien automaattisesti jokaisen pyynnön mukana.
6. Palvelin tarkistaa Session ID:n ja validoi käyttäjän.

Esimerkki: `Set-Cookie: sessionId=abc123; HttpOnly; Secure`

## Mikä on JWT?

JWT (JSON Web Token) on itsenäinen token, joka sisältää käyttäjätiedon.

**Autentikaatiokulku:**
1. Käyttäjä kirjautuu sisään.
2. Palvelin luo JWT:n.
3. Palvelin lähettää JWT:n clientille.
4. Client tallentaa JWT:n (Local Storage / Cookie).
5. Client lähettää JWT:n `Authorization`-headerissa.
6. Palvelin varmistaa tokenin allekirjoituksen.

Esimerkki JWT: `xxxxx.yyyyy.zzzzz`

**JWT:n rakenne:**
```
Header:    { "alg": "HS256", "typ": "JWT" }
Payload:   { "id": 1, "name": "John", "role": "admin" }
Signature: HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
```

Pyyntöesimerkki: `Authorization: Bearer eyJhbGciOi...`

## Vertailutaulukko

| Ominaisuus | Cookies | JWT |
|---|---|---|
| Tallennus | Selaimen cookie | Local Storage / Cookie |
| Palvelimen tila | Stateful | Stateless |
| Skaalautuvuus | Keskitasoinen | Korkea |
| Koko | Pieni | Suurempi |
| Mobiiliystävällisyys | Vähemmän | Enemmän |
| Session-hallinta | Helppo | Vaikeampi |
| Uloskirjautuminen | Helppo | Vaikeampi |
| Mikropalvelutuki | Ei ihanteellinen | Erinomainen |
| Turvallisuus | Erittäin turvallinen (HttpOnlyn kanssa) | Turvallinen, kun toteutettu oikein |

## Cookien plussat ja miinukset

**Plussat:**
- Turvallisempi HttpOnly-cookien kanssa
- Helppo mitätöidä sessioita
- Selain lähettää cookiet automaattisesti
- Sopii perinteisiin web-sovelluksiin

**Miinukset:**
- Vaatii palvelinpuolen session-tallennuksen
- Vaikeampi skaalata hajautetuissa järjestelmissä
- Sessiotietokanta kuormittaa palvelinta

## JWT:n plussat ja miinukset

**Plussat:**
- Tilaton autentikaatio (stateless)
- Ei vaadi session-tallennusta
- Helppo skaalata mikropalveluissa
- Toimii hyvin mobiilisovellusten ja API:en kanssa

**Miinukset:**
- Vaikea mitätöidä ennen vanhenemista
- Suurempi kuin session-ID:t
- Local Storage voi olla haavoittuvainen XSS-hyökkäyksille

## Kumpaa käyttää?

**Käytä cookieita kun:**
- Rakennat perinteistä web-sovellusta
- Turvallisuus on tärkein prioriteetti
- Palvelinpuolen sessiot ovat hyväksyttäviä

Esimerkkejä: pankkisovellukset, admin-dashboardit, yrityssovellukset.

**Käytä JWT:tä kun:**
- Rakennat REST API:a
- Rakennat mobiilisovellusta
- Käytössä on mikropalveluarkkitehtuuri tai hajautettu järjestelmä

Esimerkkejä: React + Node.js -sovellukset, mobiilisovellukset, SaaS-alustat.

## Moderni lähestymistapa: molemmat yhdessä

Nykyaikainen käytäntö yhdistää molemmat: lyhytikäinen **Access Token** (JWT, 15–30 min) + **Refresh Token** tallennettuna HttpOnly-cookiessa.

```
Login → Access Token (JWT) → Token Expired → Refresh Token (HttpOnly Cookie) → New Access Token
```

Tämä yhdistää JWT:n skaalautuvuuden ja cookieiden turvallisuuden, ja on laajasti käytössä moderneissa sovelluksissa kuten React, Next.js, Node.js ja mikropalveluarkkitehtuurit.
