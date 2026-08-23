<!-- tags: vinkit, devops -->

# cat ja nano — Linux-komentojen cheat sheet

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Pienet komennot, suuri voima. Kaksi peruskomentoa, joita käytetään Linux-terminaalissa jatkuvasti: `cat` tiedostojen näyttämiseen ja `nano` niiden muokkaamiseen.

## cat — Concatenate and display file content

Yhdistää ja näyttää tiedostojen sisällön. Yksinkertainen, nopea, tehokas.

### Yleiset käyttötavat

```bash
# Näytä tiedoston sisältö
cat file.txt

# Näytä rivinumeroineen
cat -n file.txt

# Yhdistä tiedostoja
cat file1.txt file2.txt > out.txt

# Luo tiedosto (kirjoita teksti, sitten Ctrl+D tallentaa)
cat > newfile.txt

# Näytä tulostumattomat merkit
cat -v file.txt
```

### Pikaesimerkki

```bash
$ cat hello.txt
Hello Linux!
Study. Practice. Grow.
Keep exploring. 🚀
```

### Vinkit

- `cat` sopii parhaiten nopeaan tiedoston katseluun.
- Käytä `less` tai `more` isoihin tiedostoihin.
- Yhdistä putkilla: `cat file.txt | grep "word"`

## nano — yksinkertainen tekstieditori terminaalissa

Helppokäyttöinen tekstieditori terminaalissa. Muokkaa mitä tahansa, missä tahansa.

### Aloitus

```bash
nano filename.txt
```

Luo tiedoston, jos sitä ei vielä ole.

### Nano-pikanäppäimet (cheat sheet)

| Näppäin | Toiminto | Näppäin | Toiminto |
|---|---|---|---|
| `^G` | Get Help (ohje) | `^X` | Exit (poistu) |
| `^O` | Write Out (tallenna) | `^W` | Where Is (etsi) |
| `^R` | Read File (lue tiedosto) | `^\` | Replace (korvaa) |
| `^Y` | Prev Page (edellinen sivu) | `^V` | Next Page (seuraava sivu) |
| `^K` | Cut Line (leikkaa rivi) | `^U` | Paste Line (liitä rivi) |
| `^C` | Current Line (nykyinen rivi) | `^J` | Justify Line (tasaa rivi) |
| `^_` | Go To Line (siirry riville) | | |
| `M-U` | Undo (kumoa) | `M-E` | Redo (tee uudelleen) |

### Esimerkkityönkulku

```bash
$ nano notes.txt      # avaa (tai luo) tiedosto
...muokkaa sisältöä...
^O                     # tallenna
^X                     # poistu
```

### Vinkit

- `Ctrl` = `^` (esim. Ctrl+O = `^O`)
- `Meta/Alt` = `M` (esim. Alt+U = `M-U`)
- Sopii täydellisesti konfiguraatioiden, skriptien ja muistiinpanojen muokkaamiseen.

> Ole utelias. Jatka oppimista. Terminaali on supervoimasi. Opi vähän tänään, automatisoi huomenna, omista tulevaisuus.
