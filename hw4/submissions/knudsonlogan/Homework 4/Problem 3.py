# -*- coding: utf-8 -*-
"""
Modify the function we developed in class for Newton’s method so that the iteration
(while loop) stops if following convergence criterion is met:
�?�*
ABCD − �?�*
A D < �,
with � being some small number e.g. 1e-6
Upload the new function as python file on canvas!

"""

import numpy as np
import matplotlib.pyplot as plt
 
# =============================================================================
#       Function Definitions
# =============================================================================


def fct( x):
    return -x**2 + 10*x + 9

def dfdx( x):
    return -2*x + 10

def my_Newton ( fct, df_dx, x0):
    """
        -implementation of newtons method for solving f(x) = 0 when f'(x) is known
    """
    N = 20
    eps = 1e-5
    i = 1                                               #change this to 1 (from i = 0) because we do one itteration outside of while loop
    xn = float(x0)
    x_next = xn - fct( xn)/df_dx(xn)                    #have to assign a value to x_next for the while loop to work, completes the first step outside of the loop
    while abs(fct(x_next) - fct( xn)) > eps and i < N:  #change the while statement to have abs( f(x_(i+1)) - f(x_i)) > epsilon)
        xn = x_next                                     # change xn to x_next before 
        x_next = xn - fct( xn)/df_dx(xn)
        print( i, 'fct_value', abs(fct( xn)), x_next)
        i += 1
    if abs( fct( x_next)) < eps:                        #changed from xn to x_next, at this point xn =! x_next
        return x_next
    else:                                               #soultion does not converge
        return np.nan

# =============================================================================
#       Parameters
# =============================================================================
x0 = -9


x_root = my_Newton( fct, dfdx, x0)
