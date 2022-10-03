#Tarea 15, para lenguajes de programacion
print ("Este programa imprime la distancia de diversos puntos (1,1),(1,2)...(1,10),(2,1)...(2,10)...(10,10) desde el origen (0,0) en un archivo llamado Distancia_entre_puntos.txt")
archivo = open("Distancia_entre_puntos.txt","w")
archivo.write("Distancia entre el origen y distintos puntos")
for i in range(1,11): #para facilitar las coordenadas, lo empezamos en 1
    for j in range(1,11):
        r=(i**2+j**2)**.5 #esta es la formula de distancia entre puntos, d=((xi-xf)**2+(yi+yf)**2)**0.5) pero xf y yf, siempre seran 0
        archivo.write("("+str(i)+","+str(j)+")="+str(r)+" \n") #se puede imprimir de una vez
archivo.close()
print ("Se imprimio el archivo") #con este mensaje nos podemos dar cuenta si termino el proceso o no