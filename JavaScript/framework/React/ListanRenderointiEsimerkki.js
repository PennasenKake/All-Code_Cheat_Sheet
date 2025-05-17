
/*
Rendering Lists
Listojen avulla voit helposti renderöidä useita komponentteja tehokkaasti.
Esimerkki: 
*/

import React from 'react';

const ListanRenderointiEsimerkki = () => {
  const myList = [1, 2, 3];
  const listItems = myList.map((item) => <li key={item}>{item}</li>);
  return <ul>{listItems}</ul>;
};

export default ListanRenderointiEsimerkki;

/*
map-metodi: Luo uuden taulukon komponentteja iteroinnin perusteella.
Key-prop: Jokaisella listakomponentilla tulisi 
olla ainutlaatuinen key-prop nopeuttaaksesi renderöintiä ja estääksesi virheitä. 
*/
