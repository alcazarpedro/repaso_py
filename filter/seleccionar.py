
def check_nombre(nombre):
    if nombre[0] == "A" :
        return True
    return False

def selccion_nombres(datos:list) -> list:
    nombres_A = list(filter(check_nombre,datos))
    return nombres_A

datos = ["Juan","Ana","Isabel","Adriana","Valeria","Angie","Ada"]
evaluador = selccion_nombres(datos)
print(evaluador)
