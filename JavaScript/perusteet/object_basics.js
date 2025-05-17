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
