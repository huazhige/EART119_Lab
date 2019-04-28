#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IDE: Spyder
Andreas Kooi
April 14, 2019

HW1.3
Consider one circle and one rectangle. The circle has a radius r = 12.6 mm. The rectangle
has sides a and b, but only a is known from the outset (a = 1.5 mm). Write a program
that uses a while loop to find the largest possible integer b that gives a rectangle area
smaller than, but as close as possible to, the area of the circle. What is the correct value
of b?
"""

#=============================
#       import nessecary modules
#============================

import numpy as np




#=============================
#       parameters and constants
#============================

radius = 12.6
a = 1.5 
b = 0


#=============================
#       computations and display
#============================

circle_area = np.pi * 2 * radius

while (a*b) <= circle_area:
    area = a*b    
    b += 1
    
b -= 1

print('The largest value b can be is ', b)