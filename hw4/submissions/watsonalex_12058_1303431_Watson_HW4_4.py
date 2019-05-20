# -*- coding: utf-8 -*-
"""
Homework 4 Part 4 - Alex Watson
    - find the root of several equations using the Secant method
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#                                   fct def
#==============================================================================

def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    x0 = float( x0)
    x1 = float( x1)
    i = 0
    while abs( fct(x1)) > tol and i < N:
        # numerical approx of derivative
        dfdt   = ( fct( x1) - fct( x0))/( x1 - x0)
        # basically Newton 
        x_next = x1 - fct( x1)/dfdt
        
        x0     = x1
        x1     = x_next
        
        i += 1
    #check if solution converged
    if abs( fct( x1)) > tol:
        return np.nan
    else:
        return x1

def fct1( x):
    return -x**5 + (x**2)/3 + 0.5

def fct2( x):
    return (np.cos( x))**2 + 0.1

def fct3( x):
    return np.sin( x/3) + 0.1*(x + 5)

#==============================================================================
#                                   Parameters
#==============================================================================
x0 = 2
#ranges
xmin1, xmax1 = -10, 10
xmin2, xmax2 = -3, 3

#==============================================================================
#                                   Find Roots
#==============================================================================
##A##
f1_root = my_Secant( fct1, -1, 1, N=50)
##B##
f2_root = my_Secant( fct2, x0, x0+5)
##C##
f3_root = my_Secant( fct3, -2, 0)

#==============================================================================
#                                   Plots
#==============================================================================
a_t1 = np.linspace(xmin1, xmax1, 1000)
a_t2 = np.linspace(xmin2, xmax2, 1000)

plt.figure()
ax1 = plt.subplot( 311)
ax1.plot([xmin1, xmax1], [0, 0], 'r--')
ax1.plot( a_t1, fct1( a_t1), 'k-', label = 'f(x)=-x^5+1/3x^2+1/2')
ax1.plot( [f1_root], [fct1( f1_root)], 'r*', ms = 14)
ax1.grid( True)
ax2 = plt.subplot( 312)
ax2.plot([xmin1, xmax1], [0, 0], 'r--')
ax2.plot( a_t1, fct2( a_t1), 'b-', label = 'f(x)=cos(x)+0.1')
ax2.plot( [f2_root], [fct2( f2_root)], 'r*', ms = 14)
ax2.grid( True)
ax3 = plt.subplot( 313)
ax3.plot([xmin2, xmax2], [0, 0], 'r--')
ax3.plot(a_t2, fct3( a_t2), 'm-', label = 'f(x)=sin(x/3)+0.1(x+5)')
ax3.plot([f3_root], [fct3(f3_root)], 'r*', ms = 14)
ax3.grid( True)
plt.xlabel( 'x')
plt.show()

print 'root a: x =', f1_root
print 'root b: x =', f2_root
print 'root c: x =', f3_root



