<!-- tags: javascript, framework, react -->

# KirjautumisEsimerkki.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/framework/React/KirjautumisEsimerkki.js)

```javascript
import React from 'react';

const KirjautumisEsimerkki = () => {
  const isLogged = true;
  return isLogged ? <div>Kirjautunut</div> : <div>Vierailija</div>;
};

export default KirjautumisEsimerkki;
```
