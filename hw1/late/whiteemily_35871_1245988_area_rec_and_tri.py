# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:48:52 2019

@author: Emily White
"""

"""
Homework 1 Problem 1
Write a program which computes the area of a rectangle (A=bc) and the
area of a triangle (A=0.5*hb).

The input of the fnc will be b and c for rectangle
And h and b for the triangle

"""

#=================================================================
#       Area of a Rectangle
#=================================================================

"""

    A1 = Area of rectangle
    b1 = height of rectangle
    c = width of rectangle
    
    Area = height * width
    
"""

# define the variables
b1 = input("height of rectangle ")
c = input("width of rectangle ")

# eq'n

A1 = b1 * c

# computations
print "area of rectangle :", A1

#============================================================
#       Area of a Triangle
#==========================================================

"""

    A2 = Area of triangle
    h = height of triangle
    b2 = base of triangle
    
    Area = 0.5 * height * base
    
"""

# define variables
h = input("height of triangle ")
b2 = input("base of triangle ")

# eq'n
A2 = 0.5 * h * b2

#computations
print "area of triangle :", A2
