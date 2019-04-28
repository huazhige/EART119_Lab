# -*- coding: utf-8 -*-

import numpy as np

# 1.

def area_of_square (b,c):
    """
    This function finds the area of a square.
    
    Variables: b (height), c (width)
    """

    A = b * c
    return float(A)

print("Area of a 10 x 5 square: " + str(area_of_square(10,5)))

def area_of_triangle (h_b,b):
    """
    This function finds the area of a triangle.
    
    Variables: h_b (height), b (length of base)
    """

    A = 0.5 * h_b * b
    return float(A)

print("Area of a triangle with height 2 and base 3: " + str(area_of_square(2,3)))

# 2.                    

def area_polygon (x_i,y_i):
    """
    This function finds the area of a polygon with i sides given the 
    vertices of the sides using a for loop.
    
    Variables: 
    x_i: the x-coordinates of each of the i points
    y_i: the y-coordinates of each of the i points
    
    Make sure that each x component corresponds with the y component, e.g.
    the first input into y_i should be the same point used for x_i
    """
    
    total1 = 0
    total2 = 0
    
    iX = np.arange(0, len(x_i), 1, dtype = int)
    iY = np.arange(0, len(y_i), 1, dtype = int)
    
    for x in iX:
        total1 += x_i[iX-1] * y_i[iX]
     
    for y in iY:
        total2 += y_i[iY-1] * x_i[iY]
    
    total1_final = total1 + x_i[-1] * y_i[1]
    total2_final = total2 + y_i[-1] * x_i[1]    

    A = 0.5 * np.abs(total1_final - total2_final)
    
    return float(A)
    
print("Area of a polygon: " + str(area_polygon(x_i = [1,3,4,3.5,2], y_i = [1,1,2,5,4])))

def area_polygon_vec (x_i,y_i):
    """
    This function finds the area of a polygon with i sides given the 
    vertices of the sides.
    
    Variables: 
    x_i: the x-coordinates of each of the i points
    y_i: the y-coordinates of each of the i points
    
    Make sure that each x component corresponds with the y component, e.g.
    the first input into y_i should be the same point used for x_i
    """
    
    iX = np.arange(0, len(x_i), 1, dtype = int)
    iY = np.arange(0, len(y_i), 1, dtype = int)
    
    total1 = np.dot(x_i[iX] + y_i[iY], np.ones(len(iY)))
    total2 = np.dot(x_i[iX] + y_i[iY], np.ones(len(iY)))
    
    total1_final = total1 + x_i[-1] * y_i[1]
    total2_final = total2 + y_i[-1] * x_i[1]
    
    A = 0.5 * np.abs(total1_final - total2_final)
    
    return float(A)

print("Area of a polygon: " + str(area_polygon_vec(x_i = [1,3,4,3.5,2], y_i = [1,1,2,5,4])))

# 3.

r = 12.6 # mm
a = 1.5 # mm
b = 0. # mm

area_of_circle =  np.pi * (r**2) # mm^2

# Now I'm going to compare the area of the rectangle (a*b) with the area of 
# the circle.

while a * b < area_of_circle:
        b += .01

print("Largest value of b: " + str(b) + "mm")