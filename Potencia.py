def Potencia (base,exponente):
    r=base**exponente
    print("base:",base)
    print("exponente: ",exponente)
    if base<1 or exponente<1:
        print("Error...!!!")
    else:
        print(r)
        
Potencia(-1,7)
Potencia(2,3)
Potencia(3,-2)