def numeroMayor ():
    A=int(input("Ingrese A: "))
    B=int(input("Ingrese B: "))
    C=int(input("Ingrese C: "))
    print("\n")
    if A>B:
        if A>C:
            print("Número mayor:",A)
        else:    
            print("Número mayor:",C)
    elif B>A:
        if B>C:
            print("Número mayor:",B)
        else:
            print("Número mayor:",C)

numeroMayor()