import random
import time
vector=[]
num=int(input("Ingrese la dimensión del vector: "))
for n in range(num):
    r=random.randint(50, 100)
    vector.append(r)
time.sleep(1)
print(vector)
for i in range(len(vector)-1):
    for j in range(len(vector)-1):
        if vector[j]>vector[j+1]:
            temporal=vector[j]
            vector[j]=vector[j+1]
            vector[j+1]=temporal
time.sleep(1)
print(vector)
