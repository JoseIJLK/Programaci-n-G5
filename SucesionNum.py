
def SucesionNum():
    n=int(input("n: "))
    suma=0
    num=1
    for n in range (n):
        r=2**num
        num+=1
        suma+=r
    print(suma)
    
SucesionNum()