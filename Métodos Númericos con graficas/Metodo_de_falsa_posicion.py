import numpy as np 
import matplotlib.pyplot as plt
print("Este programa determina usando el metodo de falsa posición  la raiz real de f(x)=cos(In(x))")
print ("¿desea evaluarlo en xl=0.1 y xu=1?(s/n)")#tiene una raiz en esos puntos
sn=str(input())
while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido
    print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
    sn=input()
if sn[0].lower()=="s":
    xl=0.1
    xu=1
else:
    xl=float(input("ingrese xl: "))
    while xl<=0: #con esto confirmamos que sean numeros continuos
        print ("ingrese un valor mayor a 0 para que el logaritmo no se indefina: ")
        xl=float(input("ingrese xl: "))
    xu=float(input("ingrese xu: "))
    while xl>=xu: #con esto confirmamos que sean numeros continuos
        print ("xl tiene que ser menor que xu, ingresa un xu mayor a ",xl)
        xu=float(input("ingrese xu: "))
a=xl
b=xu
i=1
xra=xl #solo es para almacenar el valor antiguo de xr
while True:
    fxl=np.cos(np.log(xl))
    fxu=np.cos(np.log(xu))
    xr=xu-(fxu*(xl-xu))/(fxl-fxu)
    fxr=np.cos(np.log(xr))
    fx=fxl*fxr
    if fx<(-0.0001):
        xu=xr
    elif fx>0.0001:
        xl=xr
    elif fx==0:
        print ("xr es raiz de f(x)")
        print ("f(X)=",fx)
        print ("xr=",xr)
        break
    re=(np.abs(xr-xra)/xr)
    xra=xr
    if np.abs(re)<=0.0001: #si no llega a 0, llegara a un intermedio de -0.001<=fx<=0.001 de la raiz
        print ("xr es raiz aprox de f(x) cuando")
        print ("f(X)=",fx)
        print ("xr=",xr)
        print ("Error relativo= ",re)
        break
    if i>=10000:
        print ("ya alcanzo las 10000 iteraciones, la raiz probablemente no se encuentre en el rango establecido, salir del programa")
        break
    i+=1 #El contar las repeticiones, sirve para poder evitar un bucle infinito
x=np.arange(a,b,(np.abs(a)+np.abs(b))/100)
y=np.cos(np.log(x))
plt.plot(x,y)
plt.plot(xr,fxr,"ro-")
plt.title('Grafica de:\nf(x)=cos(In(x))')
plt.xlabel('x')
plt.ylabel('y')
plt.show()