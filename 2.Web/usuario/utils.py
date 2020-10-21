from pdf417gen import encode, render_image
import os


def codificador(data):
    # Convert to code words # columns default = 6, security_level default = 2
    codes = encode(str(data), security_level=7)

    # Genera un codigo de barras como imagen
    imagen = render_image(codes)
    dir_save = os.path.dirname(os.path.abspath(__file__))
    imagen.save(dir_save + 'imagenes/codigo.jpg')
