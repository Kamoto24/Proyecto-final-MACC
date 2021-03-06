import os
from PIL import Image  # para poder abrir una imagen
import pytesseract as reconocimientoImagenes

reconocimientoImagenes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def verArchivos(extension="todas"):
    contenido = os.listdir()
    archivosAMostrar = []
    if extension == "todas":
        archivosAMostrar = contenido
    else:
        for i in range(len(contenido)):
            archivo = contenido[i]
            archivoConExtencionSeparada = os.path.splitext(archivo)
            extencionDeArchivo = archivoConExtencionSeparada[1]
            if extension == extencionDeArchivo:
                archivosAMostrar.append(archivo)
    return archivosAMostrar


def listaImagen():
    archivosJPG = verArchivos(".jpg")
    archivosPNG = verArchivos(".png")

    if archivosJPG == [] and archivosPNG == []:
        return None
    else:
        return  archivosJPG, archivosPNG

def idiomaImagen():
        opcion = int(input("Seleccione el idioma \n 1. Español \n 2. Inglés\n"))
        if opcion == 1: idioma = "spa"
        if opcion == 2: idioma = "eng"
def extraerTextoDeImagen(nombreDeImagen,idioma):
        imagenLectura = Image.open(nombreDeImagen)
        try:
            textoDeImagen = reconocimientoImagenes.image_to_string(imagenLectura, lang=idioma)
            return"TEXTO EXTRAIDO: \n", textoDeImagen
        except:
            return"No se puede realizar el reconocimiento de imágen porque ´tesseract´ no está instalado  "

#print(verArchivos(".jpg"))
#print(extraerTextoDeImagen("E.jpg","eng"))
