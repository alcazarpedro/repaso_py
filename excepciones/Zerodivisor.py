
def verificar_division(a:int,b:int) -> int:
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: incorrecto no se puede dividir entre cero")

a = int(input('Dasme un dividendo : '))
b = int(input('Dame el divisor : '))

resultado = verificar_division(a,b)
print(resultado)

