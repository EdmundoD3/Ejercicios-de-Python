#Tarea 11, para lenguajes de programacion
print ("Tabla de grados radianes")
print ("Este programa imprime una tabla de grados y radianes con saltos de 3 grados y guarda una en un archivo")
print ("|  θ  | rad")
for i in range(0,10,3): #aprovecho el valor de i, tanto para imprimir en un archivo, como en pantalla
    rad=i*3.141592654/180
    print ("|  "+str(i)+"° |",str(rad)[:7])
for i in range(12,91,3): #para tener un mejor formato, los separo para que la impresion tanto en pantalla como en archivo, se vea bien
    rad=i*3.141592654/180
    print ("| "+str(i)+"° |",str(rad)[:7])
