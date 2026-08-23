<!-- tags: vinkit, javascript-react -->

# Suojatut reitit (Protected Routes) Reactissa

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Estä luvaton pääsy yksityisille sivuille ja dashboardeille.

## Ongelma ja ratkaisu

- **Ongelma:** Ilman reittisuojausta käyttäjät voivat manuaalisesti käydä yksityisissä URL-osoitteissa ja nähdä sisältöä, jota heidän ei pitäisi nähdä.
- **Ratkaisu:** Käytä `react-router-dom`-pakettia luomaan Protected Routes -reittejä, joihin pääsevät vain autentikoidut käyttäjät.

## Asennus

```bash
npm install react-router-dom
```

## Esimerkkikoodi (ProtectedRoute.jsx)

```jsx
import { Navigate, Outlet } from "react-router-dom";

function ProtectedRoute() {
  const isAuthenticated = localStorage.getItem("token");

  return isAuthenticated ? (
    <Outlet />
  ) : (
    <Navigate to="/login" replace />
  );
}

export default ProtectedRoute;
```

## Miten suojatut reitit toimivat

1. Käyttäjä yrittää päästä osoitteeseen `/admin`.
2. `ProtectedRoute` tarkistaa autentikoinnin.
3. Onko käyttäjä autentikoitu?
   - **Kyllä:** pääsy sallitaan suojatulle sivulle.
   - **Ei:** käyttäjä ohjataan `/login`-sivulle.

## Esimerkki käytöstä

- **Autentikoimaton käyttäjä**, joka yrittää avata `example.com/admin`, ohjataan kirjautumissivulle ("Login to Continue" -lomake: sähköposti, salasana).
- **Autentikoitu käyttäjä** pääsee `example.com/admin`-sivulle ja näkee Admin Panelin (Dashboard, Users, Products, Orders, Reports, Settings, Logout) sekä dashboard-tiedot (esim. Users 1250, Orders 3420, Revenue 12 540 €).

## Hyödyt

- **Suojaa yksityiset sivut** – rajoittaa pääsyä arkaluontoisiin reitteihin.
- **Turvaa admin-dashboardit** – pitää admin-alueet turvassa.
- **Ohjaa autentikoimattomat käyttäjät** – lähettää käyttäjät kirjautumaan tarvittaessa.
- **Olennainen autentikointimalli** – must-have-ominaisuus tuotantosovelluksille.
- **Rakennettu React Routerin päälle** – hyödyntää React Routerin tehokkaita reititysominaisuuksia.

## Yleisiä autentikointistrategioita

- **JWT** – token-pohjainen autentikointi.
- **Session Auth** – palvelinpuolen istunnot ja evästeet.
- **Firebase Auth** – turvallinen autentikointi Firebasella.
- **OAuth** – sosiaalinen kirjautuminen OAuth-palveluntarjoajilla.
