def Ordena(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista
print(Ordena([50,30,200,52,34,1001,5]))
print(Ordena(["Mateo","José","Anthony"]))