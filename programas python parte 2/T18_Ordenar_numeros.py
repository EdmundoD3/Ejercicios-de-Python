#Tarea 18, para lenguajes de programacion
import numpy as np
print ("Este programa ordena numeros enteros de mayor a menor")
while True:
    print ("¿Cuantos numeros desea ordenar?")
    n=int(input())
    print (" ")
    print ("Ingresa los numeros")
    x=np.arange(n)
    for i in range(0,n):
        print ("Ingresa el numero ",i+1)
        x[i]=int(input())
    for i in range(0,n): 
        for j in range(0,n-1):
            if x[j]<=x[j+1]: #if evalua que el numero actuar sea menor que el siguiente
                y=x[j]  #si es menor cambiara el orden, almacenando el valor actual en y
                x[j]=x[j+1] # y el nuevo valor actual seria el del numero siguiente
                x[j+1]=y #el numero siguiente sera el anterior, asi que le debolvemos el valor con y
    print ("Los numeros ordenados son: ")
    for i in range(0,n):
        print (x[i])
    print("¿Desea ordenar otra lista de numeros? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    if sn[0].lower()!="s":
        break
    del x #Eliminamos la lista para poder reutilizar la variable