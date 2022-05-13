contador=0
contadorI=0
contadorN=0
while True:
    while True:
        num1=int(input("Ingrese el primer numero: "))
        num2=int(input("Ingrese el segundo numero: "))
        if num1==num2:
            print("ERROR Los numeros ingresados son iguales")
            contadorI+=1
        elif num1<1 or num2<1:
            print("ERROR Los numeros ingresados son negativos")
            contadorN+=1
        else:
            break
        contador=contador+1
    print("las veces que se ha ejecutado este codigo son: ",contador)
    print("las veces que se ibgresasor numeros iguales son: ",contadorI)
    print("las veces que se ibgresasor numeros negativos son: ",contadorN)
    x=input("Dijite q o quit para salir o cualquier tecla para continuar: ")
    if x=="q" or x=="quit":
        break