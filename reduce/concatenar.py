from functools import reduce

def concatenar_lista(texto:list) -> str:
    concatenacion = reduce(lambda letter, word : letter + word , texto)
    return concatenacion

texto = ['hola',' ','sabes',' ','Jesus',' ','te',' ','ama']

concat = concatenar_lista(texto)
print(concat)
