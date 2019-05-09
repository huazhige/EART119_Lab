#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:45:23 2019

@author: williamdean

find the roots

"""
import numpy as np
import opt_utils
import scipy.optimize as scopt
import matplotlib.pyplot as plt
# paramters
xmin, xmax = -10, 10

x0 = 5
#root finding
tol = 1e-6

#function defs

def f_1( x):
    return x**5 + (2/5)*x**2 - 2

def f_2( x):
    return np.exp(-x/10) + x

def f_3( x):
    return 10*np.sin(x/4) + 0.1*(x+12)


#find roots

def my_Secant( fct, x0, x1, tol, n = 20):
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

f_Se_x0  = opt_utils.my_Secant( f_1, x0, x0+10, N = 40)
print( 'secant  ----------- ', f_Se_x0, 'scipy: ', scopt.newton( f_1, x0, fprime = None))
f_Se_x2  = opt_utils.my_Secant( f_2, x0, x0+10, N = 40)
print( 'secant  ----------- ', f_Se_x2, 'scipy: ', scopt.newton( f_2, x0, fprime = None))
f_Se_x3  = opt_utils.my_Secant( f_3, x0, x0+10, N = 40)
print( 'secant  ----------- ', f_Se_x3, 'scipy: ', scopt.newton( f_2, x0, fprime = None))


a_x = np.linspace( xmin, xmax, 1000)
plt.plot( a_x, f_1( a_x),  'k-', label = 'f1(x)')
plt.plot( a_x, f_2( a_x),  'g-', label = 'f2(x)')
plt.plot( a_x, f_3( a_x),  'r-', label = 'f3(x)')
plt.plot( [xmin, xmax], [0,0], '--')
plt.plot( [f_Se_x0], [f_1( f_Se_x0)],   'k*', mfc = 'w', ms = 10)
plt.plot( [f_Se_x2], [f_2( f_Se_x2)],   'k*', mfc = 'w', ms = 10)
plt.plot( [f_Se_x3], [f_3( f_Se_x3)],   'r*', mfc = 'w', ms = 10)
plt.xlabel( 't')
plt.ylabel( 'Function Values')
plt.ylim( -10, 10)
plt.grid( True)
plt.legend()
plt.show()