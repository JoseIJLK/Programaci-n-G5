mayor=0
menor=0
suma=0
lista=[]
for i in range (1,6):
    estatura=float(input("Ingrese la estatura: "))
    suma+=estatura
    lista.append(estatura)
promedio=suma/5
print("El promedio es: ",promedio)
for j in range (5):
    if lista[j]<promedio:
        mayor+=1
    else:
        menor+=1
print("Hay",mayor,"personas mayor al promedio")
print("Hay",menor,"personas menor al promedio")