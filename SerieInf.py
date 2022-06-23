from math import factorial
def SerieInf():
    y=0
    x=int(input("Ingrese x: "))
    n=1
    while n<=x:
        if n==1:
            y=x
        else:
            if n==1:
                y=y-(x**n)/(factorial(n)*1)
            else:
                y=y+(x**n)/(factorial(n)*1)
        n+=2
    print(y)

SerieInf()