
def valores_unico(elementos:list,clave:str) ->list:
    clave_unica = [elemento[clave] for elemento in elementos]
    return clave_unica

personas = [
    {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Juan", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Sofía", "edad": 35, "ciudad": "Valencia"}
]
clave = "edad"
valor = valores_unico(personas,clave)
print(valor)

