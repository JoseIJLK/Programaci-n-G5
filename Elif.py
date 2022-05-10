acl=int(input("Ingrese el # de ACL: "))
if acl>=1 and acl<=99:
    print("Es un ACL Estandar")
elif acl>=100 and acl<=199:
    print("Es un ACL extendida")
else:
    print("El # ingresado no es un ACL")