# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:54:57 2019

@author: lopez
"""
"""
Problem #3 
Fnding the area of a rectangle and circle
We will find the minimum value of b that give us the about the same area for the rectangle and circle 
"""
import numpy as np
r = 12.6 #Radius in mm
Area_Cir = (r**2)*np.pi #Area of Circle

a = 1.5 # in mm
b = 0   # starting value of b 
Area_Rec = a*b 
while a*b < Area_Cir:
    b = b + .1
b = b - .1 # Value found in while loop subtracted by .1 to give area of rec ~ area circ
print('largest b possible', b )

