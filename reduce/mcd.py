from functools import reduce

def maximo_divisor(valores:list) -> int :
    comun_divisor = reduce(lambda a,b : a if b % a == 0 else b , valores)
    return comun_divisor

valor = [15,5,20]
comun = maximo_divisor(valor)
print(comun)
