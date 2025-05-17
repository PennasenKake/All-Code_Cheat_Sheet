// Moduulit ES6:ssa

// tiedosto: mathFunctions.js
export function lisää(a, b) {
  return a + b;
}

export function kerro(a, b) {
  return a * b;
}

// tiedosto: main.js
import { lisää, kerro } from './mathFunctions.js';

console.log(lisää(2, 3)); // 5
console.log(kerro(2, 3)); // 6
