#Tarea 03, para lenguajes de programacion
print("Serie de fibonacci")
print("Este programa imprime la serie de fibonacci, primero los primeros 10 numeros, despues imprime la serie hasta lo que indique")
j=1
k=0
for i in range (10):
    print(k)
    l=j
    j=k+j
    k=l
print("Esta parte imprime, la serie de fibonacci, hasta el numero que usted desee")
x=int(input("Ingrese hasta que numero desea la serie de fibonacci: "))
j=1
k=0
while k<=x:
    print(k)
    l=j
    j=k+j
    k=l