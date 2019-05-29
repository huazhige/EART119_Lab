# -*- coding: utf-8 -*-
"""
Extra Credit Part 2
Alex Watson
    -compare the mean value of a discrete function 
    with the numerical/analytical discrete integral
        - a : f(x) = sinx, xmin = 0, xmax = pi
        - b : g(x) = 2xe^x^2, xmin = 0, xmax = 1
"""

import numpy as np
##integrate utils##
import src.integrate_utils as int_utils
#==============================================================================
#                                   fct def
#==============================================================================
##a##
def fx( x):
    return np.sin( x)
##b##
def gx( x):
    return 2*x*np.exp( x**2)

#==============================================================================
#                                   params
#==============================================================================

xmin   = 0
xmax_f = np.pi
xmax_g = 1

#time steps
N = 1000
#==============================================================================
#                               mean vals
#==============================================================================
#create arrays within specified ranges
a_fx = np.linspace( xmin, xmax_f, N)
a_gx = np.linspace( xmin, xmax_g, N)

#find mean vals
##a##
mean_f = np.mean( fx(a_fx))
##b##
mean_g = np.mean( gx(a_gx))

#==============================================================================
#                               integ
#==============================================================================
#using trapezoidal numerical integration
##a##
NumInt_f = int_utils.trapezoidal( fx, xmin, xmax_f, N)
##b##
NumInt_g = int_utils.trapezoidal( gx, xmin, xmax_g, N)

#compare means to integrals
##a##
print 'f(x): mean value: ', mean_f
print 'f(x): num. integration approx: ', NumInt_f
##b##
print 'g(x): mean value: ', mean_g
print 'g(x): num. integration approx: ', NumInt_g