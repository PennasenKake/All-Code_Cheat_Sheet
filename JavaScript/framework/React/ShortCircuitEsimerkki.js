import React from 'react';

const ShortCircuitEsimerkki = () => {
  const isLoggedIn = true;
  return <div>{isLoggedIn && <div>Kirjautunut</div>}</div>;
};

export default ShortCircuitEsimerkki;