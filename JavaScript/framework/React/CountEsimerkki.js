import React, { useState } from 'react';

const CountEsimerkki = () => {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Laskuri: {count}</p>
      <button onClick={() => setCount(count + 1)}>Lisää</button>
    </div>
  );
};

export default CountEsimerkki;