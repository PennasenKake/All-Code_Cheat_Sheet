<!-- tags: python -->

# map.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/projects/map.py)

```python
import plotly.express as px
import pandas as pd

country = input("Mitä maata haluat tarkastella?: ")

data = pd.DataFrame({
    'country': [country],
    'values': [100]
})

fig = px.choropleth(
    data_frame=data,
    locations='country',
    locationmode="country names",
    color="values",
    hover_name="country",
    color_continuous_scale="Inferno",
    title=f'Maakartta: {country} korostettuna'
)

#fig.show()

fig.write_html("kartta4.html")
```
