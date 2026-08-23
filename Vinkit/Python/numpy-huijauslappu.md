<!-- tags: vinkit, python -->

# NumPy-huijauslappu (taulukot, matematiikka, muokkaus)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä. Alkuperäinen lähde: Frank Andrade, frank-andrade.medium.com.

NumPy tarjoaa työkaluja taulukoiden (array) käsittelyyn. Kaikki alla olevat esimerkit viittaavat seuraaviin taulukoihin:

```
1D-taulukko: [1, 2, 3]

2D-taulukko:  1.5  2  3
              4    5  6
```

## Aloittaminen (Getting Started)

```python
import numpy as np
```

### Taulukoiden luonti

```python
a = np.array([1, 2, 3])
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
c = np.array([[(1.5, 2, 3), (4, 5, 6)],
              [(3, 2, 1), (4, 5, 6)]],
             dtype=float)
```

### Alustavat paikkamerkit (Initial placeholders)

```python
np.zeros((3, 4))              # Luo nollataulukon
np.ones((2, 3, 4), dtype=np.int16)
d = np.arange(10, 25, 5)
np.linspace(0, 2, 9)
e = np.full((2, 2), 7)
np.random.random((2, 2))
np.empty((3, 2))
```

### Tallennus ja lataus levylle (Saving & Loading On Disk)

```python
np.save('my_array', a)
np.savez('array.npz', a, b)
np.load('my_array.npy')
```

### Tekstitiedostojen tallennus ja lataus (Saving & Loading Text Files)

```python
np.loadtxt('my_file.txt')
np.genfromtxt('my_file.csv', delimiter=',')
np.savetxt('myarray.txt', a, delimiter=' ')
```

### Taulukon tarkastelu (Inspecting Your Array)

```python
a.shape
len(a)
b.ndim
e.size
b.dtype       # datatyyppi
b.dtype.name
b.astype(int) # muuta datatyyppi
```

### Datatyypit (Data Types)

```python
np.int64
np.float32
np.complex
np.bool
np.object
np.string_
np.unicode_
```

## Taulukkomatematiikka (Array Mathematics)

### Aritmeettiset operaatiot

```python
>>> g = a - b
array([[-0.5, 0., 0.],
       [-3., 3., 3.]])

>>> np.subtract(a, b)

>>> b + a
array([[2.5, 4., 6.],
       [5., 7., 9.]])

>>> np.add(b, a)

>>> a / b
array([[0.66666667, 1., 1.],
       [0.25, 0.4, 0.5]])

>>> np.divide(a, b)

>>> a * b
array([[1.5, 4., 9.],
       [4., 10., 18.]])

>>> np.multiply(a, b)

>>> np.exp(b)
>>> np.sqrt(b)
>>> np.sin(a)
>>> np.log(a)
>>> e.dot(f)
```

### Yhdistelmäfunktiot (Aggregate functions)

```python
a.sum()
a.min()
b.max(axis=0)
b.cumsum(axis=1)   # kumulatiivinen summa
b.mean()
b.median()
a.corrcoef()        # korrelaatiokerroin
np.std(b)           # keskihajonta
```

### Taulukoiden kopiointi (Copying arrays)

```python
h = a.view()   # luo näkymän
np.copy(a)
h = a.copy()   # luo syvän kopion
```

### Taulukoiden järjestäminen (Sorting arrays)

```python
a.sort()          # järjestä taulukko
c.sort(axis=0)
```

## Taulukon muokkaus (Array Manipulation)

```python
# Taulukon transponointi
i = np.transpose(b)
i.T

# Muodon muuttaminen
b.ravel()
g.reshape(3, -2)

# Elementtien lisääminen/poistaminen
h.resize((2, 6))
np.append(h, g)
np.insert(a, 1, 5)
np.delete(a, [1])

# Taulukoiden yhdistäminen
np.concatenate((a, d), axis=0)
np.vstack((a, b))   # pinoa pystysuunnassa
np.hstack((e, f))   # pinoa vaakasuunnassa

# Taulukoiden jakaminen
np.hsplit(a, 3)   # jaa vaakasuunnassa
np.vsplit(c, 2)   # jaa pystysuunnassa
```

### Osajoukon valinta, viipalointi ja Boolean-indeksointi

```python
# Osajoukon valinta (subsetting)
b[1, 2]

# Viipalointi (slicing)
a[0:2]

# Boolean-indeksointi
a[a < 2]
```
