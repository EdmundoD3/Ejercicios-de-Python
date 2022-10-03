import numpy as np
print ("Este programa Utilizando el metodo de Newton-Raphson, calcula la raiz de x²-y=2 & y²-x=3 con x(0)=1.5 y y(0)=2.5")
x=[1.5,0] #En esta parte inicializo los valores de x0 y x1, en x1 no importa que valor ponga ya que se reescribira
y=[2.5,0] #igualmente lo hago para y0 y y1
while True: 
    dux=2*x[0] #realizamos cada una de las operaciones a parte para que evitar confuciones
    duy=-1/2*x[0]
    dvx=-1/2*y[0]
    dvy=2*y[0]
    u=x[0]**2-y[0]-2
    v=y[0]**2-x[0]-3
    x[1]=x[0]-(u*dvy-v*duy)/(dux*dvy-duy*dvx)
    y[1]=y[0]-(v*dux-u*dvx)/(dux*dvy-duy*dvx)
    #if y[1]==y[0] and y[1]==y[0]
    xo=np.abs((x[1]-x[0])/x[1])
    yo=np.abs((y[1]-y[0])/y[1])
    if yo<=0.000001 and xo<=0.000001:  #en ambos casos ocupa cumplir el resultado ya que si solo cumple 1 solo ese tendra el resultado deseado
        print ("Con un error aproximado de: ",yo,"en y & un error aproximado de: ",xo,"en x")
        break
    x[0]=x[1] #aquí almacenamos el valor de x1 en x0 para repetir hasta tener el resultado deseado
    y[0]=y[1]
print ("La raíz de x=",x[1])
print ("La raíz de y=",y[1])