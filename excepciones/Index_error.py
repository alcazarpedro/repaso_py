
def verificar_indice_lista(elementos:list,indice:int) -> int:
    try:
        return elementos[indice]
    except IndexError:
        print("ERROR: El indice esta fuera del rango dado")

valores = [1,2,3,4,5,6]
indice = int(input('Digite un indice que dese saber >_ '))
index = verificar_indice_lista(valores,indice)
print(index)
