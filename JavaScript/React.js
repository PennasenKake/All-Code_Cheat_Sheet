

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



/* */
/* */

