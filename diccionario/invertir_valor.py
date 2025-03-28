
def invertir_diccionario(valores:dict)->dict:
    dicc_invertido = {}
    for k,v in valores.items():
        dicc_invertido[v] = k
    return dicc_invertido

datos = {
    'Pedro':'Alcazar',
    'Nancy':'Vazquz',
    'Jacqueline':'Medrano'
}   

reverse = invertir_diccionario(datos)
print(reverse)
