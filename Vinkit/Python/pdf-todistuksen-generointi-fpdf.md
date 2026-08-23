<!-- tags: vinkit, python -->

# Python: PDF-todistuksen generointi (fpdf)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Yksinkertainen esimerkki suoritustodistuksen (certificate of completion) generoimisesta PDF-tiedostoksi `fpdf`-kirjastolla.

```python
from fpdf import FPDF

name = "John Doe"

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 24)
pdf.text(40, 80, "Certificate of Completion")
pdf.set_font("Arial", "", 18)
pdf.text(40, 100, f"Presented to {name}")
pdf.output("certificate.pdf")
```

Tuloksena syntyy `certificate.pdf`, jossa lukee otsikkona "Certificate of Completion" ja sen alla "Presented to John Doe". Nimi (`name`-muuttuja) voi tulla esimerkiksi käyttäjän syötteestä tai listasta, jolloin sama koodi voidaan ajaa monelle henkilölle todistusten joukkotuotantona.
