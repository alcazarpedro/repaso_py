
def verificar_edad(edad:int) -> int:
    if edad < 0:
        raise ValueError  ('La edad no puede ser negativa')
    return edad

edad = int(input('escribe una edad : '))
try :
    verificar_edad(edad)
except ValueError as e:
    print("ERROR!!!!: ",e)
    

    
        
