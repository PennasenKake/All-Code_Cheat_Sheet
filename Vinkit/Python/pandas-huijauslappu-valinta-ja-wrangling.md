<!-- tags: vinkit, python -->

# Pandas-huijauslappu (rivien/sarakkeiden valinta, data wrangling)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä. Alkuperäinen lähde: Frank Andrade, frank-andrade.medium.com.

Pandas tarjoaa data-analyysityökaluja Pythonille. Kaikki alla olevat esimerkit viittaavat seuraavaan dataframeen:

```
      col1  col2
A       1     4
B       2     5
C       3     6
```

(rivit = axis 0, sarakkeet = axis 1)

## Aloittaminen (Getting Started)

```python
# Tuo pandas
import pandas as pd

# Luo sarja (series)
s = pd.Series([1, 2, 3], index=['A', 'B', 'C'], name='col1')

# Luo dataframe
data = [[1, 4], [2, 5], [3, 6]]
index = ['A', 'B', 'C']
df = pd.DataFrame(data, index=index, columns=['col1', 'col2'])

# Lataa dataframe tiedostosta
df = pd.read_csv('filename.csv', sep=',',
                  names=['col1', 'col2'],
                  index_col=0,
                  encoding='utf-8',
                  nrows=3)
```

## Rivien ja sarakkeiden valinta (Selecting rows and columns)

```python
# Valitse yksi sarake
df['col1']

# Valitse useampi sarake
df[['col1', 'col2']]

# Näytä ensimmäiset n riviä
df.head(2)

# Näytä viimeiset n riviä
df.tail(2)

# Valitse rivit indeksin arvon perusteella
df.loc['A']
df.loc[['A', 'B']]

# Valitse rivit sijainnin perusteella
df.iloc[1]
df.iloc[1:]
```

## Datan muokkaus (Data wrangling)

```python
# Suodata arvon perusteella
df[df['col1'] > 1]

# Järjestä sarakkeiden mukaan
df.sort_values(['col2', 'col2'], ascending=[False, True])

# Tunnista duplikaattirivit
df.duplicated()

# Tunnista uniikit rivit
df['col1'].unique()

# Vaihda rivit ja sarakkeet keskenään
df = df.transpose()
df = df.T

# Poista sarake
df = df.drop('col1', axis=1)

# Kloonaa dataframe
clone = df.copy()

# Yhdistä useampi dataframe pystysuunnassa
df2 = df + 5  # uusi dataframe
pd.concat([df, df2])
```

## Yhdistäminen vaakasuunnassa (Merge multiple data frames horizontally)

```python
df3 = pd.DataFrame([[1, 7], [8, 9]],
                    index=['B', 'D'],
                    columns=['col1', 'col3'])
# df3: uusi dataframe

# Yhdistä vain täydelliset rivit (INNER JOIN)
df.merge(df3)

# Vasen sarake pysyy täydellisenä (LEFT OUTER JOIN)
df.merge(df3, how='left')

# Oikea sarake pysyy täydellisenä (RIGHT OUTER JOIN)
df.merge(df3, how='right')

# Säilytä kaikki arvot (OUTER JOIN)
df.merge(df3, how='outer')

# Yhdistä rivit indeksin perusteella
df.merge(df3, left_index=True, right_index=True)

# Täytä NaN-arvot
df.fillna(0)

# Käytä omaa funktiota
def func(x):
    return 2**x
df.apply(func)
```

## Aritmetiikka ja tilastot (Arithmetics and statistics)

```python
# Lisää kaikkiin arvoihin
df + 10

# Summa sarakkeittain
df.sum()

# Kumulatiivinen summa sarakkeittain
df.cumsum()

# Keskiarvo sarakkeittain
df.mean()

# Keskihajonta sarakkeittain
df.std()

# Laske uniikkien arvojen määrä
df['col1'].value_counts()

# Yhteenveto kuvailevista tilastoista
df.describe()
```
