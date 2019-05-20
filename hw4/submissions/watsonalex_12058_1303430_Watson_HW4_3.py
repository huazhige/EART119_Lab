# -*- coding: utf-8 -*-
"""
Homework 4 Part 3 - Alex Watson
    -update the Newton's Method equation, change the while loop parameters
"""
import numpy as np
#==============================================================================
def new_Newton( fct, df_dx, x0):
    """
        -implementation of Newton's method
        for solving f(x) = 0, when f'(x) is known
    """
    xn  = float(x0)
    eps = 1e-6
    diff = 1e5
    N   = 10
    i   = 0
    while  diff > eps and i < N:
        x_next = xn - fct( xn)/df_dx(xn)
        print( i, 'fct value', abs( fct( xn)), x_next)
        diff = fct(xn) - fct(x_next)
        xn = x_next
        i += 1
    if  diff < eps:
        return x_next
    else:
        return np.nan


def old_Newton( fct, df_dx, x0):
    """
        -implementation of Newton's method
        for solving f(x) = 0, when f'(x) is known
    """
    xn  = float(x0)
    eps = 1e-5
    N   = 10
    i   = 0
    while abs(fct( xn)) > eps and i < N:
        x_next = xn - fct( xn)/df_dx(xn)
        print( i, 'fct value', abs( fct( xn)), x_next)
        xn = x_next
        i += 1
    if abs( fct( xn)) < eps:
        return x_next
    else:
        return np.nan

#==============================================================================
#                                   Test
#==============================================================================
def fct( x):
    return x**2-1

def dfdx( x):
    return 2*x

x0 = 2

root_new = new_Newton( fct, dfdx, x0)

root_old = old_Newton( fct, dfdx, x0)

print root_new, root_old










