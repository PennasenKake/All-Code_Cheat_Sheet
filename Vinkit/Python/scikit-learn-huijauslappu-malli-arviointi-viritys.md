<!-- tags: vinkit, python -->

# Scikit-learn-huijauslappu: mallin luonti, arviointi, viritys

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Mallin luonti (Create Your Model)

### Ohjattu oppiminen (Supervised Learning Models)

**Lineaarinen regressio**
```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize=True)
```

**Tukivektorikoneet (SVM)**
```python
from sklearn.svm import SVC
svc = SVC(kernel='linear')
```

**Naive Bayes**
```python
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
```

**KNN**
```python
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
```

### Ohjaamaton oppiminen (Unsupervised Learning Models)

**Pääkomponenttianalyysi (PCA)**
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
```

**K-means**
```python
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
```

## Mallin sovittaminen (Model Fitting)

Sovitetaan ohjatut ja ohjaamattomat mallit dataan.

**Ohjattu oppiminen**
```python
lr.fit(X, y)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)
```

**Ohjaamaton oppiminen**
```python
k_means.fit(X_train)  # Fit the model to the data
pca_model = pca.fit_transform(X_train)  # Fit to data, then transform
```

## Ennustaminen (Prediction)

**Ennusta luokat**
```python
y_pred = lr.predict(X_test)          # Ohjatut estimaattorit
y_pred = k_means.predict(X_test)     # Ohjaamattomat estimaattorit
```

**Arvioi luokan todennäköisyys**
```python
y_pred = knn.predict_proba(X_test)
```

## Mallin arviointi (Evaluate Your Model's Performance)

### Luokittelumetriikat (Classification Metrics)

**Accuracy Score**
```python
knn.score(X_test, y_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)
```

**Classification Report**
```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

**Confusion Matrix**
```python
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))
```

### Regressiometriikat (Regression Metrics)

**Mean Absolute Error**
```python
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, y_pred)
```

**Mean Squared Error**
```python
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)
```

**R² Score**
```python
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)
```

### Klusterointimetriikat (Clustering Metrics)

**Adjusted Rand Index**
```python
from sklearn.metrics import adjusted_rand_score
adjusted_rand_score(y_test, y_pred)
```

**Homogeneity**
```python
from sklearn.metrics import homogeneity_score
homogeneity_score(y_test, y_pred)
```

**V-measure**
```python
from sklearn.metrics import v_measure_score
v_measure_score(y_test, y_pred)
```

## Mallin viritys (Tune Your Model)

**Grid Search**
```python
from sklearn.model_selection import GridSearchCV
params = {'n_neighbors': np.arange(1, 3),
          'metric': ['euclidean', 'cityblock']}
grid = GridSearchCV(estimator=knn, param_grid=params)
grid.fit(X_train, y_train)
print(grid.best_score_)
print(grid.best_estimator_.n_neighbors)
```
