import random
while True:
    filas=int(input("ingrese el numero de filas: "))
    if filas<4 or filas>30:
        print("Error el valor no puede ser menor a 4 o mayor a 30")
    else:
        break
while True:
    columnas=int(input("Ingrese el numero de columnas: "))
    print("\n")
    if columnas<4 or columnas>30:
        print("Error el valor no puede ser menor a 4 o mayor a 30")
    else:
        break
    
matriz = [[int() for i in range(columnas)] for j in range(filas)]
valor1=0
valor2=0
for n in range(filas*columnas):
    valor=random.randint(0,100)
    matriz[valor1][valor2]=valor
    if valor1==filas-1:
        valor1=0
        valor2+=1
    else:
        valor1+=1

for i in range(filas):
    print("|", end=" ")
    for j in range(columnas):
        print(matriz[i][j],"|",end=" ")
    print("\n")

nummay=0
for f in range(filas-1):
    for c in range(columnas-1):
        if matriz[f][c]>nummay:
            nummay=matriz[f][c]
            fila=f+1
            columna=c+1
print("El numero mayor es",nummay,"y esta en la posicion [",fila,"][",columna,"]")