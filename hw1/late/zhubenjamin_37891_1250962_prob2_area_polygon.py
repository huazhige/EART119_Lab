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

#==================================================
#           Problem 2
#==================================================

""" for loop method """

x    = (1, 3, 4, 3.5, 2)   #input x and y coordinate as arrays
y    = (1, 1, 2, 5, 4)
Sum1 = 0                    #Sum1 and sum2 starts at 0 and accumulate as
Sum2 = 0                    #    the for loop runs

for i in np.arange(1, 5):           #setting for loop range from second to last element
    Sum1 += x[i-1]*y[i]             #part of the addition x1*y2+....xn-1*yn
    Sumleft = Sum1 + x[4]*y[0]      #taking into account the last part of the addition xn*y1
   
    Sum2 += y[i-1]*x[i]             #repeat above but swapping x and y
    Sumright = Sum2 + y[4]*x[0]
    
B = abs(Sumleft - Sumright)         #absolute vaule of the difference
A = 0.5*B                           #final step of divid by half

print A         #print result




