# Reto: Funciones incorporadas
# 1. Crea un programa que de acuerdo a una lista de palabras solo imprima las que tienen más de 8 caracteres de longitud. 🧠


lista = ["anaconda", "onomatopeya", "hercules"]


def palabras_largas(lista):
    for item in lista:
        if len(item) > 8:
            print(f"{item} tiene mas de 8 caracteres")


palabras_largas(lista)
