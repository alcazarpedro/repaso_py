
def combinacion(elemento_1:list, elemento_2:list)-> list:
    nueva_lista = []
    for i in elemento_1:
        nueva_lista.append(i)
    for i in elemento_2:
        nueva_lista.append(i) 
    return nueva_lista       
    

elemento_1 = [1,2,3,4,5]
elemento_2 = [6,7,8,9,10]
lista_ordenada = combinacion(elemento_1,elemento_2)
print(lista_ordenada)