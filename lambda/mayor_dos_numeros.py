
def mayor_numero(a:int,b:int) -> int:
    mayor = lambda i, j : max(i,j)
    return mayor(a,b)

a = 67
b =40
maximo = mayor_numero(a,b)
print(maximo)