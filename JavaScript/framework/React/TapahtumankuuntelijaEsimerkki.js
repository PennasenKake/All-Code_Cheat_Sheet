
/*
Reactissa tapahtumankuuntelijat lisätään elementteihin 'on'-alkuisilla propeilla
(esim. onClick, onChange, onSubmit). Tapahtumafunktio välitetään proppina.
Synteettinen tapahtumaobjekti (esim. 'event') välitetään tapahtumafunktiolle.
Tämä objekti on Reactin alusta-agnostinen wrapper selaimen natiivitapahtumien ympärillä.

'event.preventDefault()' estää selaimen oletustoiminnon (esim. linkin seuraamisen).
*/

import React from 'react';

const TapahtumankuuntelijaEsimerkki = () => {
  const handleClick = (event) => {
    event.preventDefault();
    alert("Hei Maailma!");
  };

  return (
    <div>
      <a href="/" onClick={handleClick}>
        Sano Hei
      </a>
    </div>
  );
};

export default TapahtumankuuntelijaEsimerkki;