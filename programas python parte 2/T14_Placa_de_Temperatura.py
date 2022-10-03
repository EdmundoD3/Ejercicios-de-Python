#Tarea 14, para lenguajes de programacion
import numpy as np
Placa=np.arange(100,dtype=float).reshape(10,10)
Copp=np.arange(100,dtype=float).reshape(10,10)
ppp=np.array(np.arange(100).reshape(10,10), dtype="S")
for i in range(0,10): #aqui se le da forma a la placa, con los valores especificados mas adelante
    for j in range (0,10):
        if i==0 or i==9 or j==0 or j==9: #los datos de la orilla seran de 20.0
            Placa[i][j]=20.00
        else: #los que no, seran de 50.5
            Placa[i][j]=50.0
        Copp[i][j]=Placa[i][j]
Placa[3][5]=float(100.0) #este nodo sera fijo de 100
print ("Distribucion de temperatura en una placa metalica")
print ("Este programa calcula el estado estacionario en una placa donde en las orillas su temperatura es de 20 grados, todas las demas en 50 grados y el nodo (4,6) esta a 100 grados, los nodos de 20 grados y 100 grados, no varian su temperatura")
print ("Imprime en un archivo llamado (Distribucion de temperatura placa metalica.txt) la placa con la temperatura estacionaria")
print ("Placa original")
print (Placa)
while True: #se repetira hasta que cumpla con todos una diferencia menor a 0.01 con su temperatura anterior
    k=0
    for i in range(1,9):
        for j in range (1,9):
            if Placa[i][j] !=100:
                Placa[i][j]=float(str((Placa[i+1][j]+Placa[i-1][j]+Placa[i][j+1]+Placa[i][j-1])/4)[:5])
                com=float(Copp[i][j]-Placa[i][j])
                Copp[i][j]=Placa[i][j]
                if com <=0.01:
                    k+=1
    if k>=62:
        break
i=j=0
for x in Placa: #se transforma en str, para poderle dar una mejor presentación 
    j=0
    for y in x:
        ppp[i][j]=str(y)[:4]
        j+=1
    i+=1
archivo = open("Distribucion de temperatura placa metalica.txt","w")
archivo.write("Distribucion de temperatura en una placa metalica \n")
print ("Placa con temperatura estacionaria:")
for i in range(0,10):
    archivo.write(str(ppp[i][0:10])+" \n") #aprovechamos para imprimir tanto en pantalla como en archivo
print (ppp)
archivo.close()