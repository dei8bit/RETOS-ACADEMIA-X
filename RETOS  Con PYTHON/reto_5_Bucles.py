# Reto: Bucles
# 1. Crea un programa que sume los números pares del 1 al 10
# y se detenga cuando la suma haya sobrepasado el limite de 15,
# por ultimo imprime el ultimo resultado de la suma cuando se sobrepaso el limite. 🧠


suma = 0

for item in range(1, 11):
    if item % 2 == 0:
        suma += item
    if suma > 15:
        print(suma)
        break
