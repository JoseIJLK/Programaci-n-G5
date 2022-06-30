def Palindromo():
    num=input("Ingrese un numero: ")
    if int(num)<10:
        print(num,"no palíndromo") 
    elif num == num[::-1]: 
        print(num,"palíndromo") 
    else:
        print(num,"no palíndromo") 

Palindromo()