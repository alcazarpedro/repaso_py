
def normalizacion(sets:dict) -> dict :
    new_dict = { k.upper():v+1 for k,v in sets.items()}
    return new_dict

sets = {
    'paulina':23,
    'saon':34,
    'whonee':25
}

datos = normalizacion(sets)
print(datos)
