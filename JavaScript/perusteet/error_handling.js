// Virheenkäsittely
try {
  let tulos = jakolasku(10, 0); // määrittelemätön funktio, aiheuttaa virheen
  console.log(tulos);
} catch (virhe) {
  console.error("Tapahtui virhe: " + virhe.message);
} finally {
  console.log("Yritettiin suorittaa ohjelmakoodi");
}
