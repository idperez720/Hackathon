import qrcode
from PIL import Image


def qrspam(codigo_servicio):
    imagen = qrcode.make(codigo_servicio)
    nombre_imagen = codigo_servicio
    archivo_imagen = open('./QRTemp/' + nombre_imagen+".png", "wb")
    imagen.save(archivo_imagen)
    archivo_imagen.close()

    return './QRTemp/' + nombre_imagen+".png"
