# -*- coding: utf-8 -*-
#python 2.7
"""
Extra Credit Problem 2
Compute the mean value and integrals of
f(x) = sinx for x between 0 and pi inclusive
g(x) = 2xe^(x^2) for x between 0 and 1 inclusive
"""

import numpy as np
import integrate_utils

#==============================================================================
#function definitions
#==============================================================================
def f(x):
    return np.sin(x)

def g(x):
    return 2 * x * np.exp(x**2)

def meanvalue(fct, x0, xn):
    """
    Computes the mean value of a function by averaging 1000 sampled values of the function
    Input: fct - function to find mean value of
           x0 - left bound
           xn - right bound
    """
    xvals = np.linspace(x0, xn, 1000)
    return fct(xvals).sum() / len(xvals)
#==============================================================================
#computations
#==============================================================================

fintegral =  integrate_utils.trapezoidal(f, 0 , np.pi, 1000)
print('Function f(x), integral is', fintegral, 'mean value is', meanvalue(f, 0, np.pi))

gintegral = integrate_utils.trapezoidal(g, 0 , 1, 1000)
print('Function g(x), integral is', gintegral, 'mean value is', meanvalue(g, 0, 1))