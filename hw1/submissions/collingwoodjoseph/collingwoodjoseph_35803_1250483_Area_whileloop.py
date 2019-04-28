# -*- coding: utf-8 -*-
"""
Calculates maximum possible rectangle height such that its area is still
less than the given circle.
"""
import math

r = 12.6
a = 1.5
b = 1

#loop checks if adding 1 will cause area to be larger (or equal), and if 
#not then it adds 1 to b

while a*b < math.pi*(r**2):
    if a*(b+1) >= math.pi*(r**2):
        break
    b += 1
    
print('Maximum value for b: ' + str(b) + 'mm')