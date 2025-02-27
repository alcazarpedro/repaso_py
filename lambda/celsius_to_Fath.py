def fath(grados:int) -> int:
    conversion = lambda celsius: (celsius * 9/5)+32
    return f'fahren = {conversion(grados)}'

grados = 23
fahren  = fath(grados)
print(fahren)
