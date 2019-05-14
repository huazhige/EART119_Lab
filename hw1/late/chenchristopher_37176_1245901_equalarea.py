# -*- coding: utf-8 -*-
#python 2.7
"""
Given a circle of radius r, the program returns a side length of integer b given a side length a that 
will form a rectangle that has area as close as possible to the circle's. Note b is an underestimate.
"""

import numpy as np

#=====================================================================================================
#Input variables
#=====================================================================================================
r = 12.6 #radius of circle
a = 1.5 #known side length of rectangle

#=====================================================================================================
#Computation
#=====================================================================================================
def find_b(r, a):
    i = 1
    while a * i < np.pi * r**2:
        i += 1
    return i - 1

print(str(find_b(r, a)))

#=====================================================================================================
#Find the actual b
#Found using the equation a * b = pi * r^2 so b = (pi * r^2) / a
#=====================================================================================================
print("The true b is " + str((np.pi * r**2) / a))