
def transponer(elementos):
    matriz_transpuesta = [list(i) for i in zip(*elementos)]
    return matriz_transpuesta

elementos = [
    [1,2,3],
    [5,6,7],
    [4,8,9]
]
transpuesta = transponer(elementos)
print('Matriz Transpuesta >_- ')
print(transpuesta)
