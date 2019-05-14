#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:36:41 2019

@author: williamdean
"""
def compute_polygon_area(x_vector, y_vector):
    n = len(x_vector)
    area = 0
    for i in range(n):
        area += x_vector[i]*y_vector[i + 1%n]
        area -= y_vector[i]*x_vector[i + 1%n]
        temp = area
        area = abs(temp)/2.
        return area

# parameter
compute_polygon_area([1, 3, 4, 3.5, 2], [1, 1, 2, 5, 4])

def polygon_area( X, Y, n):
    area = 0
    j = n - 1
    for i in range (0, n):
        area += (X[j] + X[i])*(Y[j] - Y[i])
        j = i
    return int(abs(area/2.0))
#test
X = [1, 3, 4, 3.5, 2]
Y = [1, 1, 2, 5, 4]
n = len(X)
print(polygon_area(X, Y, n))