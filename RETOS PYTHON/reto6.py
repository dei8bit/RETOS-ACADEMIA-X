# Reto: Excepcioes
# 1. Crea un programa que te permita ingresar dos números y realizar una división con ellos
# maneja las excepciones de valor, de división entre cero, un error inesperado y por último indica que el programa se completó. 🧠

try:
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
    print(n1 / n2)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except (ValueError, TypeError):
    print("Parece que uno de los valores no es un número")
finally:
    print("Programa completado")