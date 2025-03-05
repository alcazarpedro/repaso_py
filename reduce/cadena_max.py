from functools import reduce

def maxima_cadena(cadena:list) -> str:
    cadena_max = reduce(lambda i,j: i if len(i) > len(j) else j, cadena)
    return cadena_max

cadena = ['ana','platzi','fabiola','loropiana']
resultado = maxima_cadena(cadena)
print (resultado)