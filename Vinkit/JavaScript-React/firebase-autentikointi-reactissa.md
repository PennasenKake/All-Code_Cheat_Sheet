<!-- tags: vinkit, javascript-react -->

# Firebase-autentikointi Reactissa

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Rakenna turvallinen autentikointi ilman omaa backendiä.

## Ongelma ja ratkaisu

- **Ongelma:** Autentikoinnin rakentaminen tyhjästä on monimutkaista ja vaatii turvallisuutta, käyttäjähallintaa ja sähköpostinkäsittelyä.
- **Ratkaisu:** Käytä Firebase Authenticationia hoitamaan rekisteröityminen, kirjautuminen, salasanan palautus, sähköpostin vahvistus ja muut vähäisellä koodimäärällä.

## Asennus

```bash
npm install firebase
```

## Esimerkkikoodi

```javascript
import { getAuth } from "firebase/auth";
import { createUserWithEmailAndPassword } from "firebase/auth";

const auth = getAuth();

const registerUser = async () => {
  try {
    const user = await createUserWithEmailAndPassword(
      auth,
      "john@example.com",
      "password123"
    );

    console.log(user);
  } catch (error) {
    console.log(error.message);
  }
};
```

## Autentikointiominaisuudet

- **User Signup** – luo uusia tilejä sähköpostilla ja salasanalla.
- **User Login** – turvallinen kirjautuminen sähköpostilla ja salasanalla.
- **Email Verification** – vahvista käyttäjän sähköposti helposti.
- **Password Reset** – lähetä salasanan palautuslinkit sekunneissa.
- **Secure & Scalable** – sisäänrakennetut turvallisuussäännöt ja skaalautuva infrastruktuuri.

Esimerkin kirjautumisnäkymässä (Login/Register/Reset Password/Verify Email -välilehdet) käyttäjä kirjautuu sähköpostilla ja salasanalla, ja "Muista minut" / "Unohditko salasanan?" -toiminnot ovat käytettävissä.

## Miten Firebase Authentication toimii

1. Käyttäjä rekisteröityy tai kirjautuu sisään React-sovelluksen kautta.
2. Pyyntö lähetetään Firebase Authille.
3. Tunnistetiedot varmennetaan turvallisesti.
4. Käyttäjä tallennetaan Firebaseen.
5. Käyttäjäsessio luodaan.

**Ei backendiä tarvita** – Firebase hoitaa infrastruktuurin, skaalautuvuuden, tietoturvan ja muun.

## Muita autentikointiratkaisuja

- **Firebase Auth** – täysi autentikointiratkaisu Google Firebaselta.
- **Auth.js** – moderni autentikointi Next.js:lle ja Reactille.
- **Supabase Auth** – avoimen lähdekoodin autentikointi Supabasella.
- **Custom JWT Auth** – oman autentikoinnin rakentaminen JWT-tokeneilla.
