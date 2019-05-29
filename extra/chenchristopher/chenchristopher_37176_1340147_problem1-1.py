# -*- coding: utf-8 -*-
#python 2.7
"""
Extra Credit Problem 1
Compute the integral of 3t^2e^(t^3) from 0 to 1 analytically and then using midpoint and trapezoidal method
"""

import numpy as np
import integrate_utils

#==============================================================================
#function definitions
#==============================================================================
def fct(t):
    return 3 * t**2 * np.exp(t**3) 

def antideriv(t):
    return np.exp(t**3)

#==============================================================================
#computations
#==============================================================================
#using midpoint method
print('The solution, using midpoint method, is ' + str(integrate_utils.midpoint(fct, 0, 1, 1000)))

#using trapezoid method
print('The solution, using trapzeoid method, is ' + str(integrate_utils.trapezoidal(fct, 0, 1, 1000)))

#exact solution
print('The exact solution is ' + str(antideriv(1) - antideriv(0)))