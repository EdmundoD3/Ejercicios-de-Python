#Tarea 16, para lenguajes de programacion
import matplotlib.pyplot as plt
import numpy as np
print ("Este programa calcula el senh(x), cosh(x) y tanh(x) (funciones hiperbolicas)")
while True:
    print ("Ingrese el valor que desea evaluar (x) de una funcion hiperbolica: ")
    x=float(input())
    senh=(np.exp(x)-np.exp(-x))/2
    cosh=(np.exp(x)+np.exp(-x))/2
    tanh=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    print ("Senh("+str(x)+")=",senh)
    print ("cosh("+str(x)+")=",cosh)
    print ("tanh("+str(x)+")=",tanh)
    print("¿Desea evaluar otra función hiperbolica? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    if sn[0].lower()!="s":
        break