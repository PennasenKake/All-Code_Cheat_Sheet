<!-- tags: vinkit, javascript-react -->

# Progressive Web Apps (service worker, manifest)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Progressive Web App (PWA) on web-sovellus, joka tarjoaa natiivisovelluksen kaltaisen käyttökokemuksen. PWA:t ovat luotettavia, nopeita, turvallisia ja toimivat myös offline-tilassa.

## Ydinominaisuudet

- **Toimii offline** — Service workerit mahdollistavat offline-toiminnallisuuden.
- **Nopea** — latautuu välittömästi ja vastaa nopeasti.
- **Asennettavissa** — voidaan asentaa aloitusnäytölle (home screen).
- **Push-ilmoitukset** — sitouttaa käyttäjiä ajankohtaisilla päivityksillä.
- **Turvallinen** — tarjotaan HTTPS:n kautta käyttäjän turvallisuuden takaamiseksi.
- **Responsiivinen** — toimii kaikilla laitteilla ja näyttökoilla.

## Miten PWA toimii

1. Käyttäjä vierailee sivustolla.
2. Service Worker rekisteröityy taustalla.
3. Sovelluskuori (app shell) välimuistitetaan ja tallennetaan paikallisesti.
4. Sovellus toimii offline-tilassa ja latautuu välittömästi toistuvilla käynneillä.

## Service Worker -esimerkki

```javascript
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('pwa-cache').then(cache =>
      cache.addAll([
        '/',
        '/index.html',
        '/styles.css',
        '/app.js',
        '/offline.html'
      ])
    )
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response =>
      response || fetch(event.request)
    )
  );
});
```

## Web App Manifest -esimerkki

```json
{
  "name": "PWA App",
  "short_name": "PWA",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#1976d2",
  "icons": [
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

## PWA:n hyödyt

- Parantunut suorituskyky ja nopeus
- Toimii offline tai huonolla verkkoyhteydellä
- Lisää käyttäjien sitoutumista ja pysyvyyttä
- Säästää dataa ja vähentää latausaikoja
- Helppo asentaa, ei tarvita sovelluskauppaa
- Kustannustehokas ja helpompi ylläpitää

## Yleisiä käyttötapauksia

- **E-commerce** — ostossovellukset ja -kaupat
- **Uutiset ja media** — uutisportaalit, blogit, aikakauslehdet
- **Sosiaaliset verkostot** — some-syötteet ja viestintä
- **Tuottavuus** — tehtävienhallinta, muistiinpanosovellukset
- **Matkailu ja majoitus** — varaukset, liput, oppaat

## PWA vs natiivisovellus

| Ominaisuus | PWA | Natiivisovellus |
|---|---|---|
| Asennus | Selaimesta (Add to Home Screen) | Sovelluskaupasta / Play Storesta |
| Alusta | Toimii millä tahansa selainlaitteella | Alustakohtainen |
| Offline-tuki | Kyllä (Service Workerin kautta) | Kyllä |
| Päivitykset | Automaattiset | Manuaaliset, sovelluskaupan kautta |
| Kustannus | Halvempi kehittää | Kalliimpi kehittää |
| Suorituskyky | Korkea (lähes natiivi) | Korkein |

## PWA:n elinkaari

```
Install (service worker asennetaan) → Cache (resurssit välimuistitetaan offline-käyttöä varten)
  → Fetch (sovellus hakee cachesta tai verkosta) → Update (service worker päivittyy taustalla)
```

## Muista

PWA:t täytyy tarjota HTTPS:n kautta turvallisuuden ja yksityisyyden varmistamiseksi. Service Worker API on Progressive Web Appin ydin — se mahdollistaa offline-tuen, välimuistituksen ja taustasynkronoinnin.
