# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def fct(x):
    return -x**2 + 10*x + 9

def dfdx(x):
    return -2*x + 10

def my_Newton(fct, dfdx, x0):
    """
    - implementation of Newton's method for solving f(x) = 0, when
        when f'(x) is known
    """
    
    
    xn = float(x0)
    eps = 1e-6
    N = 20
    i = 0
    
    while abs(fct(xn +1) - fct(xn)) < eps and i < N:
        x_next = xn - fct(xn)/dfdx(xn)
        xn = x_next
        i += 1
        print( i, 'fct_value', abs(fct(xn)), x_next)
    if abs(fct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan


x0 = -9
# independent variable range
xmin, xmax = -10, 15

#=========================================================================
# Find roots
#=========================================================================
x_root = my_Newton(fct, dfdx, x0)
print(x_root)
#opt_utils
#=========================================================================
# Plots
#=========================================================================
a_x = np.linspace( xmin, xmax, 1000)

plt.figure(1)
plt.plot(a_x, fct(a_x), 'k-')  
#k- is a black line. The other letters are just the colors
plt.plot( [x_root], [fct(x_root)], 'r*', ms =14)
plt.plot( [xmin, xmax], [0,0], 'r--')
plt.grid(True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')

plt.show()
