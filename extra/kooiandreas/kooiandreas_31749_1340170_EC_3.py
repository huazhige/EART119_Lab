# -*- coding: utf-8 -*-
# python 2.7
"""
"""


import numpy as np
import integrate_utils as int_utils

#================================================
#          fct definition
#================================================

def fct2_xy( x, y):
    return np.sqrt(x**2 + y**2)

def fct_xy( x, y):
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

def fct2_gxy( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1        
    if x >= xmin2 and x <= xmax2 and y >= ymin2 and y <= ymax2:
        f_retVal = 1
    return f_retVal

def integral_f(x,y):
    return  (x**2) * (y**3) / 6

def integral_f2(theta, r=2):
    return (r**3)*theta /3

#================================================
#           parameters 
#================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

xmin2, xmax2 = 0, 2
ymin2, ymax2 = 0, 2

a_x = np.linspace( -4, 4, 100)
a_y = np.linspace( -4, 4, 100)

#================================================
#          computations 
#================================================


fInt = int_utils.monteCarlo(fct_xy, fct_gxy, xmin - 1, xmax + 1, ymin - 1, ymax + 1, 1000)
f2Int = int_utils.monteCarlo(fct2_xy, fct_gxy, xmin - 1, xmax + 1, ymin - 1, ymax + 1, 1000)

exact_f2 = integral_f2(2*np.pi) - integral_f2(0)
exact_f = integral_f(2,1.5) - integral_f(0,0)



print('part a.)')
print('Monte Carlo Integration:' + str( round(f2Int,4)))
print('exact: ' + str(exact_f2) )

print('part b.)')
print('Monte Carlo Integration:' + str( round(fInt,4)))
print('exact: ' + str(exact_f) )
    
# I am not sure if my part a.) values are correct, but I think the methodology
# is right and I think my part b.) is correct as well.
# printed Output
'''
part a.)
Monte Carlo Integration:4.3088
exact: 16.7551608191
part b.)
Monte Carlo Integration:2.323
exact: 2.25
'''

