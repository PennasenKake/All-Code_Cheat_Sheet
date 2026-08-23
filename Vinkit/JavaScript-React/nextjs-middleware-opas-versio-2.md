<!-- tags: vinkit, javascript-react -->

# Next.js Middleware -opas (toinen versio)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Next.js Middleware mahdollistaa koodin ajamisen ennen pyynnön valmistumista. Se sijaitsee pyynnön ja vastauksen välissä.

## Middleware Flow (yleiskulku)

**User Request** → **Middleware (Runs First)** → **Route / API / Page** → **Response**

## Mikä on middleware?

Middleware ajetaan ennen pyynnön valmistumista. Sillä voi:

- Autentikoida käyttäjiä (Authenticate users)
- Valtuuttaa (Authorize, RBAC)
- Ohjata tai kirjoittaa uudelleen URL-osoitteita (Redirect or rewrite URLs)
- Käsitellä i18n:ää (kansainvälistys)
- Rajoittaa pyyntömäärää (Rate limiting)
- Lokittaa pyynnöt (Log requests)
- Havaita botit ja suojata reittejä

## Peruskoodinen middleware (middleware.js)

```javascript
// middleware.js
import { NextResponse } from 'next/server';

export function middleware(request) {
  console.log('Middleware Running');

  return NextResponse.next();
}
```

## Autentikointiesimerkki

```javascript
import { NextResponse } from 'next/server';

export function middleware(request) {
  const token = request.cookies.get('token');
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}
```

### Autentikoinnin kulku

Request → Check Token → Token? → **Yes** → Page, tai **No** → Redirect to /login.

## Role-Based Access Control (RBAC)

```javascript
import { NextResponse } from 'next/server';

export function middleware(request) {
  const role = request.cookies.get('role');
  const { pathname } = request.nextUrl;

  if (pathname.startsWith('/admin') && role !== 'admin') {
    return NextResponse.redirect(new URL('/403', request.url));
  }

  return NextResponse.next();
}
```

**Miten se toimii:** Jos käyttäjä yrittää päästä `/admin`-reitille ilman `admin`-roolia, hänet ohjataan `/403`-sivulle (Forbidden).

## Projektirakenne

```
my-app/
├── app/
├── pages/
├── middleware.js
├── next.config.js
└── package.json
```

## Pyynnön elinkaari (Request Lifecycle)

Request → Middleware → Route Handler → Server Component → Response

## Redirect-esimerkki

```javascript
import { NextResponse } from 'next/server';

export function middleware() {
  return NextResponse.redirect(
    new URL('/home', request.url)
  );
}
```

Redirect muuttaa URL-osoitteen selaimessa ja tekee uuden pyynnön.

## Rewrite-esimerkki

```javascript
import { NextResponse } from 'next/server';

export function middleware() {
  return NextResponse.rewrite(
    new URL('/new-page', request.url)
  );
}
```

Rewrite pitää URL-osoitteen samana selaimessa mutta tarjoilee eri sisältöä.

## Matcher-konfiguraatio

```javascript
export const config = {
  matcher: ['/dashboard/:path*'],
};
```

### Useita reittejä

```javascript
export const config = {
  matcher: [
    '/dashboard/:path*',
    '/admin/:path*',
    '/profile/:path*'
  ],
};
```

## Mukautettujen otsikoiden lisääminen (Add Custom Headers)

```javascript
import { NextResponse } from 'next/server';

export function middleware() {
  const response = NextResponse.next();
  response.headers.set('x-app-version', '1.0.0');
  return response;
}
```

Tulos: `x-app-version: 1.0.0`

## Pyynnön tietojen lukeminen (Access Request Information)

```javascript
export function middleware(request) {
  console.log('URL:', request.url);
  console.log('Pathname:', request.nextUrl.pathname);
  console.log('User-Agent:',
    request.headers.get('user-agent'));
  return NextResponse.next();
}
```

## Yleisiä käyttötapauksia

- **Authentication** – tarkista kirjautuminen ennen pääsyn sallimista.
- **Authorization** – salli käyttäjärooleihin perustuen.
- **Internationalization** – ohjaa käyttäjän suosimalle kielelle.
- **Analytics** – seuraa pyyntöjä ja mittareita.
- **Bot Protection** – estä ei-toivotut botit tai scraperit.
- **Rate Limiting** – rajoita pyyntöjä väärinkäytön estämiseksi.

## Parhaat käytännöt

- Pidä middleware kevyenä.
- Vältä tietokantakyselyitä middlewaressa.
- Käytä evästeitä / JWT:tä autentikointitarkistuksiin.
- Käytä matcheria rajoittamaan suoritusta.
- Suorita raskas logiikka API-reiteissä.
- Käytä välimuistia (cache) mahdollisuuksien mukaan.

## Haastattelukysymyksiä

**K1: Mitä on Next.js Middleware?**
V: Middleware ajetaan ennen pyynnön valmistumista. Se voi muokata pyyntöjä, ohjata (redirect), kirjoittaa uudelleen (rewrite) tai lisätä otsikoita (headers).

**K2: Missä middleware ajetaan?**
V: Middleware ajetaan Edge Runtimessa, lähempänä käyttäjiä paremman suorituskyvyn saavuttamiseksi.

**K3: Mikä on ero Redirectin ja Rewriten välillä?**
V: Redirect muuttaa URL-osoitteen ja tekee uuden pyynnön. Rewrite pitää URL-osoitteen samana mutta tarjoilee eri sisältöä.

## Yhteenveto

Middleware on tehokas ominaisuus Next.js:ssä, joka auttaa hallitsemaan, suojaamaan ja optimoimaan jokaista pyyntöä.
