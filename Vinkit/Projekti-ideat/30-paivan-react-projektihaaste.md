<!-- tags: vinkit, projekti-ideat -->

# 30 päivän React-projektihaaste

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

30 päivän React-oppimisen jälkeen — kolme projekti-ideaa, joilla harjoitella oikeaa, tuotantotasoista React-osaamista aloittelijasta edistyneelle.

## 1. Task Manager App (aloittelijataso)

Rakenna tehtävälista, jossa on tehtävien lisäys/muokkaus/poisto, valmiiksi merkitseminen, suodattimet ja `localStorage`-tallennus. Harjoittelee komponentteja, propseja, `useState`-hookia, lomakkeita ja listoja.

**Ominaisuudet:**
- Lisää / muokkaa / poista tehtäviä
- Merkitse valmiiksi
- Suodata (Kaikki / Aktiiviset / Valmiit)
- Pysyvä tallennus `localStorage`:en
- Siisti, responsiivinen käyttöliittymä

**Käytetyt tekniikat:** `useState`, Props, Lists, LocalStorage

## 2. E-Commerce Store (keskitaso)

Rakenna tuotelistaus, tuotesivut, ostoskori, kassaprosessi, haku, reititys, API-datan haku ja globaali tila Zustandin tai Contextin avulla.

**Ominaisuudet:**
- Tuotelistaus ja -tiedot
- Lisää ostoskoriin / poista
- Kassaprosessi (checkout flow)
- Haku ja suodattimet
- Globaali tila (Zustand/Context)
- Responsiivinen design

**Käytetyt tekniikat:** React Router, Zustand, API, Cart

## 3. SaaS Analytics Dashboard (edistynyt taso)

Rakenna autentikaatio, suojatut reitit, kaaviot, analytiikka, roolipohjaiset käyttöoikeudet, välimuisti (caching), lazy loading ja skaalautuva arkkitehtuuri esim. Redux Toolkitilla tai TanStack Queryllä.

**Ominaisuudet:**
- Autentikaatio ja roolit
- Suojatut reitit
- Analytiikka ja kaaviot
- Datan haku ja välimuistitus
- Lazy loading
- Skaalautuva arkkitehtuuri

**Käytetyt tekniikat:** Redux Toolkit, Charts, Query, Auth

## Koodiesimerkkejä eri tasoilta

```javascript
// Aloittelija → useState
const [tasks, setTasks] = useState([])

// Keskitaso → Zustand
const cart = useStore(state => state.cart)

// Edistynyt → Query
const { data } = useQuery({
  queryKey: ['analytics']
})
```

## Aloitus

```bash
npm create vite@latest react-project
# Valitse: React + JavaScript / TypeScript
# cd react-project && npm install && npm run dev
```

## Ehdotettu projektirakenne

```
src/
  app/
  features/
  pages/
  components/
  hooks/
  services/
```

## Hyvät käytännöt

- Rakenna ilman tutoriaalien suoraa kopiointia
- Keskity arkkitehtuuriin ja siistiin koodiin
- Deployaa jokainen projekti (esim. Netlifyyn)

## Yleisiä virheitä vältettäväksi

- Tutoriaaliriippuvuus (ei osaa rakentaa itsenäisesti)
- Aloittelijaprojektien ylisuunnittelu (overengineering)
- Skaalautuvuuden huomiotta jättäminen

Nämä kolme projektia simuloivat oikeita alan frontend-työnkulkuja junior-tasosta senior-tasolle: tehtävienhallinta, e-commerce-alustat, analytiikkajärjestelmät, SaaS-sovellukset ja yrityssovellukset.
