# JavaScript Cheat Sheet insinööreille

Tämä cheat sheet on suunniteltu insinööreille, jotka haluavat hyödyntää JavaScriptiä ja Reactia sovellusten kehittämiseen, datan käsittelyyn ja automatisointiin. Sisältää perus- ja React-ominaisuuksia, esimerkkejä ja vinkkejä.

## Sisällysluettelo
- [Pika-aloitus](#pika-aloitus)
- [1. Perus-JavaScript](#1-perus-javascript)
- [2. React-komponentit ja props](#2-react-komponentit-ja-props)
- [3. React-Hookit](#3-react-hookit)
- [4. Tapahtumakäsittely](#4-tapahtumakäsittely)
- [5. Ehdollinen renderöinti](#5-ehdollinen-renderöinti)
- [6. Listat ja avaimet](#6-listat-ja-avaimet)

## Pika-aloitus
JavaScript on monipuolinen kieli web-kehitykseen ja datan käsittelyyn. Aloita näillä vinkeillä:
- **Konsoli**: Käytä `console.log()` debuggaamiseen.
- **Muuttujat**: Käytä `let` ja `const` moderneissa projekteissa (`var` on vanhentunut).
- **Tiedostojen suoritus**: Suorita JavaScript-tiedostoja Node.js:llä: `node tiedosto.js`.
- **React-projekti**: Aloita React-projekti: `npx create-react-app projekti`.

## 1. Perus-JavaScript
Perusfunktiot ja rakenteet JavaScriptissä.

- **Muuttujat ja tietotyypit**:
  ```javascript
  let numero = 42; // Numero
  const nimi = "Projekti X"; // Merkkijono
  let onKaynnissa = true; // Totuusarvo
  let mittaukset = [10, 20, 30]; // Taulukko
  let projekti = { id: 1, nimi: "Rakennus A", arvo: 5000 }; // Objekti


  Funktiot:

// Tavallinen funktio
function laskePintaAla(pituus, leveys) {
  return pituus * leveys;
}
console.log(laskePintaAla(5, 3)); // 15

// Nuolifunktio
const summa = (a, b) => a + b;
console.log(summa(10, 20)); // 30

Taulukoiden käsittely:

const mittaukset = [10, 20, 30, 40];
// Map: Muuntaa arvot
const tuplattu = mittaukset.map(x => x * 2); // [20, 40, 60, 80]
// Filter: Suodattaa arvot
const yli20 = mittaukset.filter(x => x > 20); // [30, 40]
// Reduce: Laskee summan
const kokonaissumma = mittaukset.reduce((sum, x) => sum + x, 0); // 100

Insinöörisovellus: Mittaustulosten keskiarvo:

const lampotilat = [22.5, 23.1, 21.9, 22.8];
const keskiarvo = lampotilat.reduce((sum, x) => sum + x, 0) / lampotilat.length;
console.log(`Keskiarvo: ${keskiarvo} °C`); // Keskiarvo: 22.575 °C



2. React-komponentit ja props

2.1 Map-elementit (Listojen renderöinti)
map-funktiota käytetään Reactissa listojen renderöintiin. Jokaiselle listan elementille annetaan uniikki key-proppi.

const MapElementsEsimerkki = () => {
  const elementit = [
    { id: 1, nimi: "yksi", arvo: 10 },
    { id: 2, nimi: "kaksi", arvo: 20 },
    { id: 3, nimi: "kolme", arvo: 30 },
  ];

  return (
    <ul>
      {elementit.map((element) => (
        <li key={element.id}>
          Arvo nimelle {element.nimi} on {element.arvo}
        </li>
      ))}
    </ul>
  );
};

2.2 CSS Reactissa
CSS voidaan tuoda globaalisti tai moduuleina (.module.css). Moduulit estävät nimitörmäyksiä.

import "./Student.css"; // Globaali CSS

const CssReactEsimerkki = () => {
  return <div className="Student">Opiskelija Maija Meikäläinen</div>;
};

// Moduuli-CSS (kommentoitu esimerkki)
// import styles from './Student.module.css';
// const CssModuleReactEsimerkki = () => {
//   return <div className={styles.student}>Opiskelija Maija Meikäläinen (moduulilla)</div>;
// };


2.3 Tapahtumankuuntelijat
Reactissa tapahtumat lisätään on-propeilla (esim. onClick). event.preventDefault() estää oletustoiminnot.

const TapahtumankuuntelijaEsimerkki = () => {
  const handleClick = (event) => {
    event.preventDefault();
    alert("Hei Maailma!");
  };

  return (
    <div>
      <a href="/" onClick={handleClick}>
        Sano Hei
      </a>
    </div>
  );
};



2.4 Reactin tila (useState)
useState Hook hallitsee komponentin tilaa. Tila päivittyy asynkronisesti.

import React, { useState } from "react";

const TilaEsimerkki = ({ alkuNimi = "Vieras" }) => {
  const [nimi, setNimi] = useState(alkuNimi);

  const paivitaNimi = () => {
    const uusiNimi = prompt("Mikä on nimesi?");
    if (uusiNimi) setNimi(uusiNimi);
  };

  return (
    <div>
      <h1>Hei, {nimi}</h1>
      <button onClick={paivitaNimi}>Päivitä Nimi</button>
    </div>
  );
};


2.5 React-lomakkeet
Kontrolloidut komponentit hallitsevat lomakkeiden tilaa useState:lla.

import React, { useState } from "react";

const LomakeEsimerkki = () => {
  const [kayttajatunnus, setKayttajatunnus] = useState("");
  const [salasana, setSalasana] = useState("");

  const kasitteleKayttajatunnusMuutos = (event) => {
    setKayttajatunnus(event.target.value);
  };

  const kasitteleSalasanaMuutos = (event) => {
    setSalasana(event.target.value);
  };

  const kasitteleLahetys = (event) => {
    event.preventDefault();
    alert(`Käyttäjätunnus: ${kayttajatunnus}, Salasana: ${salasana}`);
  };

  return (
    <form onSubmit={kasitteleLahetys}>
      <label>
        Käyttäjätunnus:
        <input
          type="text"
          value={kayttajatunnus}
          onChange={kasitteleKayttajatunnusMuutos}
        />
      </label>
      <br />
      <label>
        Salasana:
        <input
          type="password"
          value={salasana}
          onChange={kasitteleSalasanaMuutos}
        />
      </label>
      <br />
      <button type="submit">Kirjaudu</button>
    </form>
  );
};


2.6 Toiminnalliset komponentit ja propsit

// Toiminnallinen komponentti
const MyComponent = ({ message = "Default Message" }) => {
  return <div>{message}</div>;
};

// Propsien purkaminen
const MyComponent1 = ({ message }) => {
  return <div>{message}</div>;
};


3. React-Hookit

3.1 useState
Hallitsee komponentin tilaa.

const [count, setCount] = useState(0);

3.2 useEffect
Hallitsee sivuvaikutuksia (esim. datan haku).


import React, { useEffect } from "react";

useEffect(() => {
  // Sivuvaikutus, esim. datan haku
  console.log("Komponentti renderöity");
}, []); // Tyhjä riippuvuuslista: suoritetaan vain kerran


3.3 useContext
Jakaa tietoja komponenttien välillä.

import React, { useContext, createContext } from "react";

const MyContext = createContext();

const EsimerkkiKomponentti = () => {
  const value = useContext(MyContext);
  return <div>{value}</div>;
};


3.4 Edistyneet Hookit

useReducer: Monimutkainen tilanhallinta.
javascript

const [state, dispatch] = useReducer(reducer, initialState);

useCallback: Memoisoi callback-funktion.
javascript

const memoizedCallback = useCallback(() => {
  // Callback-logiikka
}, [dependencies]);

useMemo: Memoisoi laskennan tuloksen.
javascript

const value = useMemo(() => computeValue(a, b), [a, b]);

useRef: Säilyttää muuttujia tai viittaa DOM-elementteihin.
javascript

const myRef = useRef(initialValue);


4. Tapahtumakäsittely

4.1 Perustapahtumat
javascript

const handleClick = () => {
  console.log("Nappia klikattu!");
};


4.2 Tapahtumat ja useState

import React, { useState } from "react";

const ExampleComponent = () => {
  const [inputValue, setInputValue] = useState("");

  const handleChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={handleChange}
        placeholder="Kirjoita jotain..."
      />
      <p>Syötit: {inputValue}</p>
    </div>
  );
};


5. Ehdollinen renderöinti

5.1 Ternary-operaattori
javascript

const isLogged = true;
return isLogged ? <UserGreeting /> : <GuestGreeting />;

5.2 Short Circuit Evaluation
javascript

const isLoggedIn = true;
return isLoggedIn && <UserGreeting />;

6. Listat ja avaimet
6.1 Listojen renderöinti
javascript

const myList = [1, 2, 3];
const listItems = myList.map((item) => <li key={item}>{item}</li>);

6.2 Fragmentit
javascript

return <>{listItems}</>;

