#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:25:48 2019

@author: jtbabbe
"""

import numpy as np
import matplotlib.pyplot as plt
#3D plotting
from mpl_toolkits.mplot3d import axes3d
### my modules
import integrate_utils as int_utils

#================================================
#          fct definition
#================================================
# A: original equation
def fct_xy( x, y):
    return np.sqrt(x**2 + y**2)
# A: exact for comparison
#def fct1_xy_exact( x, y):

# A: Bounds    
def fct_gxy( x, y):
    f_retVal = -1
    if (x**2 + y**2) <= 2:
        f_retVal = 1
    return f_retVal
        
# B: original
def fct2_xy( x, y):
    return x*y**2

# B: Bounds
def fct2_gxy( x, y):
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

# B: exact
def fct_Fxy2_exact( x, y):
    return .5*(x**2)*(1/3)*(y**3)

def monteCarlo_vec( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    # create n random points in x and y
    a_xran = np.random.uniform( xmin, xmax, n)
    a_yran = np.random.uniform( ymin, ymax, n)
    ############ vectorized version ###########
    m_xran, m_yran = np.meshgrid( a_xran, a_yran)
    sel = g_xy( m_xran, m_yran) >= 0
    num_inside = sel.sum()
    f_fct_mean = np.mean( f_xy( m_xran[sel], m_yran[sel]))
    # last two lines are the same for loop and vectorized solutions:
    # area of domain is approximate by q*Ar, where q is fraction of points in domain, and Ar is area of rectangle
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

# Cartesian to polar
def cart_to_pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)
#================================================
#           parameters 
#================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

a_x = np.linspace( -4, 4, 100)
a_y = np.linspace( -4, 4, 100)

#================================================
#          compute integral 
#================================================

##A##

for n in np.arange( 100, 1200, 200):
   f_Int = int_utils.monteCarlo(fct_xy, fct_gxy, xmin, xmax, ymin, ymax, n) 
   print ('3a: no. of ran points', n, 'num integral', round( f_Int, 4))
##B##
f_2Int_exact = fct_Fxy2_exact( xmax, ymax) - fct_Fxy2_exact( xmin, ymin)

for n in np.arange( 100, 1200, 200):
    f_2Int = int_utils.monteCarlo(fct2_xy, fct2_gxy, xmin, xmax, ymin, ymax, n)
    print ('3b: no. of ran points', n, 'num integral', round( f_2Int, 4), 'exact', round( f_2Int_exact, 4))

