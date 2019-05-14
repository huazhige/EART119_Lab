# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:51:43 2019

@author: Emily White
"""

"""
Homework 1 Prob 2 pt 2
Consider a polygon w five vertices in Cartesian coordinates:
    (1,1); (3,1); (4,2); (3.5, 5); (2,4)
Write a fnc to compute the area of this polygon

It will take two vectors (xi and yi) as input and return the area
of the polygon

Write diff fncs:
    1. area_polygon.py (solves eqn within a for loop)
    2. area_polygon_vec.py (solves the eqn using vector notation)
    
"""
#=======================================================================
"""
    n = total values of x
    Area = area from given equation
    x = values of x
    y = values of y
"""

#variables based on eqn given
def polygonarea(x,y):
    n = len(x)
    Area = x[n-1]*y[0] - y[n-1]*x[0] 
    for i in range(0,n-1,1):
        Area += x[i]*y[i+1] - y[i]*x[i+1] 
    return abs(Area)/2

#vector notation
x = [1, 3, 4, 3.5, 2]
y = [1, 1, 2, 5, 4]

#computations
print polygonarea(x,y)

