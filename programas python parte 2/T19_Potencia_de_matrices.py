#Tarea 19, para lenguajes de programacion
import numpy as np
print ("***POTENCIA DE MATRICES***")
print ("Este programa potencia matrices a la k potencia")
while True: #se rompera el ciclo con un break
    #Para elevar una matriz a una potencia k, tiene que ser cuadrada
    print("Ingrese el tamaño de la matriz a evaluar (n,n)")
    n=int(input("n: "))
    print("Ingrese a que potencia k desea evaluarlo")
    k=int(input("k: "))
    while n<=0:
        print ("Ingresa un valor igual o mayor a 1")
        n=int(input("n: "))
    mxn=np.arange(n*n, dtype=float).reshape(n,n) #Son tipo flotante para que puedan usar numeros muy grandes
    mxn2=np.arange(n*n, dtype=float).reshape(n,n)
    print("Ingrese la matriz a evaluar")
    for i in range(n):
         for j in range(n):
                print ("Introduzca el elemento "+str(i+1),str(j+1))
                mxn[i][j]=float(input())
                mxn2[i][j]=mxn[i][j]
    if k!=1:
        for i in range(k-1):
            SM=mxn.dot(mxn2) #aquí se multiplican las matrices, las veces que sea necesarias
            mxn2=SM
    else:
        SM=mxn
    print("La matriz original:")
    print (mxn)
    print("La matriz en potencia "+str(k)+" resultante: ")
    print (SM)
    print("¿Desea multiplicar otra matriz? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    if sn[0].lower()!="s":
        break
    del mxn #Eliminamos la lista para poder reutilizar la variable de matriz
    del mxn2
    del SM