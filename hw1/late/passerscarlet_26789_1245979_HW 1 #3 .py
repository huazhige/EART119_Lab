#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#anaconda2/python2.7
#HW 1 #3
"""
HW 1 problem 3
This script does the following:
    
    Given a circle with a radius r = 12.6mm, and a rectangle with sides 'a' and 'b'
    with only 'a' known from the outset (a = 1.5mm). This program uses a while loop
    to find the largest possible integer 'b' that gives the rectangle an area smaller
    than, but as close as possible to, the area of the circle.

@author: scarletpasser

"""


from math import pi

#############################################################################
#                           parameters/variables
#############################################################################                            

r           = 10.6     #radius of circle (mm)
area_circle = pi*r**2  #area of circle (mm**2)
b           = 0        #height of rectangle (mm)

##############################################################################
#                           define functions
##############################################################################


def area_rectangle(b):  #area of rectangle as function of b
    a = 1.3             #base of rectangle (mm)
    return b*a 

##############################################################################
#                           computations/output
##############################################################################
           
#find what b value gives the closest possible area to the circle area
while area_rectangle(b) <= area_circle: 
    b += 1
    
print "area =", area_rectangle(b) - 1, "b =",(b - 1)
