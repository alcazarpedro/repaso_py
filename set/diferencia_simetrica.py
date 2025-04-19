
def diferencia(conjunto_a:set,conjunto_b:set)-> set:

    diferencia_set = conjunto_a  ^ conjunto_b
    return diferencia_set

conjunto_a = {1,2,5,4,6,8}
conjunto_b = {3,1,2,7,6,8}

dife = diferencia(conjunto_a,conjunto_b)
print(dife)
