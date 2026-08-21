<!-- tags: javascript, framework, react -->

# FragmentEsimerkki.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/framework/React/FragmentEsimerkki.js)

```javascript
/*
Fragment Shorthand
Käytä fragmentteja välttääksesi turhaa HTML-elementtien pesittämistä.
Esimerkki: 
*/


import React from 'react';

const FragmentEsimerkki = () => {
  const myList = [1, 2, 3];
  const listItems = myList.map((item) => <li key={item}>{item}</li>);
  return <>{listItems}</>;
};

export default FragmentEsimerkki;
```
