# -*- coding: utf-8 -*-
#anaconda2, Python 2.7
"""
- compute the area of a rectangle (A=bc) and the area of a triangle (A= 0.5*hb). 
variables:
   
    b = breadth of rectangle
    a = length of rectangle
    r = radius of circle
   

"""

import numpy as np
#======================================
#       define variables
#======================================

a = 1.5 
r = 12.6
#starting at b = 0, where area of rectangle = 0
b = 0

#since our upper limit of area of rectangle is the area of the circle, 
#we need to calculate that.

Area_circ = np.pi*r**2
Area_rect = a*b

while Area_rect <= Area_circ:
    b = b+1
    Area_rect = a*b
    
"""

If we print the Area_rect, it will give us the area of the rectangle which exceeds 
the area of the circle (Area_circ), since the value of b used is the one
that stops the while loop. So, what we need is the penultimate value of b;i.e.,b-1.

"""
    
Area_rect_new = a*(b-1)   
print(Area_circ)
print(Area_rect_new)
print(b-1)
    
