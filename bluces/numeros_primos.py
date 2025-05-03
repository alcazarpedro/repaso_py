
def verificador_primo(numero:int ) -> int:
    if numero <= 1 : 
        return False
    if numero <= 3 :
        return True
    if numero % 2 == 0 or numero % 3 == 0 :
        return False
    
    i = 5
    while i * i <= numero :
        if numero % i == 0 or numero % (i + 2) == 0:
           return False
        i += 6
    return True
    
def primos_obtenidos(valores:list) -> list:
    primo = []
    for numero in valores:
        if verificador_primo(numero):
            primo.append(numero)
    return primo

valores = list(range(1,11))
prime_target = primos_obtenidos(valores)
print(prime_target)            
        
    
    
           