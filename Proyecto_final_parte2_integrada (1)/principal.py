from usuarios import iniciar_sesion, registrar_usuario
from validaciones import ingresar_entero
from proyectos import menu_proyectos
from tablas import menu_tablas
from variables import menu_variables
from mostrar import menu_mostrar
from estadistica import menu_estadistica
from archivos import menu_archivos

def menu_principal():
    opcion = 0
    while opcion != 7:
        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Proyectos")
        print("2 - Tablas")
        print("3 - Variables")
        print("4 - Mostrar")
        print("5 - Estadistica")
        print("6 - Archivos y matrices")
        print("7 - Salir")
        opcion = ingresar_entero("Opcion: ", 1, 7)
        if opcion == 1: menu_proyectos()
        elif opcion == 2: menu_tablas()
        elif opcion == 3: menu_variables()
        elif opcion == 4: menu_mostrar()
        elif opcion == 5: menu_estadistica()
        elif opcion == 6: menu_archivos()
    print("Programa finalizado.")

def acceso():
    opcion = 0
    while opcion != 3:
        print("\n========== ACCESO ==========")
        print("1 - Iniciar sesion")
        print("2 - Registrarse")
        print("3 - Salir")
        opcion = ingresar_entero("Opcion: ", 1, 3)
        if opcion == 1:
            if iniciar_sesion():
                print("Acceso correcto.")
                menu_principal()
                return
            print("Usuario o contraseña incorrectos.")
        elif opcion == 2:
            registrar_usuario()

acceso()
