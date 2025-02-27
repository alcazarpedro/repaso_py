
def ordenar_lista(valores:list) -> list:
    valores = sorted(valores , key= lambda valor : valor[1])
    return valores

valores = [('Felipe',23),('Majo',18),('Juan',27),('Saiden',29),('Adriana',15)]
lista_tupla_ordena = ordenar_lista(valores)
print(lista_tupla_ordena)