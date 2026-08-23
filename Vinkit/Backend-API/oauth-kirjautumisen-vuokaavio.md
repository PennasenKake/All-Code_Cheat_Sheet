<!-- tags: vinkit, backend-api -->

# OAuth-kirjautumisen vuokaavio

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Turvallisen kolmannen osapuolen autentikointiprosessin (OAuth) kulku vaihe vaiheelta.

## Vaiheet

1. **Käyttäjä avaa sovelluksen** – näkyvissä kirjautumisnäkymä ("Continue with Provider").
2. **Käyttäjä valitsee OAuth-tarjoajan** – esim. Google, GitHub tai Microsoft.
3. **Uudelleenohjaus valtuutuspalvelimelle** – `GET /authorize` parametreilla `client_id`, `scope=email profile`, `response_type=code`.
4. **Käyttäjän autentikointi** – käyttäjä kirjautuu valitsemallaan palveluntarjoajalla (esim. Google), mahdollisesti MFA käytössä.
5. **Lupanäyttö (consent screen)** – sovellus pyytää oikeuksia (sähköposti, profiili, perustiedot); käyttäjä hyväksyy ("Allow Access") tai peruuttaa.
6. **Valtuutuskoodi generoidaan** – palvelin luo esim. `AUTH_CODE_XYZ123`.
7. **Uudelleenohjaus takaisin sovellukseen** – `https://app.com/callback?code=XYZ123`.
8. **Backend vaihtaa koodin** – `POST /token` lähettää valtuutuskoodin ja client secretin.
9. **Access token myönnetään** – palautetaan access token ja refresh token.
10. **Käyttäjätietojen haku** – `GET /userinfo` palauttaa nimen, sähköpostin, avatarin.

**Autentikointi valmis** – käyttäjä on kirjautunut, istunto aktiivinen.

## OAuth-arkkitehtuurin osat

- **User** – kirjautumisen aloittava loppukäyttäjä.
- **Client Application** – sovellus, joka pyytää pääsyä.
- **Authorization Server** – hoitaa autentikoinnin ja käyttäjän suostumuksen.
- **Resource Server** – API, joka tarjoaa suojatut resurssit.
- **Access Token** – myöntää pääsyn suojattuihin resursseihin.
- **Refresh Token** – käytetään uusien access tokenien hakemiseen.

Arkkitehtuurin kulku: **User** → login-pyyntö → **Application (Client)**: pyytää pääsyä käyttäjän puolesta → **Authorization Server**: autentikoi käyttäjän ja myöntää tokenit → **Resource API (Server)**: tarjoaa suojatut resurssit access tokenia vastaan.

## OAuthin edut

- Ei salasanojen tallennusta sovelluksessa
- Nopeampi kirjautuminen
- Parempi tietoturva
- Parempi käyttökokemus
- Luotettavat identiteetintarjoajat

## Tietoturvan parhaat käytännöt

- Käytä aina HTTPS:ää
- Validoi state-parametri
- Säilytä tokenit turvallisesti
- Käytä lyhytikäisiä access tokeneita
- Käytä refresh token -rotaatiota
- Suojaudu CSRF-hyökkäyksiltä
