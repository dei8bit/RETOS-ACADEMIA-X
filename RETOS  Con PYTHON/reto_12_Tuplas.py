# Reto: Tuplas
# Crea un programa que te permita agregar, mostrar y buscar libros por autor utilizando las opciones del menú
# representa cada libro como una tupla con tres elementos: título, autor y año de publicación.. 🧠

biblioteca = []


def agregarLibro(titulo, autor, año: int):
    libro = (titulo, autor, año)
    return libro


def llenarBiblioteca(biblioteca: list, libro: tuple):
    biblioteca.append(libro)
    print("Libro cargado correctamente...\n")
    return biblioteca


def verBiblioteca(biblioteca: list):
    for libro in biblioteca:
        print(f"• {libro[0]} - {libro[1]}| Publicado en año: {libro[2]}")


def buscarLibro(autor: str, biblioteca: list):
    for libro in biblioteca:
        if libro[1] == autor:
            return f"• {libro[1]} -- {libro[0]} || Publicado en año: {libro[2]}\n"
    return None


libro1 = agregarLibro("El rey y el oso", "Rodo Asegurui", 1970)
libro2 = agregarLibro("Saber hacer", "Lola Carmen", 2017)
llenarBiblioteca(biblioteca, libro1)
llenarBiblioteca(biblioteca, libro2)


opcion = "no"

while opcion != "si":
    print(
        """ingrese una opcion deseadada: 
A: Agregar Libro.
V: Ver Biblioteca.
B: Buscar Libro.
Q: Salir.
"""
    )
    opcion = input("ingrese una opcion deseadada: ").lower()

    match opcion:
        case "a":
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año = input("Ingrese el año del libro: ")
            libro = agregarLibro(titulo, autor, año)
            llenarBiblioteca(biblioteca, libro)
        case "v":
            verBiblioteca(biblioteca)
            print("\n")
        case "b":
            autor = input("Ingrese el autor buscado: ")
            busqueda = buscarLibro(autor, biblioteca)
            if busqueda:
                print(busqueda)
            else:
                print("autor no encontrado")
        case "q":
            print("saliendo...")
            break
        case _:
            print("Opcion Incorrecta!!!\n")
