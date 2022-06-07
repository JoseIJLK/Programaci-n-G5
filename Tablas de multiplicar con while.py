num1=1
while num1<16:
    print("La tabla de #",num1)
    num2=1
    suma=0
    par=0
    impar=0
    while num2<16:
        r=num2*num1
        print(num2,"x",num1,"=",r)
        num2=num2+1
        if r%2==0:  
            par=par+1
        else:
            impar=impar+1
        suma=suma+r
        promedio=suma//15
    num1=num1+1
    print("La suma de los valores es:",suma)
    print("El promedio es:",promedio)
    print("Hay",par,"numeros pares")
    print("Hay",impar,"numeros impares")
