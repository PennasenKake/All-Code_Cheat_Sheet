<!-- tags: javascript -->

# callbacks.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/perusteet/callbacks.js)

```javascript
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
```
