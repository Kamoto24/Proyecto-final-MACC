import carpetas
option=1
while option>0:
    print("""¡Bienvenido! Seleccione la acción que desea realizar:
    1: Crear una nueva carpeta
    2: Entrar en una carpeta existente
    3: Ordenar archivos
    4: Salir del programa""")
    option=int(input("Digite la opción: "))
    while option !=1 and option !=2 and option !=3 and option !=4:
        int(input("Ingrese una opción válida: "))
    while option==1:
        suboption=0
        carpeta = input("Ingrese el nombre de la carpeta: ")
        carpetas.crear_carpeta(carpeta)
        print("""¿Que desea hacer en esta carpeta?
        1: Crear un archivo
        2: Salir de la carpeta""")
        suboption=int(input("Digite la opción: "))
        while suboption != 1 and suboption != 2:
            suboption = int(input("Ingrese una opción válida: "))
        while suboption==1:
            texto=input("Ingrese el nombre del archivo: ")
            contenido=input("A continuación, escriba el contenido del archivo:\n")
            carpetas.escribir_texto(texto,contenido,carpeta)
            print("""¿Desea crear otro archivo?
            1: Si
            2: No""")
            suboption=int(input("Digite la opción: "))
            while suboption != 1 and suboption != 2:
                suboption=int(input("Ingrese una opción válida: "))
        break
    while option==2:
        carpeta = input("Ingrese el nombre de la carpeta a buscar: ")
        exist=carpetas.existe(carpeta)
        while exist==True:
            suboption=0
            print("""¿Que desea hacer en esta carpeta?
            1: Crear un archivo
            2: Leer un archivo
            3: Salir de la carpeta""")
            suboption = int(input("Digite la opción: "))
            while suboption != 1 and suboption != 2 and suboption!=3:
                suboption=int(input("Ingrese una opción válida: "))
            while suboption == 1:
                texto = input("Ingrese el nombre del archivo: ")
                contenido = input("A continuación, escriba el contenido del archivo:\n")
                carpetas.escribir_texto(texto,contenido)
                print("""¿Desea crear otro archivo?
                1: Si
                2: No""")
                suboption = int(input("Digite la opción: "))
                while suboption != 1 and suboption != 2:
                    suboption = int(input("Ingrese una opción válida: "))
                if suboption==2:
                    suboption=0
            while suboption==2:
                texto = input("Ingrese el nombre del archivo a buscar: ")
                ruta = str(carpeta) + str("/") + str(texto)
                exist = carpetas.existe(ruta)
                if exist == True:
                    f = open(ruta, "r")
                    contenido=f.read()
                    print(contenido)
                    f.close
                else:
                    print("El archivo no existe")
                print("""¿Desea leer otro archivo?
                1: Si
                2: No""")
                subsuboption = int(input("Digite la opción: "))
                while suboption != 1 and suboption != 2:
                    suboption = int(input("Ingrese una opción válida: "))
                if subsuboption==2:
                    suboption=0
            while suboption==3:
                exist=None
                option=1
                suboption=0
        while exist==False:
            print("""La carpeta no existe, ¿Desea leer otra carpeta?
            1: Si
            2: No""")
            subsuboption = int(input("Digite la opción: "))
            while suboption != 1 and suboption != 2:
                suboption=int(input("Ingrese una opción válida: "))
            if suboption==1:
                option=2
                exist=None
            elif suboption==2:
                exist=None
                option=1
    while option==3:
        print("""¿Donde desea ordenar los archivos?
        1. En una carpeta creada
        2. En una carpeta existente""")
        suboption = int(input("Digite la opción: "))
        while suboption != 1 and suboption != 2:
            suboption = int(input("Ingrese una opción válida: "))
        while suboption==1:
            carpeta=input("Ingrese el nombre de la carpeta: ")
            while carpetas.existe(carpeta) == True:
                carpeta = input("Esta carpeta ya existe, por favor ingrese otro nombre: ")
            carpetas.crear_carpeta(carpeta)
            subsuboption=1
            while subsuboption==1:
                print("""¿De que forma desea ordenar los archivos?
                1. Archivos que contengan el nombre de esta carpeta
                2. Archivos que contengan cierto nombre
                3. Archivos de cierta extensión""")
                subsuboption = int(input("Digite la opción: "))
                while subsuboption != 1 and subsuboption != 2 and subsuboption !=3:
                    suboption = int(input("Ingrese una opción válida: "))
                if subsuboption==1:
                    carpetas.ordenar_nombre(carpeta)
                    print("Los archivos fueron ordenados con exito")
                elif subsuboption==2:
                    clave=input("Ingrese la palabra para ordenar los archivos: ")
                    carpetas.ordenar_palabra(carpeta,clave)
                    print("Los archivos fueron ordenados con exito")
                elif subsuboption==3:
                    sufijo = input("Ingrese la extensión para ordenar los archivos: ")
                    sufijo="."+sufijo
                    carpetas.ordenar_tipo(carpeta, sufijo)
                    print("Los archivos fueron ordenados con exito")
                print("""¿Desea ordenar mas archivos?
                1. Si
                2. No""")
                subsuboption = int(input("Digite la opción: "))
                while subsuboption != 1 and subsuboption != 2:
                    subsuboption = int(input("Ingrese una opción válida: "))
                if subsuboption==1:
                    continue
                elif subsuboption==2:
                    suboption=0
                    option=1
        while suboption==2:
            carpeta=input("Ingrese el nombre de la carpeta: ")
            exist=carpetas.existe(carpeta)
            if exist==True:
                print("""¿De que forma desea ordenar los archivos?
                1. Archivos que contengan el nombre de esta carpeta
                2. Archivos que contengan cierto nombre
                3. Archivos de cierta extensión""")
                subsuboption = int(input("Digite la opción: "))
                while subsuboption != 1 and subsuboption != 2 and subsuboption !=3:
                    suboption = int(input("Ingrese una opción válida: "))
                if subsuboption==1:
                    carpetas.ordenar_nombre(carpeta)
                    print("Los archivos fueron ordenados con exito")
                elif subsuboption==2:
                    clave=input("Ingrese la palabra para ordenar los archivos: ")
                    carpetas.ordenar_palabra(carpeta,clave)
                    print("Los archivos fueron ordenados con exito")
                elif subsuboption==3:
                    sufijo = input("Ingrese la extensión para ordenar los archivos: ")
                    sufijo="."+sufijo
                    carpetas.ordenar_tipo(carpeta, sufijo)
                    print("Los archivos fueron ordenados con exito")
                print("""¿Desea ordenar mas archivos?
                1. Si
                2. No""")
                subsuboption = int(input("Digite la opción: "))
                while subsuboption != 1 and subsuboption != 2:
                    subsuboption = int(input("Ingrese una opción válida: "))
                if subsuboption==1:
                    exist=True
                elif subsuboption==2:
                    exist=0
                    suboption = 0
                    option = 1
            elif exist==False:
                print("""La carpeta no existe, ¿Desea buscar otra carpeta?"
                1. Si
                2. No""")
                subsuboption = int(input("Digite la opción: "))
                while subsuboption != 1 and subsuboption != 2:
                    subsuboption = int(input("Ingrese una opción válida: "))
                if subsuboption == 1:
                    exist = 0
                elif subsuboption == 2:
                    exist=0
                    suboption=0
                    option=1
    while option==4:
        print("Cerrando el programa...")
        option = 0