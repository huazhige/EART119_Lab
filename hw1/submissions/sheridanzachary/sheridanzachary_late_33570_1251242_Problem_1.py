# -*- coding: utf-8 -*-
"""
1. Write a program that computes the area of a rectangle (A=b*c) and the area of a triangle
(A = 0.5*hb*b). The input of your function will be b and c for the rectangle and hb and b
for the triangle.

"""

import numpy as np

A_rect = 0 #Area of Rectangle
A_tri  = 0 #Area of Triangle
b      = float( raw_input( 'What is the length of the rectangle?')) #Side 1 of Rectangle
c      = float( raw_input( 'What is the width of the rectangle?')) #Side 2 of Rectangle
hb     = float( raw_input( 'What is the height of the triangle?')) #Height of Triangle
base   = float( raw_input( 'What is the base length of the triangle?')) #Base length of Triangle

A_rect = b*c
A_tri  = 0.5*hb*base
print 'Rectangle Area:', A_rect, '\nTriangle Area:', A_tri