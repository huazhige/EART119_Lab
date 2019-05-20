#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:52:34 2019

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import opt_utils


xmin1 = -10
xmax1 = 10
xmin2 = -10
xmax2 = 10
xmin3 = -3
xmax3 = 3

def fct_fx_1(x):
    return -1*(x**5) + 0.33*(x**2) + 0.5

def fct_fx_2(x):
    return ((np.cos(x))**2) + 0.1

def fct_fx_3(x):
    return np.sin(0.33*x) + 0.1*(x+5)

def df_dx_1(x):
    return -5*(x**4) + 0.66*x

def df_dx_2(x):
    return -2*np.cos(x) * np.sin(x)

def df_dx_3(x):
    return 0.33*np.cos(0.33*x) + 0.1





def my_Secant_1( fct_fx_1, xmin1, xmax1, tol = 1e-5, N = 20):
    """
    
    """
    xmin1 = float( xmin1)
    xmax1 = float( xmax1)
    i = 0
    while abs( fct_fx_1(xmax1)) > tol and i < N:
        # numerical approximation of derivative
        # dfdt  = ( fct_fx_1( xmax) - fct_fx_1(xmin))/(xmax - xmin)
        # basically Newton
        x_next1= xmax1 - fct_fx_1( xmax1)/df_dx_1(xmax1)
        
        xmin1    = xmax1
        xmax1    = x_next1
        print( i, abs( fct_fx_1( xmax1)), x_next1)
        i += 1
    # check if solution converged
    if abs( fct_fx_1( xmax1)) > tol:
        return np.nan
    else:
        return xmax1

def my_Secant_2( fct_fx_2, xmin2, xmax2, tol = 1e-5, N = 20):
    """
    
    """
    xmin2 = float( xmin2)
    xmax2 = float( xmax2)
    i = 0
    while abs( fct_fx_2(xmax2)) > tol and i < N:
        # numerical approximation of derivative
        # dfdt  = ( fct_fx_1( xmax) - fct_fx_1(xmin))/(xmax - xmin)
        # basically Newton
        x_next2= xmax2 - fct_fx_2( xmax2)/df_dx_2(xmax2)
        
        xmin2    = xmax2
        xmax2    = x_next2
        print( i, abs( fct_fx_2( xmax2)), x_next2)
        i += 1
    # check if solution converged
    if abs( fct_fx_2( xmax2)) > tol:
        return np.nan
    else:
        return xmax2

def my_Secant_3( fct_fx_3, xmin3, xmax3, tol = 1e-5, N = 20):
    """
    
    """
    xmin3 = float( xmin3)
    xmax3 = float( xmax3)
    i = 0
    while abs( fct_fx_3(xmax3)) > tol and i < N:
        # numerical approximation of derivative
        # dfdt  = ( fct_fx_1( xmax) - fct_fx_1(xmin))/(xmax - xmin)
        # basically Newton
        x_next3= xmax3 - fct_fx_3( xmax3)/df_dx_3(xmax3)
        
        xmin3    = xmax3
        xmax3    = x_next3
        print( i, abs( fct_fx_3( xmax3)), x_next3)
        i += 1
    # check if solution converged
    if abs( fct_fx_3( xmax3)) > tol:
        return np.nan
    else:
        return xmax3

x_root_1 = my_Secant_1( fct_fx_1, xmin1, xmax1, tol = 1e-5, N = 20)
x_root_2 = my_Secant_2( fct_fx_2, xmin2, xmax2, tol = 1e-5, N = 20)
x_root_3 = my_Secant_3( fct_fx_3, xmin3, xmax3, tol = 1e-5, N = 20)


a_x_1 = np.linspace( xmin1, xmax1, 1000)

plt.figure(1)
plt.plot( a_x_1, fct_fx_1(a_x_1), 'k-')
plt.plot( [x_root_1], [fct_fx_1(x_root_1)], 'b*', ms = 10)
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')
plt.show()

a_x_2 = np.linspace( xmin2, xmax2, 1000)

plt.figure(2)
plt.plot( a_x_2, fct_fx_2(a_x_2), 'k-')
plt.plot( [x_root_2], [fct_fx_2(x_root_2)], 'b*', ms = 10)
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')
plt.show()

a_x_3 = np.linspace( xmin3, xmax3, 1000)

plt.figure(3)
plt.plot( a_x_3, fct_fx_3(a_x_3), 'k-')
plt.plot( [x_root_3], [fct_fx_3(x_root_3)], 'b*', ms = 10)
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')
plt.show()

print(x_root_1)
print x_root_2, "--- Does not touch x axis at all"
print(x_root_3)
