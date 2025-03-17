
def cubo_check(y):
    return y ** 3

def pontecia_tres(radicales:list) -> list:
    cubico = list(map(cubo_check,radicales))
    return cubico

enteros = [9,5,3,8,13,7,17]
pontencia = pontecia_tres(enteros)
print(pontencia)
