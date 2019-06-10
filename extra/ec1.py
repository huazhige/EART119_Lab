#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:10:25 2019

@author: williamdean

Numerical Integration Extra Credit #1
"""
import numpy as np
import integrate_utils as int_utils

#================================================
#          fct definition
#================================================

def fct_x( x):
    func = (3*(x**2))*(np.exp(x**3))
    return func

def fct_gxy( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= x0 and x <= xn:
        f_retVal = 1
    return f_retVal
def fct_xexact( x):
    np.exp(x**3)
#================================================
#           parameters 
#================================================
    
x0, xn = 0, 1
N = 200
# compute integral using midpoint
for n in np.arange( 0, 1000, 100):
    fInt = int_utils.midpoint( fct_x, x0, xn, N)
print( 'number of random points', n, 'num integral', round(fInt, 4), 'exact', 1.7182)

# compute integral using trapezoids  # use N = 700
#for n in np.arange( 0, 1000, 100):
#    fInt = int_utils.trapezoidal( fct_x, x0, xn, N)
#print( 'number of random points', n, 'num integral', round(fInt, 4), 'exact', 1.7182)


