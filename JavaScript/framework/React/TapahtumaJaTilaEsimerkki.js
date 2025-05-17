import React, { useState } from 'react';

const TapahtumaJaTilaEsimerkki = () => {
  const [inputValue, setInputValue] = useState('');

  const handleChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={handleChange}
        placeholder="Kirjoita jotain..."
      />
      <p>Syötit: {inputValue}</p>
    </div>
  );
};

export default TapahtumaJaTilaEsimerkki;