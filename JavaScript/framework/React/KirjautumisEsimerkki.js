import React from 'react';

const KirjautumisEsimerkki = () => {
  const isLogged = true;
  return isLogged ? <div>Kirjautunut</div> : <div>Vierailija</div>;
};

export default KirjautumisEsimerkki;