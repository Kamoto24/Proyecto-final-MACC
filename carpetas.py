import os
import shutil
option=1
while option>0:
    print("""¡Bienvenido! Seleccione la acción que desea realizar:
    1: Crear una nueva carpeta
    2: Entrar en una carpeta existente
    3: Salir del programa""")
    option=int(input("Digite la opción: "))
    while option !=1 and option !=2 and option !=3:
        int(input("Ingrese una opción válida: "))
    while option==1:
        suboption=0
        carpeta = input("Ingrese el nombre de la carpeta: ")
        os.mkdir(carpeta)
        print("la carpeta",carpeta,"ha sido creada con éxito")
        print("""¿Que desea hacer en esta carpeta?
        1: Crear un archivo
        2: Salir de la carpeta""")
        suboption=int(input("Digite la opción: "))
        while suboption==1:
            texto=input("Ingrese el nombre del archivo: ")
            f=open(texto,"w")
            contenido=input("A continuación, escriba el contenido del archivo:\n")
            f.write(contenido)
            f.close()
            shutil.move(texto, carpeta)
            print("El archivo",texto,"ha sido creado con exito")
            print("""¿Desea crear otro archivo?
            1: Si
            2: No""")
            suboption=int(input("Digite la opción: "))
        break
    while option==2:
        carpeta = input("Ingrese el nombre de la carpeta a buscar: ")
        exist=os.path.exists(carpeta)
        while exist==True:
            suboption=0
            print("""¿Que desea hacer en esta carpeta?
            1: Crear un archivo
            2: Leer un archivo
            3: Salir de la carpeta""")
            suboption = int(input("Digite la opción: "))
            while suboption == 1:
                texto = input("Ingrese el nombre del archivo: ")
                f = open(texto, "w")
                contenido = input("A continuación, escriba el contenido del archivo:\n")
                f.write(contenido)
                f.close()
                shutil.move(texto, carpeta)
                print("El archivo", texto, "ha sido creado con exito")
                print("""¿Desea crear otro archivo?
                1: Si
                2: No""")
                suboption = int(input("Digite la opción: "))
                if suboption==2:
                    break
            while suboption==2:
                texto = input("Ingrese el nombre del archivo a buscar: ")
                exist = os.path.exists(str(carpeta)+str("/")+str(texto))
                if exist==True:
                    f = open(str(carpeta)+str("/")+str(texto), "r")
                    contenido=f.read()
                    print(contenido)
                    f.close
                else:
                    print("El archivo no existe")
                print("""¿Desea leer otro archivo?
                1: Si
                2: No""")
                subsuboption = int(input("Digite la opción: "))
                if subsuboption==2:
                    suboption=0
            while suboption==3:
                exist=0
                option=1
                suboption=0
        while exist==False:
            print("La carpeta no existe")
            exist=True
            option=1
    while option==3:
        print("Cerrando el programa...")
        option = 0