
def duplicar_numeros(entero):
    return entero * 2

def evaluador_map(elemento:list) -> list:
    elemento_duplicado = list(map(duplicar_numeros,elemento))
    return elemento_duplicado

elemento = [5,2,4,7,6,1,8,9,12]
check_map = evaluador_map(elemento)
print(check_map)
