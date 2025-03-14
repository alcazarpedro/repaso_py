
def capitilzar_cadena(texto:list) -> list:
    evaluador = list(map(str.capitalize, texto))
    return evaluador

texto = ['daniela','fernanda','leslie','jessica']
text_capitalize = capitilzar_cadena(texto)
print(text_capitalize)
