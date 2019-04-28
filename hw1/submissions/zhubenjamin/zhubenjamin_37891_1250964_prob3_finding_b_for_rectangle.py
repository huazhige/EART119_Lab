# -*- coding: utf-8 -*-
"""
Created on Apr 11, 2019
Class = Astro/Eart 119
Homework 1 - functions and vectors
Student = Benjamin Zhu (1696575)

"""
#==================================================
#           imports
#==================================================

import numpy as np
from math import pi

#==================================================
#           Problem 3
#==================================================

a   = 1.5                   #width of the rectangle
b   = np.arange(0, 1000, 1) #an array of possible length of the rectangle
R   = a*b                   #area of the rectangle

r   = 12.6                  #radius of the circle
C   = pi*r**2               #area of the circle

i = 0                       #starting the index count from the first element
while R[i] <= C:            #the while loop keeps running until the 
    i += 1                  #   area of the rectangle surpass the circle
                 
    
print b[i-1]                #print out result, i-1 so we get the result 
                            #   that's slightly less than the circle

