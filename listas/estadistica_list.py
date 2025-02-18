import numpy as np
def media(elementos):
    valores = np.array(elementos)
    return round(valores.mean(),2)


def mediana(elementos):
    valores = np.array(elementos)
    x = np.median(valores)
    return x

def moda(elementos):
    valores = np.array(elementos)
    valor_unico, frecuencia = np.unique(valores, return_counts=True)
    moda_index = np.argmax(frecuencia)
    moda = valor_unico[moda_index]
    return moda


elementos = [12,33,14,23,45,12,1,5,78,19,10,12,1]
resultados = {
    'media': media(elementos),
    'mediana' : mediana(elementos),
    'moda': moda(elementos)
}
print(resultados)


    

