
def verificador_de_archivos(archivo):
    try:
        with open("archivo.txt", 'r') as archivo:
            contiene = archivo.read()
            return contiene
    except FileNotFoundError:
        print("Archivo no existe")

archivo = "texto.txt"
with open(archivo, 'w') as texto :
    texto.write("Hola a todos, soy Pedro.\n")
print(f"El archivo {archivo} se creo exitosamente")

funcion = verificador_de_archivos(archivo)
print(funcion)
        