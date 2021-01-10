import sys 
import numpy as np
import math

print('Sistemas Flexibles de Manufactura','\n','Algebra lineal 2D para robotica')

x= float(input('Ingrese el componente en x del origen='))
y= float(input('Ingrese el componente en y del origen='))
x1=float(input('Ingrese el componente en x del destino='))
y1= float(input('Ingrese el componente en y del destino='))
tita= float(input('Ingrese el angulo= '))

h1=np.array([[math.cos(tita), - (math.sin(tita)), (x1-x)], [math.sin(tita), math.cos(tita), (y1-y)], [0,0,1]])
print(h1)
print('\n Comprobacion  ')
x2= float(input('Ingrese el componente en x del punto= '))
y2= float(input('Ingrese el componente en y del punto= '))
pg2= np.array([[x2],[y2],[1]])
print('Pg= ', pg2)
print('\n')
comprobante1= np.dot(h1, pg2)
print(comprobante1.round())
