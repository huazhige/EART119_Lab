#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:13:22 2019

@author: andrewquartuccio
"""
import math
import  numpy as np


#=================================================================
#                    Parameters
#=================================================================

max_b = 350
prec  = 1000
r = 12.6                    # Radius (mm)
a =  1.5                    # Known Leg of rect (mm)
b = np.linspace(0.0, max_b, prec)    # Unknown leg of rect (mm)

#=================================================================
#                    Calculations
#=================================================================

area_c = math.pi*(r**2)   # Area of circle
area_r = a*b[0]           # Area of rectangle

i = 0
while area_c > area_r:
    area_r = a*b[i]
    i += 1

print('The correct value of side b is: %.3f') % (b[i-2])