
def cuadrados(valores:list) -> dict:
    pares = {k:k**2 for k in valores if k % 2 == 0}
    return pares

valores = [1,2,3,4,5,6,7,8,9,10]
pares_cuadrados = cuadrados(valores)
print(pares_cuadrados)