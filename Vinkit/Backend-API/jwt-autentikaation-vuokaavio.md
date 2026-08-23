<!-- tags: vinkit, backend-api -->

# JWT-autentikaation vuokaavio

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Turvallisen käyttäjäautentikaation arkkitehtuuri JWT:llä (JSON Web Token), vaihe vaiheelta.

## Vaiheet

1. **User Login** — Käyttäjä syöttää sähköpostin ja salasanan kirjautumislomakkeeseen, joka lähetetään login-pyyntönä palvelimelle.
2. **API Server** — Express.js/Node.js-palvelin ottaa pyynnön vastaan ja validoi käyttäjätunnukset (credential validation).
3. **JWT Generation** — Palvelin generoi JWT-tokenin, joka koostuu kolmesta osasta: `header.payload.signature` (esim. `xxxxx.yyyyy.zzzzz`).
4. **Client Storage** — Token tallennetaan clientille — `localStorage`, `cookies` tai `sessionStorage`.
5. **Authenticated Request** — Jatkossa jokainen pyyntö lähettää JWT:n `Authorization`-headerissa: `Authorization: Bearer JWT_TOKEN`.
6. **Token Verification** — Palvelin varmistaa tokenin allekirjoituksen (verify signature), tarkistaa vanhenemisajan (check expiry) ja validoi käyttäjän (validate user).
7. **Protected Resource** — Kun token on validoitu, pääsy myönnetään suojattuun resurssiin ja data palautetaan (esim. Dashboard, Profile, Admin Panel, Settings).

## Kulku tiivistettynä

```
Login Request → Credential Validation → Token Generation → Token Storage
  → Authenticated Request → JWT Verification → Access Granted
```

## JWT:n rakenne

- **Header** — sisältää algoritmin ja tokenin tyypin, esim. `{ "alg": "HS256", "typ": "JWT" }`
- **Payload** — sisältää käyttäjän datan, esim. `{ "id": 1, "name": "John", "role": "admin" }`
- **Signature** — allekirjoitus, joka lasketaan headerista ja payloadista salaisella avaimella (HMACSHA256)
