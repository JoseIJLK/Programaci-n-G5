def validar(nombre,edad,cedula,email):
    
    Vcedula = len(cedula)
    if nombre.istitle():
        print ("True")
    else:
        print("False")
    
    if edad.isdigit():
        print ("True")
    else:
        print("False")
    
    if Vcedula==10:
        print ("True")
    else:
        print("False")
    
    if "@" in email:
        print ("True")
    else:
        print("False")
    
validar("Alison Porozo","35","012345490","aporozo@edu.ec")