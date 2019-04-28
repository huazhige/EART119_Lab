#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Assignment 1.2 
by Lili Callahan

"""
#######################################################################
#   Problem 2
#   This problem computes the area of an irregular polygon 
#   a) in a for loop and b) using vector notation
#######################################################################

import numpy as np
from numpy import zeros

"""
Test cases

"""
#######################################################################
#   Parameters of rectangle
#######################################################################

x = zeros(5)    # x values
x[0] = 0
x[1] = 2
x[2] = 2
x[3] = 0
x[4] = 0

y = zeros(5)    # y values
y[0] = 0
y[1] = 0
y[2] = 3
y[3] = 3
y[4] = 0

#######################################################################
#   Computations (for loop) of rectangle
#######################################################################

area_rectangle = 0
for i in range(0, 4):
    area_rectangle += (0.5)*((x[i]*y[i+1])-(y[i]*x[i+1]))
    
print("The area of my rectangle using a for loop is: " + str(area_rectangle))

#######################################################################
#   Parameters of triangle
#######################################################################

x = zeros(4)    # x values
x[0] = 3
x[1] = 2
x[2] = 0
x[3] = 3

y = zeros(4)    # y values
y[0] = 1
y[1] = 3
y[2] = 1
y[3] = 1

#######################################################################
#   Computations (for loop) of triangle
#######################################################################

area_triangle = 0
for i in range(0, 3):
    area_triangle += (0.5)*((x[i]*y[i+1])-(y[i]*x[i+1]))
    
print("The area of my triangle using a for loop is: " + str(area_triangle))

"""
Beginning of actual problem since the test cases worked

"""

#######################################################################
#   Parameters of polygon
#######################################################################

x = zeros(6)    # x values
x[0] = 1
x[1] = 3
x[2] = 4
x[3] = 3.5
x[4] = 2
x[5] = 1

y = zeros(6)    # y values
y[0] = 1
y[1] = 1
y[2] = 2
y[3] = 5
y[4] = 4
y[5] = 1

#   a)

#######################################################################
#   Computations (for loop) of polygon
#######################################################################

area_polygon = 0
for i in range(0, 5):
    area_polygon += (0.5)*((x[i]*y[i+1])-(y[i]*x[i+1]))
    
print("The area of my polygon using a for loop is: " + str(area_polygon))

#   b)

#######################################################################
#   Computations (vector notation) of polygon
#######################################################################

area_polygon_vec = (0.5)*((np.dot(y[1:], x[:5]))-(np.dot(x[1:], y[:5])))

print("The area of my polygon using vector notation is: " + str(area_polygon_vec))