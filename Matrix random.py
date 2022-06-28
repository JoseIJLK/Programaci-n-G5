import random
matrix = [[int() for i in range(4)] for j in range(4)]
for filas in range(4):
    for columnas in range(4):
        valor=random.randint(0, 100)
        matrix[filas][columnas]=valor

for i in range(4):
    print("| ", end=" ")
    for j in range(4):
        print(matrix[i][j]," | ",end=" ")
        
    print("\n")