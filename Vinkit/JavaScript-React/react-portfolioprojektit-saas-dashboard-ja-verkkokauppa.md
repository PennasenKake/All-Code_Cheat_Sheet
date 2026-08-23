<!-- tags: vinkit, javascript-react -->

# React-portfolioprojektit: SaaS dashboard ja verkkokauppa

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Osa "Projects 01–02" -sarjaa. Kaksi portfoliokelpoista React-projektia, jotka osoittavat uudelleenkäytettäviä komponentteja, tilanhallintaa, datankäsittelyä ja viimeistellyn käyttöliittymän osaamista.

## Projekti 01: SaaS Analytics Dashboard

Rakenna responsiivinen dashboard, joka näyttää liiketoimintamittareita, kaavioita, käyttäjiä, liikevaihtoa ja viimeisintä aktiviteettia.

**Mitä rakennat:**
- Responsiivinen sivupalkkinavigointi
- Mittari- ja tilastokortit
- Interaktiiviset kaaviot
- Haettava datataulukko

**Osoitettavat taidot:**
- Uudelleenkäytettävät React-komponentit
- Tila (state) ja propsit
- Datan visualisointi
- Responsiivinen dashboard-asettelu

**Portfolioarvo:** Osoittaa, että osaat rakentaa viimeisteltyjä, dataraskaita käyttöliittymiä, joita käytetään oikeissa SaaS-tuotteissa.

## Projekti 02: E-commerce Store

Rakenna täydellinen ostoskäyttöliittymä, jossa on tuotteet, suodattimet, ostoskorin tila ja kassaprosessi sekä responsiiviset sivut.

**Mitä rakennat:**
- Tuotelistaussivu
- Haku- ja kategoriasuodattimet
- Ostoskorin vetolaatikko (cart drawer)
- Tuotteen tiedot ja kassaprosessi

**Osoitettavat taidot:**
- Context tai tilanhallinta
- Dynaaminen reititys (dynamic routing)
- API-datan haku
- Lomake- ja ostoskorilogiikka

**Portfolioarvo:** Osoittaa oikeita käyttäjävirtoja, tilanhallintaa, uudelleenkäytettävää käyttöliittymää ja konversioon keskittyvää suunnittelua.

## Esimerkkikoodi (ostoskorin logiikka)

```jsx
const [cart, setCart] = useState([]);

const addToCart = (product) => {
  setCart((items) => [...items, product]);
};

const total = cart.reduce(
  (sum, item) => sum + item.price,
  0
);
```

## Yhteenveto

Dashboard todistaa käyttöliittymäosaamisen, verkkokauppa todistaa tilanhallinnan ja käyttäjävirtojen osaamisen.
