
def absoluto(x):
    if x > 0 :
        return x
    elif x < 0 :
        return -x
    else :
         return 0

def lista_absoluto(numeros:list) -> list:
    evaluador = list(map(absoluto,numeros))
    return evaluador

numeros = [1,2,3,4,0,-1,-2,-3,-4] 
salida = lista_absoluto(numeros)
print(salida)

    
