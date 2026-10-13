from datos import tablas
from validaciones import ingresar_entero, texto_no_vacio, ingresar_numero

def menu_variables():
    opcion = 0
    while opcion!= 4:
        print("\n========== VARIABLES ==========")
        print("1 - Crear variable")
        print("2 - Cargar variable")
        print("3 - Modificar variable")
        print("4 - Volver")
        opcion = ingresar_entero("Opcion: ", 1, 4)
        if opcion == 1: crear_variable()
        elif opcion == 2: cargar_variable()
        elif opcion == 3: modificar_variable()

def seleccionar_tabla():
    if len(tablas) == 0:
        print("No hay tablas.")
        return -1
    for i in range(len(tablas)):
        print(i + 1, "-", tablas[i]["nombre"])
    return ingresar_entero("Seleccione una tabla: ", 1, len(tablas)) - 1

def buscar_variable(tabla, nombre):
    for i in range(len(tabla["variables"])):
        if tabla["variables"][i] == nombre:
            return i
    return -1

def crear_variable():
    n = seleccionar_tabla()
    if n == -1: return
    tabla = tablas[n]
    nombre = texto_no_vacio("Nombre de la variable: ")
    while buscar_variable(tabla, nombre)!= -1:
        print("La variable ya existe.")
        nombre = texto_no_vacio("Nombre de la variable: ")
    tabla["variables"] = tabla["variables"] + [nombre]
    for i in range(len(tabla["datos"])):
        tabla["datos"][i] = tabla["datos"][i] + [""]
    print("Variable creada correctamente.")

def cargar_variable():
    n = seleccionar_tabla()
    if n == -1: return
    tabla = tablas[n]
    if len(tabla["variables"]) == 0:
        print("La tabla no tiene variables.")
        return
    if len(tabla["datos"]) == 0:
        filas = ingresar_entero("Cantidad de filas: ", 1, 100)
        for i in range(filas):
            fila = []
            for j in range(len(tabla["variables"])):
                nom = tabla["variables"][j].lower()
                if nom == "sabor":
                    v = texto_no_vacio(f'Fila {i+1}, {tabla["variables"][j]}: ')
                else:
                    v = ingresar_numero(f'Fila {i+1}, {tabla["variables"][j]}: ')
                fila = fila + [v]
            tabla["datos"] = tabla["datos"] + [fila]
        print("Datos cargados correctamente.")
        return

    for i in range(len(tabla["variables"])):
        print(i + 1, "-", tabla["variables"][i])
    col = ingresar_entero("Seleccione la variable: ", 1, len(tabla["variables"])) - 1
    nom = tabla["variables"][col].lower()
    for i in range(len(tabla["datos"])):
        if nom == "sabor":
            tabla["datos"][i][col] = texto_no_vacio(f'Nuevo valor para fila {i+1}: ')
        else:
            tabla["datos"][i][col] = ingresar_numero(f'Nuevo valor para fila {i+1}: ')
    print("Variable cargada correctamente.")

def modificar_variable():
    n = seleccionar_tabla()
    if n == -1: return
    tabla = tablas[n]
    if len(tabla["variables"]) == 0:
        print("La tabla no tiene variables.")
        return
    for i in range(len(tabla["variables"])):
        print(i + 1, "-", tabla["variables"][i])
    numero = ingresar_entero("Variable a modificar: ", 1, len(tabla["variables"]))
    nuevo = texto_no_vacio("Nuevo nombre: ")
    tabla["variables"][numero - 1] = nuevo
    print("Variable modificada correctamente.")

    