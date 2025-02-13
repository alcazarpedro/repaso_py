
def palabras_ordenadas(cadena:list)->list:
    palabras_unicas = sorted(list(set(cadena)))
    return palabras_unicas

cadena = ['pera','uva','melon','manzana','pera','piña','sandia','melon','uva','arandano']
ordenar = palabras_ordenadas(cadena)
print(ordenar)
