import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs ):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f'tiempo de ejecucion : {fin - inicio:.4f} segundos')
        return resultado
    return envoltura

@medir_tiempo
def esperar():
    time.sleep(2)
    print('Termino la espera')

esperar()

    

