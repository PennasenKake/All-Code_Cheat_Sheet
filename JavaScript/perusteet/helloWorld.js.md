<!-- tags: javascript -->

# helloWorld.js

[Näytä alkuperäinen tiedosto GitHubissa](JavaScript/perusteet/helloWorld.js)

```javascript


// PERUS

<>
    
    <script type="text/javascript">
        // On page script
    </script>
    <script src="filenames.js"></script> // included external js file

</>        

// FUNKTIOT
function addNumberes(a, b) {
    return a + b;
}

// KOMMENTOINTI
/* USEAMPI RIVI */

// YKSI RIVI


console.log(a);
document.writer(a);
alert(a);
confirm("Are you sure");
prompt("Are you sure");



// DATA TYYPIT 

var age = 18;                               // numerot
var name = "John Doe";                      // merkkijono
var name = {first: "John", last: "Doe"};    // objekti
var truth = false;                          // boolean
var sheets = ["HTML", "CSS", "JS"];         // array of sheets
var a; typeof a;                            // undifined
var a = null;                               // value null


// IF -ELSE STATEMENT

if ((age >= 14 ) && (age < 19))             // looginen ehto
{
    status = "Eligible.";                   // executed if condition is true
} else {                                    // else block is optional
    status = "Not eligible.";               // executed if condition is false
}



// JavaScript Loops

// for loop

for (var i = 0; i < 10; i++) {
    document.write( i + <br />);
}

// while loop

var i = 1;
while (i < 100) {
    i *= 2;
    document.write(i + ", " + <br /> );
}

// do-while loop

var i = 1;
do {
    i *= 2;
    document.write(i + ", " + <br /> );
} while (i < 100);



// JavaScript-Stringimetodit ja -ominaisuudet

// Esimerkit ja selitykset:

var abc = "abcdefghijklmnopqrstuvwxyz";

// Escape-merkkien käyttö
var esc = 'I don\'t \n know';           // \n = uusi rivi

// Merkkijonon pituuden hakeminen
var len = abc.length;                  // Merkkijonon pituus

// Osajonon etsintä ja sijainti
abc.indexOf("lmno");                   // Osajonon ensimmäinen esiintyminen
abc.lastIndexOf("lmno");               // Osajonon viimeinen esiintyminen

// Merkkijonon osan leikkaaminen
abc.slice(3, 6);                       // Leikkaa "def"

abc.replace("abc", "123");             // Korvaa osajonon toisella

// Muunnokset isoihin ja pieniin kirjaimiin
abc.toUpperCase();                     // Isoiksi kirjaimiksi
abc.toLowerCase();                     // Pieniksi kirjaimiksi

// Merkkijonojen yhdistäminen
abc.concat(" ", str2);                 // abc + " " + str2

// Yksittäisen merkin käyttö
abc.charAt(2);                         // Merkki indeksissä: "c"
abc[2];                                // Ei suositeltava, abc[2] = "C" ei toimi

// Merkkikoodi
abc.charCodeAt(2);                     // Merkin koodi indeksissä: "c" -> 99

// Pilkkominen
abc.split(",");                        // Pilkkoo pilkkujen perusteella
abc.split("");                         // Pilkkoo merkkien perusteella

// Numeron muuntaminen merkkijonoksi tietyssä kannassa
128..toString(16);                     // Muuntaa numeron heksadesimaaliseksi (16)



// JavaScript-numerometodit:

var pi = 3.141;  

// Pyöristys tiettyyn desimaaliin
pi.toFixed(0);         // Palauttaa "3"  
pi.toFixed(2);         // Palauttaa "3.14"  

// Tarkkuuden määrittäminen
pi.toPrecision(2);     // Palauttaa "3.1"  

// Numeron arvon palauttaminen
pi.valueOf();          // Palauttaa numeron itse  

// Tyyppimuunnokset
Number(true);          // Muuntaa numeroksi (1 tai 0)  
Number(new Date());    // Muuntaa millisekunnit vuodesta 1970 numeroksi  

// Merkkijonosta numeron erottaminen
parseInt("3 months");  // Palauttaa ensimmäisen numeron: "3"  
parseFloat("3.5 days");// Palauttaa "3.5"  

// Numeron maksimi- ja minimiarvot
Number.MAX_VALUE;      // Suurin mahdollinen JS-numero  
Number.MIN_VALUE;      // Pienin mahdollinen JS-numero  

// Äärettömyyteen liittyvät arvot
Number.NEGATIVE_INFINITY; // Negatiivinen äärettömyys  
Number.POSITIVE_INFINITY; // Positiivinen äärettömyys  



// JavaScript - Taulukkometodit (Arrays)

const fruits = ['🍎', '🍌', '🍓', '🍊', '🍏'];

// Muuntaa taulukon merkkijonoksi
fruits.toString(); // '🍎,🍌,🍓,🍊,🍏'

// Lisää elementin taulukon loppuun
fruits.push('🍍'); // ['🍎', '🍌', '🍓', '🍊', '🍏', '🍍']

// Poistaa viimeisen elementin taulukosta
fruits.pop(); // '🍍'

// Tarkistaa, sisältääkö taulukko tietyn elementin
fruits.includes('🍌'); // true

// Palauttaa elementin indeksin
fruits.indexOf('🍊'); // 3

// Yhdistää taulukon elementit annetulla erottimella
fruits.join('+'); // '🍎+🍌+🍓+🍊+🍏'

// Palauttaa osan taulukosta
fruits.slice(1, 3); // ['🍌', '🍓']

// Lisää elementtejä taulukkoon
fruits.splice(1, 0, '🍍'); // ['🍎', '🍍', '🍌', '🍓', '🍊', '🍏']


// JavaScript - Olioiden käsittely (Objects)

const person = {
    name: 'John',
    age: 30,
    gender: 'male',
  };
  
  const jobObject = {
    job: 'developer',
    salary: 1000,
  };
  
  // Hae kaikki olion avaimet
  Object.keys(person); // ['name', 'age', 'gender']
  
  // Hae kaikki olion arvot
  Object.values(person); // ['John', 30, 'male']
  
  // Hae kaikki olion avain-arvo-parit
  Object.entries(person); // [ ['name', 'John'], ['age', 30], ['gender', 'male'] ]
  
  // Yhdistä kaksi oliota
  Object.assign(person, jobObject);
  // Lopputulos: {name: 'John', age: 30, gender: 'male', job: 'developer', salary: 1000}


// JavaScript - Scope (Muuttujien näkyvyys)

/* Global scope */
const PIE = 3.14;

function foo() {
    console.log(PIE); // 3.14

    /* Function scope */
    const age = 32;
    console.log(age); // 32
}

/* Block scope */
if (true) {
    const fullName = 'John Doe';
    console.log(fullName); // John Doe
}

console.log(PIE); // 3.14
console.log(age); // ReferenceError: age is not defined
console.log(fullName); // ReferenceError: fullName is not defined



// JavaScript - Date ja Time

// Luodaan uusi päivämääräobjekti
const date = new Date(); // Esim. "2023-01-22T09:44:48.175Z"

// Päivämääräkomponenttien hakeminen
date.getDate();            // Päivä: 22
date.getMonth();           // Kuukausi (0-indeksi): 0
date.getFullYear();        // Vuosi: 2023
date.getHours();           // Tunnit: 9
date.getMinutes();         // Minuutit: 44
date.getSeconds();         // Sekunnit: 48
date.getMilliseconds();    // Millisekunnit: 175
date.getTime();            // Ajanhetki (millisekunnit Epochista): 1648101488175

// Päivämääräkomponenttien asettaminen
date.setDate(23);          // Aseta päivä: 23
date.setMonth(3);          // Aseta kuukausi: 3 (huhtikuu)
date.setFullYear(2024);    // Aseta vuosi: 2024
date.setHours(10);         // Aseta tunti: 10
date.setMinutes(45);       // Aseta minuutit: 45
date.setSeconds(49);       // Aseta sekunnit: 49
date.setMilliseconds(176); // Aseta millisekunnit: 176
date.setTime(1648101488176); // Aseta aikaleima: 1648101488176



// JavaScript - Tapahtumat (Events)


// <!-- Käyttäjän klikkaus -->
<>
    // JavaScript - Tapahtumat (Events)
    //  Käyttäjän klikkaus
    <input type="text" onclick="myFunction()" />
    //  Kaksoisklikkaus 
    <input type="text" ondblclick="myFunction()" />
    //  Hiiren alas painaminen 
    <input type="text" onmousedown="myFunction()" />
    //  Fokus pois elementistä 
    <input type="text" onblur="myFunction()" />
    //  Fokus elementissä 
    <input type="text" onfocus="myFunction()" />
    //  Hiiren liikkuminen elementin päälle 
    <input type="text" onmouseover="myFunction()" />
    //  Hiiren liikkuminen elementin ulkopuolelle 
    <input type="text" onmouseout="myFunction()" />
    //  Muutos tapahtumassa 
    <input type="text" onchange="myFunction()" />
    //  Näppäimen painaminen 
    <input type="text" onkeydown="myFunction()" />
    //  Näppäimen vapauttaminen 
    <input type="text" onkeyup="myFunction()" />
    //  Näppäimen painaminen ja pysyminen 
    <input type="text" onkeypress="myFunction()" />
    //  Lomakkeen lähetys 
    <form onsubmit="myFunction()"></form>
    //  Lomakkeen nollaus 
    <form onreset="myFunction()"></form>
    //  Tekstin valinta 
    <input type="text" onselect="myFunction()" /></>



// JavaScript - Async/Await

// Asynkronisen funktion määrittäminen
async function getWeatherData() {
    try {
      // Await odottaa, että fetch-pyyntö palauttaa tuloksen
      const res = await fetch('https://jsonplaceholder.typicode.com/posts');
      const data = await res.json();
  
      // Palautetaan haettu data
      return data;
    } catch (err) {
      console.log(err); // Virheenkäsittely
    }
  }

  /*
    Selitys:
    async: Tekee funktiosta asynkronisen ja mahdollistaa await-avainsanan käytön sen sisällä.
    
    await: Keskeyttää koodin suorituksen, kunnes lupaus (promise) palauttaa tuloksen. 
    Tämä tekee asynkronisesta koodista helpommin luettavaa ja hallittavaa.
    
    fetch: Käytetään tietojen hakemiseen verkosta. Se palauttaa lupauksen (promise), joka sisältää vastauksen.
  */ 


    
// JavaScript - Virheenkäsittely (Error Handling)

/* Try-Catch Block */
function foo() {
    try {
      // Koodi, joka voi aiheuttaa virheen
      console.log("Kaikki toimii hyvin!");
    } catch (e) {
      // Käsittele virhe
      console.error("Virhe tapahtui:", e);
    } finally {
      // Suoritetaan aina, riippumatta siitä tapahtuiko virhe vai ei
      console.log("Käsittely valmis.");
    }
  }
  
  /* Globaalien lupausten virheet */
  window.addEventListener("unhandledrejection", function(event) {
    console.error("Virheellinen lupaus:", event.reason);
  });
  
  /* Heitä virhe omassa koodissa */
  function checkAge(age) {
    if (age < 18) {
      throw new Error("Ikä ei täytä vaatimusta.");
    }
    console.log("Ikä hyväksytty.");
  }
  

/* 
    Selitys:
    try-catch-finally: Käytetään virheiden löytämiseen ja käsittelemiseen. 
    finally-lohkoa voidaan käyttää vapauttamaan resursseja tai suorittamaan jälkikäsittelyä.

    unhandledrejection: Mahdollistaa virheiden kuuntelun lupauksista, joilla ei ole virheenkäsittelyä.

    throw: Käytetään virheen pakottamiseen ohjelmassa, kun halutaan ilmaista, että jotain meni pieleen.
*/
```
