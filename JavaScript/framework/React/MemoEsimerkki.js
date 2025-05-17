/*
3. useMemo
Kuvaus: Memoisoi laskennan tuloksen, 
estäen sen uudelleenlaskennan jokaisella renderöinnillä.
Esimerkki: 
*/

import React, { useState, useMemo } from 'react';

const MemoEsimerkki = () => {
  const [a, setA] = useState(1);
  const [b, setB] = useState(2);
  const value = useMemo(() => a + b, [a, b]);
  return (
    <div>
      <p>Summa: {value}</p>
      <button onClick={() => setA(a + 1)}>Lisää A</button>
      <button onClick={() => setB(b + 1)}>Lisää B</button>
    </div>
  );
};

export default MemoEsimerkki;