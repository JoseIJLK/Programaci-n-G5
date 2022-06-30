def Primos():
    for i in range(2, 150 + 1):
        primos = True
        for j in range(2,i):
            if i == j:
                break
            elif i%j == 0:
                primos = False
            else:
                continue
        if primos == True:
            print('|',i, end='')

Primos()