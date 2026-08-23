<!-- tags: vinkit, backend-api -->

# Käyttäjän kirjautumisen vuokaavio (bcrypt, JWT)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Turvallisen kirjautumisprosessin (user login flow) vaiheet palvelinpuolelta katsottuna, bcryptillä ja JWT:llä toteutettuna.

## Vaiheet

1. **User** — Käyttäjä syöttää sähköpostin ja salasanan.
2. **Login Form** — Lomake sisältää sähköposti-, salasanakentät ja Login-painikkeen.
3. **POST /api/login** — Selain lähettää pyynnön palvelimelle.
4. **Find User** — Palvelin hakee käyttäjän `users`-taulusta:
   ```sql
   SELECT * FROM users
   WHERE email = ?
   ```
5. **Password Verification** — Salasana tarkistetaan `bcrypt.compare()`-funktiolla: syötetty salasana → verrataan tallennettuun hashiin.
6. **Password Match?** — Haarautuminen:
   - **Ei täsmää** → Invalid Credentials, `401 Unauthorized`
   - **Täsmää** → Authentication Success
7. **Generate JWT** — Palvelin generoi JWT-tokenin onnistuneen tunnistautumisen jälkeen.
8. **Set Cookie** — Token asetetaan cookieen: `HttpOnly`, `Secure`, `SameSite`.
9. **Send Response** — Token tallennettu cookieen, käyttäjä tunnistettu.
10. **Protected Dashboard** — Käyttäjä pääsee suojattuun näkymään, kirjautuneena.

## Turvallisuuselementit

- **Salasanaturvallisuus:** bcrypt-hajautus (hashing), vahva ja turvallinen, yksisuuntainen salaus.
- **Session-turvallisuus:** HttpOnly-cookiet, turvallinen tiedonsiirto, SameSite-suojaus.
- **Autentikaatio:** JWT-varmennus, tilaton ja skaalautuva, väärentämissuojattu (tamper resistant).
