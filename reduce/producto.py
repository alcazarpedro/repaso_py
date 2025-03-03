from functools import reduce

def producto_numeros(numeros:list ) -> int:
    producto = reduce(lambda a,b : a*b,numeros)
    return producto

numero = list(range(1,6))
reduce_producto = producto_numeros(numero)
print(reduce_producto)
