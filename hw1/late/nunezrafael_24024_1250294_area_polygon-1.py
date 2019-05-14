# -*- coding: utf-8 -*-
"""
Spyder Editor
Homework 1 ASTR/EART 112
Rafael Nunez
#2.1
"""
import numpy as np
"""
Parameters
"""
xVal = [1.0, 3, 4, 3.5, 2]  #all the x values of the points
yVal = [1.0, 1, 2, 5, 4]    #all the y values of the points
v1 = 0                      #initial value of the first variable in the area equation
v2 = 0                      #initial value of the second variable in the area equation
#I have v1 and v2 here set to zero initially to add to them in the for loop later
"""
Function
"""

for i in range(len(xVal)):  #takes i in the range of the x values
    if i == len(xVal) - 1:  
        y = yVal[0]
    else:
        y = yVal[i+1]       #takes into account the last term in the first variable so as to not get an error for i=6 in a list that has a length of 5
    v1 += xVal[i] * y       #the first variable in the equation
    #print v1
    
for i in range(len(yVal)):
    if i == len(yVal) - 1:
        x = xVal[0]
    else:
        x = xVal[i+1]
    v2 += yVal[i] * x
    #print v2
# the second for loop does the same thing as the first but for y being the first term instead of x
A = 0.5*( v1 - v2)          #solves for area
print "the area of A is", A
    






