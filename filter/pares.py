
def check_par(num):
    if num % 2 == 0:
        return True
    return False

def numeros_pares(valores:list) -> list:
    evaluador_par = list(filter(check_par,valores))
    return evaluador_par

valores = [3,4,5,6,7,8,1,2]
new_list_par = numeros_pares(valores)
print(new_list_par)
