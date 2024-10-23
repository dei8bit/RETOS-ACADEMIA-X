# Reto: Números
# 1. Crea un programa que te permita convertir un número decimal a binario, octal o hexadecimal
# de acuerdo a la opción que elija un usuario mediante un menú en consola. 🧠


option = False

while option != True:
    print("h = hexadecimal | o = octal | b = binario | q = salir\n")
    try:
        numero = int(input("ingrese un numero: "))
    except ValueError:
        print("error!!  , usted Ingreso un numero \n ")
    option = input("ingrese una opcion: ").lower()

    match option:
        case "h":
            print(f"Conversion hexadecimal: {hex(numero)}")
        case "o":
            print(f"Conversion octal: {oct(numero)}")
        case "b":
            print(f"Conversion binario: {bin(numero)}")
        case "q":
            print("saliendo...")
            break
        case _:
            print("opcion incorrecta")
