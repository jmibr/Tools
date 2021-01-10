import sys 
import numpy as np
import math

print('Sistemas Flexibles de Manufactura','\n','Algebra lineal 3D para robotica')

x= float(input('Ingrese el componente en x del origen='))
y= float(input('Ingrese el componente en y del origen='))
z= float(input('Ingrese el componente en z del origen='))
x1=float(input('Ingrese el componente en x del destino='))
y1= float(input('Ingrese el componente en y del destino='))
z1= float(input('Ingrese el componente en z del destino='))
tita= int(input('Ingrese el angulo en x= '))
alfa=int(input('Ingrese el angulo en y= '))
ffi= int(input('Ingrese el angulo en z= '))

costita= math.cos(math.radians(tita))
sentita= math.sin(math.radians(tita))
cosalfa= math.cos(math.radians(alfa))
senalfa= math.sin(math.radians(alfa))
cosffi= math.cos(math.radians(ffi))
senffi= math.sin(math.radians(ffi))

h1=np.array([[(cosalfa*cosffi), (cosffi*sentita*senalfa - costita*senffi), (costita*cosffi*senalfa + sentita*senffi), (x1-x)],[(cosalfa*senffi), ((costita*senffi) + (sentita*senalfa*senffi)), (-cosffi*sentita + costita*senalfa*senffi), (y1-y)], [-senalfa, (cosalfa*sentita), (costita*cosalfa),(z1-z)], [0,0,0,1]])
print(h1.round())
