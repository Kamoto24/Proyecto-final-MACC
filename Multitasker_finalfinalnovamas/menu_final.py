import tkinter as tk
from tkinter import ttk
import carpetas
import leer_imagen
intro="""BIENVENIDO A LA INTERFAZ DE SU BLOC DE NOTAS"
----------------------------------------------------------------
PARA INICIAR, RECUERDE TENER EN CUENTA QUE:
El BLOC DE NOTAS consta de tres opciones para facilitar su trabajo, las cuales son:
1.Escribir información para posteriormente guardarla en el archivo que desee
2.Obtener la información que esta en el archivo que desee, para poder visualizarla desde BLOC DE NOTAS
3.Ordenar sus archivos según lo requiera, agrupando por carpetas con cierto nombre archivos con el mismo nombre
¡Ya puede iniciar!
----------------------------------------------------------------"""
def popup(mensaje):
   top= tk.Toplevel(ventana)
   top.title("Mensaje")
   tk.Label(top, text= mensaje, font=(fonta)).pack()
   ttk.Button(top,text="Aceptar",style="TButton",command=top.destroy).pack()
def hide():
    for i in hidelist:
        i.pack_forget()
    hidelist.clear()
def menu():
    hide()
    label1=tk.Label(ventana,text="¡Bienvenido! Por favor, elija una opción:",font=fonta)
    label1.pack()
    hidelist.append(label1)
    opcion1=ttk.Button(ventana,text="Crear una nueva carpeta",style="TButton",command=crear_carpeta)
    opcion1.pack()
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="Entrar en una carpeta existente", style="TButton",command=entrar_carpeta)
    opcion2.pack()
    hidelist.append(opcion2)
    opcion3 = ttk.Button(ventana, text="Ordenar archivos", style="TButton",command=ordenar_archivos)
    opcion3.pack()
    hidelist.append(opcion3)
    opcion4 = ttk.Button(ventana, text="Calculadora", style="TButton", command=calculadora)
    opcion4.pack()
    hidelist.append(opcion4)
    opcion5 = ttk.Button(ventana, text="Extraer texto de imagen", style="TButton", command=carpeta_imagenes)
    opcion5.pack()
    hidelist.append(opcion5)
    opcion6 = ttk.Button(ventana, text="Salir del programa", style="TButton",command=ventana.destroy)
    opcion6.pack()
    hidelist.append(opcion6)
#Opcion 1: Crear carpetas
def save_archivo(nombre,data,carpeta,actualoption):
    if actualoption==1:
        end=menu
    elif actualoption==2:
        end=entrar_carpeta
    contenido=data.get()
    carpetas.escribir_texto(nombre,contenido,carpeta)
    hide()
    label1 = tk.Label(ventana, text="¿Desea crear otro archivo?", font=fonta)
    label1.pack()
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Si", style="TButton",command=lambda: crear_archivo(carpeta))
    opcion1.pack()
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="No", style="TButton", command=end)
    opcion2.pack()
    hidelist.append(opcion2)
def contenido_archivo(data,carpeta,actualoption):
    nombre=data.get()
    hide()
    label1 = tk.Label(ventana, text="A continuacion, ingrese el contenido del archivo: ", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: save_archivo(nombre,entry1,carpeta,actualoption))
    confirm.pack()
    hidelist.append(confirm)
    #Poner mensaje
def crear_archivo(carpeta,actualoption):
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre del archivo: ", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: contenido_archivo(entry1,carpeta,actualoption))
    confirm.pack()
    hidelist.append(confirm)
def save_carpeta(data,actualoption):
    carpeta=data.get()
    if carpetas.existe(carpeta) == False:
        popup(carpetas.crear_carpeta(carpeta))
        hide()
        label1 = tk.Label(ventana, text="¿Que desea hacer en esta carpeta?", font=fonta)
        label1.pack()
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Crear un nuevo archivo", style="TButton", command=lambda: crear_archivo(carpeta,actualoption))
        opcion1.pack()
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="Salir de la carpeta", style="TButton", command=menu)
        opcion2.pack()
        hidelist.append(opcion2)
    else:
        popup("Esta carpeta ya existe, ingrese otro nombre")
        crear_carpeta()
def crear_carpeta():
    actualoption=1
    hide()
    label1=tk.Label(ventana,text="Ingrese el nombre de la carpeta: ",font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton",command= lambda:save_carpeta(entry1,actualoption))
    confirm.pack()
    hidelist.append(confirm)
#Opcion 2: Entrar en carpeta
def leer(data,carpeta):
    texto=data.get()
    ruta = str(carpeta) + str("/") + str(texto)
    exist = carpetas.existe(ruta)
    if exist==False:
        hide()
        label1 = tk.Label(ventana, text="El archivo no existe, ¿Desea buscar otro archivo?", font=fonta)
        label1.pack()
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton",command=entrar_archivo(carpeta))
        opcion1.pack()
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
        opcion2.pack()
        hidelist.append(opcion2)
    elif exist==True:
        hide()
        txt=texto+"\n"+carpetas.leer(ruta)
        popup(txt)
        label1 = tk.Label(ventana, text="¿Desea buscar otro archivo?", font=fonta)
        label1.pack()
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=entrar_archivo)
        opcion1.pack()
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=entrar_carpeta)
        opcion2.pack()
        hidelist.append(opcion2)
def entrar_archivo(carpeta):
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre del archivo a buscar: ", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: leer(entry1, carpeta))
    confirm.pack()
    hidelist.append(confirm)
def save_entrada(data,actualoption):
    carpeta=data.get()
    exist=carpetas.existe(carpeta)
    if exist==False:
        hide()
        label1 = tk.Label(ventana, text="La carpeta no existe, ¿Desea buscar otra carpeta?", font=fonta)
        label1.pack()
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton",command=entrar_carpeta)
        opcion1.pack()
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
        opcion2.pack()
        hidelist.append(opcion2)
    elif exist==True:
        hide()
        label1 = tk.Label(ventana, text="¿Que desea hacer en esta carpeta?", font=fonta)
        label1.pack()
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Crear un nuevo archivo", style="TButton", command=lambda: crear_archivo(carpeta,actualoption))
        opcion1.pack()
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="Leer un archivo", style="TButton", command=lambda: entrar_archivo(carpeta))
        opcion2.pack()
        hidelist.append(opcion2)
        opcion3 = ttk.Button(ventana, text="Salir de la carpeta", style="TButton", command=menu)
        opcion3.pack()
        hidelist.append(opcion3)
def entrar_carpeta():
    actualoption=2
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre de la carpeta a buscar: ", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: save_entrada(entry1,actualoption))
    confirm.pack()
    hidelist.append(confirm)
#Opcion 3: Ordenar archivos
def continuar():
    hide()
    label1 = tk.Label(ventana, text="¿Desea ordenar mas archivos? ", font=fonta)
    label1.pack()
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=ordenar_archivos)
    opcion1.pack()
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
    opcion2.pack()
    hidelist.append(opcion2)
def nombre_carpeta(carpeta):
    hide()
    carpetas.ordenar_nombre(carpeta)
    popup("Los archivos fueron ordenados con éxito")
    continuar()
def palabra_carpeta(carpeta,data):
    hide()
    clave=data.get()
    carpetas.ordenar_palabra(carpeta,clave)
    popup("Los archivos fueron ordenados con éxito")
    continuar()
def palabra_clave(carpeta):
    hide()
    label1 = tk.Label(ventana, text="Ingrese la palabra clave para ordenar los archivos", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: palabra_carpeta(carpeta,entry1))
    confirm.pack()
    hidelist.append(confirm)
def tipo_carpeta(carpeta,data):
    hide()
    sufijo="."+data.get()
    carpetas.ordenar_tipo(carpeta,sufijo)
    popup("Los archivos fueron ordenados con éxito")
    continuar()
def tipo_sufijo(carpeta):
    hide()
    label1 = tk.Label(ventana, text="Ingrese la extensión para ordenar los archivos: ", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: tipo_carpeta(carpeta,entry1))
    confirm.pack()
    hidelist.append(confirm)
def tipo_orden(data):
    carpeta = data.get()
    exist = carpetas.existe(carpeta)
    if exist == False:
        hide()
        label1 = tk.Label(ventana, text="La carpeta no existe, ¿Desea buscar otra carpeta?", font=fonta)
        label1.pack()
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=ordenar_archivos)
        opcion1.pack()
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
        opcion2.pack()
        hidelist.append(opcion2)
    elif exist == True:
        hide()
        label1 = tk.Label(ventana, text="¿Como desea ordenar los archivos?", font=fonta)
        label1.pack()
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Archivos que contengan el nombre de esta carpeta", style="TButton",command=lambda: nombre_carpeta(carpeta))
        opcion1.pack()
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="Archivos que contengan cierto nombre", style="TButton", command=lambda: palabra_clave(carpeta))
        opcion2.pack()
        hidelist.append(opcion2)
        opcion3 = ttk.Button(ventana, text="Archivos de cierta extensión", style="TButton", command=lambda : tipo_sufijo(carpeta))
        opcion3.pack()
        hidelist.append(opcion3)
def ordenar_archivos():
    hide()
    label1 = tk.Label(ventana, text="¿En que carpeta desea ordenar los archivos?", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda : tipo_orden(entry1))
    confirm.pack()
    hidelist.append(confirm)
#Opcion 4: Calculadora
def calculadora():
    import calculadora
    widget_principal = calculadora.Tk()
    calculadora.Interfaz(widget_principal)
    widget_principal.mainloop()
#Opcion 5: Leer texto de imagen
def extraerTextoDeImagen(imagen):
    text=leer_imagen.extraerTextoDeImagen(imagen)
    hide()
    popup(text)
    label1 = tk.Label(ventana, text="¿Desea extraer texto de otra imagen?", font=fonta)
    label1.pack()
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=carpeta_imagenes)
    opcion1.pack()
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
    opcion2.pack()
    hidelist.append(opcion2)
def idioma_imagen(data):
    imagen=data.get()
    hide()
    label1 = tk.Label(ventana, text="Seleccione el idioma de la imagen", font=fonta)
    label1.pack()
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Español", style="TButton", command=lambda : extraerTextoDeImagen(imagen))
    opcion1.pack()
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="Inglés", style="TButton", command=lambda: extraerTextoDeImagen(imagen))
    opcion2.pack()
    hidelist.append(opcion2)
def lista_imagenes(data):
    carpeta=data.get()
    hide()
    label1 = tk.Label(ventana, text=leer_imagen.listaImagen(carpeta), font=fonta)
    label1.pack()
    hidelist.append(label1)
    label2 = tk.Label(ventana, text="Ingrese el nombre de la imagen (junto con su extensión)", font=fonta)
    label2.pack()
    hidelist.append(label2)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda : idioma_imagen(entry1))
    confirm.pack()
    hidelist.append(confirm)
def carpeta_imagenes():
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre de la carpeta con las imágenes", font=fonta)
    label1.pack()
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack()
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda : lista_imagenes(entry1))
    confirm.pack()
    hidelist.append(confirm)
#Declaracion de variables
ventana=tk.Tk(className="Multitasker")
ventana.geometry("500x600")
fonta="Gadugi 16"
ttk.Style(ventana).configure('TButton', font=(fonta))
actualoption=0
hidelist=[]
popup(intro)
menu()
ventana.mainloop()