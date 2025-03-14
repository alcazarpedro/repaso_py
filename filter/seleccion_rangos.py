
def check_rangos(numero):
    if numero in range(10,21):
        return True
    return False

def rango_filter(lista:list) ->list:
    rango = list(filter(check_rangos,lista))
    return rango

lista = [5,7,10,9,12,4,13,14,15,16,1,20]
filtrar_range = rango_filter(lista)
print(filtrar_range)
