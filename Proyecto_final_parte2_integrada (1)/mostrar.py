from datos import tablas

def menu_mostrar():
    print("\n========== MOSTRAR ==========")
    if len(tablas) == 0:
        print("No hay tablas.")
        return

    for i in range(len(tablas)):
        tabla = tablas[i]
        print("\nTabla:", tabla["nombre"])

        # Encabezados
        for j in range(len(tabla["variables"])):
            print(f"{tabla['variables'][j]:<15}", end="")
        print()
        print("-" * (15 * len(tabla["variables"])))

        # Datos
        for j in range(len(tabla["datos"])):
            for k in range(len(tabla["datos"][j])):
                print(f"{str(tabla['datos'][j][k]):<15}", end="")
            print()
        print()
        
