# Reto: Diccionarios
# Crea un programa que te permita gestionar tareas y estas se almacenan en un diccionario.
# donde la clave es la descripción de la tarea y el valor es un diccionario que contiene los detalles de la tarea. 
# Puedes agregar tareas, mostrar la lista de tareas, completar tareas, y eliminar la última tarea utilizando diferentes métodos de diccionario. 🧠


tareas = {}
opcion = False


def agregarTarea(tareas: dict, nombre: str, dificultad: str, estado: str, vencimiento: str):
    if nombre not in tareas:  # se agrega la tarea si esta  no esta en el diccionario.
        tareas[nombre] = {"dificultad": dificultad, "estado": estado, "vencimiento": vencimiento}
        return True   
    else:
        return False  


def mostrarTareas(tareas:dict):
  if tareas:
    print("↓↓ LISTA DE TAREAS ↓↓")
    for descripcion, detalles in tareas.items():
        print(f"🔹 {descripcion}: {detalles["estado"]} - |{detalles["vencimiento"]}| - nivel: 🔥 {detalles["dificultad"]} ")
  else: print("No hay ninguna tarea aun ❗❕ \n")


def completarTareas(tareas:dict,nombre:str):
    if nombre in tareas:
       tareas[nombre]["estado"] = "Completada ✔"
       print(f"{nombre} - {tareas[nombre]["estado"]}")
    else: print("No existe la tarea ❗❕")

   
def eliminarUltimaTarea(tareas:dict):
  if tareas:
    tareas.popitem()
  else :print("No hay tareas que eliminar ❗❕")

while not opcion:
    print("Gestor de Tareas:")
    print("""
    • A --> Agregar Tareas
    • V --> Ver Tareas
    • C --> Completar Tarea.
    • E --> Eliminar la ultima tarea.
    • S --> Salir
    """)

    respuesta = input("Selecciona una opción: ").upper()
    
    match respuesta:
        case "A":
            nombre = input("ingrese el nombre de la tarea: ")
            dificultad = input("ingrese la dificultad de la tarea: ")
            vencimiento = input("ingrese el vencimiento de la tarea: ")
            if agregarTarea(tareas, nombre, dificultad, "Pendiente ⏳", vencimiento):
                print("tarea agregada exitosamente ✅")
            else: print("Ya existe la tarea ❗❕")
        case "V":
            mostrarTareas(tareas)
        case "C":
            nombre = input("ingrese el nombre de la tarea a completar: ")
            completarTareas(tareas,nombre)
        case "E":
            eliminarUltimaTarea(tareas)
        case "S":
            opcion = not opcion
            print("Saliendo del gestor de tareas..🏃🚪")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción válida ❗❕ .\n")
