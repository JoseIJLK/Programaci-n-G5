import random
def Tabla():
    matriz=[[int()for i in range(8)]for j in range(11)]
    matriz[0][0]="Marca/Dia"
    matriz[1][0]="Chevrolet"
    matriz[2][0]="Mazda"
    matriz[3][0]="Nissan"
    matriz[4][0]="Toyota"
    matriz[5][0]="Hyundai"
    matriz[6][0]="Kia"
    matriz[7][0]="Renault"
    matriz[8][0]="Great Wall"
    matriz[9][0]="JAC"
    matriz[10][0]="Chery"
    matriz[0][1]="L"
    matriz[0][2]="M"
    matriz[0][3]="M"
    matriz[0][4]="J"
    matriz[0][5]="V"
    matriz[0][6]="S"
    matriz[0][7]="T"

    for m in range(6):
        for n in range(10):
            valor=random.randint(0,4)
            matriz[n+1][m+1]=valor
    suma=0
    n=1
    f=1
    while n<11:
        valor=matriz[n][f]
        suma+=valor
        matriz[n][7]=suma
        f+=1
        if f==7:
            n+=1
            f=1
            suma=0
            
    for i in range(11):
        print("|",end="")
        for j in range(8):
            print(matriz[i][j],"|",end="")
        print("\n")

Tabla()