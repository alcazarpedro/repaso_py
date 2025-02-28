
def palindrmo_str(palabra:str) -> bool:
    pldo = lambda cadena : cadena == cadena[::-1]
    return pldo(palabra)

palabra = "dabalearrozalazorraelabad"
palindromo = palindrmo_str(palabra)
print(palindromo)
