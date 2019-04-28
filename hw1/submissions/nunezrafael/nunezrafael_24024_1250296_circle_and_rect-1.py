# -*- coding: utf-8 -*-
"""
Spyder Editor
Homework 1 ASTR/EART 112
Rafael Nunez
#3
"""
import math
import numpy as np
"""
Parameters
"""
r = 12.6                        #given radius
a = 1.5                         #given length
b = np.linspace( 0, 500, 5000)  #range where the width could be
"""
Functions
"""
Ac = math.pi*r**2               #area of a circle formula
print "the area of the circle is %f mm^2" % (Ac)

Ar = a*b                        #area of a rectangle

i = 0                           #gives i an initial value for the while loop to start from
while Ar[i] <= Ac: 
    i += 1                      #as long as the area of the rectangle is smaller than the area of the circle, i will keep going up in steps of 1 until Ar is bigger than Ac
print "the closest Ar can get to Ac is", (Ar[i-1]), "mm^2" 
print "the value of b is", (b[i-1]), "mm"
#I used i-1 because the i place is when Ar is bigger than Ac and we want it to be smaller by a small amount (to an approximation of .1 due to the steps I took in the range of b)