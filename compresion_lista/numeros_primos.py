
def n_primos(numeros:list,n:int)->list:
    primos=[i for i in numeros if i % 2 !=0][:n]
    
    return primos

numeros = [2,13,4,5,6,12,27,45,23,9,10,14,11,3,7,15]
n = 5
salida = n_primos(numeros,n)
print(salida)

