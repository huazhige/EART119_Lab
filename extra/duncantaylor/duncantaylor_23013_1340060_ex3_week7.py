# -*- coding: utf-8 -*-

"""
Compute the values of the following definite integrals using Monte Carlo Integration.
Compare your results to the exact solution. (Hint: For the first integral, you have to
perform a coordinate transform from cartesian to polar coordinates to solve the
problem analytically).

"""
#=================================imports======================================

import numpy as np
import integrate_utils as int_u


#============================Functions=========================================

def fxy(r, theta):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return np.sqrt(x**2 + y**2)

def wxy(x,y):
    return x*y**2


def int_fxy(r, theta):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return np.sqrt(x**2 + y**2)

def int_wxy(x,y):
    return (y**3)/3


def fct_gxy( x, y):
    """
    Rectangular domain
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

def fct_hxy(r, theta):
    """
    Circular domain
    """
    f_retVal = -1
    if r <= 2 and theta >= 0 and theta <= 2*np.pi:
        f_retVal = 1
    return f_retVal

#===================== Parameters==============================================

xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

#=======================Calculations===========================================

mc_fxy = int_u.monteCarlo(fxy, fct_hxy, 0, 2, 0, 2*np.pi, 1000)
mc_wxy = int_u.monteCarlo(wxy, fct_gxy, xmin - 1, xmax + 1, ymin - 1, ymax + 1, 1000)

#=========================Results==============================================

print 'a)'
print 'Exact solution: 16.7551608191' #from calculator
print 'Montecarlo value:', mc_fxy
print 'Difference:', 16.7551608191 - mc_fxy
print 'b)'
print 'Exact solution:', int_wxy(2, 1.5)
print 'Montecarlo value:', mc_wxy
print 'Difference:', int_wxy(2, 1.5) - mc_wxy                                        