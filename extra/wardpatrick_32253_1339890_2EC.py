# -*- coding: utf-8 -*-

"""

Discretize the following functions between xmin, xmax using N=1000 sample points.
Compute the mean value of the function in the given domain and compare it to the
integral of the function over the same domain. You can compute the integral
numerically or analytically.

"""
import numpy as np
import integrate_utils as IU

#================================================================
#                       Functions
#================================================================
def fx(x):
    return np.sin(x)

def gx(x):
    return 2*x*np.exp(x**2)


def int_fx(x):
    return (-1) * np.cos(x)

def int_gx(x):
    return (np.exp(x**2))
#================================================================
#                       Parameters
#================================================================
a_min = 0
a_max = np.pi

b_min = 0
b_max = 1

a_x = np.linspace(a_min, a_max, 1000)
b_x = np.linspace(b_min, b_max, 1000)
#================================================================
#                       Calcs
#================================================================
a_mean = np.mean(fx(a_x))
b_mean = np.mean(gx(b_x))

a_int = IU.trapezoidal(fx, a_min, a_max, 1000)
b_int = IU.trapezoidal(gx, b_min, b_max, 1000)
#================================================================
#                       Results
#================================================================
print 'a)'
print 'Mean value:', a_mean
print 'Integral value:', a_int
print 'Difference:', a_int - a_mean

print 'b)'
print 'Mean value:', b_mean
print 'Integral value:', b_int
print 'Difference:', b_int - b_mean