<!-- tags: vinkit, devops -->

# Ilmaiset hosting-alustat moderneja sovelluksia varten

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Osa laajempaa "Deploy Your Apps for Free" -sarjaa (osa 4/7: Hosting Platforms 09–12). Tehokkaita pilvialustoja backend-palveluihin, edge-sovelluksiin, API:hin ja nopeaan kehitykseen.

## 09. Fly.io — Edge Cloud

- **Sopii:** Docker-sovellukset, full-stack-sovellukset, globaalit julkaisut.
- **Ilmaiset ominaisuudet:** edge-julkaisu, globaalit alueet, HTTPS, Docker-tuki.

## 10. Koyeb — Cloud Platform

- **Sopii:** API:t, backend-sovellukset, kontit.
- **Ilmaiset ominaisuudet:** Git-julkaisu, automaattinen skaalaus, global edge, HTTPS.

## 11. Deno Deploy — Edge Functions

- **Sopii:** JavaScript, TypeScript, API:t.
- **Ilmaiset ominaisuudet:** edge-funktiot, nopea julkaisu, globaali verkko, HTTPS.

Esimerkkikoodi (`main.ts`):

```typescript
export default {
  async fetch(req) {
    return new Response(
      "Hello, world!"
    )
  }
}
```

## 12. Glitch — Instant Development

- **Sopii:** Node.js, oppiminen, nopeat prototyypit.
- **Ilmaiset ominaisuudet:** live-muokkaus, välitön esikatselu, Remix-projektit, yhteistyö.

Esimerkkikoodi (`index.js`):

```javascript
const http = require('http');

http.createServer((req, res) => {
  res.end('Hello from Glitch!');
}).listen(3000);
```

## Yhteenveto

Fly.io tehostaa edge-sovelluksia, Koyeb skaalaa pilvisovelluksia, Deno Deploy ajaa edge-funktioita ja Glitch on täydellinen nopeaan prototyyppaukseen.
