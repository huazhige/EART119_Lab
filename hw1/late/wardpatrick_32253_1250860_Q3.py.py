# -*- coding: utf-8 -*-

"""

Q3

A circle has a radius r = 12.6 mm. The rectangle
has sides a and b, but only a is known from the outset (a = 1.5 mm).
Write a program that uses a while loop to find the largest possible integer b 
that gives a rectangle area smaller than, but as close as possible to, 
the area of the circle. What is the correct value of b?

"""
import math

r = 12.6
a = 1.5
b = 1
dn= 1

areaC = math.pi*r**2
areaR = a*b

while areaR+1 < areaC:
    b += dn
    areaR = a*b
    
print ('Area of circle:   ', areaC)
print ('Area of rectangle:',areaR)
print ('Difference:       ',areaC - areaR)
print ('b value:          ', b)