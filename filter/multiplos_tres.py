
def check_three(multiplo):
    if multiplo % 3 == 0:
        return True
    return False

def multiplos(numeros:list) -> list:
    evaluador_tres = list(filter(check_three,numeros))
    return evaluador_tres

valores = [24,10,33,12,5,7,16,21,22,36]
multiplo_de_tres = multiplos(valores)
print(multiplo_de_tres)
