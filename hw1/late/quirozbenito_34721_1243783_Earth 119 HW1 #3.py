# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:32:59 2019
Earth 119 HW1 Problem #3
@author: Benny Quiroz
"""

"""
3. We are given a circle and a rectangle with one known side length. This script
will find the longest integer length of the unknown side such that the area of the rectangle
is smaller that that of the circle. 
"""
import numpy

r = 12.6
#radius of circle
aside = 1.5
#side length of a
bside = 0
#our variable for the side length of b
c_area = numpy.pi*r**2
# the area of the circle

while c_area >= aside*bside:
    bside += 1
#When the critical value is reached, the loop's condition will still be true. 
#Therefore it will still increment bside.
#We must subtract one to get the correct answer. 
print bside - 1

