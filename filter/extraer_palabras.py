
def check_longitud(cadena):
    if len(cadena) == 5 :
        return True
    return False

def extraer_letter(elementos:list) -> list:
    evaluador = list(filter(check_longitud,elementos))
    return evaluador

elementos = ['Saiden','Pedro','Cafe','Pytho','Andrea','teamo']
check = extraer_letter(elementos)
print(check)
