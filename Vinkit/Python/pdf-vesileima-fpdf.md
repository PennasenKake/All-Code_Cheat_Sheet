<!-- tags: vinkit, python -->

# Python: PDF-vesileiman lisääminen (fpdf)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Esimerkki, jossa PDF-tiedostoon lisätään vinossa oleva vesileimateksti `fpdf`-kirjastolla ennen varsinaisen sisällön kirjoittamista.

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.set_text_color(200, 200, 200)
pdf.rotate(30)
pdf.text(40, 100, "WATERMARK SAMPLE")
pdf.rotate(0)
pdf.set_text_color(0, 0, 0)
pdf.text(10, 20, "Original PDF Content")
pdf.output("watermarked.pdf")
```

Idea: `rotate(30)` kääntää seuraavaksi piirrettävän tekstin 30 asteen kulmaan (vesileima), jonka jälkeen `rotate(0)` palauttaa kulman normaaliksi varsinaista sisältöä varten. Vaalean harmaa väri (`set_text_color(200, 200, 200)`) tekee vesileimasta huomaamattoman taustaelementin.
