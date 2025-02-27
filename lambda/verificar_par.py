
def par(elemento:int)-> bool:
    valor_par = lambda i : i % 2 == 0 
    return valor_par(elemento )

elemento = 24
resultado = par(elemento)
print(resultado)