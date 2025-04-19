

def eliminar_numeros(conjunto:list) -> set:
    pares = []
    for i in conjunto:
        if i % 2 == 0:
            pares.append(i)
    set_pares  = set(pares)
    return set_pares
        


    

    


conjunto = [1,2,3,4,5,6,7,8]
output = eliminar_numeros(conjunto)
print(output)