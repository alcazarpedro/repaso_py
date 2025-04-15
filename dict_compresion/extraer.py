
def extraccion_de_datos(emplados:list) -> dict :
    extraer = {empleado['nombre'] : empleado['salario'] for empleado in empleados}
    return extraer

empleados = [
    {
        'nombre' :'Alberto',
        'ocupacion' : 'Administrador',
        'salario' : 12000
    },
    {
        'nombre' : 'Fabiola',
        'ocupacion' : 'Banca',
        'salario' : 13400
    },
    {
        'nombre' :'Datsy',
        'ocupacion' : 'contadora',
        'salario' : 15780
    }
]
data_employes = extraccion_de_datos(empleados)
print(data_employes)

