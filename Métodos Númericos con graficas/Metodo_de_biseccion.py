import numpy as np 
import matplotlib.pyplot as plt
print("Este programa determina usando el metodo de biseccion la raiz real de fx=(e^(-x/4))*sen(4x)")
print ("¿desea evaluarlo en xl=0.1 y xu=1?(s/n)")#para cumplir los requicitos del problema
sn=str(input())
while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido
    print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
    sn=input()
if sn[0].lower()=="s":
    xl=0.1
    xu=1.0
else:
    xl=float(input("ingrese xl: "))
    xu=float(input("ingrese xu: "))
    while xl>xu: #con esto confirmamos que sean numeros continuos
        print ("xl tiene que ser menor que xu, ingresa un xu mayor a ",xl)
        xu=float(input("ingrese xu: "))
no="s"
a=xl
b=xu
i=1
xra=xl
while True:
    xr=(xl+xu)/2
    fxl=np.exp(-xl/4)*np.sin(4*xl)
    fxr=np.exp(-xr/4)*np.sin(4*xr)
    fx=fxl*fxr
    if fxl==0: #si uno de los 2 es 0, fx sera 0, y si no es fxr, esto probocara que el resultado no sea el de la raiz, asi que en caso
        #de que suceda que fxl sea raiz, entonces, xr adquirira el valor y saldra en fx==0
        xr=xl
        fxr=fxl
    if fx<0:
        xu=xr
    elif fx>0:
        xl=xr
    elif fx==0: #si la funcion es igual a 0, entonces es raíz 
        print ("xr es raiz de f(x)")
        print ("f("+xr+")=",fx)
        print ("xr=",xr)
        break
    re=(np.abs(xr-xra)/xr)
    xra=xr
    if re>=(-0.0001) and re<=0.0001: #si no llega a 0, llegara a un intermedio de -0.0001<=fx<=0.0001 de la raiz
        print ("xr es raiz aprox de f(x) cuando: ")
        print ("f(X)=",fx)
        print ("xr=",xr)
        print ("Error relativo= ",re)
        break
    if i>=10000:
        print ("ya alcanzo las 10000 iteraciones, la raiz probablemente no se encuentre en el rango establecido, salir del programa")
        no="n" #asi no imprimira la coordenada de la raiz en la grafica
        break
    i+=1 #El contar las repeticiones, sirve para poder evitar un bucle infinito
x=np.arange(a,b,(np.abs(a)+np.abs(b))/100)
y=np.exp(-x/4)*np.sin(4*x)
plt.plot(x,y)
if no!="n":
    plt.plot(xr,fxr,"ro-")
plt.title('Grafica de:\nfx=(e^(-x/4))*sen(4x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()