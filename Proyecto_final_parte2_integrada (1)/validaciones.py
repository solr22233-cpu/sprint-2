def es_entero(texto):
    if len(texto) == 0:
        return False
    inicio = 1 if texto[0] == "-" else 0
    if inicio == len(texto):
        return False
    for i in range(inicio, len(texto)):
        if texto[i] < "0" or texto[i] > "9":
            return False
    return True

def es_numero(texto):
    if len(texto) == 0:
        return False
    inicio = 1 if texto[0] == "-" else 0
    if inicio == len(texto):
        return False
    puntos = 0
    for i in range(inicio, len(texto)):
        if texto[i] == ".":
            puntos += 1
        elif texto[i] < "0" or texto[i] > "9":
            return False
    return puntos <= 1 and texto not in [".", "-."]

def ingresar_entero(mensaje, minimo, maximo):
    dato = input(mensaje)
    while not es_entero(dato) or int(dato) < minimo or int(dato) > maximo:
        print("Dato invalido.")
        dato = input(mensaje)
    return int(dato)

def ingresar_numero(mensaje):
    dato = input(mensaje)
    while not es_numero(dato):
        print("Debe ingresar un numero.")
        dato = input(mensaje)
    return float(dato)

def texto_no_vacio(mensaje):
    dato = input(mensaje)
    while len(dato) == 0:
        print("El dato no puede estar vacio.")
        dato = input(mensaje)
    return dato


def es_rango(numero, minimo, maximo):
    """Devuelve True si numero esta dentro del rango inclusivo."""
    return minimo <= numero <= maximo


def es_par(numero):
    return numero % 2 == 0


def es_primo(numero):
    """Comprueba si un entero es primo usando una funcion recursiva."""
    if numero < 2:
        return False
    return _divisor_primo(numero, 2)


def _divisor_primo(numero, divisor):
    if divisor * divisor > numero:
        return True
    if numero % divisor == 0:
        return False
    return _divisor_primo(numero, divisor + 1)


def es_multiplo(numero, otro):
    if otro == 0:
        return False
    return numero % otro == 0
