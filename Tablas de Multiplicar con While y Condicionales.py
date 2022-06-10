num1=1
while True:
    tablas=int(input("Ingrese el numero de tablas: "))
    if tablas<2:
        print("Error el numero no puede ser menor a 2")
    elif tablas>100:
        print("El numero no puede ser mayor a 100")
    else:
        break
while True:
    multiplicar=int(input("Ingrese hasta que numero multiplicar: "))
    if multiplicar<2:
        print("Error el numero no puede ser menor a 2")
    elif multiplicar>100:
        print("El nuumero no puede ser mayor a 100")
    else:
        break
while num1<=tablas:
    print("La tabla del #",num1)
    num2=1
    suma=0
    par=0
    impar=0
    while num2<=multiplicar:
        r=num2*num1
        print(num1,"x",num2,"=",r)
        num2+=1
        if r%2==0: 
            par+=1
        else:
            impar+=1
        suma+=r
    print("La suma de los valores de la tabla es:",suma)
    print("El promedio de los valores de tabla es:",suma//multiplicar)
    print("Hay",par,"numeros pares en la tabla del #",num1)
    print("Hay",impar,"numeros impares en la tabla del #",num1,"\n")
    num1+=1