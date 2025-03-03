from functools import reduce

def numero_max(elementos:list) -> int:
    mayor = reduce(lambda i,j: max(i,j),elementos)
    return mayor

elementos = [0,67,12,45,87,12,1,2,34,9,85]
mayor_numero = numero_max(elementos)
print(f'numero mayor de la lista {elementos} es >_ {mayor_numero}')

