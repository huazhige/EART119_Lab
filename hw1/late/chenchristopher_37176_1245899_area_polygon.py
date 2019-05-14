# -*- coding: utf-8 -*-
#python 2.7
"""
Computes the area of a polygon given its vertices
"""

import numpy as np

#=====================================================================================================
#Input variables: array of all the x-coordinates and array of all the corresponding y-coordinates
#=====================================================================================================
x = np.array([1, 3, 4, 3.5, 2])
y = np.array([1, 1, 2, 5, 4])

#=====================================================================================================
#Computation using A = 0.5(sum of x(n-1)y(n) - sum of y(n-1)x(n))
#=====================================================================================================
sum = 0
for i in range(x.size):
    sum = sum + 0.5 * (x[i - 1] * y[i] - y[i - 1] * x[i])
print(str(sum) + " square units")