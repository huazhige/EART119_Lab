# -*- coding: utf-8 -*-
"""
Compute the integral of the following function within the given domain. Use both
midpoint and trapezoidal methods! Compare your results to the exact solution of the
definite integral.

Evaluate integral numerically from 0 to 1

f(t) = 3*(t**2) * (e**(t**3))

integral = (e**(t**3))
"""
#==================================imports ====================================

import numpy as np
import integrate_utils as int_u
import matplotlib.pyplot as plt


e = np.exp(1)

#=============================Define function and integral ====================

def f_t(t):
    return 3*(t**2) * (e**(t**3))

a = f_t(1)
print(a)

def int_f_t(t):
    return (e**(t**3))

b = int_f_t(0)
print(b)

#============================exact solution====================================
    
ex_sol = int_f_t(1) - int_f_t(0)

#===================Apply trapezoidal and midpoint methods ====================

trap_result = int_u.trapezoidal(f_t, 0, 1, 10)

midpoint_result = int_u.midpoint(f_t, 0, 1, 10)

#==results(when using %10.2f, 10 is number of spaces, 2 is nuber of decimals)==
print("Trapezoidal rule results: %.20f" %trap_result)
print("Midpoint method results: %.20f" %midpoint_result)

"""
Trapezoidal rule results: 1.75204264178808499786
Midpoint method results: 1.70148276900918782317

"""
