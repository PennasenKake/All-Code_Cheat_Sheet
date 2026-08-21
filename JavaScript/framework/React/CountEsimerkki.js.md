<!-- tags: javascript, framework, react -->

# CountEsimerkki.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/framework/React/CountEsimerkki.js)

```javascript
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
```
