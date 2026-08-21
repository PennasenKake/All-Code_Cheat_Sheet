<!-- tags: javascript, socket -->

# App.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/Socket/App.js)

```javascript
// client/src/App.js
// Pääkomponentti, joka yhdistää chat-komponentit

import React from 'react';
import ChatRoom from './components/ChatRoom';
import ChatNamespace from './components/ChatNamespace';

function App() {
  return (
    <div>
      <h1 style={{ textAlign: 'center', padding: '20px' }}>Socket.IO Chat -esimerkit</h1>
      <ChatRoom />
      <hr style={{ margin: '20px 0' }} />
      <ChatNamespace />
    </div>
  );
}

export default App;
```
