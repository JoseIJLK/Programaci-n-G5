def direccion(calle,barrio,ciudad):
    print("Su direccion es:")
    print("Su ciudad es: ",ciudad)
    print("El barrio de entrega es: ",barrio)
    print("La calle de su domicilio es: Av.",calle)
    
ci=input("Ingrese la ciudad: ")
cl=input("Ingrese la calle de entrega: ")
ba=input("Ingrese el sector de referencia para la entrega: ")

direccion(cl,ba,ci)