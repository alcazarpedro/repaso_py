def frecuencia(elementos:list) -> dict:
    longitudes = {}
    for k in elementos:
        longitudes[k] = len(k)
    return longitudes

elementos = ['python','java','rust','script'] 
out = frecuencia(elementos)
print(out)


