
def longitudes(texto):
    return len(texto)

def longitud_palabras(cadena:list) -> list:
    resultado = list(map(longitudes,cadena))
    return resultado

cadena = ['hidrogeno','oxigeno','sodio','nitrogeno']
output = longitud_palabras(cadena)
print(output)
