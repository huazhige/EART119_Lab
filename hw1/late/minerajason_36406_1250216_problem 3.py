# -*- coding: utf-8 -*-
"""

Code by Jason Minera
using python 2.7
due 4/14/19

Question:
Consider one circle and one rectangle. The circle has a radius r = 12.6 mm. 
The rectangle has sides a and b, but only a is known from the outset 
(a = 1.5 mm). Write a program that uses a while loop to find the largest 
possible integer b that gives a rectangle area smaller than, but as close as 
possible to, the area of the circle. What is the correct value of b?
"""
from math import pi # i have to use pi for the area of the circle 
r = 12.6 # giving the value of r as 12.6
area_of_circ = pi*r**2

print'The area of your circle with a radius 12.6 mm is %.3f mm^2' % (area_of_circ)   # i want this to be more interactive, i want the user to see it as if the computer is talking to you

a = 1.5                  #known value of a

i = 0                    #this is the starting point of the while loop to find the value of b 

'''
i had trouble figuring out what was the value for b. At the begining i was trying to
get the area of the rectangle first. For example run the while loop with a function that would give me the area of
the rectangle. i was having float problems. so i figured dividing the area of the known circle and the value of a 
would get me the value of b that i wanted. 

'''



while i <= (area_of_circ/a): 
    largest_b_val = float(i)
    
    i = i + 0.1
    
print'b is most likely %.1f mm' %(largest_b_val)    #printing out the value of be after the while loop has finished to an accuracy to the tenths place

largest_area_rec = a*largest_b_val                  #now i want to print out the value of the area of the rectangle using the b value that i got on top.

print 'Your largest area of your rectangle is %.2f mm^2' %(largest_area_rec)        #finally i print out that value here with an accuracy in the hundrendth place
