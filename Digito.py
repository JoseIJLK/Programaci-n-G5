def Digito ():
    N=int(input("Ingrese un n�mero: "))
    num=10
    while True:
        if N<num:
            num=num//10
            print("Digito:",N//num)
            break
        else:
            num=num*10
Digito()