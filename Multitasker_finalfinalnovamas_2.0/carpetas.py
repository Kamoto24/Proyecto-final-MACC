import os #Se importa la libreria os para el manejo de rutas y creacion de carpetas
import shutil #Se importa la libreria shutil para mover archivos con mas facilidad
import pathlib
from pathlib import Path #Se importa pathlib y Path para coordinar las rutas principales y nombres de archivos
def crear_carpeta(carpeta): #Función para crear una carpeta con el nombre que ponga el usuario
    os.mkdir(carpeta)
    return "la carpeta '"+carpeta+"' ha sido creada con éxito"
def escribir_texto(texto,contenido,carpeta): #Función para crear un archivo .txt con el nombre y el texto introducido, en la carpeta establecida
    f = open(texto, "w")
    f.write(contenido)
    f.close()
    mover(texto,carpeta)
    return "El archivo '"+texto+"' ha sido creado con exito"
def existe(multimedia): #Funcion que evalua si una carpeta o archivo ya existe para evitar errores
    return os.path.exists(multimedia)
def mover(media,destino): #Funcion para mover un archivo al destino que se requiera
    shutil.move(media,destino)
def leer(ruta): #Funcion para leer el contenido de algun archivo .txt ya existente definido por el usuario
    f = open(ruta, "r")
    contenido = f.read()
    f.close
    return contenido
def ordenar_nombre(carpeta): #Función para ordenar archivos que contengan el nombre de la carpeta destino
    local = pathlib.Path(__file__).parent.absolute()
    contenido = os.listdir(local)
    for i in contenido:
        for j in range(0,len(i)-len(carpeta)):
            if carpeta == i[j:j+len(carpeta)]:
                mover(i,carpeta)
def ordenar_palabra(carpeta,clave): #Función para ordenar archivos que contengan cierto nombre o palabra clave en la carpeta destino
    local = pathlib.Path(__file__).parent.absolute()
    contenido = os.listdir(local)
    for i in contenido:
        for j in range(0,len(i)-len(clave)):
            if clave == i[j:j+len(clave)]:
                mover(i,carpeta)
def ordenar_tipo(carpeta,sufijo): #Función para ordenar archivos que contengan cierto sufijo en la carpeta destino
    local = pathlib.Path(__file__).parent.absolute()
    contenido = os.listdir(local)
    for i in range(0,len(contenido)):
        p=Path(contenido[i])
        if p.suffix==sufijo:
            mover(p.name, carpeta)
