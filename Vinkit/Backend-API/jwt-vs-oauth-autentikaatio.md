<!-- tags: vinkit, backend-api -->

# JWT vs OAuth 2.0 -autentikaatio

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## JWT (JSON Web Token)

JWT on tokenipohjainen autentikointimenetelmä. Kun käyttäjä kirjautuu onnistuneesti sisään, palvelin generoi tokenin ja lähettää sen clientille. Client sisällyttää tämän tokenin jokaiseen suojattuun pyyntöön.

**JWT-kulku:**
1. Käyttäjä kirjautuu sisään.
2. Palvelin varmistaa tunnistetiedot.
3. Palvelin generoi JWT:n.
4. Client tallentaa JWT:n (`localStorage` / `sessionStorage` / cookie).
5. Client lähettää JWT:n jokaisen pyynnön mukana: `Authorization: Bearer <token>`.
6. Palvelin varmistaa JWT:n.
7. Pääsy myönnetty.

**JWT:n rakenne:** `xxxxx.yyyyy.zzzzz` → Header . Payload . Signature

Esimerkki: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6IkpvaG4ifQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

**JWT:n edut:**
- Tilaton (stateless) autentikointi
- Nopea ja skaalautuva
- Toimii hyvin REST API:en kanssa
- Cross-platform-tuki

**JWT:n haitat:**
- Tokenia ei voi helposti mitätöidä
- Suurempi tokenin koko
- Täytyy säilyttää turvallisesti

## OAuth 2.0

OAuth on valtuutuskehys (authorization framework), joka mahdollistaa käyttäjien kirjautumisen toisen palveluntarjoajan kautta jakamatta salasanaansa. Yleisiä tarjoajia: Google, GitHub, Facebook, Microsoft.

**OAuth-kulku:**
1. Käyttäjä klikkaa "Login with Google".
2. Uudelleenohjaus Googleen.
3. Käyttäjä kirjautuu sisään.
4. Google pyytää lupaa (permission).
5. Authorization Code palautetaan.
6. Backend vaihtaa koodin Access Tokeniin.
7. Käyttäjä on kirjautunut sisään.

**OAuth-komponentit:**
- Resource Owner (käyttäjä)
- Client (oma sovellus)
- Authorization Server
- Resource Server
- Access Token
- Refresh Token

## JWT vs OAuth 2.0 -vertailu

| Ominaisuus | JWT | OAuth 2.0 |
|---|---|---|
| Tarkoitus | Autentikointi | Valtuutus (authorization) |
| Kirjautuminen | Oma sovellus | Kolmannen osapuolen tarjoajat |
| Token | JWT Token | Access Token |
| Käyttäjän salasana | Oma palvelin varmistaa | Tarjoaja varmistaa |
| Paras käyttö | REST API:t, mobiilisovellukset | Sosiaalinen kirjautuminen, yrityssovellukset |
| Tilaton | Kyllä | Riippuu toteutuksesta |
| Refresh tokenit | Valinnainen | Yleisesti käytössä |

## Milloin käyttää JWT:tä

- REST API:t
- Single Page -sovellukset (React, Angular, Vue)
- Mobiilisovellukset
- Mikropalvelut
- Sisäiset autentikointijärjestelmät

## Milloin käyttää OAuthia

- Login with Google
- Login with GitHub
- Login with Microsoft
- Kolmannen osapuolen API-pääsy
- Yritysautentikointi

## Hyvät käytännöt

- Käytä aina HTTPS:ää
- Pidä JWT:n voimassaoloaika lyhyenä (15–30 min)
- Käytä refresh tokeneita turvallisesti
- Tallenna tokenit HttpOnly Secure -cookieihin, kun mahdollista
- Älä koskaan paljasta client secreteja frontend-koodissa
- Validoi tokenin allekirjoitus jokaisella suojatulla pyynnöllä

## Nyrkkisääntö

Käytä **JWT:tä**, kun rakennat autentikointia omalle sovelluksellesi. Käytä **OAuth 2.0:aa**, kun käyttäjien täytyy kirjautua ulkoisten tarjoajien kautta tai sovelluksesi tarvitsee delegoidun pääsyn kolmannen osapuolen palveluihin.
