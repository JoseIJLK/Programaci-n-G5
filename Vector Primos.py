import random
def vector():
    vector=[]
    primos=[]
    num=int(input("Ingrese la dimensión del vector: "))
    for n in range(num):
        r=random.randint(50, 100)
        vector.append(r)
        def numprimos(r, i=2):
            if i >= r:
                primos.append(r)
            elif r % i != 0:
                return numprimos(r, i + 1)
        numprimos(r)
      
    print("El vector es:")    
    print(vector)
    print("Los numeros primos son:")
    print(primos)
    def maymen(vector):
        mayor=max(vector)
        menor=min(vector)
        print("El numero mayor es: ",mayor)
        print("El numero menor es: ",menor)
    maymen(vector)
vector()