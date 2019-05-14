#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Assignment 1.3 
by Lili Callahan

"""

#######################################################################
#   Problem 3
#   This problem computes the largest value that the base, b, of
#   a rectangle with a fixed side, a = 1.5 mm, can have to make its area
#   as close as possible to (but not greater than) the fixed
#   area of a circle with radius r = 12.6 mm
#######################################################################

import math

#######################################################################
#   Parameters
#######################################################################

a = 1.5     # Side    
r = 12.6    # Radius     

def area_rect(b, a):            # Area of rectangle
    return a*b
b=0
area_cir = math.pi*12.6**2      # Area of circle (pi*r**2)

#######################################################################
#   Computations
#######################################################################

while area_rect(b, 1.5) <= area_cir:
    b += 1
    
print("b = " + str(b-1) + "mm")