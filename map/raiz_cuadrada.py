import math

def map_sqrt(x):
    return round(math.sqrt(x),2)

def raiz_cuadrada(enteros:list)  -> list:
    cuadrada = list(map(map_sqrt,enteros))
    return cuadrada

numeros = [144,56,25,16,9,34,64,36,81]
raiz = raiz_cuadrada(numeros)
print(raiz)

    