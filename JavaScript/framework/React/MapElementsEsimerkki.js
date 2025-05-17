
/*
Map-funktiota käytetään yleisesti Reactissa listojen renderöintiin.
Se iteroi taulukon läpi ja luo jokaiselle elementille uuden JSX-elementin.
'key'-prop on tärkeä antaa jokaiselle listan elementille, jotta React voi
tehokkaasti päivittää ja uudelleenrenderöidä niitä. Yleensä 'key' on
elementin uniikki ID tai indeksi, jos uniikkeja ID:itä ei ole.
*/

import React from 'react';

const MapElementsEsimerkki = () => {
  const elementit = [
    { id: 1, nimi: "yksi", arvo: 10 },
    { id: 2, nimi: "kaksi", arvo: 20 },
    { id: 3, nimi: "kolme", arvo: 30 },
  ];

  return (
    <ul>
      {elementit.map((element) => (
        <li key={element.id}>
          Arvo nimelle {element.nimi} on {element.arvo}
        </li>
      ))}
    </ul>
  );
};

export default MapElementsEsimerkki;