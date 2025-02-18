
def rotar_derecha(valores,n):
    n = n % len(valores)
    return valores[-n:] + valores[:-n]

def rotar_izquierda (valores,n):
    n = n % len(valores)
    return valores[n:] + valores[:n]

valores = [2,7,5,11,15,13,3,17,1]
n = 3
x = 2
derecha = rotar_derecha(valores,n)
izquierda = rotar_izquierda(valores,x)

print(f'rotacion_derecha: {derecha} , rotacion_izquierda: {izquierda}')

