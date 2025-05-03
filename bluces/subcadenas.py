
def verificador_subcadenas(palabras:list,subcadena:str) -> list :
    lista_subcadenas = []
    for elemento in palabras :
        if subcadena in elemento :
            lista_subcadenas.append(elemento)
    return lista_subcadenas

palabras = ['manzana','naranja','banana','limon']
subcadena = 'ana'
out = verificador_subcadenas(palabras, subcadena)
print(out)
        


