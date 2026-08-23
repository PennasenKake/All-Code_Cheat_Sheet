<!-- tags: vinkit, jarjestelmasuunnittelu -->

# Micro Frontend -arkkitehtuuri

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Micro Frontend -arkkitehtuurilla rakennetaan skaalautuvia frontend-sovelluksia itsenäisten tiimien avulla.

## Mikä on Micro Frontend?

Micro Frontend on arkkitehtuurityyli, jossa suuri frontend-sovellus jaetaan pienempiin, itsenäisiin sovelluksiin, joita eri tiimit voivat kehittää, testata, julkaista ja ylläpitää erikseen. Ajattele sitä "mikropalveluina frontendille".

## Perinteinen monoliittinen frontend vs. Micro Frontend

**Perinteinen monoliittinen frontend:** yksi sovellus sisältää kaikki näkymät (Home, Products, Cart, Checkout, Profile) yhtenä kokonaisuutena.

**Micro Frontend -arkkitehtuuri:** Container/Host Application yhdistää erilliset tiimit ja sovellukset:

| Tiimi | Sovellus |
|-------|----------|
| Home Team | Home App |
| Product Team | Product App |
| Cart Team | Cart App |
| Checkout Team | Checkout App |
| Profile Team | Profile App |

## Miksi käyttää Micro Frontendejä?

1. **Itsenäinen kehitys** – eri tiimit voivat työskennellä samanaikaisesti (Team A: Home, Team B: Products, Team C: Cart, Team D: Checkout).
2. **Itsenäinen julkaisu** – voit julkaista vain muuttuneen moduulin (esim. päivitä Product-moduuli → julkaise vain Product-moduuli).
3. **Teknologiavapaus** – eri tiimit voivat käyttää eri kehyksiä (esim. Home: React, Products: Angular, Cart: Vue, Profile: React) — "polyglot frontend".
4. **Skaalautuvuus** – suuria sovelluksia on helpompi hallita. Sopii mm. verkkokauppoihin, pankkiportaaleihin, SaaS-alustoihin ja yrityssovelluksiin.

## Esimerkki käytännöstä: Amazon

Eri tiimit vastaavat eri osista: Navbar Team, Search Team, Product Team, Cart Team, Checkout Team, Recommendation Team. Jokainen osio voidaan kehittää itsenäisesti.

## Micro Frontend -lähestymistavat

1. **Build-Time Integration** – paketit jaetaan npm:n kautta. Plussat: yksinkertainen, nopea. Miinukset: vaatii uudelleenkäännöksen, tiukka kytkentä (tight coupling).
2. **Runtime Integration** – sovellukset ladataan dynaamisesti. Tämä on nykyään suosituin lähestymistapa.
3. **Iframe-pohjainen** – `<iframe src="app.com"></iframe>`. Plussat: täydellinen eristys. Miinukset: huono kommunikointi, SEO-ongelmat, suorituskykyhaittaa.

## Webpack Module Federation

Suosittu Micro Frontend -ratkaisu, joka esiteltiin Webpack 5:ssä.

### Host Application

```javascript
new ModuleFederationPlugin({
  name: "host",
  remotes: {
    products: "products@http://localhost:3001/remoteEntry.js"
  }
});
```

### Remote Application

```javascript
new ModuleFederationPlugin({
  name: "products",
  filename: "remoteEntry.js",
  exposes: {
    "./ProductList": "./src/ProductList"
  }
});
```

### Käyttö

```javascript
import ProductList from "products/ProductList";
```

Komponentti latautuu dynaamisesti.

## Projektirakenne

```
microfrontend-project/
├── host-app/
├── product-app/
├── cart-app/
├── checkout-app/
└── profile-app/
```

Jokainen sovellus sisältää: `src/`, `public/`, `package.json`, `webpack.config.js`.

## Kommunikointi Micro Frontendien välillä

1. **Custom Events**

```javascript
// Lähetä tapahtuma
window.dispatchEvent(
  new CustomEvent("cartUpdated", {
    detail: { count: 5 }
  })
);

// Vastaanota tapahtuma
window.addEventListener("cartUpdated", (event) => {
  console.log(event.detail);
});
```

2. **Jaettu tila (Shared State)** — Redux, Context API, Zustand, RxJS:

```javascript
store.dispatch(addToCart());
```

3. **URL-reititys** — reititys toimii kommunikointikeinona: `/products`, `/cart`, `/profile`.

## Haasteet

1. **Jaetut riippuvuudet** – Ongelma: sovellus A käyttää React 18:aa, sovellus B React 19:aa. Ratkaisu: Module Federation Shared Dependencies.
2. **Tyylikonfliktit** – Ongelma: `.button { color: red; }` vs. `.button { color: blue; }`. Ratkaisu: CSS Modules, Tailwind CSS, Shadow DOM.
3. **Suorituskyky** – Liian monta mikrosovellusta voi lisätä verkkopyyntöjä, bundle-kokoa ja latausaikaa.
4. **Tilanhallinta** – Tilan jakaminen sovellusten välillä muuttuu monimutkaiseksi. Tarvitaan Event Bus, Shared Store tai API-pohjainen synkronointi.

## Parhaat käytännöt

- Pidä Micro Frontendit itsenäisinä (kommunikoivat vain Hostin kautta).
- Erillinen omistajuus (Team Product → Product App, Team Cart → Cart App, jne.).
- Jaa vain tarpeelliset kirjastot (esim. `shared: { react: { singleton: true }, "react-dom": { singleton: true } }`).
- Käytä CI/CD-putkea: Code Push → Build → Test → Deploy.

## Edut

- Itsenäiset tiimit
- Nopeampi kehitys
- Itsenäinen julkaisu
- Parempi skaalautuvuus
- Teknologiajoustavuus
- Helpompi ylläpito

## Haitat

- Monimutkaisempi arkkitehtuuri
- Jaetun tilan haasteet
- Riippuvuuksien hallintaongelmat
- Suorituskykyhaittaa
- Virheenjäljitys voi olla vaikeaa

## Milloin käyttää Micro Frontendejä?

- Useat tiimit työskentelevät samalla tuotteella.
- Sovellus on hyvin laaja.
- Tarvitaan itsenäisiä julkaisuja.
- Eri teknologiat/kehykset ovat välttämättömiä.
- Projekti noudattaa mikropalveluarkkitehtuuria.

**Vältä Micro Frontendejä pienissä projekteissa** — lisääntynyt monimutkaisuus yleensä ylittää hyödyt.

### Haastattelumääritelmä

Micro Frontend on arkkitehtuuri, joka jakaa suuren frontend-sovelluksen pienempiin, itsenäisesti julkaistaviin ja ylläpidettäviin frontend-sovelluksiin. Jokaisen micro frontendin omistaa erillinen tiimi, ja niitä voidaan kehittää, testata ja julkaista itsenäisesti, samalla kun ne integroituvat yhdeksi käyttäjäkokemukseksi.
