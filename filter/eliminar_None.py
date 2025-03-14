
def check_None(elemento):
    if elemento != None :
        return True
    return False

def evaluador_None(valores:list) -> list:
    sin_None = list(filter(check_None,valores))
    return sin_None

valores = [("Software",1500),("Hardware",2000),None,("Servicios Externos",2345),None,None,("Labor",4560)]
output_none = evaluador_None(valores)
print(output_none)
