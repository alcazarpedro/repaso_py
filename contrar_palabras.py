
def contador_palabras(cadena:str)->dict:
    contador = {letter:cadena.count(letter) for letter in set(cadena)}
    return contador

cadena = input('ingresa una palabra_>- ')
output = contador_palabras(cadena)
print(output)
