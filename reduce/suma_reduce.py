from functools import reduce
def sumar_reduce(valores:list) -> int:
    suma = reduce(lambda x,y : x + y , valores)
    return suma

valores = [3,15,9,23,7,11,55]
sumando = sumar_reduce(valores)
print(f'el total de la suma de la lista {valores} es : {sumando}')
