# Reto: Sets
# Crea un programa que te permita gestionar un sistema bibliotecario a partir de dos sucursales 
#  donde realices una consulta para: 
#• encontrar libros comunes
#• encontrar libros únicos en cada biblioteca
#• combinar ambas bibliotecas para conocer los libros disponibles en sistema
#• verifica si una biblioteca es un subconjunto de la otra
#• añade la funcionalidad de agregar un nuevo libro a ambas bibliotecas.


sucursal1 = {"libro1","libroC"}
sucursal2 = {"libro1","libro2","libroB","libroC"}


def librosComunes(sucursal1,sucursal2):
  librosComunes = sucursal1 & sucursal2
  return librosComunes



def librosUnicos(sucursal1,sucursal2):
  librosUnicos = sucursal1 - sucursal2
  return librosUnicos



def combinarBibliotecas(biblioteca1,biblioteca2):
  combinacion = biblioteca1 | biblioteca2
  return combinacion



def verificarSuconjunto(sucursal1,sucursal2):
 return sucursal1.issubset(sucursal2)



def agregarLibro(libro,sucursal1,sucursal2):
  sucursal1.add(libro)
  sucursal2.add(libro)
  return "libros agregados..."


libros_Comunes = librosComunes(sucursal1,sucursal2)
print(f"Los libros comunes en ambas bibliotecas son: {libros_Comunes}") # Los libros comunes en ambas bibliotecas son: {'libro1', 'libroC'}

libros_unicosS1 = librosUnicos(sucursal1,sucursal2)
libros_unicosS2 = librosUnicos(sucursal2,sucursal1)

if len(libros_unicosS1)>0: print(f"Los libros unicos en la sucursal 1 son: {libros_unicosS1}")
else: print("la sucursal 1 no tiene libros unicos") # la sucursal 1 no tiene libros unicos
if len(libros_unicosS2)>0: print(f"Los libros unicos en la sucursal 2 son: {libros_unicosS2}") # Los libros unicos en la sucursal 2 son: {'libro2', 'libroB'}
else: print("la sucursal 2 no tiene libros unicos")

sucursales_combinadas = combinarBibliotecas(sucursal1,sucursal2)
print(f"Libros de las sucursales combinadas {sucursales_combinadas}") # Libros de las sucursales combinadas {'libro1', 'libroC', 'libro2', 'libroB'}

subconjuntoS1 = verificarSuconjunto(sucursal1,sucursal2)
subconjuntoS2 = verificarSuconjunto(sucursal2,sucursal1)
if subconjuntoS1: print("la sucursal 1 es un subconjunto de la sucursal 2") # la sucursal 1 es un subconjunto de la sucursal 2
if subconjuntoS2: print("la sucursal 2 es un subconjunto de la sucursal 1")

agregarLibro("nuevoLibroMutuo",sucursal1,sucursal2)
print(sucursal1) # {'libro1', 'nuevoLibroMutuo', 'libroC'}
print(sucursal2) # {'libro2', 'nuevoLibroMutuo', 'libro1', 'libroC', 'libroB'}

