
def collatz(n:int) -> list:
    secuencia_collatz = []
    while n != 1 :
        if n % 2 == 0:
            n=  n // 2
        else :
            n =  3 * n +1
        secuencia_collatz.append(n)    
    return secuencia_collatz       

n = int(input("digite un numero : "))
secuencia = collatz(n)
print(secuencia)
