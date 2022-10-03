#Tarea 05, para lenguajes de programacion
print("Este programa calcula la energia radiada por un cuerpo negro para la temperatura leida en grados fahrenheit utilizando la ley de Stefan-Boltzman; Eb=σT^4 ;σ=0.174X10^-8")
sn="s"
while sn[0]=="s" or sn[0]=="S": #sn[0] se lee el primer caracter para poder limitar las opciones y solo necesitar la s o S de si
    f=float(input("Ingresa la temperatura que desea evaluar en fahrenheit, del cuerpo negro a evaluar: "))
    r=f+460
    Eb=0.1714E-8*r**4 #Esta operasion no da la energia radiada
    print("La energia irradiada es: "+str(Eb))
    print("¿Desea evaluar otra energia? (si/no): ")
    sn= input()
    while sn[0]!="s" and sn[0]!="S" and sn[0]!="N" and sn[0]!="n": #Esta parte evalua si se ingresa un valor no valido
        print("Valor "+str(sn)+" no valido, Ingresa uno valido, ¿Desea evaluar otra energia? (si/no): ")
        sn =input()
print("Fin del programa")