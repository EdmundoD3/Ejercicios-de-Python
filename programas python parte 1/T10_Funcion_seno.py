#Tarea 10, para lenguajes de programacion
print ("Este programa utilizando la serie:")
print ("senx=Σ((-1)^n)x^(2n+1)/(2n+1)!")
print ("obtiene la funcion seno(θ) Donde n es el numero de terminos de la serie que toma y evalua n=4,6,9,10 e imprime esos valores")
while True:
    rg=float(input("Ingresa el angulo a evaluar en grados: "))
    rad=rg*3.141592654/180 #x son los radianes, asi que transformamos los grados en radianes
    acum=0 #inicializamos este acumulador, para que funcione como sumatoria
    print ("Seno("+str(rg)+")=")
    for i in range(0,11):
        fact=1
        k=2*i+1
        kk=k
        for j in range(1,k): #aqui se utiliza la funcion factorial
            fact=kk*fact
            kk=kk-1
        if fact==0:#si factorial es igual a 0, se convertira en 1
            fact=1
        s=((-1)**i)*(rad**(k))/fact
        acum=acum+s #aqui sumamos la funcion, para aproximar seno
        if i==4: #aqui se imprime el valor buscado, donde i es n
            print ("En n=4 es: ",acum)
        elif i==6:
            print ("En n=6 es: ",acum)
        elif i==9:
            print ("En n=9 es: ",acum)
        elif i==10:
            print ("En n=10 es: ",acum)
    print("¿Desea obtener otra funcion seno? si/no")
    sn=input()
    while sn[0].lower()!="s" and sn[0].lower()!="n": #comprobamos que ingresaron un valor valido para que continue o termine
        print("El valor "+str(sn)+" No es valido, ingrese si/no: ")
        sn=input()
    if sn[0].lower()=="n": #si es un n, se rompe el ciclo, y termina el programa
        break
print ("***Fin***")