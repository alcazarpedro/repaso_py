
def concatenar_condicion(elemeto1:tuple,elemento2:tuple) -> tuple:
    concatenar = ()
    if len(elemeto1) == len(elemento2):
        concatenar = elemeto1 + elemento2
    else:
        return elemeto1, elemento2
    return concatenar

elemento1 = (1,2,3,5,4)
elemento2 = (4,5,6,7,1)
salida = concatenar_condicion(elemento1,elemento2)
print(salida)
    