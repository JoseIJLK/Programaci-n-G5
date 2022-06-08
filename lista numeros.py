lista=[]
suma=0
for i in range (1,11):
    valor=int(input("Ingrese un numero:"))
    lista.append(valor)
    suma+=valor
print("La lista es ",lista)
print("la suma de los valores es: ",suma)
print("El promedio es: ",suma/10)