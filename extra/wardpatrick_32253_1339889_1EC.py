# -*- coding: utf-8 -*-

"""

Compute the integral of the following function within the given domain. Use both
midpoint and trapezoidal methods! Compare your results to the exact solution of the
definite integral.

"""
import numpy as np
import integrate_utils as IU


#================================================================
#                       Functions
#================================================================
def ft(t):
    return 3*t**2*np.exp(t**3)

def int_ft(t):
    return np.exp(t**3)

#================================================================
#                       Calcs
#================================================================

exact_sol = int_ft(1) - int_ft(0)

trap = IU.trapezoidal(ft, 0, 1, 1000)
mid  = IU.midpoint(ft, 0, 1, 1000)

#================================================================
#                       Results
#================================================================

print 'Exact solution:', exact_sol
print 'Trapezoidal method:', trap
print '     difference', exact_sol-trap
print 'Midpoint method:', mid
print '     difference', exact_sol-mid