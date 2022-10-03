#Tarea 17, para lenguajes de programacion
print ("Este programa calcula la hipotenusa usando los catetos")
while True:
    print ("Introduce el cateto A")
    x=float(input())
    print ("Introduce el cateto B")
    y=float(input())
    z=(x**2+y**2)**.5 #c²=(a²+b²)**0.5
    print ("La hipotenusa es:",z)
    print ("¿Desea obtener otra hipotenusa usando dos catetos(si/no)?")
    sn=input() #con esto se sabra si se repite o no
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    if sn[0].lower()!="s":
        break #se sale del while