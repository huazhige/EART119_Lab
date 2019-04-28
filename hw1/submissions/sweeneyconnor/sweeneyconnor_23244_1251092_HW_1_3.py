# -*- coding: utf-8 -*-
"""
HW1 Q3

Consider one circle and one rectangle. The circle has a radius r = 12.6 mm. The rectangle
has sides a and b, but only a is known from the outset (a = 1.5 mm). Write a program
that uses a while loop to find the largest possible integer b that gives a rectangle area
smaller than, but as close as possible to, the area of the circle. What is the correct value
of b?
"""
A_circ = 498.8           # Area = pi*r**2 = pi*(12.6)**2 ~498.8
a = 1.5
b = 1
while b < 498.8/1.5:
    b = b + 1
if b > 498.8/1.5:
    b = b - 1
    print "The largest value of b is:", b, "mm"   


    
    
    
    
    
    