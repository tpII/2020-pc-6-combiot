from pdf417gen import encode, render_image
from combi.settings import MEDIA_ROOT
import requests
from bs4 import BeautifulSoup
import ast
from pyzxing import BarCodeReader


def codificador(data, reserva):
    # Convert to code words # columns default = 6, security_level default = 2
    codigo = encode(str(data), security_level=7)

    # Genera un codigo de barras como imagen
    imagen = render_image(codigo)
    imagen.save(MEDIA_ROOT + '/barcode.png')
    reserva.codigo = MEDIA_ROOT + '/barcode.png'
    reserva.save()


# ALTERNATIVA con un decodificador online externo
def decodificar_1():
    ff = [
        ('images', ('barcode.png', open(MEDIA_ROOT + '/barcode.png', 'rb'), 'image/png'))
    ]
    response = requests.post(
        url='https://zxing.org/w/decode',
        files=ff
    )
    html = BeautifulSoup(response.text, "html.parser")
    entradas = html.find_all('pre')
    datos = entradas[0]
    datos = str(datos)
    datos = datos[:-6]
    datos = datos[5:]
    datos = datos.replace("'", "\"")
    datos = ast.literal_eval(datos)
    return datos


# ALTERNATIVA pyzxing (Python + Java)
def decodificar_2():
    reader = BarCodeReader()
    results = reader.decode(MEDIA_ROOT + '/barcode.png')
    datos = results[0]['parsed'].replace("'", "\"")
    return ast.literal_eval(datos)
