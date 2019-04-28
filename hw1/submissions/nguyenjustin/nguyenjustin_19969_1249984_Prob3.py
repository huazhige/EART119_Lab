# -*- coding: utf-8 -*-
#Created by: Justin Nguyen
#Recent edit: 4/13/2019
"""
Write a program that uses a while loop to find the largest possible integer b 
that gives a rectangle area smaller than, but as close as possible to, 
the area of the circle. What is the correct value of b?

    Variables:
        Radius of circle = r = 12.6 mm 
        Rectangle sides a = 1.5 mm , b = ?
"""
# Interpreter: Python 2.7, Anaconda2
# Import add-ons 
import numpy as np
import math
#==============================================================================
"""                              Problem 3                                  """
#==============================================================================
#Establish what the area of the circle is
r = 12.6 #mm
ac = (math.pi)*r**2
print "Area of the circle: ",ac, "mm"

#Set up the while loop to find b
a = 1.5 #mm
b = 0
while a * b < math.pi * r ** 2:
    b += 1

print "The largest possible integer for b is ", b - 1, "mm."
