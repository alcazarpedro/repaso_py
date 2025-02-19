
def eliminar(elementos:list)->list:
    elementos_unicos = []
    for valor in elementos:
        if valor not in elementos_unicos:
            elementos_unicos.append(valor)
    return elementos_unicos

elementos = [5,1,4,2,3,1,6,2,1,8]
sin_duplicados = eliminar(elementos)
print(sin_duplicados)

