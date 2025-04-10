def filtrar_datos(datos:dict) -> dict:
    numericos = {v for v in datos if datos[v] is not str }
    return numericos

datos = {
    'Mexico': 235412,
    'Francia': 'Paris',
    'Colombia': 56799,
    'Espana': 'Madrid',
    'Peru': 12345
}

output = filtrar_datos(datos)
print(output)