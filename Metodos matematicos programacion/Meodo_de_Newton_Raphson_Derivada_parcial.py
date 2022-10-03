#Echo por Edmundo David Rdz. Mendoza
import numpy as np
print ("Este programa Utilizando el metodo de Newton-Raphson, calcula la raiz de x²+xy=10 & y+3xy²=57 con x[0]=0.5 & y[0]=6")
x=[0.5,0] #En esta parte inicializo los valores de x0 y x1, en x1 no importa que valor ponga ya que se reescribira
y=[6.0,0] #igualmente lo hago para y0 y y1
while True:
    dux=2*x[0]+y[0]
    duy=x[0]
    dvx=3*y[0]**2
    dvy=1+6*x[0]*y[0]
    u=x[0]**2+x[0]*y[0]-10
    v=y[0]+3*x[0]*y[0]**2-57
    x[1]=x[0]-(u*dvy-v*duy)/(dux*dvy-duy*dvx)
    y[1]=y[0]-(v*dux-u*dvx)/(dux*dvy-duy*dvx)
    #if y[1]==y[0] and y[1]==y[0]
    xo=np.abs((x[1]-x[0])/x[1])
    yo=np.abs((y[1]-y[0])/y[1])
    if yo<=0.00001 and xo<=0.00001: #en ambos casos ocupa cumplir el resultado ya que si solo cumple 1 solo ese tendra el resultado deseado
        print ("Con un error aproximado de: ",yo,"en y & un error aproximado de: ",xo,"en x")
        break
    x[0]=x[1] #aquí almacenamos el valor de x1 en x0 para repetir hasta tener el resultado deseado
    y[0]=y[1]
print ("La raiz de x=",x[1])
print ("La raiz de y=",y[1])