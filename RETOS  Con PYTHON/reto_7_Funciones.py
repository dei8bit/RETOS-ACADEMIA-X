# Reto: Funciones
# 1. Crea un programa que de acuerdo a una lista de números realice:
# la suma de los cuadrados de los números pares y la suma de los cubos de los números impares
# realiza la operación final utilizando una tercera función que recibe la lista, la función de suma de cuadrados y la de cubos. 🧠

lista = [1, 2, 3, 6, 7, 9]


def cuadrado(num):
    return num**2


def cubo(num):
    return num**3


def elevadora(lista):
    for item in lista:
        if item % 2 == 0:
            print(cuadrado(item))
        else:
            print(cubo(item))


elevadora(lista)
