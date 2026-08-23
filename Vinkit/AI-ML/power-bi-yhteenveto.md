<!-- tags: vinkit, ai-ml -->

# Power BI pähkinänkuoressa

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Tiivis yhteenveto Power BI:n keskeisistä käsitteistä: työnkulku, datamalli, visualisoinnit, DAX ja julkaisu.

## Työnkulku (5 vaihetta)

1. **Connect** – yhdistä dataan useista lähteistä (Excel, tietokannat, pilvi).
2. **Transform** – siivoa, muokkaa ja muunna data Power Queryssä.
3. **Model** – rakenna taulujen väliset relaatiot ja datamalli.
4. **Visualize** – luo interaktiivisia raportteja rikkailla visualisoinneilla.
5. **Share** – julkaise ja jaa oivalluksia, tue datavetoista päätöksentekoa.

## Datamalli: taulut ja relaatiot

Suositeltu rakenne on **tähtimalli (star schema)** – paras suorituskyvyn ja helpon analysoinnin kannalta. Esimerkkirakenne:

- **Date** (DateID, Date, Month, Quarter, Year)
- **Product** (ProductID, ProductName, Category, SubCategory)
- **Customer** (CustomerID, CustomerName, City, Segment)
- **Store** (StoreID, StoreName, City, Region)
- **Sales** (faktataulu keskellä: DateID, ProductID, CustomerID, StoreID, SalesAmount, Quantity, Discount) – yhdistyy kaikkiin ulottuvuustauluihin.

### Relaatiotyypit

- **One-to-Many (1 → *)** – yleisin relaatiotyyppi.
- **One-to-One (1 → 1)** – harvinaisempi.
- **Many-to-Many (* → *)** – käytettävä varoen.

## Power BI -visualisoinnit

Card, Bar Chart, Line Chart, Column Chart, Pie/Donut, Table, Matrix, Map, Slicer.

## DAX-perusteet

- `MEASURE` – laskettu arvo, jota käytetään visualisoinneissa.
- `SUM()` – laskee arvot yhteen.
- `COUNT()` – laskee rivien määrän.
- `AVERAGE()` – laskee arvojen keskiarvon.
- `CALCULATE()` – muuttaa suodatuskontekstia.
- `FILTER()` – suodattaa taulun.

DAX = Data Analysis Expressions, Power BI:n kaavakieli.

Esimerkkimitta:

```dax
Total Sales =
CALCULATE(
    SUM(Sales[SalesAmount]),
    Sales[Discount] > 0
)
```

## Suodatuskonteksti (Filter Context)

Suodatuskonteksti ratkaisee, mikä data on näkyvissä laskelmille ja visualisoinneille. Ilman suodatinta näkyy kaikki data; suotimen/slicerin kanssa vain suodatettu data näkyy ja vaikuttaa laskentaan.

## Julkaisu ja jako

1. Luo raportti Power BI:ssä.
2. Julkaise Power BI -palveluun.
3. Jaa tiimin tai organisaation kanssa.
4. Suojaa rivitason tietoturvalla (Row-Level Security).

## Power BI:n komponentit

Reports, Dashboards, Datasets, Workspaces, Apps.
