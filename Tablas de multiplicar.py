for n in range (1,16):
    print("La tabla de #",n)
    suma=0
    par=0
    impar=0
    for i in range (1,16):
        r=i*n
        print(i,"x",n,"=",r)
        if r%2==0:  
            par=par+1
        else:
            impar=impar+1
        suma=suma+r
        promedio=suma//15
    print("La suma de los valores es:",suma)
    print("El promedio es:",promedio)
    print("Hay",par,"numeros pares")
    print("Hay",impar,"numeros impares")    
