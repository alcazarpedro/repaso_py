def combinar_dict(datos:dict,elementos:dict) -> dict:
    diccionario_set = {}
    for k,v in datos.items():
        if k in elementos:
            diccionario_set[k] = v + elementos[k]
    return diccionario_set

datos = {
    'Pedro' : 10,
    'Valente': 7,
    'Jose': 9
}    
elementos = {
    'Pedro':8,
    'Valeria': 9,
    'Jose': 10
}   

combinar = combinar_dict(datos,elementos)
print(combinar)


