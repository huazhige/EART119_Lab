# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:01:26 2019

Area of a Rectangle and a Circle
"""
from math import pi
import numpy as np

#==========================================================
#                      parameters
#========================================================== 

r = 12.6 #radius of circle (mm)
a = 1.5  #length of one side of rectangle


#==========================================================
#                      Compute
#==========================================================

C = pi*r**2 # area of a circle
R = a*b     # area of a rectangle

#find largest possible length of b that gives rectangle area smaller than the circle
i = 1
while C > R[i]:
    largest_area = R[i]
    i += 1
   
print 'the largest possible value of b is' ,b[i]
print 'the largest possible area of the rectangle is' ,R[i]