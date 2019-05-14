# -*- coding: utf-8 -*-
"""
*************************************Homework 1*********************************************
    Problem 3
    Consider one circle and one rectangle. The circle has a radius r = 12.6 mm. The rectangle
    has sides a and b, but only a is known from the outset (a = 1.5 mm). Write a program
    that uses a while loop to find the largest possible integer b that gives a rectangle area
    smaller than, but as close as possible to, the area of the circle. What is the correct value
    of b?
    
    
Annaconda 2, Python 2.7
"""

#============================================
#               Importing Packages
#============================================

import numpy as np

#============================================
#               Define Varriables
#============================================
r = 12.6 #mm
a = 1.5 #mm

#============================================
#               Calculation
#============================================

b = 1 #starting b at lowest integer
while a*b < r**2*np.pi: #checking condition where area_square < area_circle
    b += 1              #if the while statement is true, the b is increased by one and the next integer is checked in the while loop
print("Largest integer, b, where square area is less than circle area:\n%smm"%(b))

    