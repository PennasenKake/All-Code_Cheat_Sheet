<!-- tags: javascript, framework, react -->

# MyComponent.js

[Näytä alkuperäinen tiedosto GitHubissa](JavaScript/framework/React/MyComponent.js)

```javascript
import React from 'react';

// Toiminnallinen komponentti oletuspropeilla
const MyComponent = ({ message = "Default Message" }) => {
  return <div>{message}</div>;
};

// Propsien purkaminen
const MyComponentDestructured = ({ message }) => {
  return <div>{message}</div>;
};

export default MyComponent;
```
