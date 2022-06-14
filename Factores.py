def factor():
    numero=int(input("Ingrese un numero: "))
    factores=[]
    f=1
    while f<=numero:
        if numero%f==0:
            factores.append(numero//f)
            factores.sort()
        f+=1
    print("los factores de", numero,"son: ")
    for f in factores:
        print(f,end=",")
factor()