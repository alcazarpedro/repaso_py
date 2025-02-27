
def invertir_str(texto:str) -> str:
    texto_invertido = lambda cadena : cadena[::-1]
    return texto_invertido(texto)

texto = 'letter'
reverse_text = invertir_str(texto)
print(reverse_text)