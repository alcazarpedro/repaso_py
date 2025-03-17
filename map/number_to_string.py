
def evaluador_int_to_str(numeros):
    return str(numeros)

def map_int_to_str(valores:list) -> list:
    cadena = list(map(evaluador_int_to_str,valores))
    return cadena

valores = [12,34,56,1,76,87,44,90]
mapeo = map_int_to_str(valores)
print(mapeo)
