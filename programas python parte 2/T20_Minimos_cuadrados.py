#Tarea 20, para lenguajes de programacion
import matplotlib.pyplot as plt
import numpy as np
print ("Minimos cuadrados")
print ("Este programa calcula la pendiente (m), la intercepcion(b) y el coeficiente de relacion(r) de una regresion lineal")
print ("¿Cuantos datos (en pares (x1,y1) se considera 1) desea evaluar? (minimo 3)")
n=int(input())
while n<3:
    print ("Ingresa un valor mayor a 2: ")
    n=int(input())
x=np.arange(n, dtype=float)
y=np.arange(n, dtype=float)
acc=np.arange(n, dtype=float) #es un acumulador
sx=0
sy=0
sxy=0
sx2=0
sy2=0
for i in range(n):
    print ("Ingresa el dato x("+str(i+1)+"):")
    x[i]=float(input())
    print ("Ingresa el dato y("+str(i+1)+"):")
    y[i]=float(input())
    sx=sx+x[i] #sx es sumatorai en x
    sy=sy+y[i] #sy sumatoria en y
    sxy=sxy+x[i]*y[i] #sumatoria en x*y
    sx2=sx2+x[i]**2 #sumatoria en x**2
    sy2=sy2+y[i]**2 #sumatoria en y**2
print ("TABLA DE DATOS")
print ("#dato, x , y")
for i in range(n):
    print (str(i+1)+".-",x[i]," ,",y[i])
for i in range(n):
    acc[i]=x[i]
for i in range(0,n): #Este servira para poder encontrar el mas grande y el mas chico valor de x, para graficar
    for j in range(0,n-1):
        if acc[j]>=acc[j+1]: #if evalua que el numero actuar sea menor que el siguiente
            yac=acc[j]  #si es menor cambiara el orden, almacenando el valor actual en y
            acc[j]=acc[j+1] # y el nuevo valor actual seria el del numero siguiente
            acc[j+1]=yac #el numero siguiente sera el anterior, asi que le debolvemos el valor con y
#yp=y promedio, xp=x promedio,r=coeficiente de corelacion
#Σx=sx,Σy=sy,Σxy=sxy,Σx²=sx2
#La pendiente esta dada por m=(Σxy-(Σx)*yp)/(Σx²- (Σx)xp)
yp=sy/n
xp=sx/n
m=(sxy-sx*yp)/(sx2-sx*xp)
r=(n*sxy-sx*sy)/(((n*sx2-sx**2)*(n*sy2-sy**2))**.5)
b=yp-m*xp
print ("Σx=",sx,", Σy=",sy,", Σxy=",sxy,", Σx²=",sx2, ", Σy²=",sy2)
print ("m=",m)
print ("r=",r)
print ("b=",b)
xs=(x[n-1]-x[0])/(n-1)
x1=[acc[0],acc[n-1]]
y1=[m*x1[0]+b,m*x1[1]+b] #como es una ecuacion lineal, no necesita mas puntos, solo 2
plt.plot(x,y,"b*", label="Datos") #los puntos son marcados con estrellas para poder diferenciarlos de la linealizacion
plt.plot(x1,y1,"m-",label="Linializado")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Minimos cuadrados")
