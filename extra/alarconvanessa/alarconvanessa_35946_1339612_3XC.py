# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:06:57 2019

python 3.7

@author: Nessa
"""

# -*- coding: utf-8 -*-
# python 3.7
"""
"""
import numpy as np
### my modules
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
    if x >= xmin and x >= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

#================================================
#           parameters 
#================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

a_x = np.linspace( -4, 4, 100)
a_y = np.linspace( -4, 4, 100)

x2min, x2max = 0, 2
y2min, y2max = 0, 2

#================================================
#          compute integral 
#================================================
for n in np.arange(100, 1200, 200):
    fInt2 = int_utils.monteCarlo(fct2_xy, fct_gxy, x2min -1, x2max + 1, y2min - 1, y2max + 1, n)
print( 'a) integral of (x^2 + y^2)^0.5 = ', fInt2)

for n in np.arange(100, 1200, 200):
    fInt = int_utils.monteCarlo(fct_xy, fct_gxy, xmin - 1, xmax + 1, ymin - 1, ymax + 1, n)
print ('b) integral of xy^2 = ', round(fInt,4))


"""
The real value of a is ~ 3.5

The real value of b is ~ 2.25

Output console (although it is different every time because of random generation of numbers)

a) integral of (x^2 + y^2)^0.5 =  3.5728502443735106
b) integral of xy^2 =  2.9842

"""
