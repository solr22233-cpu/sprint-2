from datos import proyectos
from validaciones import ingresar_entero, texto_no_vacio

def menu_proyectos():
    opcion = 0
    while opcion != 4:
        print("\n========== PROYECTOS ==========")
        print("1 - Generar proyecto")
        print("2 - Mostrar proyectos")
        print("3 - Modificar proyecto")
        print("4 - Volver")
        opcion = ingresar_entero("Opcion: ", 1, 4)
        if opcion == 1: generar_proyecto()
        elif opcion == 2: mostrar_proyectos()
        elif opcion == 3: modificar_proyecto()

def generar_proyecto():
    nombre = texto_no_vacio("Nombre del proyecto: ")
    for i in range(len(proyectos)):
        if proyectos[i] == nombre:
            print("El proyecto ya existe.")
            return
    proyectos[:] = proyectos + [nombre]
    print("Proyecto creado correctamente.")

def mostrar_proyectos():
    if len(proyectos) == 0:
        print("No hay proyectos.")
        return
    for i in range(len(proyectos)):
        print(i + 1, "-", proyectos[i])

def modificar_proyecto():
    if len(proyectos) == 0:
        print("No hay proyectos.")
        return
    mostrar_proyectos()
    n = ingresar_entero("Proyecto a modificar: ", 1, len(proyectos))
    proyectos[n - 1] = texto_no_vacio("Nuevo nombre: ")
    print("Proyecto modificado correctamente.")
