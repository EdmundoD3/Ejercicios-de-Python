#Tarea 09, para lenguajes de programacion
import numpy as np
print ("***MULTIPLICACIÓN DE MATRICES***")
print("Este programa multiplica 2 matrices")
sn="s" #inicializamos con "s" para que pueda empezar el programa
while sn[0].lower()=="s": #con lower, ya no nos preocupamos que ingresen un valor en mayusculas, y solo ocupamos la primer letra de si
    print("Ingrese el tamaño de la primer matriz")
    n=int(input("Renglones: "))
    while n<=0:
        print ("Ingresa un valor igual o mayor a 1")
        n=int(input("Renglones: "))
    m=int(input("Columnas: "))
    while m<=0:
        print ("Ingresa un valor igual o mayor a 1")
        m=int(input("Columnas: "))
    print("Ingrese el tamaño de la segunda matriz")#La segunda matriz debe coincidir sus renglones con las columnas de la primer matriz
    #asi que solo pedimos las columnas
    print ("La columna de la primer matriz son del mismo tamaño que los renglones de la segunda matriz")
    mm=int(input("Columnas: "))
    while m<=0:
        print ("Ingresa un valor igual o mayor a 1")
        mm=int(input("Columnas: "))
    mxn=np.arange(m*n).reshape(n,m)
    mxn2=np.arange(mm*m).reshape(m,mm)
    print("Ingrese la primer matriz")
    for i in range(n):
         for j in range(m):
                print ("Introduzca el elemento "+str(i+1),str(j+1))
                mxn[i][j]=input()
    print ("Ingrese la segunda matriz")
    for i in range(m):
        for j in range(mm):
            print ("Introduzca el elemento "+str(i+1),str(j+1))
            mxn2[i][j]=input()
    SM=mxn.dot(mxn2) #aquí se multiplican las matrices
    print("La multiplicación de matrices es:")
    print("La primer matriz:")
    print (mxn)
    print("La segunda matriz:")
    print (mxn2)
    print("La matriz resultante: ")
    print (SM)
    print("¿Desea multiplicar otra matriz? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    del mxn #Eliminamos la lista para poder reutilizar la variable de matriz
    del mxn2
    del SM
print("***Fin***")