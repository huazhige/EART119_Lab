# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:09:08 2019

@author: eric_
"""
import math
b = 500
r = 12.6 #mm
a = 1.5 #mm
Area_rectangle = a*b
Area_circle = math.pi*r**2
n = .01 #step increment of b

while Area_rectangle > Area_circle:
    b -= n
    Area_rectangle = a*b
    print("rectangle: ", Area_rectangle, "b : ", b)
print("Area of rectangle = ", Area_rectangle )
print("Area of circle = ", Area_circle)
print("b = ", b)

#b approaches 332.5 mm