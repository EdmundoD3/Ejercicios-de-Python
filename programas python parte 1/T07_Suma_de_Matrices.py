#Tarea 07, para lenguajes de programacion
import numpy as np
print("Este programa suma 2 matrices")
sn="s" #inicializamos con "s" para que pueda empezar el programa
while sn[0].lower()=="s": #con lower, ya no nos preocupamos que ingresen un valor en mayusculas, y solo ocupamos la primer letra de si
    print("Ingrese el tamaño de la matriz")
    n=int(input("Renglones: "))
    while n<=0:
        print ("Ingresa un valor igual o mayor a 1")
        n=int(input("Renglones: "))
    m=int(input("Columnas: "))
    while m<=0:
        print ("Ingresa un valor igual o mayor a 1")
        m=int(input("Columnas: "))
    mxn=np.arange(m*n).reshape(n,m) #aqui asignamos el tamaño de la variable
    print("Ingrese la primer matriz")
    for i in range(n):
         for j in range(m):
                print ("Introduzca el elemento "+str(i+1),str(j+1))
                mxn[i][j]=input()
    mxn2=np.arange(m*n).reshape(n,m)
    print ("Ingrese la segunda matriz")
    for i in range(n):
        for j in range(m):
            print ("Introduzca el elemento "+str(i+1),str(j+1))
            mxn2[i][j]=input()
    SM=mxn+mxn2 #aquí se suman las matrices
    print("La suma de matrices es:")
    print("La primer matriz:")
    print (mxn)
    print("La segunda matriz:")
    print (mxn2)
    print("La matriz resultante: ")
    print (SM)
    print("¿Desea sumar otra matriz? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    del mxn #Eliminamos la lista para poder reutilizar la variable de matriz
    del mxn2
    del SM
print("***Fin***")