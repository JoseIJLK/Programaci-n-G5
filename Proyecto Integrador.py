def Calculadora():
    while True:
        print("--------------------------------Proyecto Integrador--------------------------------")
        print("------------------------------Calculadora de Momentos------------------------------")
        
        while True:    
            fuerza=int(input("Ingrese la fuerza: "))
            if fuerza<0:
                print("Error el valor de fuerza no puede ser negativa")
            else:
                break
            
        while True:
            distancia=int(input("Ingrese la distancia: "))
            if distancia<0:
                print("Error el valor de distancia no puede ser negativa")
            else:
                break
            
        def UFuerza():
            print("\nEscoja la unidad de media de la fuerza")
            print("Newton (N): 1")
            print("Kilonewton (kN): 2")
            print("Libra Fuerza (lb): 3")
            while True:
                UF=int(input("Ingrese su elección: "))
                if UF<1 or UF>3:
                    print("Error el valor ingresado no se encuentra en la tabla")
                else:
                    break
            if UF==1:
                UF="N"
            if UF==2:
                UF="kN"
            if UF==3:
                UF="lb"
            return UF
                
        def UDistancia():
            print("\nEscoja la unidad de medida de la distancia")
            print("Kilómetro (km): 1")
            print("Metro (m): 2")
            print("Centímetro (cm): 3")
            print("Milímetro (mm): 4")
            print("Pies (ft): 5")
            while True:
                UD=int(input("Ingrese su elección: "))
                if UD<1 or UD>5:
                    print("Error el valor ingresado no se encuentra en la tabla")
                else:
                    break
            if UD==1:
                UD="km"
            if UD==2:
                UD="m"
            if UD==3:
                UD="cm"
            if UD==4:
                UD="mm"
            if UD==5:
                UD="ft"
            return UD
                
            
        def Direccion():
            print("\nEscoja la direccion de la fuerza")
            print("↑: 1")
            print("↓: 2")
            print("→: 3")
            print("←: 4")
            while True:
                D=int(input("Ingrese su elección: "))
                if D<1 or D>4:
                    print("Error el valor ingresado no se encuentra en la tabla")
                else:
                    break
            if D==1:
                D="Antihorario"
            if D==2:
                D="Horario"
            if D==3:
                D="Antihorario"
            if D==4:
                D="Horario"
            return D
                
        def Momento():
            Momento=fuerza*distancia
            return Momento
        
        RUF=UFuerza()
        RUD=UDistancia()
        RD=Direccion()
        M=Momento()
        
        print("\nEl momento de",fuerza,RUF,"a",distancia,RUD,"de distancia es de",M,RUF,"*",RUD,"en sentido",RD)
        R=input("Desea reiniciar el programa: ")
        if R=="NO" or R=="No" or R=="no":
            break
        
Calculadora()