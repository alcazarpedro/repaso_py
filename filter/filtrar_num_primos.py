
def check_primos(primos):
    if primos % 2 != 0 :
        return True
    return False

def evaluar_primos(enteros:list) -> list:
    primos_filter = list(filter(check_primos,enteros))
    return primos_filter

enteros = [2,1,4,3,6,5,10,7,8,9,11]
primos_output = evaluar_primos(enteros)
print(primos_output)


