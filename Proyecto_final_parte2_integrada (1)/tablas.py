from datos import tablas
from validaciones import ingresar_entero, texto_no_vacio

def menu_tablas():
    opcion = 0
    while opcion != 4:
        print("\n========== TABLAS ==========")
        print("1 - Crear tabla")
        print("2 - Modificar tabla")
        print("3 - Mostrar tablas")
        print("4 - Volver")
        opcion = ingresar_entero("Opcion: ", 1, 4)
        if opcion == 1: crear_tabla()
        elif opcion == 2: modificar_tabla()
        elif opcion == 3: mostrar_tablas()

def crear_tabla():
    nombre = texto_no_vacio("Nombre de la tabla: ")
    for i in range(len(tablas)):
        if tablas[i]["nombre"] == nombre:
            print("La tabla ya existe.")
            return
    tablas[:] = tablas + [{"nombre": nombre, "variables": [], "datos": []}]
    print("Tabla creada correctamente.")

def mostrar_tablas():
    if len(tablas) == 0:
        print("No hay tablas.")
        return
    for i in range(len(tablas)):
        print(i + 1, "-", tablas[i]["nombre"])

def modificar_tabla():
    if len(tablas) == 0:
        print("No hay tablas.")
        return
    mostrar_tablas()
    n = ingresar_entero("Tabla a modificar: ", 1, len(tablas))
    tablas[n - 1]["nombre"] = texto_no_vacio("Nuevo nombre: ")
    print("Tabla modificada correctamente.")
