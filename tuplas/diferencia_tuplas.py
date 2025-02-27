
def diferencias(valores_1:tuple,valores_2:tuple) -> tuple:
    resultado = set  (valores_1 + valores_2)
    resultado = tuple(resultado)

    return resultado

valores_1 = (1,2,3,4)
valores_2 = (3,4,5,6)
out = diferencias(valores_1,valores_2)
print(out)    
