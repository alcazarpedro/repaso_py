
def tupla_diccionario(nombres:list,datos:list) -> dict:
    dicc = {nombre:dato for nombre ,dato in zip(nombres,datos) }
    return dicc

nombres = ["Pedro","Mateo","Juan"]
datos =[(35,'Betsaida','Pescador'),(34,'Cafarnaum','Publicano'),(21,"Galilea",'Pescador')]
diccionario = tupla_diccionario(nombres,datos)
print(diccionario)

    