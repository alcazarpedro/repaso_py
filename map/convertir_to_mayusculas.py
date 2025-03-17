

def str_lower_to_upper(palabras:list) -> list:
    map_upper = list(map(str.upper,palabras))
    return map_upper

cadena = ['hola','adios','me encantas','hi','bye','i love it']
upper_list = str_lower_to_upper(cadena)
print(upper_list)
