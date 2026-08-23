<!-- tags: vinkit, python -->

# Data Viz -huijauslappu (Matplotlib/Seaborn)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä. Alkuperäinen lähde: Frank Andrade, frank-andrade.medium.com.

Matplotlib on Pythonin 2D-piirtokirjasto, joka tuottaa kuvaajia monessa eri muodossa.

## Matplotlib

### Työnkulku (Workflow)

Peruskulku matplotlib-kuvaajien luomisessa: valmistele data, piirrä, muokkaa, tallenna ja näytä kuvaaja.

```python
import matplotlib.pyplot as plt
```

### Esimerkki viivakaaviosta (Example with lineplot)

```python
# Valmistele data
x = [2017, 2018, 2019, 2020, 2021]
y = [43, 45, 47, 48, 50]

# Piirrä ja muokkaa kuvaajaa
plt.plot(x, y, marker='o', linestyle='--',
         color='g', label='USA')
plt.xlabel('Years')
plt.ylabel('Population (M)')
plt.title('Years vs Population')
plt.legend(loc='lower right')
plt.yticks([41, 45, 48, 51])

# Tallenna kuvaaja
plt.savefig('example.png')

# Näytä kuvaaja
plt.show()
```

**Merkit (markers):** `'.'`, `'o'`, `'v'`, `'<'`, `'>'`
**Viivatyylit (line styles):** `'-'`, `'--'`, `'-.'`, `':'`
**Värit (colors):** `'b'`, `'g'`, `'r'`, `'y'` (sininen, vihreä, punainen, keltainen)

### Pylväskaavio (Barplot)

```python
x = ['USA', 'UK', 'Australia']
y = [40, 50, 33]
plt.bar(x, y)
plt.show()
```

### Piirakkakaavio (Piechart)

```python
plt.pie(y, labels=x, autopct='%.0f%%')
plt.show()
```

### Histogrammi (Histogram)

```python
ages = [15, 16, 17, 30, 31, 32, 35]
bins = [15, 20, 25, 30, 35]
plt.hist(ages, bins, edgecolor='black')
plt.show()
```

### Laatikko-piiskakaavio (Boxplots)

```python
ages = [15, 16, 17, 30, 31, 32, 35]
plt.boxplot(ages)
plt.show()
```

### Pisteparvi (Scatterplot)

```python
a = [1, 2, 3, 4, 5, 4, 3, 2, 5, 6, 7]
b = [7, 2, 3, 5, 5, 7, 3, 2, 6, 3, 2]
plt.scatter(a, b)
plt.show()
```

### Osakuvaajat (Subplots)

Alla oleva koodi luo useita kuvaajia halutulla määrällä rivejä ja sarakkeita ('n').

```python
fig, ax = plt.subplots(nrows=1,
                        ncols=2,
                        sharey=True,
                        figsize=(12, 4))

# Piirrä ja muokkaa kutakin kuvaajaa
ax[0].plot(x, y, color='g')
ax[0].legend()
ax[1].plot(a, b, color='r')
ax[1].legend()
plt.show()
```

## Seaborn

### Työnkulku (Workflow)

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```

### Viivakaavio (Lineplot)

```python
plt.figure(figsize=(10, 5))
flights = sns.load_dataset("flights")
may_flights = flights.query("month=='May'")
ax = sns.lineplot(data=may_flights,
                   x="year", y="passengers")
ax.set(xlabel='x', ylabel='y',
       title='my_title', xticks=[1, 2, 3])
ax.legend(title='my_legend', title_fontsize=13)
plt.show()
```

### Pylväskaavio (Barplot)

```python
tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", data=tips)
```

### Histogrammi (Histogram)

```python
penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins, x="flipper_length_mm")
```

### Laatikko-piiskakaavio (Boxplot)

```python
tips = sns.load_dataset("tips")
ax = sns.boxplot(x=tips["total_bill"])
```

### Pisteparvi (Scatterplot)

```python
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip")
```

### Kuvaajan ulkoasu (Figure aesthetics)

```python
sns.set_style('darkgrid')          # tyylit
sns.set_palette('husl', 3)         # paletit
sns.color_palette('husl')          # värit

# Akseleiden otsikon, x- ja y-nimikkeiden, asteikkomerkintöjen ja selitteen fonttikoko
plt.rc('axes', titlesize=18)
plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=13)
plt.rc('legend', fontsize=13)
plt.rc('font', size=13)
```
