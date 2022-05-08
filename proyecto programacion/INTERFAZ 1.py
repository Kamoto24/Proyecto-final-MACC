print("BIENVENIDO A LA INTERFAZ DE SU BLOC DE NOTAS")
print("----------------------------------------------------------------")
print("PARA INICIAR, RECUERDE TENER EN CUENTA QUE:")
print("\n 1. Crear una carpeta nueva con el nombre de su preferencia")
print("\n 2. Crear los archivos txt donde quiera guardar la información y guardarlos en la carpeta creada en el paso 1")
print("\n 3, Guardar este archivo en la carpeta de el paso 1., en esa misma carpeta deberan estar los archivos txt")
print("\n 4. ¡YA PUEDE INICIAR!")
print("-----------------------------------------------------------------")
print("El BLOC DE NOTAS consta de dos opciones para facilitar su trabajo, las cuales son:")
print("\n 1.Escribir información para posteriormente guardarla en el archivo que desee")
print("\n 2. Obtener la información que esta en el archivo que desee, para poder visualizarla desde BLOC DE NOTAS")

opcion=input("Por favor, seleccione la opción de la cual desea hacer uso: (opcion1 o opcion2): ")
if opcion=="opcion1":
    seguir="SI"
    while seguir=="SI":
        ##introducir el código para poder realizar la acción numero 1
        seguir=input("Desea guadar otra información (SI/NO):")
elif opcion=="opcion2":
    leer="SI"
    while leer=="SI":
        ##introducir código para poder realizar la acción numero 2
        leer=input("Desea leer otra informacion (SI/NO):")