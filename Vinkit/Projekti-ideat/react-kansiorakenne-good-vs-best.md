<!-- tags: vinkit, projekti-ideat -->

# React-projektin kansiorakenne: "Good" vs "Best"

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Vertailu kahdesta tavasta järjestää React-projektin `src/`-kansio: yksinkertaisempi rakenne pienille projekteille ja skaalautuvampi, feature-pohjainen rakenne suurille tuotantosovelluksille.

## "Good" rakenne — hyvä pieniin projekteihin

```
src/
  components/
    Navbar.jsx
    Footer.jsx
    Button.jsx
  pages/
    Home.jsx
    About.jsx
    Contact.jsx
  assets/
    images/
    icons/
  App.jsx
  main.jsx
```

**Plussat:**
- Helppo ymmärtää
- Nopea aloittaa
- Sopii hyvin aloittelijoille

**Miinukset:**
- Ei skaalaudu hyvin
- Komponentit menevät sekaisin projektin kasvaessa
- Vaikea ylläpitää suurissa projekteissa

## "Best" rakenne — tuotantovalmis ja skaalautuva

```
src/
  assets/
    images/
    icons/
    fonts/
  components/
    common/
      Button/
      Input/
      Modal/
    layout/
      Navbar/
      Sidebar/
      Footer/
  features/
    auth/
      components/
      services/
      hooks/
      pages/
    products/
    users/
  hooks/
    useAuth.js
    useFetch.js
  services/
    api.js
    axios.js
  store/
    redux/
    context/
  routes/
    index.jsx
  utils/
    helpers.js
    constants.js
  styles/
    global.css
  App.jsx
  main.jsx
```

**Plussat:**
- Skaalautuva
- Helppo ylläpitää
- Tiimityöhön sopiva
- Feature-pohjainen arkkitehtuuri
- Käytössä oikeissa tuotantoprojekteissa

**Miinukset:**
- Enemmän alkuasetusta
- Voi tuntua monimutkaiselta pienissä projekteissa

## Nyrkkisääntö projektin koon mukaan

| Projektin tyyppi | Suositeltu rakenne |
|---|---|
| Portfolio-sivusto | Good |
| Landing page | Good |
| Admin dashboard | Best |
| E-commerce-sovellus | Best |
| SaaS-sovellus | Best |
| Yrityssovellus | Best |

## Tärkein huomio

Aloittelijoiden yleisin virhe on organisoida koodi vain tiedostotyypin mukaan (components, pages, css). Ammattitiimit organisoivat koodin sen sijaan feature-/domain-pohjaisesti (esim. `auth`, `products`, `users`, `dashboard`), koska se skaalautuu paljon paremmin sovelluksen kasvaessa.
