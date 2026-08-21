<!-- tags: javascript -->

# object_basics.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/perusteet/object_basics.js)

```javascript
// Olio (object)
let henkilö = {
  nimi: "Matti",
  ikä: 30,
  tervehti: function() {
    console.log("Hei, olen " + this.nimi);
  }
};

// Pääsy ominaisuuksiin
console.log(henkilö.nimi);
henkilö.tervehti();
```
