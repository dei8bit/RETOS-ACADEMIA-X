# Reto: Texto
# 1. Crea un programa que te permita realizar las siguientes operaciones utilizando un texto multilínea:
# 📌 Imprime la longitud del texto.
# 📌 Reemplaza todas las ocurrencias de 'python' con 'Python'.
# 📌 Encuentra la posición de la primera aparición de la palabra 'desafiante'.
# 📌 Elimina espacios en blanco al principio y al final del texto.
# 📌 Divide el texto en una lista de palabras.
# 📌 Verifica si el texto comienza con la palabra 'Este'. 🧠
# Utiliza el siguiente texto:
# """Este es un texto de ejemplo.
# python es un lenguaje de programación desafiante y poderoso.
# """


texto = """Este es un texto de ejemplo.
python es un lenguaje de programación desafiante y poderoso.
"""

texto_modificado = texto.replace('python', 'Python')
posicion =  texto_modificado.find('desafiante')
texto_sin_espacios = texto_modificado.strip()
lista_palabras = texto_sin_espacios.split()


print(f"longitud del texto: {len(texto)}")
print(texto_modificado)
print(f"primera posicion de desafiante {posicion}")
print(texto_sin_espacios)
print(lista_palabras)
if texto_sin_espacios.startswith('Este'):
    print("El texto comienza con la palabra 'Este'")
else:
    print("El texto no comienza con la palabra 'Este'")