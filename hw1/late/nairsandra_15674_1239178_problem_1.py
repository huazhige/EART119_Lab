# -*- coding: utf-8 -*-
#anaconda2, Python 2.7
"""
- compute the area of a rectangle (A=bc) and the area of a triangle (A= 0.5*hb). 
variables:
   
    b = breadth of rectangle = base of triangle
    c= length of rectangle
    h_b = height of triangle
   

"""

#import numpy
#======================================
#       define variables
#======================================

b = 30
c = 20
h_b = 50

#======================================
#     compute areas
#======================================

A_t = 0.5*h_b*b
"""
    :input
    variables:
       h_b = height of triangle
       b = base of triangle   
    :output
        Area of triangle)
"""

print(A_t)

A_r = b*c
"""
    :input
    variables:
        b = breadth of rectangle
        c= length of rectangle    
    :output
        Area of rectangle)
"""
print(A_r)