<!-- tags: vinkit, python -->

# Scikit-Learn-huijauslappu (esikäsittely, koulutus/testijako)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Sklearn on ilmainen koneoppimiskirjasto Pythonille. Se sisältää erilaisia luokittelu-, regressio- ja klusterointialgoritmeja. Alkuperäinen lähde: Frank Andrade, frank-andrade.medium.com.

## Aloittaminen (Getting Started)

Peruskulku: ladataan data, jaetaan se koulutus- ja testijoukkoon, skaalataan joukot, luodaan malli, sovitetaan malli dataan koulutetulla mallilla ja lopuksi arvioidaan mallin suorituskykyä testijoukolla.

```python
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X, y = iris.data[:, :2], iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
accuracy_score(y_test, y_pred)
```

## Datan lataus (Loading the Data)

Datan tulee olla numeerista ja tallennettuna NumPy-taulukoihin tai SciPy sparse -matriisiin (myös numeeriset taulukot kuten Pandas DataFrame käyvät).

```python
>>> import numpy as np
>>> X = np.random.random((10,5))
>>> array([[0.21,0.33],
           [0.23, 0.60],
           [0.48, 0.62]])
>>> y = np.array(['A','B','A'])
>>> array(['A', 'B', 'A'])
```

## Koulutus- ja testidata (Training and Test Data)

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)  # Splits data into training and test set
```

## Datan esikäsittely (Preprocessing The Data)

### Standardointi (Standardization)

Standardoi piirteet poistamalla keskiarvon ja skaalaamalla yksikkövarianssiin.

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)
```

### Normalisointi (Normalization)

Jokainen näyte (datamatriisin rivi), jossa on vähintään yksi nollasta poikkeava arvo, skaalataan itsenäisesti muista näytteistä niin, että sen normi on yksi.

```python
from sklearn.preprocessing import Normalizer
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)
```

### Binarisointi (Binarization)

Binarisoi data (asettaa piirrearvot nollaksi tai ykköseksi kynnysarvon perusteella).

```python
from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=0.0).fit(X)
binary_X = binarizer.transform(X_test)
```

### Kategoristen piirteiden koodaus (Encoding Categorical Features)

Imputointimuunnin puuttuvien arvojen täydentämiseen.

```python
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit_transform(X_train)
```

### Puuttuvien arvojen imputointi (Imputing Missing Values)

```python
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=0, strategy='mean')
imp.fit_transform(X_train)
```

### Polynomisten piirteiden generointi (Generating Polynomial Features)

```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(5)
poly.fit_transform(X)
```
