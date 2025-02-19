
def encontrar_sublistas(valores,s):
    n = len(valores)
    resultado = []

    for i in range(n):
        for j in range(i,n):
            sublista = valores[i:j+1]
            if sum(sublista) == s:
                resultado.append(sublista)
    return resultado

valores = [5,3,7,1,2,12,11]
valor_s = 15

sublistas_encotradas = encontrar_sublistas(valores,valor_s)
if sublistas_encotradas:
    print('sublista encontradas: ')
    for sublista in sublistas_encotradas:
        print(sublista)
else:
    print('No se encontro ninguna sublista igual al valor_s >_- ', valor_s)    
