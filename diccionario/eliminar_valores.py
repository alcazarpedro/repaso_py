def eliminar_none(datos:dict)-> dict:
    datos_dict = {}
    for k,v in datos.items():
        if v is not None:
            datos_dict[k] = v
    return datos_dict

datos ={
    'Jorge': 'Ing.sistemas',
    'Sebastian': 'Finanzas',
    'Pedro Luis': 'Analista de Datos',
    'ana': None
}      

eliminados = eliminar_none(datos)
print(eliminados)

