
def Fahrenheit(grados):
    return (grados*9/5)+32

def celsius_a_fahr(celsius:list) -> list:
    evaluador = list(map(Fahrenheit,celsius))
    return evaluador

celsius = [23,29,35,37,-10,27,22]
fahr = celsius_a_fahr(celsius)
print(fahr)
