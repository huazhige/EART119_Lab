# -*- coding: utf-8 -*-
"""
                                Homework 1 Problem 2
                                    Alex Watson
    - compute the area of a polygon created using Cartesian coordinates using:
        - a for loop
        - a vectorized solution

"""
import numpy as np
#==============================================================================
#                                   Parameters
#==============================================================================
vec_x = np.array([1, 3, 4, 3.5, 2])
vec_y = np.array([1, 1, 2, 5, 4])

#==============================================================================
#                                   Function
#==============================================================================

##for loop##

def poly_area_for( vec_x, vec_y):
    sum = 0 
    for i in range(5):
        sum1 = vec_x[i-1]*vec_y[i]
        sum2 = vec_y[i-1]*vec_x[i]
        sum += sum1 - sum2
        A1   = 0.5*abs(sum)
    print A1
        
##vector method##
        
def poly_area_vec( vec_x, vec_y):
    A2 = 0.5*((vec_x[0]*vec_y[1] + vec_x[1]*vec_y[2] + vec_x[2]*vec_y[3] + vec_x[3]*vec_y[4] + vec_x[4]*vec_y[0]) - (vec_y[0]*vec_x[1] + vec_y[1]*vec_x[2] + vec_y[2]*vec_x[3] + vec_y[3]*vec_x[4] + vec_y[4]*vec_x[0]))
    print A2
    
#==============================================================================
#                                   Run functions
#==============================================================================
poly_area_for( vec_x, vec_y)

poly_area_vec( vec_x, vec_y)