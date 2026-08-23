<!-- tags: vinkit, backend-api -->

# JWT-tokenien refresh-rotaatio

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

"Stop storing JWTs like it's 2015" – refresh token -rotaatio korjaa yleisen tietoturvaongelman.

> Jos sovellus tallentaa JWT:n `localStorage`-tilaan eikä koskaan rotatoi sitä, kyseessä ei ole autentikointi vaan tikittävä aikapommi.

## Ongelma

Useimmat oppaat opettavat: "generoi JWT, tallenna se, valmis." Mutta pitkäikäiset tokenit, jotka varastetaan XSS-hyökkäyksellä, antavat hyökkääjälle pysyvän pääsyn. Toisaalta lyhytikäiset tokenit ilman rotaatiota pakottavat käyttäjät kirjautumaan jatkuvasti uudelleen, mikä tuhoaa käyttökokemuksen.

## Ratkaisu

Käytä lyhytikäisiä access tokeneita (15 min) yhdistettynä rotatoiviin refresh tokeneihin, jotka tallennetaan `httpOnly`-evästeisiin. Jokainen refresh-pyyntö myöntää uuden refresh tokenin ja mitätöi vanhan – varastettu token muuttuu hyödyttömäksi heti kun sitä käytetään kerran.

## Refresh token -rotaation kulku

1. **Login** – käyttäjä kirjautuu sähköpostilla ja salasanalla.
2. **Access token** – lyhytikäinen (15 min), lähetetään Authorization-headerissa.
3. **Refresh token** – tallennettu `httpOnly`-evästeeseen, pitkäikäinen (7 päivää), rotatoituu joka käytöllä.
4. **Rotate & replace** – refresh tokenia käytetään uusien tokenien hakemiseen.
5. **Old token invalidated** – vanhaa refresh tokenia ei voi enää käyttää.

Toistuu: joka refresh rotatoi tokenin.

## Koodiesimerkki

```javascript
// POST /refresh
app.post("/refresh", async (req, res) => {
  const oldToken = req.cookies.refreshToken;
  const payload = jwt.verify(oldToken, process.env.REFRESH_SECRET);

  await revokeToken(oldToken); // invalidate immediately

  const newAccess = jwt.sign(
    { id: payload.id },
    process.env.ACCESS_SECRET,
    { expiresIn: "15m" }
  );
  const newRefresh = jwt.sign(
    { id: payload.id },
    process.env.REFRESH_SECRET,
    { expiresIn: "7d" }
  );

  await storeToken(newRefresh);

  res.cookie("refreshToken", newRefresh, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
  });
  res.json({ accessToken: newAccess });
});
```

Asennus: `npm install jsonwebtoken cookie-parser`

## Avainkohdat

- Access tokenit vanhenevat nopeasti, mikä rajoittaa vuotojen aiheuttamaa vahinkoa.
- Refresh tokenit rotatoituvat joka käytöllä – uudelleenkäytön tunnistus estää replay-hyökkäykset.
- `httpOnly` + secure-evästeet estävät JavaScript/XSS-pääsyn kokonaan.
- Tallenna refresh tokenit aina palvelinpuolella, jotta ne voidaan mitätöidä.
- Älä koskaan tallenna refresh tokeneita `localStorage`-tilaan.
