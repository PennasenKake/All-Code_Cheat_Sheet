<!-- tags: vinkit, devops -->

# 7 Git-komentoa -huijauslappu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

7 Git-komentoa, joita jokainen kehittäjä googlettaa yhä uudelleen.

## 1. Peru viimeisin commit (Undo Last Commit)

Peruu viimeisimmän commitin mutta pitää muutokset staged-tilassa.

```bash
git reset --soft HEAD~1
```

Peruu commitin, pitää muutokset (staged).

## 2. Näytä commit-historia (View Commit History)

Näytä siisti, lyhyt commit-historia.

```bash
git log --oneline
```

Lyhyt ja siisti commit-historia.

## 3. Luo uusi haara (Create New Branch)

Luo ja vaihda uuteen haaraan.

```bash
git checkout -b feature-name
```

Luo ja vaihtaa uuteen haaraan.

## 4. Vaihda haaraa (Switch Branch)

Vaihda olemassa olevaan haaraan.

```bash
git switch branch-name
```

Vaihtaa toiseen haaraan.

## 5. Poista paikallinen haara (Delete Local Branch)

Poista paikallinen haara, joka on jo yhdistetty (merged).

```bash
git branch -d branch-name
```

Poistaa yhdistetyn haaran turvallisesti.

## 6. Näytä muutetut tiedostot (See Changed Files)

Tarkista työhakemiston tila.

```bash
git status
```

Näyttää muokatut, staged ja seuraamattomat tiedostot.

## 7. Hae uusimmat muutokset (Pull Latest Changes)

Hae ja yhdistä uusimmat muutokset etärepositoriosta.

```bash
git pull origin main
```

Hakee uusimmat muutokset etärepositoriosta.

## Rehellisesti sanottuna...

Jopa senior-kehittäjät googlettavat yhä Git-komentoja. Ero on siinä, että he tallentavat hyödyllisiä huijauslappuja.

## Pro-vinkki

Hallitse Git ja vältät lukemattomia projektin päänsärkyjä.
