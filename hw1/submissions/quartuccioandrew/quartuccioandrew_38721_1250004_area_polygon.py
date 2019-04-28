#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:24:17 2019

    Problem 2: computes the area of a polygon given the x,y
    coordinates of the vertices
    
@author: andrewquartuccio
"""

#=================================================================
#                   Imports
#=================================================================


#=================================================================
#                    Parameters
#=================================================================

x = [1, 3, 4, 3.5, 2]
y = [1, 1, 2, 5.0, 4]
N = len(x)

#=================================================================
#                    Function Definitions
#=================================================================

def area_polygon(x, y):
    sum1 = 0.0
    sum2 = 0.0
    for i in range(1,N):
        print i, N
        sum1 += abs(x[i-1]*y[i])
        sum2 += abs(y[i-1]*x[i])
        
        print 'sum 1 = %d, sum 2 = %d' % (sum1, sum2)
        
    
    sum1 += abs(x[i]*y[0])
    sum2 += abs(y[i]*x[0])
    
    print 'sum 1 = %d, sum 2 = %d' % (sum1, sum2)
    
    return (0.5)*(sum1-sum2)

    
#=================================================================
#                    Function Call and Error Display
#=================================================================

if N == len(y):
    final_area = area_polygon(x,y)
    print final_area
else:
    print('Error, invalid coordinates')