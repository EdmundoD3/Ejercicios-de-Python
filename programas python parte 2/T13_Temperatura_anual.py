#Tarea 13, para lenguajes de programacion
import numpy as np
print ("Este programa imprime una tabla del promedio anual de temperatura con respecto a longitud y latitud y su promedio total")
print ("Tanto en un archivo llamado Tabla_de_temperatura.txt como en pantalla")
#se almacena los valores de la tabla, en una matriz, para poder evaluarla e imprimirla mas facil
ttemp = np.array([[90.0,90.5,91.0,91.5,92.0,92.5],[68.2,72.1,72.5,74.1,74.4,74.2],[69.4,71.1,71.9,73.1,73.6,73.7],[68.9,70.5,70.9,71.5,72.8,73.0],[68.6,69.9,70.4,70.8,71.5,72.2],[68.1,69.3,68.8,70.2,70.9,71.2],[68.3,68.8,69.6,70.0,70.5,70.9]])
gn=["30.0N","30.5N","31.0N","31.5N","32.0N","32.5N"]
Lat=np.array([0,0,0,0,0,0,0], dtype='f')#con esta variable se guardara y sumara la latitud
Lon=np.array([0,0,0,0,0,0,0], dtype='f')#con esta la longitud
ss=np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00], dtype='f')#con esta guardaremos una version recortada de longitud
sp=np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00], dtype='f')#al igual esta pero con latitud
palabra="Latitud"
for i in range(1,7): #sumamos la temperatura para poder sacar el promedio
    for j in range(0,6):
        Lat[i] += float(ttemp[i][j])
        Lon[i] += float(ttemp[j+1][i-1])
for i in range(1,7): #sacamos el promedio
    Lat[i]=Lat[i]/6.0
    Lon[i]=Lon[i]/6.0
print ("Tabla de Temperatura")
print (8*" "+"Longitud")
i=0
for x in Lon: #este nos sirve para almacenar el valor de la longitud en str de solo 4 digitos, asi dara un mejor formato
    ss[i]= str(x)[:4]
    i+=1
i=0
for x in Lat:
    sp[i]= str(x)[:4]
    i+=1
archivo = open("Tabla_de_temperatura.txt","w") #Se imprime tanto en pantalla como en archivo
archivo.write("Tabla de Temperatura \n")
archivo.write(8*" "+"Longitud \n")
for i in range(0,7):
    if i==0:
        print (palabra[i],5*" ",ttemp[i,:6],"Prom")
        archivo.write(str(palabra[i])+7*" "+str(ttemp[i,:6])+" Prom \n")
    else:
        print (palabra[i],gn[i-1],ttemp[i,:6],sp[i])
        archivo.write(str(palabra[i])+" "+str(gn[i-1])+" "+str(ttemp[i,:6])+" "+str(sp[i])+"\n")
print ("Promed= "+str(ss[1:]))
archivo.write("Promed= "+ str(ss[1:])+"\n")
archivo.close()