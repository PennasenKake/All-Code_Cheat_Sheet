
/*
Tila ('state') on React-komponentin muistia. Se on JavaScript-objekti, joka
sisältää komponentin muuttuvia tietoja. Kun tila muuttuu, komponentti
uudelleenrenderöityy.

'useState' on React Hook, jota käytetään funktionaalisissa komponenteissa tilan
hallintaan. Se palauttaa kaksi arvoa: nykyisen tilan ja funktion tilan päivittämiseen.
Tilapäivitykset ovat asynkronisia.
*/


import React, { useState } from 'react';

const TilaEsimerkki = ({ alkuNimi = "Vieras" }) => {
  const [nimi, setNimi] = useState(alkuNimi);

  const paivitaNimi = () => {
    const uusiNimi = prompt("Mikä on nimesi?");
    if (uusiNimi) setNimi(uusiNimi);
  };

  return (
    <div>
      <h1>Hei, {nimi}</h1>
      <button onClick={paivitaNimi}>Päivitä Nimi</button>
    </div>
  );
};

export default TilaEsimerkki;