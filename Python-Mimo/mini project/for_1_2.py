libros = [("PROGRAMACION",2023,5), ("C++", 2010, 2),("Python", 2019, 1)]

for (titulo, anio, cant) in libros:
    print(f"{titulo} publicado {anio} catidad {cant}")

print("\n")
# enumerate(libros, 1)  agrega un contador automantico que empieza en 1
# Te da Dos cosas: el numero de posicion i y el contenido del libro 

for i, (titulo, anio, cant) in enumerate(libros, 1):
    print(f"{i}.{titulo} publicado {anio} catidad {cant}")

buscar = input("Libro a buscar: ")

libro_encontrado = buscar in libros


if not libro_encontrado:
    print("no hay ese libro que busca")
else:
    print(f"SI HAY ESE LIBRO REGISTRADO {libro_encontrado}")


