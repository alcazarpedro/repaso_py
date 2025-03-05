from functools import reduce
def factorial(elementos:list) -> int:
    factor = reduce(lambda x,y: x * y , elementos)
    return factor

n = int(input('dame un numero >_ '))
elementos = list(range(1,n+1))
producto = factorial(elementos)
print(f'factorial de la lista {elementos} es : {producto}')

