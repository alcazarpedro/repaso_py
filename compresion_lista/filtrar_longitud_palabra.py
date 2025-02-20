
def filtrar_len(valores:list, n:int) -> list:
    filtrar =[i for i in valores if len(i) > n ]
    return filtrar

valores = ['lapiz','lis','papel','ana','python','apple']
n = 4
salida = filtrar_len(valores,n)
print(salida)

