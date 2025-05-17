

// React - KOMPONENTIT JA PROPS 
// --------------------------------------------------------------------------
// 1. Map-elementit (Listojen renderöinti)
// --------------------------------------------------------------------------

/*
Map-funktiota käytetään yleisesti Reactissa listojen renderöintiin.
Se iteroi taulukon läpi ja luo jokaiselle elementille uuden JSX-elementin.
'key'-prop on tärkeä antaa jokaiselle listan elementille, jotta React voi
tehokkaasti päivittää ja uudelleenrenderöidä niitä. Yleensä 'key' on
elementin uniikki ID tai indeksi, jos uniikkeja ID:itä ei ole.
*/

const mapElementsEsimerkki = () => {
  const elementit = [
    { id: 1, nimi: 'yksi', arvo: 10 },
    { id: 2, nimi: 'kaksi', arvo: 20 },
    { id: 3, nimi: 'kolme', arvo: 30 }
  ];

  return (
    <ul>
      {elementit.map((element) => (
        <li key={element.id}> // Käytetään elementin ID:tä 'key'-proppina
          Arvo nimelle {element.nimi} on {element.arvo}
        </li>
      ))}
    </ul>
  );
};

// --------------------------------------------------------------------------
// 2. CSS Reactissa
// --------------------------------------------------------------------------

/*
Reactissa CSS:ää voidaan tuoda moduulina (.module.css) tai perinteisenä .css-tiedostona.
Tuotaessa perinteisenä tiedostona, tyylit ovat globaaleja. CSS-moduulit luovat
paikallisia tyyliluokkia, mikä ehkäisee nimitörmäyksiä eri komponenttien välillä.

Tässä esimerkissä oletetaan, että on olemassa 'Student.css'-tiedosto, joka sisältää
'.Student'-nimisen tyyliluokan.
*/

import './Student.css'; // Tuodaan globaalit tyylit

const cssReactEsimerkki = () => {
  return (
    <div className="Student"> // Käytetään 'Student.css'-tiedoston tyyliä
      Opiskelija Maija Meikäläinen
    </div>
  );
};

// Jos käytetään CSS-moduuleita:
// import styles from './Student.module.css';
// const cssModuleReactEsimerkki = () => {
//   return (
//     <div className={styles.student}> // Käytetään CSS-moduulin luomaa tyyliluokkaa
//       Opiskelija Maija Meikäläinen (moduulilla)
//     </div>
//   );
// };

// --------------------------------------------------------------------------
// 3. Tapahtumankuuntelijat (Event Listeners)
// --------------------------------------------------------------------------

/*
Reactissa tapahtumankuuntelijat lisätään elementteihin 'on'-alkuisilla propeilla
(esim. onClick, onChange, onSubmit). Tapahtumafunktio välitetään proppina.
Synteettinen tapahtumaobjekti (esim. 'event') välitetään tapahtumafunktiolle.
Tämä objekti on Reactin alusta-agnostinen wrapper selaimen natiivitapahtumien ympärillä.

'event.preventDefault()' estää selaimen oletustoiminnon (esim. linkin seuraamisen).
*/

const tapahtumankuuntelijaEsimerkki = () => {
  const handleClick = (event) => {
    event.preventDefault(); // Estää linkin oletustoiminnon
    alert('Hei Maailma!');
  };

  return (
    <div>
      <a href="/" onClick={handleClick}>
        Sano Hei
      </a>
    </div>
  );
};

// --------------------------------------------------------------------------
// 4. Reactin tila (React State)
// --------------------------------------------------------------------------

/*
Tila ('state') on React-komponentin muistia. Se on JavaScript-objekti, joka
sisältää komponentin muuttuvia tietoja. Kun tila muuttuu, komponentti
uudelleenrenderöityy.

'useState' on React Hook, jota käytetään funktionaalisissa komponenteissa tilan
hallintaan. Se palauttaa kaksi arvoa: nykyisen tilan ja funktion tilan päivittämiseen.
Tilapäivitykset ovat asynkronisia.
*/

const tilaEsimerkki = (props) => {
  const [nimi, setNimi] = useState(props.alkuNimi); // 'nimi' on tila, 'setNimi' on päivitysfunktio

  const paivitaNimi = () => {
    const uusiNimi = prompt('Mikä on nimesi?');
    if (uusiNimi) {
      setNimi(uusiNimi); // Päivitetään tilaa 'setNimi'-funktiolla
    }
  };

  return (
    <div>
      <h1>Hei, {nimi}</h1>
      <button onClick={paivitaNimi}>
        Päivitä Nimi
      </button>
    </div>
  );
};

// Komponentin käyttö: <TilaEsimerkki alkuNimi="Vieras" />

// --------------------------------------------------------------------------
// 5. React-lomakkeet (React Forms)
// --------------------------------------------------------------------------

/*
Reactissa lomakkeiden tilaa hallitaan yleensä komponentin tilan avulla.
Lomake-elementtien (esim. <input>, <textarea>, <select>) 'value'-proppi
on sidottu komponentin tilaan, ja 'onChange'-tapahtumankuuntelijaa käytetään
tilan päivittämiseen käyttäjän syöttäessä tietoja. Tätä kutsutaan "kontrolloiduiksi
komponenteiksi".

'onSubmit'-tapahtumankuuntelijaa käytetään lomakkeen lähetyksen käsittelyyn.
'event.preventDefault()' estää selaimen oletuslähetyksen.
*/

const lomakeEsimerkki = () => {
  const [kayttajatunnus, setKayttajatunnus] = useState('');
  const [salasana, setSalasana] = useState('');

  const kasitteleKayttajatunnusMuutos = (event) => {
    setKayttajatunnus(event.target.value);
  };

  const kasitteleSalasanaMuutos = (event) => {
    setSalasana(event.target.value);
  };

  const kasitteleLahetys = (event) => {
    event.preventDefault(); // Estää oletuslähetyksen
    alert(`Käyttäjätunnus: ${kayttajatunnus}, Salasana: ${salasana}`);
    // Tässä voisi olla koodia lomakkeen tietojen lähettämiseen
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

// HUOM: Muista tuoda React-kirjasto jokaisen komponenttitiedoston alkuun:
// import React, { useState } from 'react';


/*
Functional Components (Toiminnalliset komponentit):
Toiminnalliset komponentit ovat Reactin käyttöliittymän rakentamisen perusyksiköitä. 
*/
const MyComponent = (props) => {
    return <div>{props.message}</div>;
  };
  

/*
Destructuring Props (Propsien purkaminen):
Tehokas tapa käyttää prop-arvoja suoraan komponentin sisällä.
*/
const MyComponent1 = ({ message }) => {
    return <div>{message}</div>;
  };
  

/*
Default Props (Oletuspropsit):
Mahdollistaa oletusarvojen antamisen propseille. 
*/
MyComponent.defaultProps = {
    message: "Default Message",
  };

  


// REACT - HOOKS (USETSTATE, USEEFFECT, USECONTEXT)



/*
1. useState
Kuvaus: Mahdollistaa komponentin tilan hallinnan. Voit seurata ja päivittää tietoja komponentin sisällä.
Esimerkki: 
*/
const [count, setCount] = useState(0);


/*
2. useEffect
Kuvaus: Käytetään sivuvaikutusten hallintaan, 
kuten datan hakuun, tilauksen käsittelyyn tai siivouksen suorittamiseen.
Esimerkki: 
*/
useEffect(() => {
    // Sivuvaikutuslogiikka tässä
}, [dependencies]); // Luettelo riippuvuuksista
  
/*
3. useContext
Kuvaus: Jakaa tietoja komponenttien välillä ilman tarvetta viedä tietoa propseilla.
Esimerkki: 
*/
const value = useContext(MyContext);



// REACT - Advanced Hooks: useReducer, useCallback, useMemo, and useRef

/*
1. useReducer
Kuvaus: Tarjoaa rakenteellisen tavan hallita monimutkaisia tiloja. 
Käytetään usein, kun useState ei riitä tilapäivityksiin.
Esimerkki: */
const [state, dispatch] = useReducer(reducer, initialState);


/*
2. useCallback
Kuvaus: Memoisoi callback-funktion, 
jotta lapsikomponentit eivät renderöidy uudelleen tarpeettomasti.
Esimerkki: 
*/
const memoizedCallback = useCallback(() => {
    // callback logiikka
}, [dependencies]);
  
/*
3. useMemo
Kuvaus: Memoisoi laskennan tuloksen, estäen sen uudelleenlaskennan jokaisella renderöinnillä.
Esimerkki: 
*/
const value1 = useMemo(() => {
    return computeValue(a, b);
}, [a, b]);


/*
4. useRef
Kuvaus: Palauttaa olion, jossa on .current-property, 
jota voi käyttää säilyttämään muuttujia tai viittaamaan DOM-elementteihin.
Esimerkki: 
*/
const myRef = useRef(initialValue);



// REACT - Event Handling yhdistettynä useState-hookiin


/*
Tapahtumien käsittely
Tapa määritellä funktioita, jotka vastaavat tiettyihin käyttäjän vuorovaikutuksiin, 
kuten klikkauksiin, lomakkeen lähettämiseen ja syötteiden muutoksiin. 
*/
const handleClick = () => {
    // Käsittele klikkaustapahtuma
    console.log("Nappia klikattu!");
};
  



/*
useState tapahtumakäsittelyssä
Integroi tapahtumakäsittelijät useState-hookiin, 
jolloin voit päivittää komponentin tilaa dynaamisesti käyttäjän syötteen perusteella. 
*/
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

export default ExampleComponent;




/*
    Selitys:
    handleClick on yksinkertainen tapahtumakäsittelijä, joka reagoi klikkaustapahtumaan.

    handleChange päivittyy automaattisesti, kun käyttäjä muuttaa syötteitä.

    useState mahdollistaa tilan (state) hallinnan 
    ja sen dynaamisen muutoksen, esimerkiksi tekstikentän arvojen muuttuessa.
*/



// React - Conditional Rendering (Ehdollinen renderöinti)

/*
Ternary Operator
Kuvaus: Käytetään boolean-ehdon perusteella näyttämään joko yksi tai toinen komponentti.
Esimerkki:
*/
return isLogged ? <UserGreeting /> : <GuestGreeting />;


/*
Short Circuit Evaluation
Kuvaus: Käytetään boolean-ehdon perusteella näyttämään komponentti vain, jos ehto on tosi.
Esimerkki:
*/
return isLoggedIn && <UserGreeting />;



// React - Lists and Keys



/*
Rendering Lists
Listojen avulla voit helposti renderöidä useita komponentteja tehokkaasti.
Esimerkki: 
*/
const myList = [1, 2, 3];

const listItems = myList.map((item) => (
  <li key={item}>{item}</li>
));
/*
map-metodi: Luo uuden taulukon komponentteja iteroinnin perusteella.
Key-prop: Jokaisella listakomponentilla tulisi 
olla ainutlaatuinen key-prop nopeuttaaksesi renderöintiä ja estääksesi virheitä. 
*/


/*
Fragment Shorthand
Käytä fragmentteja välttääksesi turhaa HTML-elementtien pesittämistä.
Esimerkki: 
*/
return <>{listItems}</>;
// Fragmentit: <></>-lyhennemuoto toimii kuten <React.Fragment>.


/* */
/* */
/* */


