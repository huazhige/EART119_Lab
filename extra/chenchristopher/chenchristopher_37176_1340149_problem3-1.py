# -*- coding: utf-8 -*-
#python 2.7
"""
Extra Credit Problem 3
Compare the definite integrals of the following functions using analytical and Monte Carlo method
"""

import numpy as np
import integrate_utils

#==============================================================================
#function definitions
#==============================================================================
def f(x, y):
    return (x**2 + y**2)**0.5

def regionf(x, y):
    return 2 - ((x**2 + y**2)**0.5)

def w(x, y):
    return x * y**2

def regionw(x, y):
    if np.logical_and(np.logical_and(x >=0, x <= 2), np.logical_and(y >= 0, y <= 1.5)):
        return 1
    else:
        return -1
    
#==============================================================================
#computations
#==============================================================================
#analytical solution for f(x, y) over region sqrt(x^2 + y^2) <= 2 (can be solved using a polar coordinate transformation)
print('The analytical solution for integral of f(x, y) is ' + str(16 * np.pi / 3))

#solution using monte carlo method for f(x,y)
print('The solution for the integral of f(x, y) using the Monte Carlo Method is ' + str(integrate_utils.monteCarlo(f, regionf, -2, 2, -2, 2, 1000)))

print('')

#analytical solution for w(x, y) over region x between 0 and 2, y between 0 and 1.5
print('The analytical solution for integral of w(x, y) is ' + str(2.25))

#solution using monte carlo method for w(x, y)
print('The solution for the integral of w(x, y) using the Monte Carlo Method is ' + str(integrate_utils.monteCarlo(w, regionw, 0, 2, 0, 1.5, 1000)))