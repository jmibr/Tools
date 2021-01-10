#las librerias que se utilizaran 
import numpy as np 
import math as m  #las operaciones matematicas se pueden realizar con numpy pero prefiero hacerlas con math

#Hardwiring las variables
l1=0.105 #longitud del link 1
l2=0.135 #longitud del link 2
theta0=90 #angulo del link 0
theta1=90 #angulo del link 1
theta2=-90 #angulo del link 2
#los siguientes angulos son los angulos default del robot
thetai0=0 #angulo inicial o default del link 0
thetai1=90 #angulo inicial o default del link 1
thetai2=-90 #angulo inicial o default del link 2


#debido a que m.cos funciona con los valores en radianes hay que convertir los grados a radianes y aprovecho para darle un nombre a estas variables
#utilize c para coseno y s para seno para que coincidieran con las variables de la matriz
c0=m.cos(m.radians(theta0))
c1=m.cos(m.radians(theta1))
c2=m.cos(m.radians(theta2))
s0=m.sin(m.radians(theta0))
s1=m.sin(m.radians(theta1))
s2=m.sin(m.radians(theta2))

#guiandome de la ecuacion de la cinematica directa cargo en la matriz las operaciones
a1=np.array([[(c0*(c1*c2 - s1*s2)), -c0*(c1*s2 + s1*c2), s0, c0*(l2*c1*c2 - l2*s1*s2 + l1*c1)],
[s0*(c1*c2 -s1*s2), -s0*(c1*s2 + s1*c2), -c0, s0*(l2*c1*c2 - l2*s1*s2 +l1*c1)],
[s1*c2 + c1*s2, -s1*s2+c1*c2, 0, l2*s1*c2 +l2*c1*s2 +l1*s1], [0,0,0,1]])

#aqui utilice el redondeo de numpy y lo ajuste a 3 decimales
print('Matriz Resultante', '\n',np.round(a1,3)) #de por si los numeros solo daban 3 decimales pero las respuestas salian en notacion cientifica

#a1x, a1y y a1z presentan las coordenadas xyz de la posicion del end effector
a1x=c0*(l2*c1*c2 - l2*s1*s2 + l1*c1)
a1y=s0*(l2*c1*c2 - l2*s1*s2 +l1*c1)
a1z=l2*s1*c2 +l2*c1*s2 +l1*s1
xyz=[a1x, a1y,  a1z] #cargue estos valores en una lista
print('Posicion TCP en XYZ', '\n',np.round(xyz,3)) #nuevamente redondee para que no se imprimieran en notacion cientifica

#Esta seccion es para calcular la cantidad de angulos que se movio el robot en zyx con respecto a las coordenadas default
zout= theta2 - thetai2
yout=theta1 - thetai1
xout=theta0 - thetai0
zyx=[zout,yout,xout]
print('Rotacion en ZYX', '\n', zyx )

