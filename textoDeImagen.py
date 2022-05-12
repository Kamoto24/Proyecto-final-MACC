import os
from PIL import Image #para poder abrir una imagen
import pytesseract as reconocimientoImagenes

reconocimientoImagenes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def verArchivos(extencion = "todas"):
    #nombreDeCarpeta = input("Ingrese el nombre de la carpeta: ")
    contenido = os.listdir()
    archivosAMostrar = []
    if extencion =="todas":
        archivosAMostrar = contenido
        
    else:
        for i in range (len(contenido)):
            archivo = contenido[i]
            archivoConExtencionSeparada = os.path.splitext(archivo)
            extencionDeArchivo = archivoConExtencionSeparada[1]
            #print(extencionDeArchivo)
            if extencion == extencionDeArchivo:
                archivosAMostrar.append(archivo)
    
    return archivosAMostrar

def extraerTextoDeImagen():
    archivosJPG = verArchivos(".jpg")
    archivosPNG = verArchivos(".png")
    
    if archivosJPG == [] and archivosPNG == []:
        print ("En la carpeta no hay archivos con las extenciones jpg o png")
    else:
        print("Las imágenes en esta carpeta son: ",  archivosJPG, " y ", archivosPNG)
        

        nombreDeImagen = input("Ingrese el nombre de la imagen (junto con su extención): ")
        opcion= int(input("Seleccione el idioma \n 1. Español \n 2. Inglés\n"))
        if opcion ==1: idioma = "spa"
        if opcion ==2: idioma = "eng"
        imagenLectura = Image.open(nombreDeImagen)
        try:
            textoDeImagen = reconocimientoImagenes.image_to_string(imagenLectura, lang = idioma)
            print("TEXTO EXTRAIDO: \n", textoDeImagen )
        except: 
            print("No se puede realizar el reconocimiento de imágen porque ´tesseract´ no está instalado  ")

#print(verArchivos(".jpg"))
#extraerTextoDeImagen()