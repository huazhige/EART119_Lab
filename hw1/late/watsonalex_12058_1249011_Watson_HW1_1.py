# -*- coding: utf-8 -*-
"""
                            Homework 1: Problem 1
                                Alex Watson
    -Find the area of a rectangle and the area of a triangle
"""
import numpy as np

#==============================================================================
#                               Variables
#==============================================================================

b   = float( raw_input( 'Base: '))
c   = float( raw_input( 'Height of rectangle: '))
h_b = float( raw_input( 'Height of triangle: '))

#==============================================================================
#                               Area calculations
#==============================================================================

A_rec = b*c

A_tri = 0.5*b*h_b

# Print solutions

print( 'Rectangle Area: ', A_rec)
print( 'Triangle Area: ', A_tri)