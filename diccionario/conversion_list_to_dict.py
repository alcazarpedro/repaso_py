def conversion(nombres:list,edades:list) -> dict:
    datos = {}
    for nombre,edad in zip(nombres,edades):
        datos[nombre] = edad
    return datos

nombres = ['Juan','Ismale','Valentina']
edades = [23,43,56] 
converse = conversion(nombres,edades)
print(converse)



