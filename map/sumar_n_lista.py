
def map_n(num):
    return num + 12


def suma(numeros:list) -> list:
    sumando=list(map(map_n,numeros))
    return sumando

    
    

enteros = [4,12,5,6,11,22]

lista_n = suma(enteros)
print(lista_n)
