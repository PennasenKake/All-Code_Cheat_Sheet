<!-- tags: vinkit, python -->

# Pandas-huijauslappu osa 2 (aggregointi, visualisointi, CSV-vienti)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä. Alkuperäinen lähde: Frank Andrade, frank-andrade.medium.com. Jatkoa tiedostolle "Pandas-huijauslappu (rivien/sarakkeiden valinta, data wrangling)".

## Hierarkkinen indeksointi (Hierarchical indexing)

```python
# Luo hierarkkinen indeksi
df.stack()

# Pura hierarkkinen indeksi
df.unstack()
```

## Aggregointi (Aggregation)

```python
# Luo ryhmäobjekti
g = df.groupby('col1')

# Iteroi ryhmien yli
for i, group in g:
    print(i, group)

# Aggregoi ryhmät
g.sum()
g.prod()
g.mean()
g.std()
g.describe()

# Valitse sarakkeet ryhmistä
g['col2'].sum()
g[['col2', 'col3']].sum()

# Muunna arvoja
import math
g.transform(math.log)

# Käytä listafunktiota jokaiseen ryhmään
def strsum(group):
    return ''.join([str(x) for x in group.value])

g['col2'].apply(strsum)
```

## Datan vienti (Data export)

```python
# Data NumPy-taulukkona
df.values

# Tallenna data CSV-tiedostona
df.to_csv('output.csv', sep=",")

# Muotoile dataframe taulukkomerkkijonoksi
df.to_string()

# Muunna dataframe dictiksi
df.to_dict()

# Tallenna dataframe Excel-taulukkona
df.to_excel('output.xlsx')
```

## Visualisointi (Visualization)

```python
# Tuo matplotlib
import matplotlib.pyplot as plt

# Aloita uusi kaavio
plt.figure()

# Pisteparvi (scatter plot)
df.plot.scatter('col1', 'col2', style='ro')

# Pylväskaavio (bar plot)
df.plot.bar(x='col1', y='col2', width=0.7)

# Aluekaavio (area plot)
df.plot.area(stacked=True, alpha=1.0)

# Laatikko-piiskakaavio (box-and-whisker plot)
df.plot.box()

# Histogrammi yhdestä sarakkeesta
df['col1'].plot.hist(bins=3)

# Histogrammi kaikista sarakkeista
df.plot.hist(bins=3, alpha=0.5)

# Aseta asteikon merkinnät
labels = ['A', 'B', 'C', 'D']
positions = [1, 2, 3, 4]
plt.xticks(positions, labels)
plt.yticks(positions, labels)

# Valitse piirrettävä alue
plt.axis([0, 2.5, 0, 10])  # [x:sta, x:hen, y:stä, y:hen]

# Nimeä kaavio ja akselit
plt.title('Correlation')
plt.xlabel('Nunstück')
plt.ylabel('Slotermeyer')

# Tallenna viimeisin kaavio
plt.savefig('plot.png')
plt.savefig('plot.png', dpi=300)
plt.savefig('plot.svg')
```
