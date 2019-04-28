#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

 Use a while loop to find largest possible integer b that gives a rectangle area
smaller than, but as close as possible to, the area of the circle 
@author: jtbabbe
"""
import numpy as np

#=============================
#              variables
#=============================

# circle
r_circle    =  12.6 # mm

# rectangle
a           =  1.5  # mm
b           =  0    # mm, starting value for while loop

#===================================
#              function def
#==================================

# area of circle fx
def f_circleArea( r):
    return   float(np.pi) * float(r**2)

# area of rec fx
def f_aR ( a, b):
    return float(a) * float(b)

#=====================================
#               create while loop
#=====================================


while f_aR( a, b) <= f_circleArea( r_circle):
    b += .1
print 'Maximum value of b =', b, 'mm'
    
     
    











