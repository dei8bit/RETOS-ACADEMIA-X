# Reto: Variables y tipos de datos
# 📌 Crea una variable con un número entero, una con un decimal, una de texto y una booleana.
# 📌 Cambia el valor de tu variable que contiene el entero y el texto.
# 📌 Crea una lista de números y una de frutas.
# 📌 Crea una tupla con los colores para pintar una casa y un rango de 1 a 5.
# 📌 Crea un diccionario con la cantidad de frutas de un almacén.
# 📌 Crea un conjunto numérico con set y uno con frozenset.
# 📌 Crea una variable con valor nulo.
# 📌 Crea una oración donde menciones el producto y su precio utilizando F-strings.
# 📌 Valida el tipo de variable de tus variables de entero y texto.
# 📌 Imprime en consola todas las operaciones que realizaste. 🧠


entero = 20
decimal = 22.3
texto = "Aloha"
booleano = True

entero = 30
texto = "hola♥"

numeros = [0, 9, 6, 7]

frutas = ["🍍", "🍅", "🍓", "🍉"]

tupla = ("amarillo", "celeste", "violeta", [1, 2, 3, 4, 5])

diccionario = {"manzana": 15, "peras": 13, "bananas": 17}


conjunto_numerico1 = {1, 2, 2, 3, 4, 5}
conjunto_numerico2 = frozenset([1, 2, 3, 4, 5])

variable = None

producto = "televisor"
precio = 245

oracion = f"el prodcuto {producto} tiene un precio de: $ {precio}"


print(entero)
print(decimal)
print(texto)
print(booleano)
print(numeros)
print(frutas)
print(tupla)
print(diccionario)
print(conjunto_numerico1)
print(conjunto_numerico2)
print(variable)
print(oracion)
print(type(entero))
print(type(texto))
