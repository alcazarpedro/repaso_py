
def impar_par(elemento:int)->str:
    if elemento % 2 == 0:
        return f'{elemento} es par'
    else:
        return f'{elemento} es impar'
    
elemento = int(input('dame un numero racional : '))

out = impar_par(elemento)
print(out)