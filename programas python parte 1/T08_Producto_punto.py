#Tarea 08, para lenguajes de programacion
import numpy as np
print("Este programa hace el producto punto de 2 vectores en R3, calcula e imprime")
a=np.arange(3)
b=np.arange(3)
ab=np.arange(3)
V=["i","j","k"]
sn="s"
while sn[0].lower()=="s": #Aquí evaluamos si se repetira o no el programa, con lower solo tendremos que evaluar un s en minusculas
    print("Ingrese el primer vector <ai,aj,ak>")
    for i in range(0,3):
        print ("Ingrese la componente a"+V[i])
        a[i]=input()    
    print("Ingrese el segundo vector <bi,bj,bk>")
    for i in range(0,3):
        print ("Ingrese la componente b"+V[i])
        b[i]=input()
        ab[i]=a[i]*b[i]
    print ("Los vectores ")
    print ("a=<"+str(a)+">")
    print ("b=<"+str(b)+">")
    print ("Su producto punto a·b es: "+str(ab))
    print ("¿Desea evaluar otro producto punto? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
print ("*** Fin ***")