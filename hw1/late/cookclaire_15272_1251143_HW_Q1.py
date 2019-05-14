# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:55:04 2019

Area of a Rectangle and Triangle

"""
#==========================================================
#                      parameters
#==========================================================
b   = input('input length') #length of shape
c   = input ('input width')  #Width of rectangle
h_b = input ('input height') #Height of triangle
 
#==========================================================
#                      Compute
#==========================================================

R = b*c       #Area of Rectangle

T = 0.5*h_b*b #Area of Triangle

print (R)
print (T)