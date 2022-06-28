matriz = [[int() for i in range(4)] for j in range(4)]

num1=0
num2=0
while num1<4:
    matriz[num1][num2]=int(input("Ingrese un valor: "))
    if num2==3:
        num1+=1
        num2=0
    else:
        num2+=1