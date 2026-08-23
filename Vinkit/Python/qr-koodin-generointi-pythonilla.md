<!-- tags: vinkit, python -->

# QR-koodin generointi Pythonilla

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Yksinkertainen tapa generoida QR-koodi tekstistä tai URL-osoitteesta `qrcode`-kirjastolla.

## Koodi

```python
import qrcode

data = input("Enter text or URL: ")

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR code generated successfully!")

# source code --> clcoding.com
```

## Esimerkkiajo

```
Enter text or URL:  Hello Python
QR code generated successfully!
```

Ohjelma tallentaa generoidun QR-koodin `qrcode.png`-tiedostoon.

## Huomio

Vaatii `qrcode`-kirjaston asennuksen: `pip install qrcode[pil]`
