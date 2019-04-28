#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Assignment 1.1 
by Lili Callahan

"""

#######################################################################
#   Problem 1
#   This problem computes the area of a 
#   rectangle and the area of a triangle
#######################################################################

#######################################################################
#   Parameters for area of the rectangle
#######################################################################

b = 4   # Base
c = 5   # Height

#######################################################################
#   Computations for area of the rectangle
#######################################################################
                 
def area_rec(b, c):
    return b*c

print("The area of my rectangle is: " + str(area_rec(4, 5)) + "mm^2")

#######################################################################
#   Parameters for area of the triangle
#######################################################################

h = 4   # Base
B = 5   # Height

#######################################################################
#   Computations for the area of the triangle
#######################################################################

def area_tri(h, B):
    return 0.5*h*B

print("The area of my triangle is: " + str(area_tri(4, 5)) + "mm^2")