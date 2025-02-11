def conversor_divisa(moneda,divisa):
    if moneda == 'USD':
        MXN = 20.64
        return divisa * MXN
    elif moneda == 'EUR':
        MXN = 21.25
        return divisa * MXN
    elif moneda == 'YEN':
        MXN = 0.14
        return divisa * MXN
    elif moneda == 'WON':
        MXN = 0.014
        return divisa * MXN
    else:
        return 'Lo siento no se encontro tu divisa'
    
moneda = input("ingresa tu clave _> ")
divisa = float(input("cantidad que quieres convertir"))

out = conversor_divisa(moneda,divisa)
print(out)