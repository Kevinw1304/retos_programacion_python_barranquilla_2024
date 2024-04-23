
def incremento (n):
    return n+1
        
def decremento (n):        
    return n-1

def suma (n,m):
    for i in range (m):
        n=incremento (n)
    return n

def resta (n,m):
    for i in range (m):
        n=decremento (n)
    return n    

def multiplicación (n,m):
    acumulador = 0
    for i in range (m):
        acumulador=suma(acumulador,n)
    return acumulador    



