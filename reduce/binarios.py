from functools import reduce

def binario(lista:list) -> list:
    n_binario = reduce(lambda acum , numero : acum + [bin(numero)[2:]],lista,[])
    return n_binario

lista = [4,3,2,5]
new_binary = binario(lista)
print(new_binary)

