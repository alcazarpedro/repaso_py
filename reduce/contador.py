from functools import reduce

def contar_palabra(palabras:list) -> int :
    contador = reduce(lambda conta, letra : conta + [len(letra)],palabras,[])
    return contador

palabras = ['cadena','texto','frase']
cont = contar_palabra(palabras)
print(cont)