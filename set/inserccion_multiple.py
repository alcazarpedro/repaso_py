
def inserccion(a:list, b:list,c:list) -> set:
    conjunto_1 = set(a)
    conjunto_2 = set(b)
    conjunto_3 = set(c)

    comunes = conjunto_1.intersection(conjunto_2).intersection(conjunto_3)


    return comunes

a = [5,1,2,3,6,7,8,9,5,6]
b= [9,2,3,7,10,1,0,8]
c = [4,11,6,12,8,13,5,14]
output = inserccion(a,b,c)
print(output)

