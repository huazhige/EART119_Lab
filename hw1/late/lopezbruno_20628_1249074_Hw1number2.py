# -*- coding: utf-8 -*-
#python 2.7, Anaconda 2
"""
Created on Sat Apr 13 15:54:35 2019

@author: bruno

This program takes the radius of a cirlce(12.6mm) and one of the sides of a rectangle (1.5mm)
and finds the largest value of the other side (b) so that the area of the rectangle is just
smaller than the area of the circle, whos radius is known.
"""

import numpy as np

circleRadius = 12.6/1000 #m
a = 1.5/1000 #m
#Computers the area of a circle
circleArea = np.pi * (circleRadius ** 2) #m

#generatres 1000 ewual spaces from 0,10. This is done to find most accurate value of b
c = np.linspace(0,10,1000)

rectangleArea = a * c

#This term is  the index holder and is used to get to the next index of the variable c
i = 0

#goes through 1000 possible values of C and stops when the value of C
# is just big enough to make the expression below false
while rectangleArea[i] < circleArea:
    #Finds the biggest value c and stores it in a variable named b
    b = rectangleArea[i] / a
    #moves onto the next index
    i += 1
    
print "The largest possible value for b is: %d millimeters or %1.2f meters" % ((b*1000), b)




