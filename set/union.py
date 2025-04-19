
def union_set(conjunto_a:set,conjunto_b:set) -> set:
    
    union_nuevo = conjunto_a | conjunto_b
    return union_nuevo

conjunto_a = {1,2,3,4,5}
conjunto_b = {4,6,7,8,9}

new_union = union_set(conjunto_a,conjunto_b)
print(new_union)

