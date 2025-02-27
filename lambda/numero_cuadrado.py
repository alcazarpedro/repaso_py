
def cuadrado_lambda(numero:int) -> int:
    cuadrado = lambda x : x **2
    return cuadrado(numero)
    

numero = 6
numero_c = cuadrado_lambda(numero)
print(numero_c)