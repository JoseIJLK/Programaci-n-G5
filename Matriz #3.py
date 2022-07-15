import random
while True:
    filas=int(input("Ingrese el numero de filas: "))
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

print("Los valores de la diagonal principal son:")
for k in range(filas):
    print("|",matriz[k][k],end=" | ")
print("\n")

print("Los valores de la diagonal secundaria son:")
v=columnas-1
for l in range(filas):
    print("|",matriz[l][v],end=" | ")
    v-=1
print("\n")