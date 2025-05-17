
/*
4. useRef
Kuvaus: Palauttaa olion, jossa on .current-property, 
jota voi käyttää säilyttämään muuttujia tai viittaamaan DOM-elementteihin.
Esimerkki: 
*/

import React, { useRef } from 'react';

const RefEsimerkki = () => {
  const myRef = useRef(null);
  const focusInput = () => myRef.current.focus();
  return (
    <div>
      <input ref={myRef} />
      <button onClick={focusInput}>Fokusoi</button>
    </div>
  );
};

export default RefEsimerkki;