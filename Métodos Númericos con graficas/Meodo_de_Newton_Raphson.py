import matplotlib.pyplot as plt
import numpy as np
print ("Utilice el método de Newton-Raphson para calcular la raíz de f(x) = cos⁴(4x)4x empleando como valor inicial x0=1")
print ("¿el valor inicial sera 1, y error aproximado sera de 0.0001 ¿desea cambiar el valor inicial por otro?(si/no)")
sn=str(input())
x=[1.0,0.0]
val=0.0001
while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido
    print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
    sn=str(input())
if sn=="s": #con este el usuario ingresa cuanto desea evaluar
    print ("Ingresa el valor inicial: ")
    x[0]=float(input())
while True:
    x[1]=x[0]-(4*x[0]*(np.cos(4*x[0]))**4)/(4*(np.cos(4*x[0])**3)*(-4*np.sin(4*x[0])+np.cos(4*x[0])))
    if x[1]==x[0]:
        print ("Con un error aproximado de: 0")
        break
    if x[1]!=0: #En caso de que el denominador sea 0, se ignorara esta evaluación para evitar errores
        y=np.abs((x[1]-x[0])/x[1])
    if y<=val:
        print ("Con un error aproximado de: ",y)
        break
    x[0]=x[1]
print ("La raiz de f(x) = cos⁴(4x)4x es: ")
print ("xr=",x[1])
