from functools import reduce
def multiplos_primos(valores:list) -> int:
    multiplo_tres_cinco = []
    
    for elemento in valores:
        if elemento % 3 == 0 or elemento % 5 ==0 :
            multiplo_tres_cinco.append(elemento)
    suma = reduce(lambda a,b : a+b,multiplo_tres_cinco)    
    return f'la suma de los multiplos 3 o 5 es : {suma}'

valores = list(range(1,1000))
new_listas = multiplos_primos(valores)
print(new_listas)

