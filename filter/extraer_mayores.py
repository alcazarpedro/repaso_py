import random
def check_maximo(numeros,valor_maximo):
    return numeros == valor_maximo

def maximo(valores:list) -> list:
    
    valor_maximo = max(valores)
    filtar =  filter(lambda x : check_maximo(x,valor_maximo), valores)

    return list(filtar)

valores = [23,45,65,1,123,0,2,5,6,7,891]

check_filter = maximo(valores)
print(check_filter)
