

from tkinter import Tk,Text,Button,END,re

class Interfaz:
#funciones a usar
    #Crea un botón, por parametro solo recibe el numero que se quiere poner en el boton.
    def crearlosbotones(self, numero, escribir=True, ancho=7, alto=2):
        return Button(self.emergente, text=numero, width=ancho, height=alto, font=("Comic Sans MS",10), command=lambda:self.click(numero,escribir))
    
    def click(self, texto, escribir):
        #Cuando'escribir' es True, el texto se muestra. Si es False, no.
        if not escribir:
           if texto=="=" and self.operacion!="":
                #Si se presiona = y hay algo para operar.Se cambia valor de dividir por el slash.
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                resultado=str(eval(self.operacion))
                self.operacion=""
                self.limpiarlacaja()
                self.escribirenlacaja(resultado)
            #Si se presionó el botón de borrado, limpiar la caja
           elif texto==u"\u232B":#u232B significa borrar
                self.operacion=""
                self.limpiarlacaja()
        else:
            self.operacion+=str(texto)
            self.escribirenlacaja(texto)
        return
    
    def limpiarlacaja(self):
        self.caja.configure(state="normal")
        self.caja.delete("1.0", END)
        self.caja.configure(state="disabled")
        return
    
    def escribirenlacaja(self, numero):
        self.caja.configure(state="normal")
        self.caja.insert(END, numero)
        self.caja.configure(state="disabled")
        return
#CONTRUCTOR
    def __init__(self, emergente):
        #Inicializar la ventana con un título
        self.emergente=emergente
        self.emergente.title("Calculadora FINAL")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.caja=Text(emergente, state="disabled", width=20, height=9, background="gold", foreground="midnight blue", font=("Comic Sans MS",8))

        #Ubicar la pantalla en la ventana
        self.caja.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        #Inicializar la operación mostrada en la caja como string vacío
        self.operacion=""

        #Crear los botones de la calculadora
        boton_num_1=self.crearlosbotones(7)
        boton_num_2=self.crearlosbotones(8)
        boton_num_3=self.crearlosbotones(9)
        boton_num_4=self.crearlosbotones(u"\u232B",escribir=False)#borrar
        boton_num_5=self.crearlosbotones(4)
        boton_num_6=self.crearlosbotones(5)
        boton_num_7=self.crearlosbotones(6)
        boton_num_8=self.crearlosbotones(u"\u00F7")#dividir
        boton_num_9=self.crearlosbotones(1)
        boton_num_10=self.crearlosbotones(2)
        boton_num_11=self.crearlosbotones(3)
        boton_num_12=self.crearlosbotones("*")
        boton_num_13=self.crearlosbotones(".")
        boton_num_14=self.crearlosbotones(0)
        boton_num_15=self.crearlosbotones("+")
        boton_num_16=self.crearlosbotones("-")
        boton_num_17=self.crearlosbotones("=",escribir=False,ancho=7,alto=2)

        
        botones=[boton_num_1, boton_num_2,boton_num_3,boton_num_4,boton_num_5,boton_num_6,boton_num_7,boton_num_8,boton_num_9,boton_num_10,boton_num_11,boton_num_12, boton_num_13,boton_num_14,boton_num_15,boton_num_16, boton_num_17]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        #Ubicar el último botón al final
        botones[16].grid(row=5,column=0,columnspan=4)
        
        return


    


    


widget_principal=Tk()
calculadora=Interfaz(widget_principal)
widget_principal.mainloop()