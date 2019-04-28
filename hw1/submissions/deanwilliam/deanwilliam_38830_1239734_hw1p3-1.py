#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:17:00 2019

@author: williamdean
Problem 3 while loop
"""
import math
r = 12.6 #radius of circle in mm
A_circle = math.pi*r**2
a = 1.5 #length of side a in mm
b = A_circle/a
A_rectangle = a*b
# find greatest value of b so that A_circle is just larger than A_rectangle
i = 0
while A_rectangle <= A_circle:
    A_rectangle = b*a
    print( b)
    b += 1

