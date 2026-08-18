<!-- tags: javascript, framework, react -->

# ShortCircuitEsimerkki.js

[Näytä alkuperäinen tiedosto GitHubissa](JavaScript/framework/React/ShortCircuitEsimerkki.js)

```javascript
import React from 'react';

const ShortCircuitEsimerkki = () => {
  const isLoggedIn = true;
  return <div>{isLoggedIn && <div>Kirjautunut</div>}</div>;
};

export default ShortCircuitEsimerkki;
```
