#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:33:25 2019

@author: williamdean

HW4P3 modified Newton Root Method
"""
import numpy as np

#eps = 1e-5

def fct( x):
    return -x**2 + 10*x + 9

def dfdx( x):
    return -2*x + 10

#def naive_Newton(f, dfdx, x, eps):
#    while abs(f(x)) > eps:
#        x = x - float(f(x))/dfdx(x)
#        return x
#print naive_Newton(f, dfdx, 1000, 0.001)

def my_Newton( fct, dfdx, x0):
    """
    -implementation of Newton's method for solving
    f(x)=0, when f'(x) is known
    """
    xn = float(x0)
    eps = 1e-6
    n = 20
    i = 0
    while i < n:
        x_next = xn - fct( xn) / dfdx(xn)
        print( n, 'fct_value', abs( fct( xn)), x_next)
        if (abs(fct(x_next) - fct(xn)) < eps): #going to assume you want abs(x)
            return x_next

        xn = x_next
        i += 1

    return np.nan