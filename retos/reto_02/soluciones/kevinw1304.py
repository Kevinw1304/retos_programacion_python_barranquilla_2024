

def conteo_421(n: int):
   
    contador = 0
    while n>1:
        if n%2 == 0:
            n=n//2
        else:
            n=3*n+1
        contador += 1
    return contador    

        


if __name__ == '__main__':
    print(conteo_421(20))
    