
def invertir(datos:dict) -> dict:
    unicos_k_v = {v:k for k,v in datos.items() if datos[k] != k }
    return unicos_k_v


datos = {
    'Jiu' : 'Corea Sur',
    'Alcazar': 'Colombia',
    'Perez': 'Mexico',
    'Jiu' : 'Corea Sur'
}

output = invertir(datos)
print(output)

