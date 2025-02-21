import random
def generador_matriz(n,m):
    matriz =[[random.randint(1,50) for _ in range(n)] for _ in range(m)]
    generador = [fila for fila in matriz]
    return generador
n = 5
m = 3
matriz_generada = generador_matriz(n,m)
print(matriz_generada)