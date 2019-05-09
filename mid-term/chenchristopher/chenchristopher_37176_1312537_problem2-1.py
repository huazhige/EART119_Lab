# -*- coding: utf-8 -*-
#python 2.7
"""
Midterm problem 2
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#parameters
#==============================================================================
#our interbal of interest is between -10 and 10 exclusive
xvals = np.linspace(-10, 10, 1000)

#==============================================================================
#function definitions
#==============================================================================
def f1(x):
    return x**5 + 0.4 * x **2 - 2

def f2(x):
    np.exp(-1 * x / 10.) + x
    
def f3(x):
    return 10 * np.sin(0.25 * x) + 0.1 * (x + 12)

#==============================================================================
#computations
#==============================================================================
def my_Secant(fct, x0, x1, tol, N):
    """
    Uses the secant method to find the roots of a function.
    Input: fct = function you want to find roots of
           x0 = one of your initial endpoint guesses
           x1 = the other initial endpoint guess
           tol = the accepted error of the root
           N = max number of iterations before giving up if no convergence
    Output: root of a function
    """
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(fct(x1)) > tol and i < N:
        #numerical approximation of derivative
        dfdt = (fct(x1) - fct(x0)) / (x1 - x0)
        #basically Newton's method
        x_next = x1 - fct(x1) / dfdt
        x0 = x1
        x1 = x_next
        i += 1
    
    #Check for convergence
    if abs(fct(x1)) < tol:
        return x_next
    else:
        return np.nan

root1 = my_Secant(f1, 5, 6, 1e-6, 100)
#root2 = my_Secant(f2, 5, 6, 1e-6, 100)
root3 = my_Secant(f3, 5, 6, 1e-6, 100)
#==============================================================================
#plotting
#==============================================================================
plt.figure(1, figsize = (12, 10))

#function 1
plt.subplot(311)
plt.plot(xvals, f1(xvals))
plt.plot(root1, f1(root1), 'ko')
print(str(root1) + 'is a root of function 1.')

#function 2
plt.subplot(312)
#must exlcude values of x >= 0
sel = xvals <= 0
negxvals = xvals[sel]
plt.plot(negxvals, f2(xvals))
print(str(root2) + 'is a root of function 2.')

# =============================================================================
# #function 3
# ax3 = plt.subplot(312)
# ax3.plot(xvals, f3(xvals))
# =============================================================================
print(str(root3) + 'is a root of function 3.')