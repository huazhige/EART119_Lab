# -*- coding: utf-8 -*-

"""
Brady Lobmeyer 4/13/2019
using a while loop to find a max length of a rectangle side,
with a known side length and while keeping the total rectangle 
area less than a area of a cicle with radius 12.6mm.

"""
import numpy as np
import math

#==============================================================
#           Known Dimensions
#==============================================================
rc = 12.6 #('radius of circle')
a = 1.5 #('length a')
n = 20
b = np.linspace(320, 340, n, dtype = int) #('variable b')


#==============================================================
#           Areas
#==============================================================

Acir= math.pi*rc**2 #('area of circle')
Arec = a*b #('area of a rectangle with a variable')
print Acir
print Arec
#==============================================================
#           while loop
#==============================================================
i = 1
('area of circle > area of rectangle with integer variable b')
while Acir > Arec[i]:
    largest_b = Acir/a
    i += 1
print( 'maximum b')    
print ((int(largest_b)))

largest_b= 332



    