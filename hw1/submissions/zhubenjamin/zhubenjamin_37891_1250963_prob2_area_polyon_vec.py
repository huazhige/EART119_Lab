# -*- coding: utf-8 -*-
"""
Created on Apr 11, 2019
Class = Astro/Eart 119
Homework 1 - functions and vectors
Student = Benjamin Zhu (1696575)

"""

#==================================================
#           Problem 2
#==================================================

""" vector notation method """

x   = (1, 3, 4, 3.5, 2)   #input x and y coordinate as arrays
y   = (1, 1, 2, 5, 4)

#pulling out numbers from the index one by one and plug into the calculation
B   = abs(( x[0]*y[1] + x[1]*y[2] + x[2]*y[3] + x[3]*y[4] + x[4]*y[0])\
          - ( y[0]*x[1] + y[1]*x[2] + y[2]*x[3] + y[3]*x[4] + y[4]*x[0]))

#final step of divid by half
A   = 0.5*B

print A