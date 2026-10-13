usuarios = [{"usuario": "admin", "clave": "1234"}]

def buscar_usuario(nombre):
    for i in range(len(usuarios)):
        if usuarios[i]["usuario"] == nombre:
            return i
    return -1

def registrar_usuario():
    nombre = input("Usuario: ")
    while len(nombre) == 0 or buscar_usuario(nombre) != -1:
        print("Usuario invalido o ya existente.")
        nombre = input("Usuario: ")
    clave = input("Contraseña: ")
    while len(clave) == 0:
        print("La contraseña no puede estar vacia.")
        clave = input("Contraseña: ")
    usuarios[:] = usuarios + [{"usuario": nombre, "clave": clave}]
    print("Usuario registrado correctamente.")

def iniciar_sesion():
    nombre = input("Usuario: ")
    clave = input("Contraseña: ")
    for i in range(len(usuarios)):
        if usuarios[i]["usuario"] == nombre and usuarios[i]["clave"] == clave:
            return True
    return False
