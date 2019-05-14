# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:37:15 2019

Problem 3

@author: Nessa
"""
# /////////////////////////////////////////////////////////////////////////////
#                       Variables
#//////////////////////////////////////////////////////////////////////////////
import math as m

eps = 0.1
r = 12.6
a = 1.5
b = eps


#////////////////////////////////////////////////////////////////////////////
#computations
#//////////////////////////////////////////////////////////////////////////

def area_circle(r):
    return float(m.pi*r**2)

circleArea = area_circle(r)
rectangleArea = 0
while (1):
    rectangleArea = a * b
    if (circleArea - rectangleArea) < eps:
        break
    if (rectangleArea - circleArea) >= 0:
        b -= eps
        break
    b += eps

print ('b= ', b)




