#Tarea 04, para lenguajes de programacion
print("Este programa con los coeficientes de La formula general, determina si la ecuación cuadratica tiene dos raices reales y diferentes, sus dos raices son iguales o si son imaginarias")
print("La formula general es: x=(-b±√(b²-4ac))/(2a) , y la ecuacion cuadratica es: ax²+bx+c")
a=float(input("Ingrese (a): "))
while a == 0:
    a=input("El termino cuadratico no puede ser 0, Ingrese (a): ")
b=float(input("Ingrese (b): "))
c=float(input("Ingrese (c): "))
d=b**2-4*a*c #con la discriminante podemos encontrar la naturaleza de sus raices
if d == 0: #si la discriminante es 0 nos daran raices iguales, por lo tanto solo ocupamos imprimir una raiz
    print("Las dos raices son reales e iguales")
    x=-b/2*a
    print("r="+str(x))
elif d < 0: #si la discriminante es menor a 0,las raices seran complejas
        print("Las dos raices son complejas")
        x1=-b/2*a
        x2=((-d)**0.5)/2*a #al ser la discriminante negativa, la multiplicamos por -1 para poder obtener la raiz
        print("r1= "+str(x1)+"+"+str(x2)+"i")
        print("r2= "+str(x1)+"-"+str(x2)+"i")
elif d > 0: #la raiz es positiva, por lo tanto la raiz se podra efectuar sin problemas y nos dara un resultado de raiz real y diferente
        print("Las dos raices son reales y diferentes")
        x1=(-b+d**0.5)/2*a
        x2=(-b-d**0.5)/2*a
        print("r1= "+str(x1))
        print("r2= "+str(x2))