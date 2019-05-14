# -*- coding: utf-8 -*-
#Created by: Justin Nguyen
#Recent edit: 4/13/2019
"""
    Write a function to compute the area of this polygon.
        With Cartesian coordinates:
            (1,1) (3,1) (4,2) (3.5,5) (2,4)

    Based on the Shoelace formula:
A = 0.5*|(x1*y1+x2*y2+..+x_n_1*yn+xn*y1)-(y1*x2+y2*x3+..+y_n_1*xn+yn*x1)|

"""
# Interpreter: Python 2.7, Anaconda2
# Import add-ons 
import numpy as np
#==============================================================================
"""                              Problem 2                                  """
#==============================================================================
"""
 Start with defining the variables aka the Cartesian Coordinates of the poly
     in clockwise order
"""
my_coords = [(2,4), (3.5,5), (4,2), (3,1), (1,1)]

#Then create function and for loop based on the Shoelace Formula
def area_polygon_vec(my_coords):
    n = len(my_coords) # of corners
    area = 0.0
    for x in range(n):
        y = (x + 1) % n
        #Now to establish the alternating pattern in the formula
        area += my_coords[x][0] * my_coords[y][1]
        area -= my_coords[y][0] * my_coords[x][1]
    #Then form the equation
    area = abs(area) / 2.0
    return area

print "Area of the polygon is ",area_polygon_vec(my_coords)
