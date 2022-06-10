def suma(*a):
    print("\nTipo de datos del argumento:",
         type(a))
    sum = 0
    for n in a:
        sum +=n
        #sum=sum+n

    print("Suma:",sum)

suma(3)
suma(1)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)
suma(1,2,3,5,6,7,8,9,10)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17)
