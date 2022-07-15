import random
while True:    
    matriz = [[int() for i in range(8)] for j in range(11)]
    valor1=0
    valor2=0
    for a in range(88):
        valor=random.randint(0,10)
        matriz[valor1][valor2]=valor
        if valor1==10:
            valor1=0
            valor2+=1
        else:
            valor1+=1   
    matriz[0][0]="           "
    n=1
    for b in range(10):
        matriz[b+1][0]="Materia "+str(n)
        n+=1
    n=1
    for c in range(7):
        matriz[0][c+1]="Nota "+str(n)
        n+=1
    while True:
        print("\n")
        print("Promedio de notas de una materia M")
        print("Promedio de notas en todas las materias N")
        print("Visulizar todas las notas de todas las materias V")
        e=input("Ingrese su eleccion: ")
        if e=="M" or e=="m":
            m=int(input("Ingrese de que materia (1-10) desea el promedio de notas: "))
            print("\n","La materia escogida es:")
            for d in range(2):
                print("|", end=" ")
                for e in range(8):
                    if d>=1:
                        print(matriz[m][e],"  |   ",end=" ")
                    else:
                        print(matriz[d][e],"|",end=" ")
                print("\n")
            suma=0
            n=1
            for f in range(7):
                valor=matriz[m][n]
                suma+=valor
                n+=1
            print("El promedio de las notas en la materia",m,"es:",suma//7)
        if e=="N" or e=="n":
            m=int(input("Ingrese de que nota (1-7) desea el promedio: "))
            print("\n","La materia escogida es:")
            for d in range(11):
                print("|", end=" ")
                for e in range(2):
                    if e>=1:
                        print(matriz[d][m],"  |   ",end=" ")
                    else:
                        print(matriz[d][e],"|  ",end=" ")
                print("\n")
            suma=0
            n=1
            for f in range(10):
                valor=matriz[n][m]
                suma+=valor
                n+=1
            print("El promedio de la nota",m,"en todas las materias es:",suma//10)
        if e=="V" or e=="v":
            for j in range(11):
                print("|", end=" ")
                for k in range(8):
                    if j>=1:
                        print(matriz[j][k],"  |   ",end=" ")
                    else:
                        print(matriz[j][k],"|",end=" ")
                print("\n")
        r=input("Desea cambiar de notas: ")
        if r=="SI" or r=="Si" or r=="si":
            break
    c=input("Desea terminar el programa: ")
    if c=="SI" or c=="Si" or c=="si":
        break