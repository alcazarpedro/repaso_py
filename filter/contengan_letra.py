
def check_e(cadena):
    if "e" in cadena:
        return True
    return False

def evaluador(palabras:list) -> list :
    palabras_e = list(filter(check_e,palabras))
    return palabras_e

palabras = ["Pedro","Juan","Jose","Ariane"]
filtrado = evaluador(palabras)
print(filtrado)
