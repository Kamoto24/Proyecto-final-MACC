import os
import shutil
import pathlib
from pathlib import Path
def crear_carpeta(carpeta):
    os.mkdir(carpeta)
    return "la carpeta '"+carpeta+"' ha sido creada con éxito"
def escribir_texto(texto,contenido,carpeta):
    f = open(texto, "w")
    f.write(contenido)
    f.close()
    mover(texto,carpeta)
    return "El archivo '"+texto+"' ha sido creado con exito"
def existe(multimedia):
    return os.path.exists(multimedia)
def mover(media,destino):
    shutil.move(media,destino)
def leer(ruta):
    f = open(ruta, "r")
    contenido = f.read()
    f.close
    return contenido
def ordenar_nombre(carpeta):
    local = pathlib.Path(__file__).parent.absolute()
    contenido = os.listdir(local)
    for i in contenido:
        for j in range(0,len(i)-len(carpeta)):
            if carpeta == i[j:j+len(carpeta)]:
                mover(i,carpeta)
def ordenar_palabra(carpeta,clave):
    local = pathlib.Path(__file__).parent.absolute()
    contenido = os.listdir(local)
    for i in contenido:
        for j in range(0,len(i)-len(clave)):
            if clave == i[j:j+len(clave)]:
                mover(i,carpeta)
def ordenar_tipo(carpeta,sufijo):
    local = pathlib.Path(__file__).parent.absolute()
    contenido = os.listdir(local)
    for i in range(0,len(contenido)):
        p=Path(contenido[i])
        if p.suffix==sufijo:
            mover(p.name, carpeta)