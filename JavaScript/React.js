

// React - KOMPONENTIT JA PROPS 

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


