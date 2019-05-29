# -*- coding: utf-8 -*-
"""
Extra credit problem 3
"""

import numpy as np

#FUNCTION DEFINITIONS
def f_rt(r, theta):
    return ((r*np.cos(theta))**2 + (r*np.sin(theta))**2)**.5

def w_xy(x,y):
    return x*y**2

def wxy_int(x,y):
    return (y**3)/3

def f_r_domain(r, theta):
    f_retVal = -1
    if r <= 2 and theta >= 0 and theta <= 2*np.pi:
        f_retVal = 1
    return f_retVal

def w_xy_domain(x,y):
    f_retVal = -1
    if x >= 0 and x <= 2 and y >= 0 and y <= 1.5:
        f_retVal = 1
    return f_retVal

def monteCarlo( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    a_xran = np.random.uniform( xmin, xmax, n)
    a_yran = np.random.uniform( ymin, ymax, n)
    f_fct_mean = 0
    num_inside = 0 # number of points with x,y; g(x,y) >= 0
    for i in range( n): # x loop
        for j in range( n): # y loop
            if g_xy( a_xran[i], a_yran[j]) >= 0:
                num_inside += 1
                f_fct_mean += f_xy( a_xran[i], a_yran[j])
    f_fct_mean /= num_inside
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

#CALCULATING THE INTEGRALS
w_int = monteCarlo(w_xy, w_xy_domain, 0, 2, 0, 1.5, 1000)
f_int = monteCarlo(f_rt, f_r_domain, 0, 2, 0, 2*np.pi, 1000)
w_exact = wxy_int(2, 1.5)

print('Exact value integral w(x,y):' + str(w_exact))
print('MonteCarlo value w(x,y): ' + str(w_int))
print('Exact value integral f(r,theta): 16.7552')
print('MonteCarlo value f(r,theta): ' + str(f_int))