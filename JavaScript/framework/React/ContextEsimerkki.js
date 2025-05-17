/*
3. useContext
Kuvaus: Jakaa tietoja komponenttien välillä ilman tarvetta viedä tietoa propseilla.
Esimerkki: 
*/


import React, { useContext, createContext } from 'react';

const MyContext = createContext();

const ContextEsimerkki = () => {
  const value = useContext(MyContext);
  return <div>{value}</div>;
};

const App = () => (
  <MyContext.Provider value="Konteksti-arvo">
    <ContextEsimerkki />
  </MyContext.Provider>
);

export default App;