
def vocales(cadena:str) -> int:
    vocal = 'aeiuo'
    
    count_vocal = len(list(filter(lambda texto: texto in vocal,cadena)))
    return count_vocal

cadena = 'Margarita'
numero_de_vocales = vocales(cadena)
print(numero_de_vocales)