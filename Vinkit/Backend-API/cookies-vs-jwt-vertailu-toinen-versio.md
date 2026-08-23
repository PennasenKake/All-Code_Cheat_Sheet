<!-- tags: vinkit, backend-api -->

# Cookies vs JWT -vertailu (toinen versio)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Toinen, tarkempaan turvallisuusvertailuun keskittyvä infografiikka cookieista ja JWT:stä autentikointimenetelminä.

## Vertailutaulukko

| Ominaisuus | Cookies | JWT |
|---|---|---|
| Tallennus | Selaimen cookie | LocalStorage, SessionStorage tai cookie |
| Palvelinsessio | Yleensä vaaditaan (sessio tallennettu palvelimelle) | Ei vaadita (tilaton) |
| Koko | Pieni | Suurempi |
| Turvallisuus | HttpOnly, Secure, SameSite-liput | Vaatii turvallisen tallennuksen |
| Skaalautuvuus | Vähemmän skaalautuva (vaatii palvelinsession) | Erittäin skaalautuva (ei palvelinsessiota) |
| Mobiilisovellukset | Harvinaisempi | Laajasti käytössä |
| Cross-domain | Monimutkaisempi | Helpompi API:en kanssa |
| Paras käyttö | Perinteiset web-sovellukset | REST API:t, mobiilisovellukset, mikropalvelut |
| Lähetystapa | Selain lähettää automaattisesti | Lähetetään manuaalisesti headerissa |
| CSRF-riski | Korkeampi (tarvitsee CSRF-suojauksen) | Matalampi (Authorization-headeria käyttäen) |
| Tokenin varkaus | Vaikeampi HttpOnlyn kanssa | Helpompi, jos tallennettu turvattomasti |
| Mitätöinti (revocation) | Helppo | Tokenia ei voi helposti mitätöidä ennen vanhenemista |

## Cookie-autentikaation kulku

```
User Login → Server Validates User → Session Created → Session ID Stored in Cookie
  → Browser Sends Cookie Automatically → Server Verifies Session → Access Granted
```

**Esimerkki:** `Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict`

**Edut:** lähetetään automaattisesti selaimen toimesta, helppo toteuttaa, HttpOnly suojaa JavaScript-pääsyltä, sopii perinteisille sivustoille.

**Haitat:** vaatii palvelinpuolen session-tallennuksen, vaikeampi skaalata.

## JWT-autentikaation kulku

```
User Login → Server Validates User → JWT Generated → Token Sent to Client
  → Client Stores JWT → Client Sends JWT in Header → Server Verifies JWT → Access Granted
```

**JWT:n rakenne:** `Header . Payload . Signature`

Esimerkki: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6IkpvaG4ifQ...`

**JWT payload -esimerkki:**
```json
{
  "id": 101,
  "name": "John",
  "role": "admin",
  "exp": 1750000000
}
```

**JWT:n lähetys:** `Authorization: Bearer <token>`

**Edut:** tilaton autentikointi, helppo skaalata, sopii REST API:hin, toimii hyvin mobiilisovellusten kanssa.

**Haitat:** tokenia ei voi helposti mitätöidä ennen vanhenemista, suurempi payload-koko, turvaton tallennus voi johtaa XSS-riskeihin.

## Turvallisuusvertailu

| Näkökulma | Cookies | JWT |
|---|---|---|
| XSS-suojaus | Vahva HttpOnlyn kanssa | Riippuu tallennustavasta |
| CSRF-riski | Korkeampi (tarvitsee suojauksen) | Matalampi Auth-headerin kanssa |
| Tokenin varkaus | Vaikeampi HttpOnlyn kanssa | Helpompi, jos tallennettu turvattomasti |

## Milloin käyttää cookieita?

- Perinteiset web-sovellukset
- Palvelinpuolella renderöidyt sovellukset
- Pankki-/admin-dashboardit
- Kun käytössä on palvelinpuolen sessiot

## Milloin käyttää JWT:tä?

- REST API:t
- Mobiilisovellukset
- Mikropalveluarkkitehtuuri
- Single Page -sovellukset (React, Angular, Vue)

## Haastattelukysymyksen vastaus

Cookiet tallentavat session-tunnisteen ja nojaavat palvelinpuolen sessioihin, kun taas JWT tallentaa autentikointidatan allekirjoitetun tokenin sisään ja mahdollistaa tilattoman autentikoinnin. Cookieita käytetään yleisesti perinteisissä web-sovelluksissa, kun taas JWT on suosittu API:ssa, mobiilisovelluksissa ja skaalautuvissa hajautetuissa järjestelmissä.

## Moderni suositus

Tallenna JWT turvalliseen, HttpOnly-cookieen paremman turvallisuuden saavuttamiseksi — tämä yhdistää molempien menetelmien vahvuudet.
