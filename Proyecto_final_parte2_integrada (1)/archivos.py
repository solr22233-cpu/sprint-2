"""Lectura de CSV y representacion en diccionarios y matrices."""
import csv
from procesamiento import convertir_a_numero, convertir_booleano, obtener_columna, sumar_numeros
from validaciones import ingresar_entero, texto_no_vacio


def convertir_dato(texto):
    valor = convertir_booleano(texto)
    if isinstance(valor, bool):
        return valor
    return convertir_a_numero(texto)


def leer_csv(ruta):
    registros = []
    with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            registro = {}
            for clave in fila:
                registro[clave] = convertir_dato(fila[clave])
            registros = registros + [registro]
    return registros


def diccionarios_a_matriz(registros):
    if len(registros) == 0:
        return [], []
    encabezados = list(registros[0].keys())
    matriz = []
    for registro in registros:
        fila = []
        for encabezado in encabezados:
            fila = fila + [registro.get(encabezado, "")]
        matriz = matriz + [fila]
    return encabezados, matriz


def menu_archivos():
    print("\n========== ARCHIVOS Y MATRICES ==========")
    ruta = texto_no_vacio("Ruta del archivo CSV (ejemplo.csv): ")
    try:
        registros = leer_csv(ruta)
    except (OSError, csv.Error):
        print("No se pudo leer el archivo. Compruebe la ruta y el formato CSV.")
        return
    if len(registros) == 0:
        print("El archivo no contiene registros.")
        return
    encabezados, matriz = diccionarios_a_matriz(registros)
    print("\nRegistros leidos:", len(registros))
    print("Datos representados como diccionarios:")
    for registro in registros:
        print(registro)
    print("\nMatriz:")
    print(encabezados)
    for fila in matriz:
        print(fila)
    print("\nColumnas disponibles:")
    for i in range(len(encabezados)):
        print(i + 1, "-", encabezados[i])
    columna = ingresar_entero("Seleccione columna para sumar valores numericos: ", 1, len(encabezados)) - 1
    valores = obtener_columna(matriz, columna)
    total = sumar_numeros(valores)
    print("Suma de valores numericos de esa columna:", total)
