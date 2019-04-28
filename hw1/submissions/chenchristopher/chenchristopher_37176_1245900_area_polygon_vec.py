# -*- coding: utf-8 -*-
#python 2.7
"""
Computes the area of a polygon given its vertices
"""

import numpy as np

#=====================================================================================================
#Input variables: array of all the x-coordinates and array of all the corresponding y-coordinates
#=====================================================================================================
x = [1, 3, 4, 3.5, 2]
y = [1, 1, 2, 5, 4]

#=====================================================================================================
#Computation using A = 0.5(sum of x(n-1)y(n) - sum of y(n-1)x(n))
#=====================================================================================================
def area(x, y):
    #aligning the arrays to use the dot product
    #the copy arrays are shifted by moving the first element all the way to the end
    y_copy = list(y)
    y_copy.append(y[0])
    del y_copy[0]
    
    x_copy = list(x)
    x_copy.append(x[0])
    del x_copy[0]
    
    return 0.5 * (np.dot(x, y_copy) - np.dot(y, x_copy)) #Area formula expressed with dot product

print(str(area(x, y)) + " square units")