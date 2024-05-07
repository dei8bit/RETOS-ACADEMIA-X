# Reto: Condicionales
# Crea un programa que solicita al usuario que ingrese su edad, 
# luego determina su clasificación de edad (niño, adolescente, adulto, adulto mayor) 
# y proporciona detalles adicionales utilizando la expresión match para una clasificación más específica de acuerdo a su edad. 🧠

edad = int(input("Por favor ingrese su edad: "))


if edad <14: 
  print("Eres un Niño")
  clasificacion= "niño"
elif edad <24: 
  print("Eres un Adolescente")
  clasificacion= "adolescente"
elif edad <40: 
  print("Eres un Adulto")
  clasificacion= "adulto"
elif edad <120: 
  print("Eres un Adulto mayor")
  clasificacion= "adulto mayor"
else: 
  print("es imposible que hayas vivido tanto con la tecnologia del siglo 21")
  clasificacion="no clasificable"

match clasificacion:
  case "niño": print("Es importante comer bien cuando eres niño")
  case "adolescente": print("Es importante estar concetrado cuando eres adolescente")
  case "adulto": print("Es importante ser comunicativo cuando eres adulto")
  case "adulto mayor": print("Es importante ser paciente cuando eres un adulto mayor")
  case _: pass
 