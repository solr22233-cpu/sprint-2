from datos import tablas
from validaciones import ingresar_entero

def suma(lista):
    total = 0
    for i in range(len(lista)): total += lista[i]
    return total

def promedio(lista): return suma(lista) / len(lista)

def maximo(lista):
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor: mayor = lista[i]
    return mayor

def minimo(lista):
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor: menor = lista[i]
    return menor

def ordenar(lista):
    a = lista[:]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                aux = a[i]; a[i] = a[j]; a[j] = aux
    return a

def seleccionar_datos():
    if len(tablas) == 0:
        print("No hay tablas.")
        return []
    for i in range(len(tablas)): print(i + 1, "-", tablas[i]["nombre"])
    tabla = tablas[ingresar_entero("Seleccione una tabla: ", 1, len(tablas)) - 1]
    if len(tabla["variables"]) == 0 or len(tabla["datos"]) == 0:
        print("La tabla no tiene datos.")
        return []
    for i in range(len(tabla["variables"])): print(i + 1, "-", tabla["variables"][i])
    col = ingresar_entero("Seleccione una variable: ", 1, len(tabla["variables"])) - 1
    datos = []
    for i in range(len(tabla["datos"])):
        if tabla["datos"][i][col] != "": datos = datos + [tabla["datos"][i][col]]
    return datos

def menu_estadistica():
    opcion = 0
    while opcion != 7:
        print("\n========== ESTADISTICA ==========")
        print("1 - Frecuencias")
        print("2 - Maximo y minimo")
        print("3 - Media aritmetica")
        print("4 - Media geometrica")
        print("5 - Dispersion")
        print("6 - Posicion")
        print("7 - Volver")
        opcion = ingresar_entero("Opcion: ", 1, 7)
        if opcion == 1: frecuencias()
        elif opcion == 2: max_min()
        elif opcion == 3: media()
        elif opcion == 4: geometrica()
        elif opcion == 5: dispersion()
        elif opcion == 6: posicion()

def frecuencias():
    d = seleccionar_datos()
    if len(d) == 0: return
    a = ordenar(d); valores = []
    for x in a:
        if x not in valores: valores = valores + [x]
    for x in valores:
        cantidad = 0
        for y in d:
            if y == x: cantidad += 1
        print(x, "-", cantidad)

def max_min():
    d = seleccionar_datos()
    if len(d) > 0: print("Maximo:", maximo(d), " Minimo:", minimo(d))

def media():
    d = seleccionar_datos()
    if len(d) > 0: print("Media aritmetica:", promedio(d))

def geometrica():
    d = seleccionar_datos()
    if len(d) == 0: return
    producto = 1
    for x in d:
        if x <= 0:
            print("La media geometrica requiere valores positivos.")
            return
        producto *= x
    print("Media geometrica:", producto ** (1 / len(d)))

def dispersion():
    d = seleccionar_datos()
    if len(d) == 0: return
    media_d = promedio(d); total = 0
    for x in d: total += (x - media_d) ** 2
    varianza = total / len(d)
    print("Rango:", maximo(d) - minimo(d))
    print("Varianza:", varianza)
    print("Desvio estandar:", varianza ** 0.5)

def posicion():
    d = seleccionar_datos()
    if len(d) == 0: return
    a = ordenar(d); mitad = len(a) // 2
    if len(a) % 2 == 0: mediana = (a[mitad-1] + a[mitad]) / 2
    else: mediana = a[mitad]
    print("Mediana:", mediana)
