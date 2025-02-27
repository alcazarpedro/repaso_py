
def suma_numeros(x:int,y:int,z:int) -> int:
    suma = lambda a,b,c : a + b + c
    return suma(x,y,z)

x = int(input('dame un numero: '))
y = int(input('dame un numero: '))
z = int(input('dame un numero: '))

sumando = suma_numeros(x,y,z)
print(sumando)

