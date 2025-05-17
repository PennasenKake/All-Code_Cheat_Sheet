// Luokat ja oliot (ES6-luokat)

// Luokan määrittely
class Henkilö {
  constructor(nimi, ika) {
    this.nimi = nimi;
    this.ika = ika;
  }

  esittäydy() {
    console.log(`Hei, olen ${this.nimi} ja olen ${this.ika} vuotta vanha.`);
  }
}

// Luodaan olio luokasta
const henkilö1 = new Henkilö("Matti", 40);
henkilö1.esittäydy(); // Hei, olen Matti ja olen 40 vuotta vanha.
