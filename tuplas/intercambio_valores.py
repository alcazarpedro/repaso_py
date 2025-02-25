
def intercambio(a:int,b:int)-> tuple:
    
    tupla = (a,b)
    a,b = b,a
    tupla = (a,b)
    
    return tupla 

a = 19
b= 17
salida = intercambio(a,b)
print(salida)       


