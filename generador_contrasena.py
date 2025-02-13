import random
import string

def contrasena_generador(elementos):
    caracteres = string.ascii_letters+string.digits+string.punctuation
    pasword = ''.join(random.choices(caracteres,k= elementos))
    return pasword

elementos = int(input('dame la longitud de tu constraseña_> '))
output = contrasena_generador(elementos)
print(output)
