libros = []

def registrar_libros():
    num_lib = int(input("Digite el numero de libros a ingresar "))

    i = 1 
    while i <= num_lib:
        
        titulo = input("Titilo: ")
        anio = int(input("anio: "))
        cant = int(input("cantidad: "))
        libros.append((titulo, anio, cant))
        i += 1

        print("\n Libro registrado correctamente")

def mostrar():

    print("\n ---LISTA DE LIBROS ----")
    if not libros:
        print("No hay libros registrados")
    else:    
      for i, (titulo, anio, cant) in enumerate(libros, 1):
        print(f"{i} El libro {titulo} publicado {anio} cantidad {cant}")
    
def buscar_libros():
    buscar = input("Ingrese el titulo del libro que desea buscar: ")

    libro_encontrado = False

    for titulo, anio, cant in libros:
        if titulo == buscar:
            libro_encontrado = True
            print(f"Econtrado {titulo} - anio: {anio} - cantidad: {cant}")
            break
    if not libro_encontrado:
        print(f"No hay ese libro ")
    #cantidad_a = libros.count(libro)
    #print(f"Hay una {cantidad_a} ejemplares disponibles")

while True:
    print("=======================")
    print("------MENU-------")
    print("=======================")
    print("1.Registrar libros ")
    print("2.Mostrar libros ")
    print("3.buscar")
    print("4.salir")

    try:

        opcion = int(input("Digite la opcion a realizar: "))
        if opcion == 1:
            registrar_libros()
            #print("a")
        elif opcion == 2:
            mostrar()
            #print("b")
        elif opcion == 3:
            buscar_libros()
        elif opcion == 4:
            print("Hasta pronto")
            break
        else:
            print("Opcion invalida")

    except ValueError:
        print("Por favor, ingrese el numero valido ")
    