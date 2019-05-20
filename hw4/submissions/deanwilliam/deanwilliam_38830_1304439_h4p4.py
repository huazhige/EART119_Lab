#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:30:35 2019

@author: williamdean

HW4p4 find the root of functions using Secant Method

"""
import numpy as np

def f_1( x):
    return -(x**5.0) + ((x**2)/3) + 0.5
def f_2( x):
    return np.cos(x)**2 + 0.1
def f_3 ( x):
    return np.sin(x/3) + 0.1*(x + 5.0)


def my_Secant( fct, x0, x1, tol = 1e-5, n = 20):
    """
    
    """
    x0 = float( x0)
    x1 = float( x1)
    i = 0
    while abs( fct(x1)) > tol and i < n:
        # numerical approx. of derivative
        dfdt = (fct( x1) - fct( x0))/( x1 - x0)
        x_next = x1 - fct( x1)/dfdt
        
        x0 = x1
        x1 = x_next
        print( i, 'fct_value', abs( fct( x1)), x_next)
        i += 1
    # check is solution converged
    if abs( fct( x1)) > tol:
        return np.nan
    else:
        return x1
# 1 diverges 
# 2 doesn't converge