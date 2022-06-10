def keyw(**datos):
    print("\nTipo de datos del argumento:",type(datos))

    for key, value in datos.items():
        print("{} is {}".format(key,value))

keyw(Firstname="Juan", 
     Lastname="Domínguez", 
     Age=42, 
     Phone=1234567890)
keyw(Firstname="John", 
     Lastname="Wood",
     Email="johnwood@nomail.com",
     Country="Wakanda", 
     Age=25, 
     Phone=9876543210)