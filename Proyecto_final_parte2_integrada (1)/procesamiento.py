"""Funciones genericas y reutilizables para procesar listas y matrices."""


def transformar_lista(lista, funcion):
    resultado = []
    for elemento in lista:
        resultado = resultado + [funcion(elemento)]
    return resultado


def filtrar_lista(lista, condicion):
    resultado = []
    for elemento in lista:
        if condicion(elemento):
            resultado = resultado + [elemento]
    return resultado


def obtener_columna(matriz, indice):
    columna = []
    for fila in matriz:
        if indice < len(fila):
            columna = columna + [fila[indice]]
    return columna


def sumar_numeros(lista):
    total = 0
    for dato in lista:
        if isinstance(dato, (int, float)) and not isinstance(dato, bool):
            total += dato
    return total


def convertir_a_numero(texto):
    try:
        if "." in texto:
            return float(texto)
        return int(texto)
    except ValueError:
        return texto


def convertir_booleano(texto):
    valor = texto.strip().lower()
    if valor == "true" or valor == "verdadero" or valor == "si":
        return True
    if valor == "false" or valor == "falso" or valor == "no":
        return False
    return texto
