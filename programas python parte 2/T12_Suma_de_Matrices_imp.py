#Tarea 12, para lenguajes de programacion
import numpy as np
print("Este programa suma 2 matrices muestra en pantalla e imprime dichas matrices")
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
                print ("Introduzca el elemento "+str(i+1),",",str(j+1))
                mxn[i][j]=input()
    mxn2=np.arange(m*n).reshape(n,m)
    print ("Ingrese la segunda matriz")
    for i in range(n):
        for j in range(m):
            print ("Introduzca el elemento "+str(i+1),",",str(j+1))
            mxn2[i][j]=input()
    SM=mxn+mxn2 #aquí se suman las matrices
    print ("Ingrese un nombre para la matriz a imprimir")
    nom=str(input())
    archivo = open(nom+".txt","w")
    print("La suma de matrices es:")
    print("La primer matriz:")
    archivo.write("La primer matriz: \n")
    print (mxn)
    archivo.write(str(mxn)+"\n")
    print("La segunda matriz:")
    archivo.write("La segunda matriz: \n")
    print (mxn2)
    archivo.write(str(mxn2)+"\n")
    print("La matriz resultante: ")
    archivo.write("La matriz resultante: \n")
    archivo.write(str(SM)+"\n")
    print (SM)
    archivo.close()
    print ("El archivo se guardo en ("+nom+".txt)")
    print("¿Desea sumar otra matriz? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    del mxn #Eliminamos la lista para poder reutilizar la variable de matriz
    del mxn2
    del SM