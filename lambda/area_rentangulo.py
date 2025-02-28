
def area(base:int,altura:int) -> int:
    calculo = lambda a,b : a * b
    return calculo(base,altura)

base = 12
altura = 16
area_calculada = area(base,altura)
print(f'base : {base} cm , altura : {altura} cm area es : {area_calculada} cm')
