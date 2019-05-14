# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:56:03 2019

@author: Emily White
"""
"""
Homework 1 Problem 3
Consider one circle and one rectangle. Circle with radius r = 12.6mm

Rectangle with sides a and b, but only a is known from the outset (a=1.5mm)

Write a program which uses a while loop to find the largest possible integer
b which gives a rectangle area smaller than, but close to, the area of circle

What is the correct value of b?

"""
"""
    r = radius of the circle
    a = outset/height from rectangle
    b = unknown length for rectangle
    circle_a = area of the circle
    
"""
#import modules
import math

#define the variables
r = 12.6
a = 1.5

# the area of the circle
circle_a = math.pi*r**2

# using a while loop to find largest integer b can be
b = 0
while a*b < circle_a:
    b += 1
b -= 1  #required to recieve correct value of b

# computations
print "Correct value of b: ", b


















