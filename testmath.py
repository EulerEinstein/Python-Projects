from math import *

x=3
y=0
angle = radians(45)

x_new = x*cos(angle) + y*sin(angle)
y_new = x*sin(angle) - y*cos(angle)

print(x_new,y_new)

