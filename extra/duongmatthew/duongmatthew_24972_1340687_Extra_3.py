# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:11:39 2019
    - Solves for the integral of functions over a domain using the Monte Carlo 
    method and compares results to the exact integral value.

@author: Matthew
"""
from __future__ import division

import numpy as np
### my modules
import integrate_utils as int_utils

#==============================================================================
#                                 fct definition
#==============================================================================
def fctf_xy( x, y):                
    return np.sqrt(x**2 + y**2)

def fctf_rh(r, h):            # function of f defined in polar form
    return r**2               # an extra r is there since dxdy = rdrdh
                              # for this script, h = theta or the angle
def fctw_xy( x, y):
    return x*y**2

def fct_gxy( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

def fct_grh(r, h):        
    """
    - circular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if r >= rmin and r <= rmax and h >= hmin and h <= hmax:
        f_retVal = 1
    return f_retVal

def int_f(r, h):               # exact integrated function for fctf
    return h*1./3*(r**3) 

def int_w(x, y):               # exact integrated function for fctw
    return .5*(x**2)*1./3*(y**3)
#==============================================================================
#                                    parameters 
#==============================================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5

rmin, rmax = 0, 2             # polar boundaries for this function
hmin, hmax = 0, 2*np.pi

#==============================================================================
#                                    compute integral 
#==============================================================================
# compute definite integral
for n in np.arange(100, 1200, 200):
    fInt = int_utils.monteCarlo(fctf_rh, fct_grh, rmin-1, rmax+1, hmin-1, hmax+1, n)
    print ( 'no. ran points', n, 'num integral', round(fInt, 4), 'exact', 
           int_f(rmax, hmax) - int_f(rmin, hmin))


for n in np.arange(100, 1200, 200):
    fInt = int_utils.monteCarlo(fctw_xy, fct_gxy, xmin-1, xmax+1, ymin-1, ymax+1, n)
    print ( 'no. ran points', n, 'num integral', round(fInt, 4), 'exact', 
           int_w(xmax, ymax) - int_w(xmin, ymin))

