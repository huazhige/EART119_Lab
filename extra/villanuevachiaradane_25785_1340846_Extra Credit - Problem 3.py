#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
#3D plotting
from mpl_toolkits.mplot3d import axes3d
### my modules
import integrate_utils as int_utils

# =========================1=============================
#                  Function Definitions
# =======================================================
def fct_xy(x, y):
    return x*y**2

def fct2_xy(x, y):
    return np.sqrt(x**2 + y**2)

def fct_Fxy_exact(x, y):
    return 0.5*(x**2)*1./3*(y**3)

def fct_gxy(x, y):
    """
        Rectangular Domain
    Return: -1 for points outside
    """
    f_retVal = -1
    # checks if x is within the boundary:
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

def fct2_gxy(x, y):
    f_retVal = -1
    if np.sqrt(x**2 + y**2) <= r:
        f_retVal = 1
    return f_retVal

# =========================2=============================
#                     Parameters
# =======================================================
xmin = 0
xmax = 2
ymin = 0
ymax = 1.5

r = 2

# =========================3=============================
#                   Compute Integral
# =======================================================
#compute definite integral
# print('Exact solution:', round(fct
for n in np.arange(100, 11000, 1000):
    fInt = int_utils.monteCarlo(fct_xy, fct_gxy, xmin - 1, xmax + 1, ymin - 1, ymax + 1, n)
    fInt2 = int_utils.monteCarlo(fct2_xy, fct2_gxy, 0, r, 0, r, n)
    print('Number of random points:', n, '\n',
          'Numerical integral (Part A):', round(fInt2, 4), '\n',
          'Numerical integral (Part B):', round(fInt, 4), '\n',
          'Exact solution:', 2./3, '\n')

