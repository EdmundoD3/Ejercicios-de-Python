#Tarea 06, para lenguajes de programacion
print("Este programa usando la ley de planck imprime la potencia emitida por un cuerpo negro macromatico, de las longitudes desde 0.2 micrometros, hasta 6.1 micrometros variando de 0.1 micrometros")
w=0.2
from math import exp
while w<=6.1:
    m=exp((2.5896E4)/(w*3460))
    E=(1.187E8)/((w**5)*(m-1.0))
    print("Longitud de onda "+str(w))
    print("Potencia "+str(E))
    w+=0.1
print("***Fin***")