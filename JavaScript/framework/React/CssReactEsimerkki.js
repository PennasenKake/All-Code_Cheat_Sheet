
// --------------------------------------------------------------------------
// 2. CSS Reactissa
// --------------------------------------------------------------------------

/*
Reactissa CSS:ää voidaan tuoda moduulina (.module.css) tai perinteisenä .css-tiedostona.
Tuotaessa perinteisenä tiedostona, tyylit ovat globaaleja. CSS-moduulit luovat
paikallisia tyyliluokkia, mikä ehkäisee nimitörmäyksiä eri komponenttien välillä.

Tässä esimerkissä oletetaan, että on olemassa 'Student.css'-tiedosto, joka sisältää
'.Student'-nimisen tyyliluokan.
*/

import React from 'react';
import '../styles/Student.css'; // Globaali CSS

const CssReactEsimerkki = () => {
  return <div className="Student">Opiskelija Maija Meikäläinen</div>;
};

// Moduuli-CSS (kommentoitu esimerkki)
// import styles from '../styles/Student.module.css';
// const CssModuleReactEsimerkki = () => {
//   return <div className={styles.student}>Opiskelija Maija Meikäläinen (moduulilla)</div>;
// };

export default CssReactEsimerkki;