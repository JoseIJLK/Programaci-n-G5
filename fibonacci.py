#Importar del modulo math la raiz cuadrada
from math import sqrt as raiz
#Funcion Formula
def Formula(n):
    #Devolver la formula
    return ((1+raiz(5))**n-(1-raiz(5))**n)//(2**n*raiz(5))
#Funcion Fibonacci
def Fibonacci(num):
    #Contador n
    n=0
    #Calculo con el valor de n en la Formula
    f=int(Formula(n))
    #Bucle para el valor de f
    while f<=num:
        #Mostrar en pantalla el valor de f con formato
        print(f,end=" ")
        #Sumar 1 al contador n 
        n+=1
        #Volver el valor de f a la formula original
        f=int(Formula(n))
#Fibonacci(8)