from math import sin,cos,tan,radians
print("Funciones trigonométricas sen, cos, tan.")
def FuncionesTri(angulo):
    x=radians(angulo)
    print("Sin:",angulo,"=",sin(x))
    print("Cos:",angulo,"=",cos(x))
    print("Tan:",angulo,"=",tan(x))
    
FuncionesTri(30)
FuncionesTri(60)
FuncionesTri(90)
FuncionesTri(120)    