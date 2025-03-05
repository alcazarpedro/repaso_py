from functools import reduce
def menor_de_una_list(valores:list) -> int:
    menor = reduce(lambda a,b : a if a < b else b , valores)
    return menor

valor = [23,45,12,6,124,1,2,9,10]
minimo = menor_de_una_list(valor)
print(f'menor de la lista {valor} es : {minimo}')