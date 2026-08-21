<!-- tags: javascript, framework, react -->

# CallbackEsimerkki.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/framework/React/CallbackEsimerkki.js)

```javascript
/*
2. useCallback
Kuvaus: Memoisoi callback-funktion, 
jotta lapsikomponentit eivät renderöidy uudelleen tarpeettomasti.
Esimerkki: 
*/

import React, { useState, useCallback } from 'react';

const CallbackEsimerkki = () => {
  const [count, setCount] = useState(0);
  const memoizedCallback = useCallback(() => {
    console.log(`Laskuri: ${count}`);
  }, [count]);
  return <button onClick={memoizedCallback}>Loggaa laskuri</button>;
};

export default CallbackEsimerkki;
```
