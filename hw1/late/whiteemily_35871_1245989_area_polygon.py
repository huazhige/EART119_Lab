# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:54:35 2019

@author: Emily White
"""
"""
Homework 1 Problem 2 pt 1
Consider a polygon w five vertices in Cartesian coordinates:
    (1,1); (3,1); (4,2); (3.5, 5); (2,4)
Write a fnc to compute the area of this polygon

It will take two vectors (xi and yi) as input and return the area
of the polygon

Write diff fncs:
    1. area_polygon.py (solves eqn within a for loop)
    2. area_polygon_vec.py (solves the eqn using vector notation)
    
"""

# note: len() is the number of items/length of object
# += adds -= subtracts another value with variable's value, making a new value
# the % is a modulus operator and returns the remainder of dividing two values
# abs() is absolute value


#==================================================================
#                       Area of a Polygon
#==================================================================

#using a for loop


"""
    A = Area of Polygon
    l = total number of cordinates
    v = vertices/coordinates
    vectors: x , y
"""

def A(v):
    l = len(v)
    Area = 0
    for x in range(l):
        y = ( x + 1 ) % l
        Area += v[x][0] * v[y][1] #first half of eqn
        Area -= v[y][0] * v[x][1] #second half of eqn
    Area = abs(Area) / 2.0
    return Area

# use given coordinates via list
v = [(1,1), (3,1), (4,2), (3.5,5), (2,4)]
print A(v)

