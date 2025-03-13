
def check_bool(elemento):
    if elemento == True:
        return True
    return False

def filtrar_True(valores:list) -> list:
    evaluador = list(filter(check_bool,valores))
    return evaluador

valor = [12,'Paris',23.4,False,3,'Francia',True,'Joven',True,2,4,5,True]

output = filtrar_True(valor)
print(output)


