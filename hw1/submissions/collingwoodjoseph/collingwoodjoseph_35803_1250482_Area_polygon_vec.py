# -*- coding: utf-8 -*-

"""
Calculates the area of an irregular polygon using vector notation.
"""

import numpy as np

x_input = np.array([1,3,4,3.5,2])
y_input = np.array([1,1,2,5,4])

print('X-coords: ' + str(x_input) + '\nY-coords: ' + str(y_input))

#Calculates area by shifting the index and computing the dot product.

def Area_poly_vec(x_coords,y_coords):

    x_shift = np.roll(x_coords,1)
    y_shift = np.roll(y_coords,1)

    Area = np.dot(x_coords,y_shift) - np.dot(y_coords,x_shift)
    Area = 0.5*(np.abs(Area))
    
    return Area

Area = Area_poly_vec(x_input,y_input)

print('The area is: ' + str(Area))