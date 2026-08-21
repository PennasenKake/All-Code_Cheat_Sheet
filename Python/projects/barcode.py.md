<!-- tags: python -->

# barcode.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/projects/barcode.py)

```python
import Python.valmiit.barcode as barcode
from barcode.writer import ImageWriter
from IPhython.display import Image, display

def generate_barcode(data):
    Barcodeclass = barcode.get_barcode_class('code128')
    code = Barcodeclass(data, writer=ImageWriter())
    barcode_filename = code.save("barcode")

    print("Generating barcode")

    display(Image(filename=barcode_filename))

data = '1234-5678-9101'
generate_barcode(data)
```
