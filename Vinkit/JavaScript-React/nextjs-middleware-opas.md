<!-- tags: vinkit, javascript-react -->

# Next.js Middleware -opas

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Aja logiikkaa ennen pyyntöjen valmistumista ja suojaa reittejä helposti.

## Mihin middlewarea käytetään

- Suojaa reittejä (Protect Routes)
- Autentikoi käyttäjiä (Authenticate Users)
- Suodattaa pyyntöjä (Filter Requests)
- Parantaa suorituskykyä (Improve Performance)

## Yleiskuva middlewaren toiminnasta

**Request** → **Middleware** → **Response**, ja middleware voi laukaista **Route Protection** (reittisuojauksen) ennen vastauksen palauttamista.

## 1. Luo middleware.js

Middleware ajetaan ennen kuin pyyntö saavuttaa sivun.

```javascript
export function middleware(request) {
  return NextResponse.next();
}
```

### Projektirakenne

```
src/
├── middleware.js
└── app/
```

## 2. Lue pyynnön tiedot (Read Request Information)

```javascript
export function middleware(request) {
  const path = request.nextUrl.pathname;
  console.log(path);

  return NextResponse.next();
}
```

Kulku: Browser Request → Middleware → Route Path. Esimerkkipolkuja: `/dashboard`, `/profile`, `/admin`.

## 3. Autentikoinnin tarkistus (Authentication Check)

```javascript
const token = request.cookies.get("token");

if (!token) {
  return NextResponse.redirect(
    new URL("/login", request.url)
  );
}
```

Kulku: User Request → Check Token → **Allow Access (Continue)** tai **Redirect Login (/login)**.

## 4. Täsmää tiettyihin reitteihin (Match Specific Routes)

```javascript
export const config = {
  matcher: [
    "/dashboard/:path*",
    "/admin/:path*"
  ]
};
```

### Suojatut reitit vs. julkiset reitit

- **Protected Routes** (middleware sovellettu): `/dashboard/*`, `/admin/*`
- **Public Routes** (ei middlewarea): `/`, `/about`, `/contact`

## Middleware Flow (kokonaiskulku)

1. **Request** – käyttäjä tekee pyynnön.
2. **Middleware** – middleware-logiikka ajetaan.
3. **Authentication** – käyttäjän/tokenin varmennus.
   - **Allow** – jatka pyydettyyn reittiin.
   - **Redirect** – ohjaa kirjautumis- tai virhesivulle.
4. **Response** – sivu- tai API-vastaus palautetaan.

## Parhaat käytännöt

- Pidä middleware kevyenä.
- Vältä raskaita tietokantakyselyitä.
- Käytä reittitäsmääjiä (route matchers).
- Käsittele autentikointi varhaisessa vaiheessa.
- Ohjaa luvattomat käyttäjät uudelleen.
