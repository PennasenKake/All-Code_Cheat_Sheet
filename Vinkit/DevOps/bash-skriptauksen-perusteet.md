<!-- tags: vinkit, devops -->

# Bash-skriptauksen perusteet

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Yhteen annotoituun `script.sh`-esimerkkiin koottu läpileikkaus Bash-skriptauksen peruselementeistä. Alla koko skripti sellaisenaan, ja kunkin osan selitys.

```bash
#!/bin/bash

username="Jay"
filename=$3

read -p "Enter your username: " user
echo "Username: $user"

if [ "$EUID" -ne 0 ]; then
    echo "You are not running this script as the root user."
else
    echo "You are running this script as the root user."
fi

echo "Counting to 5:"
for i in {1..5}; do
    echo "$i"
done

function greet() {
    echo "Hello, $1!"
}
greet "Alice"

echo "Enter a number between 1 and 2: "
read num
case $num in
    1) echo "You chose one." ;;
    2) echo "You chose two." ;;
    *) echo "Invalid choice." ;;
esac

if [ -e "$filename" ] && [ -d "$filename" ]; then
    echo "File exists and is a directory."
else
    echo "File does not exist or is not a directory."
fi

echo "First argument: $1"
echo "Second argument: $2"

cat nonexistent-file.txt 2> /dev/null
echo "Exit status: $?"

fruits=("Apple" "Orange" "Banana")
echo "Fruits: ${fruits[0]}"

declare -A capitals
capitals[USA]="Washington D.C."
capitals[France]="Paris"
echo "Capital of France: ${capitals[France]}"

current_date=$(date)
echo "Today's date is: $current_date"

echo "This is a sample text." > example.txt
find / -name hello.txt &> /dev/null

result=$( expr 15 - 2 )
echo $result

SRC="/path/to/foo.cpp"
BASEPATH=${SRC##*/}
echo $BASEPATH

trap 'echo "Received SIGTERM signal. Cleaning up..."; exit' SIGTERM

# This is a single line comment

: '
this is a multiline
comment'
```

## Osien selitykset

- **Shebang-rivi** (`#!/bin/bash`) – kertoo järjestelmälle, millä tulkilla skripti ajetaan.
- **Muuttujat** (`username="Jay"`, `filename=$3`) – muuttujien asetus, `$3` viittaa kolmanteen komentoriviargumenttiin.
- **Käyttäjän syöte** (`read -p ...`) – kysyy syötteen käyttäjältä ja tallentaa sen muuttujaan.
- **Ehtolause (if)** – `$EUID` kertoo käyttäjän ID:n; tarkistetaan ajetaanko skriptiä root-käyttäjänä.
- **For-silmukka** – `for i in {1..5}; do ... done` laskee 1:stä 5:een.
- **Funktiot** – `function greet() { ... }` määrittelee funktion, jota kutsutaan argumentilla.
- **Case-ehtolause** – `case ... in ... esac` valitsee toiminnon syötteen arvon perusteella.
- **Tiedosto-operaatiot** – `-e` tarkistaa tiedoston olemassaolon, `-d` onko se hakemisto.
- **Komentoriviargumentit** – `$1`, `$2` viittaavat skriptille annettuihin argumentteihin.
- **Poistumiskoodit (exit status)** – `$?` sisältää edellisen komennon paluuarvon; `2>` ohjaa virheet (stderr) haluttuun paikkaan.
- **Indeksoidut taulukot** – `fruits=("Apple" "Orange" "Banana")`, elementtiin viitataan `${fruits[0]}`.
- **Assosiatiiviset taulukot** – `declare -A` luo avain-arvo-taulukon, esim. `capitals[France]="Paris"`.
- **Komentokorvaus (command substitution)** – `$(date)` suorittaa komennon ja sijoittaa tuloksen muuttujaan.
- **Komentorivin uudelleenohjaukset** – `>` kirjoittaa tiedostoon, `&>` ohjaa sekä stdoutin että stderrin.
- **Aritmeettiset operaatiot** – `$( expr 15 - 2 )` laskee tuloksen.
- **Parametrien laajennus (parameter expansion)** – `${SRC##*/}` poistaa polusta kaiken viimeiseen `/`-merkkiin asti (jättää tiedostonimen).
- **Prosessin signaalien käsittely** – `trap ... SIGTERM` suorittaa siivoustoimet, kun skripti saa SIGTERM-signaalin.
- **Kommentit** – `#` yhden rivin kommentti, `: ' ... '` monirivinen kommentti.
