// muuttujien määrittely ja tyypit

// var, let ja const erot
var x = 5;         // Vanha tapa, voi aiheuttaa ongelmia
let y = 10;        // Suositeltu muuttuja, voi muuttua
const z = 15;      // Vakio, ei voi muuttaa arvoa

// eri tietotyypit
let nimi = "Matti";          // merkkijono (string)
let ika = 30;                // numero (number)
let totuus = true;           // boolean (true tai false)
let tyhja = null;            // tyhjä arvo
let määrittelemätön;          // undefined

console.log(typeof nimi);    // string
console.log(typeof ika);     // number
console.log(typeof totuus);  // boolean
console.log(typeof tyhja);   // object (JavaScriptin erikoisuus)
console.log(typeof määrittelemätön); // undefined
