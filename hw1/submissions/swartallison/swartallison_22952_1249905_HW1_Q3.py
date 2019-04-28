# Allison Swart
# Astro/Earth 119 Homework 1
# April 13, 2019

#anaconda2/python2.7

import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Problem 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
r = 10.6
circle_area = np.pi*r**2

def rectangle_area(b):
    a = 1.3
    return a*b

while rectangle_area <= circle_area:
    a = 1.3
    b = a + 1
    b+= 1
    
print 'rectangle area =', rectangle_area(b) - 1, 'b =', (b-1)