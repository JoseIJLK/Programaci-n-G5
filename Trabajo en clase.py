import random
while True:
    while True:
        num=int(input("Ingrese la dimension: "))
        vector1=[]
        vector2=[]
        if num<5:
            print("Error no puede ingresar un numero menor a 5")
        elif num>30:
            print("Error no puede ingresar un numero mayor a 30")
        else:
            for n in range(num):
                r1=random.randint(0, 100)
                vector1.append(r1)
            for i in range(num):
                r2=random.randint(0, 100)
                vector2.append(r2)
            print("Vector 1")
            print(vector1)
            print("Vector 2")
            print(vector2,end="\n")
            break
    
    print("\n""Suma S")
    print("Resta R")
    print("Multiplicación M")
    print("División D")
    oper=input("Ingrese la operacion que desea realizar: ")
    if oper=="S" or  oper=="s":
        suma=[]
        for i in range(len(vector1)):
            suma.append(vector1[i]+vector2[i])
        print(suma)
    elif oper=="R" or oper=="r":
        resta=[]
        for i in range(len(vector1)):
            resta.append(vector1[i]-vector2[i])
        print(resta)
    elif oper=="M" or oper=="m":
        multiplicación=[]
        for i in range(len(vector1)):
            multiplicación.append(vector1[i]*vector2[i])
        print(multiplicación)
    elif oper=="D" or oper=="d":
        división=[]
        for i in range(len(vector1)):
            división.append(vector1[i]/vector2[i])
        print(división)
    
    R=input("Desea continuar Si o No: ")
    if R=="no" or R=="No" or R=="NO":
        break