# Reto: Listas
# Crea un programa que te permita realizar un CRUD (Crear, leer, actualizar y borrar) de usuarios de una lista. 🧠


usuarios = []


def newUser(users):
    username = input("Ingrese nombre de usuario: ")
    for user in users:
        if user["username"] == username:
            print("¡El nombre de usuario ya existe! Por favor, elija otro.")
            return users
    profesion = input("Ingrese su profesión: ")
    password = input("Ingrese una contraseña: ")
    users.append({"username": username, "profesion": profesion, "password": password})
    print("Usuario agregado exitosamente.")
    return users


userExample = [
    {"username": "alejandro", "password": "insegura123", "profesion": "maestro"},
    {"username": "penelope", "password": "veamos", "profesion": "boxeadora"},
]


def readUser(username, users):
    for usuario in users:
        if usuario["username"] == username:
            return usuario
        else:
            return None


usuarioBuscado = readUser("alejandro", userExample)

if usuarioBuscado is None:
    print("Usuario no encontrado")
else:
    print(usuarioBuscado)


def updateUser(users, key, data, username):
    for usuario in users:
        if usuario["username"] == username:
            if key in usuario:
                usuario[key] = data
                return users
            else:
                return f"El campo '{key}' no existe para actualizar."
    return f"No se encontró el usuario con nombre de usuario '{username}'."


def removeUser(username, users):
    new_users = []
    user_removed = False
    for usuario in users:
        if usuario["username"] == username:
            user_removed = True
            print("Datos del usuario eliminados...")
        else:
            new_users.append(usuario)
    if not user_removed:
        print(
            f"No se encontró ningún usuario con el nombre |{username}| de usuario proporcionado."
        )
    return new_users


salir = False

while not salir:
  print("Eliga la opcion deseada:\n")
  print("""
        • C: Crear Usuario
        • A: Actualizar Datos
        • B: Borrar Usuario
        • L: Leer Usuario
        • Q: Salir.
        """)
  option = input("Inrese una opcion: ").lower()

  match option:
    case "c":
        newUser(usuarios)
    case "l":
        username = "Ingrese nombre de usuario a leer: "
        readUser(username,usuarios)
    case "a":
        username = "Ingrese nombre de usuario a actualizar: "
        key = "Ingrese campo a actualizar: "
        data = "Ingrese el nuevo valor: "
        updateUser(usuarios, key, data, username)
    case "b":
        username = "Ingrese nombre de usuario a borrar: "
        readUser(username,usuarios)
    case "q":
        print("saliendo...")
        salir = True
