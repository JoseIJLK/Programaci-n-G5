edad=int(input("Ingrese su edad: "))
if edad>=0 and edad<=11:
    print("Usted es un niño")
elif edad>=12 and edad<=17:
    print("Usted es un adolecente")
elif edad>=18 and edad<=29:
    print("Usted es un joven")
elif edad>=30 and edad<=45:
    print("Usted es un adulto")
elif edad>=46 and edad<=100:
    print("Usted es un adulto mayor")
