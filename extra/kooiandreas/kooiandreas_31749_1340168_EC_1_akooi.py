#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:51:43 2019

@author: andreaskooi
"""

#=====================
# functions
#=====================

def fct_t(t):
    return (3*t**2)*np.exp(t**3)

def integral_fct_t(t):
    return np.exp(t**3)

#=====================
# imports
#=====================

import numpy as np
import integrate_utils as iu


#=====================
#computations
#=====================

# integrate fct_t using trapezoid, midpoint methods
trap_val = iu.trapezoidal(fct_t, 0, 1, 100)
mid_val = iu.midpoint(fct_t, 0, 1, 100)

# the exact integral solution
exact_val = integral_fct_t(1) - integral_fct_t(0)

#=====================
#print results
#=====================

print('The integration of f(t) using the trapezoidal method is: ' + str(trap_val))
print('The integration of f(t) using the midpoint method is: ' + str(mid_val))
print('The exact integration of f(t) is: ' + str(exact_val))




# Console output:
#The integration of f(t) using the trapezoidal method is: 1.7186215916047791
#The integration of f(t) using the midpoint method is: 1.7181119551669362
#The exact integration of f(t) is: 1.718281828459045
