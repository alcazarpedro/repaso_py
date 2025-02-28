
def remplazo_por_guiones(cadena:list) -> str:

    remplazo = lambda letter : "_".join(letter)
    return remplazo(cadena)

cadena = ['Dios','Te','Bendiga']
texto = remplazo_por_guiones(cadena)
print(texto)
