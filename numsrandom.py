import random
def aleatorio(n):
    lista=[]
    for i in range(n):
        r = random.randint(0, 100)
        lista.append(r)        
    print(lista)
