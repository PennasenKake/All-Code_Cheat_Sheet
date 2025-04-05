import barcode
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