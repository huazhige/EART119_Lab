# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:43:37 2019

@author: Emily White
"""
"""
    CODE CREATED IN CLASS (MODIFIED)
    focused only on the Newton method to achieve the convergence criterion:
            f(x0^(i+1)) - f(x0^i) < eps
    
"""
import numpy as np
import matplotlib.pyplot as plt
#import src.opt_utils as opt_utils
#=============================================================================
#                   fnc definitions
#=============================================================================
def fct(x):
    return -x**2 + 10*x + 9

def dfdx(x):
    return -2*x + 10

def my_Newton( fct, df_dx, x0):
    """
        - implementation of Newton's method for solving f(x) = 0, when f'(x) is known
    """
    xn = float(x0)
    xn1 = float(x0+1)
    xn2 = xn1 - xn
    eps = 1e-6 #value close enough to zero
    N = 20
    i = 0
    while fct(xn1) - fct(xn) < eps and i < N:
        x_next = xn - (fct(xn1) - fct(xn))/df_dx(xn)
        print(i, 'fct_value', abs(fct(xn1) - fct(xn)), x_next) #gets it close to 0, ie the purpose
        xn2 = x_next
        i += 1
    if abs(fct(xn2)) < eps:
        return x_next
    else: #soln did not converge
        return np.nan
#returning nan as a soln to say it did not converge
"""
def my_Secant(fct, x0, x1, tol = 1e-5, N = 20):
    
# tol = tolerance
    
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(fct(x1)) > tol and i < N:
        #numerical approx of derivative
        dfdt = (fct(x1) - fct(x0))/(x1-x0)
        # basically Newton
        x_next = x1 - fct(x1)/dfdt
        
        x0 = x1
        x1 = x_next
        print(i, 'fct_value', abs(fct(x0)), x_next)
        i+= 1
    # check if soln converged
    if abs(fct(x1)) > tol:
        return np.nan
    else:
        return x1
"""
#=============================================================================
#                       parameters
#=============================================================================
x0 = -9
#independent variable range
xmin, xmax = -10, 15

#=============================================================================
#                   find roots
#=============================================================================
x_root = my_Newton(fct, dfdx, x0)
#opt_utils.

#x_rootSec = my_Secant(fct, x0, x0+10)
#=============================================================================
#                   plots
#=============================================================================
a_x = np.linspace(xmin, xmax, 1000)

plt.figure(3)
plt.plot(a_x, fct(a_x), 'k-')
plt.plot([x_root], [fct(x_root)], 'r*', ms = 14)
#plt.plot([x_rootSec], [fct(x_rootSec)], 'b*', ms = 10) #b* blue star, ms is size of star
plt.plot([xmin, xmax], [0,0], 'r--',)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('Fct values f(x)')
plt.show()
