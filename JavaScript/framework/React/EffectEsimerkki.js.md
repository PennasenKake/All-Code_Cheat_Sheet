<!-- tags: javascript, framework, react -->

# EffectEsimerkki.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/framework/React/EffectEsimerkki.js)

```javascript
/*
2. useEffect
Kuvaus: Käytetään sivuvaikutusten hallintaan, 
kuten datan hakuun, tilauksen käsittelyyn tai siivouksen suorittamiseen.
Esimerkki: 
*/


import React, { useEffect, useState } from 'react';

const EffectEsimerkki = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    console.log("Komponentti renderöity");
    // Esimerkki datan hausta (kommentoitu, koska ei oikeaa APIa)
    // fetch('https://api.example.com/data')
    //   .then(response => response.json())
    //   .then(data => setData(data));
    setData({ message: "Esimerkkidata" }); // Simuloitu data
  }, []);

  return <div>{data ? data.message : "Ladataan..."}</div>;
};

export default EffectEsimerkki;
```
