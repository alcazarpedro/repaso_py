
def verificador_error(texto:str) -> str:
    try:
        numero = int(texto)
        return numero
    except ValueError:
        print("No se puede convertir a int")

texto = input("Escribe lo que sea >_ ")
output = verificador_error(texto)
print(output)
