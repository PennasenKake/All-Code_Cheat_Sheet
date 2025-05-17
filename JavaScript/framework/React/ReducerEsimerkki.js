
/*
1. useReducer
Kuvaus: Tarjoaa rakenteellisen tavan hallita monimutkaisia tiloja. 
Käytetään usein, kun useState ei riitä tilapäivityksiin.
Esimerkki: */

import React, { useReducer } from 'react';

const reducer = (state, action) => {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    default:
      return state;
  }
};

const ReducerEsimerkki = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return (
    <div>
      <p>Laskuri: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>Lisää</button>
    </div>
  );
};

export default ReducerEsimerkki;