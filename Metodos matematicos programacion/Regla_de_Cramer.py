import numpy as np
print ("Regla de Cramer")
print ("Este programa usando la regla de cramer, permite resolver sistemas de ecuaciones lineales.\nMinimo 2 ecuaciones de 2 incógnitas y maximo 4 ecuaciones de 4 incognitas\nDe la forma ax1+bx2+cx3=k ; De tal modo que si tenemos 2 ecuaciones de la forma ax+by+cz=d, x sera x1, y=x2 & z=x3\ny a sera la constante del termino 1, b del 2, c del 3 y así sucesivamente; al final pidiendo k\n¿Cuantas incógnitas  tienen las ecauciones a evaluar? ejemplo: x1+x2=k ; son de 2 incognitas, no se incluye k\nTome en cuenta que el numero de incognitas, determina cuantas ecuaciones son\n")
n=int(input("Ingresa el numero de terminos: "))
while n<2 or n>=5:
    if n>=5: #si es 5 o mayor el sistema sera grande, asi que se le da una alvertencia
        print ("El numero de incognitas es mayor a 4")
    else:
        print ("El numero de incognitas es menor a 2")
    print ("Ingrese uno de 2 a 4 incognitas, Ingresa el numero de incógnitas: ")
    n=int(input())
print ("La cantidad de ecuaciones, son: ",n)
Me=np.random.random((n,(n+1))) #Lo rellena con decimales para que se calcule con mas precisión 
Dt=np.random.random((n,n)) #la funcion det ocupa que sea una matriz cuadrada, asi que asigno solo los valores que ocupamos para la determinante
gDt=np.random.random((n,n))
xn=np.random.random(n)
for i in range(n):
    print ("De la ecuacion",(i+1))
    for j in range(n+1):
        if j!=n: #con esto se le da mas la presentacion de la lectura ya que el xn+1 es el igual y si lo pedimos como xn+1 se podria mal interpretar
            print ("Ingrese el coeficiente de x"+str(j+1))
        else:
            print ("Ingrese k =")
        Me[i][j]=float(input())
xpr=np.random.random((n)) #esta matriz solo es para poder darle una presentacion 
xpr=xpr.astype(str) #aqui se transforma en str
for i in range(n):
    xpr[i]="x"+str(i+1)
for i in range(n):
    xpr[i]=""
    for j in range(n+1):
        if j!=n:
            if Me[i][j]>0: #si el termino es positivo, lo imprime con el signo +, si no, ya incluye - 
                if j==0: #si es el primer termino, no es necesario que imprima el signo de + al principio
                    xpr[i]=xpr[i]+str(Me[i][j])+"x"+str(j+1)
                else:
                    xpr[i]=xpr[i]+" + "+str(Me[i][j])+"x"+str(j+1)
            else:
                xpr[i]=xpr[i]+str(Me[i][j])+"x"+str(j+1)
        else: #despues del igual, no importa si no tiene el signo + ó -
            xpr[i]=xpr[i]+" = "+str(Me[i][j])

i=0 
for x in Me: #aqui almacenamos los valores para la determinate
    j=0
    for y in x:
        if j!=n: #con este nos saltamos el valor que no deseamos que es despues del igual
            Dt[i][j]=Me[i][j]
            gDt[i][j]=Me[i][j] #guardamos la matriz para recuperar la determinante
        j=j+1
    i+=1
dd=np.linalg.det(Dt) #guardamos el valor de la determinante para la regla de cramer
if dd!=0: #si la determinante es diferente de 0 se puede resolver
    for j in range(n):
        for i in range(n):
            Dt[i][j]=Me[i][n]
        xn[j]=np.linalg.det(Dt) #Se calcula la nueva determinante
        Dt=gDt.copy() #aqui copio la matriz que habiamos guardado previamente
    for i in range(n):
        print ("De la ecuacion "+str(i+1)+":",xpr[i])
    for i in range(n):
        xn[i]=xn[i]/dd
        print ("x"+str(i+1)+"=",xn[i])
else: #si no, solo mandamos un mensaje de que no se puede resolver con la regla de cramer
    print ("Este sistema de ecuaciones no se puede resolver con la Regla de cramer")
