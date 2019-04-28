# -*- coding: utf-8 -*-
#Created by: Justin Nguyen
#Recent edit: 4/13/2019
"""
Write a program that computes the area of a rectangle (A=bc) 
    and the area of a triangle (A= 0.5*hb). 
The input of your function will be b and c for the rectangle and hb and b for 
    the triangle
"""
# Interpreter: Python 2.7, Anaconda2
# Import add-ons 
import numpy as np
#==============================================================================
"""                              Problem 1                                  """
#==============================================================================
"""
 Variables in formulas
Ar = Area of Rectangle
br = one side of rectangle (Width)
cr = other side of rectangle (Height)

At = Area of Triangle
h = height of triangle
b = base of triangle
 """
#==============================================================================
# Ask for the parameters of rectangle
br = float(raw_input('Please enter the width of a rectangle: '))
cr = float(raw_input('Please enter the height of a rectangle: '))

# Calculate the Area of the Rectangle
Ar = br * cr
print(" Area of a Rectangle is: %.1f" %Ar)
#==============================================================================
# Ask for the parameters of triangle
h = float(raw_input('Please enter the height of a triangle: '))
b = float(raw_input('Please enter the base of a triangle: '))

#Calculate the Area of the Triangle
At = 0.5 * h * b
print(" Area of a Triangle is: %.1f" %At)
