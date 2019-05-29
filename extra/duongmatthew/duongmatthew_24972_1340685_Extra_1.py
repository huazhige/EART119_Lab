# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:37:44 2019
    - Calculates the integral of a function using the trapezoidal and midpoint 
    methods and compares it to the exact solution
    
@author: maduong
"""

import numpy as np
### my modules
import integrate_utils as int_utils

#==============================================================================
#                                 fct definition
#==============================================================================
def fct_t (t):                    # function defined
    return 3*t**2*np.exp(t**3)
def int_f(t):                    # integrated function
    return np.exp(t**3)

#==============================================================================
#                                 paramters
#==============================================================================
tmin, tmax = 0, 1        # initlal time value and final time value respectively
N = 100                  # can increase this value for increased accuracy

#==============================================================================
#                                 compute integral
#==============================================================================
f_trapint = int_utils.trapezoidal(  fct_t, tmin, tmax, N)   # integrals 
f_midint =  int_utils.midpoint(  fct_t, tmin, tmax, N)   
f_exact = int_f(tmax) - int_f(tmin)  # exact solution

print ('Trapezoidal Integral:   ', f_trapint)
print ('Midpoint Integral:   ', f_midint)
print ('Exact solution:    ', f_exact)
