# -*- coding: utf-8 -*-
"""
Extra Credit Part 1
Alex Watson
 - Numerical integration of definite integrals
    - ex: f(t) = 3t**2*exp( t^3)
          F(t) = exp( t^3)
          between: a, b
          with F'(t) = f(t)
"""
import numpy as np
##integ utils##
import src.integrate_utils as int_utils
#==============================================================================
#                               fct definition
#==============================================================================
def fct_f( t):
    return 3*t**2*np.exp(t**3)

def fct_F( t):
    return np.exp( t**3)

#==============================================================================
#                               parameters
#==============================================================================
xmin, xmax = 0, 1
N          = 10

#==============================================================================
#                          num integration & plotting
#==============================================================================
# exact sol
f_IntExact = fct_F( xmax) - fct_F( xmin)

#numerical approx.
f_IntTrap = int_utils.trapezoidal( fct_f, xmin, xmax, N)
f_IntMid  = int_utils.midpoint( fct_f, xmin, xmax, N)

#compare exact and numerical
print 'exact integral: ', f_IntExact 
print 'num. approx (trapezoidal): ', f_IntTrap
print 'num. approx (midpoint): ', f_IntMid

