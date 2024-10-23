# Reto: Operadores

# 📌 Crea dos variables numéricas y realiza una suma, resta, multiplicación, división, potencia y modulo con ellas dos.
# 📌 Crea dos variables numéricas e incrementa en 3 la primera y la segunda increméntala en su doble.
# 📌 Crea dos variables numéricas diferentes y compara si son iguales, diferentes, mayor o menor una de otra.
# 📌 Crea dos variables booleanas diferentes y realiza las operaciones and, or y not.
# 📌 Crea una lista del 1 al 5 y verifica si el numero 3 se encuentra en la lista y si el numero 6 no se encuentra.
# 📌 Crea dos variables con diferente texto y verifica si son o no son idénticas.
# 📌 Crea dos variables numéricas y realiza las operaciones binarias (&, |, ^, ~, <<, >>). 🧠


num1 = 23
num2 = 55

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
potencia = num1**num2
modulo = num1 % num2

incremento_en_tres = num1 * 3
incremento_en_dos = num2 * 2

numero1 = 77
numero2 = 66

bool1 = True
bool2 = False

lista = [1, 2, 3, 4, 5]

texto1 = "SOFOCLES"
texto2 = "sofocles"

number1 = 10
number2 = 12

print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division}")
print(f"potencia: {potencia}")
print(f"modulo: {modulo}")

print(f"incremento en tres: {incremento_en_tres}")
print(f"incremento en dos: {incremento_en_dos}")

print(f"numero1==numero2: {numero1==numero2}")
print(f"numero1!=numero2: {numero1!=numero2}")
print(f"numero1>numero2: {numero1>numero2}")
print(f"numero1<numero2: {numero1<numero2}")
print(f"bool1 and bool2: {bool1 and bool2}")
print(f"bool1 or bool2: {bool1 or bool2}")
print(f"not bool1: {not bool1}")
print(f"not bool2: {not bool2}")

print(f"3 esta en lista: {3 in lista}")
print(f"6 NO esta en lista {6 not in lista}")

print(f"texto1==texto2: {texto1==texto2}")
print(f"number1 & number2: {number1 & number2}")
print(f"number1 | number2: {number1 | number2}")
print(f"number1 ^ number2: {number1 ^ number2}")
print(f"~number1: {~number1}")
print(f"~number2: {~number2}")
print(f"number1 << number2: {number1 << number2}")
print(f"number1 >> number2: {number1 >> number2}")
