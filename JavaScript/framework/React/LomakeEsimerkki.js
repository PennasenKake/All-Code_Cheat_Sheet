
/*
Reactissa lomakkeiden tilaa hallitaan yleensä komponentin tilan avulla.
Lomake-elementtien (esim. <input>, <textarea>, <select>) 'value'-proppi
on sidottu komponentin tilaan, ja 'onChange'-tapahtumankuuntelijaa käytetään
tilan päivittämiseen käyttäjän syöttäessä tietoja. Tätä kutsutaan "kontrolloiduiksi
komponenteiksi".

'onSubmit'-tapahtumankuuntelijaa käytetään lomakkeen lähetyksen käsittelyyn.
'event.preventDefault()' estää selaimen oletuslähetyksen.
*/


import React, { useState } from 'react';

const LomakeEsimerkki = () => {
  const [kayttajatunnus, setKayttajatunnus] = useState('');
  const [salasana, setSalasana] = useState('');

  const kasitteleKayttajatunnusMuutos = (event) => {
    setKayttajatunnus(event.target.value);
  };

  const kasitteleSalasanaMuutos = (event) => {
    setSalasana(event.target.value);
  };

  const kasitteleLahetys = (event) => {
    event.preventDefault();
    alert(`Käyttäjätunnus: ${kayttajatunnus}, Salasana: ${salasana}`);
  };

  return (
    <form onSubmit={kasitteleLahetys}>
      <label>
        Käyttäjätunnus:
        <input
          type="text"
          value={kayttajatunnus}
          onChange={kasitteleKayttajatunnusMuutos}
        />
      </label>
      <br />
      <label>
        Salasana:
        <input
          type="password"
          value={salasana}
          onChange={kasitteleSalasanaMuutos}
        />
      </label>
      <br />
      <button type="submit">Kirjaudu</button>
    </form>
  );
};

export default LomakeEsimerkki;