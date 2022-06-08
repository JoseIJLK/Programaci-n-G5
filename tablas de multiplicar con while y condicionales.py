num1=1
while True:
    n=int(input("Ingrese el numero de tablas: "))
    if n<1:
        print("Error el numero debe ser positivo")
    else:
        break
while True:
    m=int(input("Ingrese hasta que numero multiplicar: "))
    if m<1:
        print("Error el numero debe ser positivo")
    else:
        break
while num1<=n:
    print("La tabla de #",num1)
    num2=1
    suma=0
    par=0
    impar=0
    while num2<=m:
        r=num2*num1
        print(num2,"x",num1,"=",r)
        num2+=1
        if r%2==0:  
            par+=1
        else:
            impar+=1
        suma+=r
    num1+=1
    print("La suma de los valores es:",suma)
    print("El promedio es:",suma//m)
    print("Hay",par,"numeros pares")
    print("Hay",impar,"numeros impares","\n")