# -*- coding: utf-8 -*-
#python2.7


# =============================================================================
#                              Problem 3.
# =============================================================================

import numpy as np

def my_Newton(fct, df_dx, x0):
    """
    Implementation of Newton's method for solving f(x) = 0, when f'(x) is known
    """
    
    xn = float(x0)
    eps = 1e-5
    N = 20
    i = 0
    while abs((fct( xn**(i+1)) - fct( xn**i))) > eps and i < N:
        x_next = xn - fct(xn)/df_dx(xn)
        print( i, 'fct_value', abs(fct(xn)), x_next)
        xn = x_next
        i += 1
    if abs( fct(xn)) < eps:
        return x_next
    else: # solution did not converge
        return np.nan
    

# The code below is to test if my_Newton works with the modification
    
# =============================================================================
# def f ( t):
#     """
#     The function f given in homework 4 problem 2
#     """
#     
#     c = 1.1
#     t_0 = 2.5
# 
#     Ans = c * (t - t_0)**2
#     
#     return Ans
# 
# def dfdt ( t):
#     """
#     The derivative of f(t)
#     """
#     c = 1.1
#     t_0 = 2.5
#     
#     Ans = 2*c*(t-t_0)
#     
#     return Ans
# 
# my_Newton(f, dfdt, 2.6)
# =============================================================================
