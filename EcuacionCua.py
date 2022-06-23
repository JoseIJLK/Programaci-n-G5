from math import sqrt as raiz
def EcuacionCua(a, b, c):
    print("a: ",a)
    print("b: ",b)
    print("c: ",c)
    f=((b**2)-4*a*c)
    if a==0:
        print("División para cero")
    elif f==0:
        x=(-b/(2*a))
        print("Única solución:")
        print("x=",x)
    elif f<0:
        print("Raiz negativa")
    elif f>0:
        x1=(-b+raiz(f))/(2*a)
        x2=(-b-raiz(f))/(2*a)
        print("Dos soluciones:")
        print ("x1=",x1)
        print ("x2=",x2)

EcuacionCua(0,7,1)
EcuacionCua(2,1,2)
EcuacionCua(1,-8,16)
EcuacionCua(1,4,-5)