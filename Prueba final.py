import random
while True:
    filas=int(input("Ingrese el numero de filas: "))
    if filas<4 or filas>10:
        print("Error el valor no puede ser menor a 4 o mayor a 10")
    else:
        break
while True:
    columnas=int(input("Ingrese el numero de columnas: "))
    if columnas<4 or columnas>10:
        print("Error el valor no puede ser menor a 4 o mayor a 10")
    else:
        break
    
matriz = [[int() for i in range(columnas)] for j in range(filas)]

def numrandom():
    for f in range(filas):
        for c in range(columnas):
            valor=random.randint(0,5)
            matriz[f][c]=valor
        
numrandom()

for i in range(filas):
    print("|", end=" ")
    for j in range(columnas):
        print(matriz[i][j],"|",end=" ")
    print("\n")

def sumaf(fila):
    sumaf=0
    for s in range(columnas):
        valorf=matriz[fila-1][s]
        sumaf+=valorf
    print("la suma de la fila",fila,"es:",sumaf)
    
def sumac(columna):
    sumac=0
    for b in range(filas):
        valorc=matriz[b][columna-1]
        sumac+=valorc
    print("la suma de la columna",columna,"es:",sumac)
    print("\n")

for k in range(filas):   
    sumaf(k+1)
    sumac(k+1)

def promedio():
    sumat=0
    for p in range(filas):
        for q in range(columnas):
            suma=matriz[p][q]
            sumat+=suma
    print("El promedio de los numeros de la matriz es:",sumat/(filas*columnas))
promedio()