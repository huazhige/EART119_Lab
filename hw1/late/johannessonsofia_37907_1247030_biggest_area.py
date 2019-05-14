# -*- coding: utf-8 -*-

"""
-A circle has radius r and a rectangle has one side of length a and
 is fixed and its other side is of length b but this value is
 variable, this program calculates the largest integer value b where
 the rectangles area is still equal or less than the area of 
 the circle
 
"""

import numpy as np

r = 12.6
a = 1.5
b = 0

A_circ = np.pi*r**2

while A_circ>a*b:
    b+=1
    
print('largest integer value of b.',b-1)
print('area of circle', A_circ)
print('area of rectangle',(b-1)*a)