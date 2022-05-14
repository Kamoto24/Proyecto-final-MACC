import time #Se importa el modulo time para separar algunas acciones en su ejecución
import tkinter as tk 
from tkinter import ttk #Se importa tkinter y ttk para la creación de todo lo que contine la interfaz gráfica
import carpetas 
import leer_imagen
import piedrapapelotijera #Se importan los archivos carpetas.py, leer_imagen.py y piedrapapelotijera.py para llamar las funciones dentro de estas cuando se requiera
intro="""
                                                                        BIENVENIDO A SU MULTITASKER

Para iniciar, tenga en cuenta que:
El MULTITASKER consta de 6 opciones para facilitar su trabajo, las cuales son:
1. Escribir información para posteriormente guardarla en el archivo que desee
2. Obtener la información que esta en el archivo que desee, para poder visualizarla desde BLOC DE NOTAS
3. Ordenar sus archivos según lo requiera, agrupando por carpetas con cierto nombre archivos con el mismo nombre
4. Usar una calculadora interactiva para hacer operaciones rápidas
5. Extraer texto de una imagen que contenga cadenas de caracteres
6. Jugar juegos adicionales como piedra, papel o tijera a modo de pasatiempo 

                                                                                      ¡Ya puede iniciar! 
"""
def popup(mensaje): #Funcion para generar un "popup" que imprime el texto que se defina en forma de ventana temporal
   top= tk.Toplevel(ventana)
   top.title("Mensaje")
   tk.Label(top, text= mensaje, font=(fonta),justify="left").pack()
   ttk.Button(top,text="Aceptar",style="TButton",command=top.destroy).pack()
def hide(): #Función para ocultar los botones, labels o cajas de texto que ya no se usen y dar paso a otras segun se requiera
    for i in hidelist:
        i.pack_forget()
    hidelist.clear()
def menu(): #Función con el menú principal del programa y todas las acciones que puede realizar
    hide()
    label1=tk.Label(ventana,text="¡Bienvenido! Por favor, elija una opción:",font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    opcion1=ttk.Button(ventana,text="Crear una nueva carpeta",style="TButton",command=crear_carpeta)
    opcion1.pack(pady=2)
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="Entrar en una carpeta existente", style="TButton",command=entrar_carpeta)
    opcion2.pack(pady=2)
    hidelist.append(opcion2)
    opcion3 = ttk.Button(ventana, text="Ordenar archivos", style="TButton",command=ordenar_archivos)
    opcion3.pack(pady=2)
    hidelist.append(opcion3)
    opcion4 = ttk.Button(ventana, text="Calculadora", style="TButton", command=calculadora)
    opcion4.pack(pady=2)
    hidelist.append(opcion4)
    opcion5 = ttk.Button(ventana, text="Extraer texto de imagen", style="TButton", command=lista_imagenes)
    opcion5.pack(pady=2)
    hidelist.append(opcion5)
    opcion6 = ttk.Button(ventana, text="Piedra, papel o tijera", style="TButton", command=elegir)
    opcion6.pack(pady=2)
    hidelist.append(opcion6)
    opcion7 = ttk.Button(ventana, text="Salir del programa", style="TButton",command=ventana.destroy)
    opcion7.pack(pady=2)
    hidelist.append(opcion7)
#Opcion 1: Crear carpetas
def save_archivo(nombre,data,carpeta,actualoption): #Funcion para guardar el archivo .txt creado y preguntar si desea crear otro o salir de la opción
    if actualoption==1:
        end=menu
    elif actualoption==2:
        end=entrar_carpeta
    contenido=data.get()
    carpetas.escribir_texto(nombre,contenido,carpeta)
    hide()
    label1 = tk.Label(ventana, text="¿Desea crear otro archivo?", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Si", style="TButton",command=lambda: crear_archivo(carpeta))
    opcion1.pack(pady=2)
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="No", style="TButton", command=end)
    opcion2.pack(pady=2)
    hidelist.append(opcion2)
def contenido_archivo(data,carpeta,actualoption): #Función que pide al usuario el contenido del archivo .txt
    nombre=data.get()
    hide()
    label1 = tk.Label(ventana, text="A continuacion, ingrese el contenido del archivo: ", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: save_archivo(nombre,entry1,carpeta,actualoption))
    confirm.pack()
    hidelist.append(confirm)
    #Poner mensaje
def crear_archivo(carpeta,actualoption): #Función que pide al usuario el nombre del archivo .txt
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre del archivo: ", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: contenido_archivo(entry1,carpeta,actualoption))
    confirm.pack()
    hidelist.append(confirm)
def save_carpeta(data,actualoption): #Funcion que guarda la carpeta creada y pregunta si desea crear un archivo en la carpeta o salir de la misma
    carpeta=data.get()
    if carpetas.existe(carpeta) == False:
        popup(carpetas.crear_carpeta(carpeta))
        hide()
        label1 = tk.Label(ventana, text="¿Que desea hacer en esta carpeta?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Crear un nuevo archivo", style="TButton", command=lambda: crear_archivo(carpeta,actualoption))
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="Salir de la carpeta", style="TButton", command=menu)
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
    else:
        popup("Esta carpeta ya existe, ingrese otro nombre")
        crear_carpeta()
def crear_carpeta(): #Archivo que pregunta al usuario el nombre de la carpeta a crear
    actualoption=1
    hide()
    label1=tk.Label(ventana,text="Ingrese el nombre de la carpeta: ",font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton",command= lambda:save_carpeta(entry1,actualoption))
    confirm.pack()
    hidelist.append(confirm)
#Opcion 2: Entrar en carpeta
def leer(data,carpeta): #Funcion que evalua si el archivo ingresado existe o no
    texto=data.get()
    ruta = str(carpeta) + str("/") + str(texto)
    exist = carpetas.existe(ruta)
    if exist==False: #Si no existe, notifica que el archivo no existe y pregunta si desea buscar otro o salir de la opción
        hide()
        label1 = tk.Label(ventana, text="El archivo no existe, ¿Desea buscar otro archivo?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton",command=entrar_archivo(carpeta))
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
    elif exist==True: #Si existe, imprime el contenido del archivo y pregunta si desea buscar otro o salir de la opción
        hide()
        txt=texto+".txt:\n\n"+carpetas.leer(ruta)
        popup(txt)
        label1 = tk.Label(ventana, text="¿Desea buscar otro archivo?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=entrar_archivo)
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=entrar_carpeta)
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
def entrar_archivo(carpeta): #Función que pide al usuario ingresar el nombre del archivo que desea buscar
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre del archivo a buscar: ", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: leer(entry1, carpeta))
    confirm.pack()
    hidelist.append(confirm)
def save_entrada(data,actualoption): #Funcion que evalua si la carpeta ingresada existe o no
    carpeta=data.get()
    exist=carpetas.existe(carpeta)
    if exist==False: #Si no existe, notifica al usuario que no existe y pregunta si desea buscar otra o salir de la opción
        hide()
        label1 = tk.Label(ventana, text="La carpeta no existe, ¿Desea buscar otra carpeta?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton",command=entrar_carpeta)
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
    elif exist==True: #Si existe, pregunta al usuario que desea hacer en esta carpeta, crear un archivo, leer un archivo o salir
        hide()
        label1 = tk.Label(ventana, text="¿Que desea hacer en esta carpeta?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Crear un nuevo archivo", style="TButton", command=lambda: crear_archivo(carpeta,actualoption))
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="Leer un archivo", style="TButton", command=lambda: entrar_archivo(carpeta))
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
        opcion3 = ttk.Button(ventana, text="Salir de la carpeta", style="TButton", command=menu)
        opcion3.pack(pady=2)
        hidelist.append(opcion3)
def entrar_carpeta(): #Funcion que pregunta al usuario el nombre de la carpeta a buscar
    actualoption=2
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre de la carpeta a buscar: ", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: save_entrada(entry1,actualoption))
    confirm.pack()
    hidelist.append(confirm)
#Opcion 3: Ordenar archivos
def continuar(): #Funcion que pregunta al usuario si desea ordenar mas archivos o salir de la opción
    hide()
    label1 = tk.Label(ventana, text="¿Desea ordenar mas archivos? ", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=ordenar_archivos)
    opcion1.pack(pady=2)
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
    opcion2.pack(pady=2)
    hidelist.append(opcion2)
def nombre_carpeta(carpeta): #Funcion que notifica que los archivos fueron ordenados con exito
    hide()
    carpetas.ordenar_nombre(carpeta)
    popup("Los archivos fueron ordenados con éxito")
    continuar()
def palabra_carpeta(carpeta,data): #Funcion que notifica que los archivos fueron ordenados con exito
    hide()
    clave=data.get()
    carpetas.ordenar_palabra(carpeta,clave)
    popup("Los archivos fueron ordenados con éxito")
    continuar()
def palabra_clave(carpeta): #Funcion que pregunta al usuario la palabra clave para ordenar los archivos
    hide()
    label1 = tk.Label(ventana, text="Ingrese la palabra clave para ordenar los archivos", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: palabra_carpeta(carpeta,entry1))
    confirm.pack()
    hidelist.append(confirm)
def tipo_carpeta(carpeta,data):  #Funcion que notifica que los archivos fueron ordenados con exito
    hide()
    sufijo="."+data.get()
    carpetas.ordenar_tipo(carpeta,sufijo)
    popup("Los archivos fueron ordenados con éxito")
    continuar()
def tipo_sufijo(carpeta): #Funcion que pregunta al usuario el sufijo para ordenar los archivos
    hide()
    label1 = tk.Label(ventana, text="Ingrese la extensión para ordenar los archivos: ", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda: tipo_carpeta(carpeta,entry1))
    confirm.pack()
    hidelist.append(confirm)
def tipo_orden(data): #Funcion que evalua si la carpeta ingresada existe
    carpeta = data.get()
    exist = carpetas.existe(carpeta)
    if exist == False: #Si no existe, notifica al usuario que no existe y pregunta si desea buscar otra o salir de la opción
        hide()
        label1 = tk.Label(ventana, text="La carpeta no existe, ¿Desea buscar otra carpeta?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=ordenar_archivos)
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
    elif exist == True: #Si existe, pregunta al usuario si desea ordenar los archivos por nombre de la carpeta, palabra clave o sufijo
        hide()
        label1 = tk.Label(ventana, text="¿Como desea ordenar los archivos?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Archivos que contengan el nombre de esta carpeta", style="TButton",command=lambda: nombre_carpeta(carpeta))
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="Archivos que contengan cierto nombre", style="TButton", command=lambda: palabra_clave(carpeta))
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
        opcion3 = ttk.Button(ventana, text="Archivos de cierta extensión", style="TButton", command=lambda : tipo_sufijo(carpeta))
        opcion3.pack(pady=2)
        hidelist.append(opcion3)
def ordenar_archivos(): #Funcion que pregunta al usuario en que carpeta desea ordenar los archivos
    hide()
    label1 = tk.Label(ventana, text="¿En que carpeta desea ordenar los archivos?", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda : tipo_orden(entry1))
    confirm.pack()
    hidelist.append(confirm)
#Opcion 4: Calculadora
def calculadora(): #Funcion que abre la calculadora
    import calculadora
    widget_principal = calculadora.Tk()
    calculadora.Interfaz(widget_principal)
    widget_principal.mainloop()
#Opcion 5: Leer texto de imagen
def extraerTextoDeImagen(imagen,idioma): #Imprime el texto extraido de la imagen y pregunta si desea ingresar otra imagen o salir de la opción
    text=leer_imagen.extraerTextoDeImagen(imagen,idioma)
    hide()
    popup(text)
    label1 = tk.Label(ventana, text="¿Desea extraer texto de otra imagen?", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=lista_imagenes)
    opcion1.pack(pady=2)
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
    opcion2.pack(pady=2)
    hidelist.append(opcion2)
def idioma_imagen(data): #Funcion pide al usuario la imagen para extraer el texto
    imagen=data.get()
    exist = carpetas.existe(imagen)
    if exist == False: #Si no existe, notifica al usuario que la imagen no existe y le pregunta si desea ingresar otra o salir de la opción
        hide()
        label1 = tk.Label(ventana, text="La imagen no existe, ¿Desea buscar otra imagen?", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=lista_imagenes)
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
    if exist==True: #Si existe, pide el idioma en el que desee el programa, español o inglés
        hide()
        label1 = tk.Label(ventana, text="Seleccione el idioma de la imagen", font=fonta)
        label1.pack(pady=10)
        hidelist.append(label1)
        opcion1 = ttk.Button(ventana, text="Español", style="TButton", command=lambda : extraerTextoDeImagen(imagen,"spa"))
        opcion1.pack(pady=2)
        hidelist.append(opcion1)
        opcion2 = ttk.Button(ventana, text="Inglés", style="TButton", command=lambda: extraerTextoDeImagen(imagen,"eng"))
        opcion2.pack(pady=2)
        hidelist.append(opcion2)
def lista_imagenes(): #Función que pide al usuario la imagen que desee
    hide()
    label1 = tk.Label(ventana, text="Ingrese el nombre de la imagen (junto con su extensión)", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=2)
    hidelist.append(entry1)
    confirm = ttk.Button(ventana, text="Confirmar", style="TButton", command=lambda : idioma_imagen(entry1))
    confirm.pack()
    hidelist.append(confirm)
#Opción 6: Piedra, papel o tijera
def resultado(objeto): #Muestra al usuario la opción que eligio, como terminó el juego y pregunta si quiere jugar otra vez
    hide()
    texto=piedrapapelotijera.jugar(objeto)
    popup(texto)
    label1 = tk.Label(ventana, text="¿Desea jugar de nuevo?", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Si", style="TButton", command=elegir)
    opcion1.pack(pady=2)
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="No", style="TButton", command=menu)
    opcion2.pack(pady=2)
    hidelist.append(opcion2)
def elegir(): #Función que pregunta al usuario el elemento con el que desea jugar
    hide()
    label1 = tk.Label(ventana, text="¿Con que elemento desea jugar?", font=fonta)
    label1.pack(pady=10)
    hidelist.append(label1)
    opcion1 = ttk.Button(ventana, text="Piedra", style="TButton", command=lambda: resultado("piedra"))
    opcion1.pack(pady=2)
    hidelist.append(opcion1)
    opcion2 = ttk.Button(ventana, text="Papel", style="TButton", command=lambda: resultado("papel"))
    opcion2.pack(pady=2)
    hidelist.append(opcion2)
    opcion3 = ttk.Button(ventana, text="Tijera", style="TButton", command=lambda: resultado("tijera"))
    opcion3.pack(pady=2)
    hidelist.append(opcion3)
#Declaracion de variables
ventana=tk.Tk(className="Multitasker")
ventana.geometry("500x600") #Crea la ventana principal
fonta="Gadugi 18" #Fuente del texto del programa
ttk.Style(ventana).configure('TButton', font=(fonta))
actualoption=0 #Variable para saber que opción se encuentra en uso
hidelist=[] #Lista de los labels, botones y entradas a eliminar
menu() #Llama a la funcion menu para crearlo
time.sleep(1) #Delay de 1 segundo par separar ambas ventanas
popup(intro) #Llamado a la función popup para crear una ventana con un texto introductorio previamente declarado
ventana.mainloop()
