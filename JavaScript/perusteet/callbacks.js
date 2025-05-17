// Callback-funktiot

function teeJotain(callback) {
  console.log("Aloitetaan tehtävä");
  callback();  // Kutsutaan callback-funktiota
  console.log("Tehtävä suoritettu");
}

function tervehdys() {
  console.log("Hei! Tämä on callback-funktio.");
}

teeJotain(tervehdys);

/*
Tulostus:
Aloitetaan tehtävä
Hei! Tämä on callback-funktio.
Tehtävä suoritettu
*/
